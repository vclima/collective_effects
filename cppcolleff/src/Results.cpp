#include <cppcolleff/Results.h>

double calc_moments(
    const my_PartVector& p,
    Particle_t& ave,
    Particle_t& std,
    const int init,
    const int fin,
    const bool this_turn)
{
    if (!this_turn) {
        double avexx (0.0);
        for (int i=init;i<fin;++i) avexx += p[i].xx;
        return avexx;
    }
    for (int i=init;i<fin;++i){
        ave += p[i];
        std += p[i]*p[i];
    }
    return ave.xx;
}

double Results_t::calc_stats(
    const Bunch_t& bun,
    const long turn)
{
    ThreadPool pool (get_num_threads());
    return calc_stats(bun, turn, pool);
}

double Results_t::calc_stats(
    const Bunch_t& bun,
    const long turn,
    ThreadPool& pool)
{
    const bool this_turn = calc_this_turn(turn);
    ave.push_back(Particle_t (0.0));
    std.push_back(Particle_t (0.0));
    auto& rave = ave.back();
    auto& rstd = std.back();
    //
    const my_PartVector& p = bun.particles;

    unsigned int nr_th = get_num_threads();
    my_Ivector lims (get_bounds(0,p.size()));
    my_PartVector aves (nr_th,Particle_t());
    my_PartVector stds (nr_th,Particle_t());
    std::vector< std::future<double> > res;

    for (unsigned int i=0;i<nr_th;++i){
        res.emplace_back(pool.enqueue(calc_moments, ref(p), ref(aves[i]),
                         ref(stds[i]), lims[i], lims[i+1], this_turn));
    }
    if (!this_turn){
        double avexx (0.0);
        for(int i=0; i<nr_th; ++i) avexx += res[i].get();
        return avexx /= bun.num_part;
    }
    for(int i=0; i<nr_th; ++i){
        res[i].get();
        rave += aves[i];
        rstd += stds[i];
    }
    rave /= bun.num_part;
    rstd /= bun.num_part;
    rstd = sqrt(rstd - rave * rave);

    if (save_bunch_this_turn(turn)) {
        char filename[50];
        sprintf(filename,"turn%07lu_bunch.txt",turn);
        bun.to_file(filename);
    }
    if (print_in_screen) {
        if (turn == 0) {
            fprintf(stdout,"%7s %12s %12s   %12s %12s   %12s %12s   %12s %12s \n","turn",
                    "<xx> [um]","std(xx) [um]","<xl> [urad]","std(xl) [urad]",
                    "<de> [%]","std(de) [%]","<ss> [mm]","std(ss) [mm]"
                );
        }
        if (print_this_turn(turn)){
            fprintf(stdout,"%07lu %12.6f %12.6f   %12.6f %12.6f   %12.6f %12.6f   %12.6f %12.6f \n",turn,
                    1e6*ave.back().xx,1e6*std.back().xx,
                    1e6*ave.back().xl,1e6*std.back().xl,
                    1e2*ave.back().de,1e2*std.back().de,
                    1e3*ave.back().ss,1e3*std.back().ss
                );
        }
    }
    return rave.xx;
}

void Results_t::register_FBkick(const long turn, const double& kik)
{
    if (FB && calc_this_turn(turn)) {FBkick.push_back(kik);}
}

void Results_t::register_Wkicks(const long turn, const my_Dvector& kik)
{
    if (Wl && calc_this_turn(turn)) {Wlkick.push_back(kik[0]);}
    if (Wd && calc_this_turn(turn)) {Wdkick.push_back(kik[1]);}
    if (Wq && calc_this_turn(turn)) {Wqkick.push_back(kik[2]);}
}


void Results_t::to_file(const char* filename) const
{
    auto g_bool = [](bool cond){return (cond) ? "true":"false";};

	ofstream fp(filename);
	if (fp.fail()) exit(1);
	fp.setf(fp.left | fp.scientific);
	fp.precision(15);
    fp << setw(30) << "% number_of_turns" << nturns << endl;
    fp << setw(30) << "% calc_statistics_every" << calc_every << " turns" << endl;
    fp << setw(30) << "% print_in_screen" << g_bool(print_in_screen) << endl;
    fp << setw(30) << "% print_in_screen_every" << print_every << " calcs" << endl;
    fp << setw(30) << "% save_bunch" << g_bool(save_bunch) << endl;
    fp << setw(30) << "% save_bunch_every" << save_bunch_every << " turns" << endl;
    fp << setw(30) << "% save_distribution_xx" << g_bool(save_distribution_xx) << endl;
    fp << setw(30) << "% save_distribution_xl" << g_bool(save_distribution_xl) << endl;
    fp << setw(30) << "% save_distribution_de" << g_bool(save_distribution_de) << endl;
    fp << setw(30) << "% save_distribution_ss" << g_bool(save_distribution_ss) << endl;
    fp << setw(30) << "% save_distributions_every" << save_distributions_every << " turns" << endl;
    fp << setw(30) << "% keep_feedback_kicks" << g_bool(FB) << endl;
    fp << setw(30) << "% keep_wake_long_kicks" << g_bool(Wl) << endl;
    fp << setw(30) << "% keep_wake_dipo_kicks" << g_bool(Wd) << endl;
    fp << setw(30) << "% keep_wake_quad_kicks" << g_bool(Wq) << endl;
    fp << setw(26) << "# <xx> [m]";
    fp << setw(26) << "<xl>";
    fp << setw(26) << "<de>";
    fp << setw(26) << "<ss> [m]";
    fp << setw(26) << "std(xx) [m]";
    fp << setw(26) << "std(xl)";
    fp << setw(26) << "std(de)";
    fp << setw(26) << "std(ss) [m]";
    if (Wl) fp << setw(26) << "Long Wake Kick";
    if (Wd) fp << setw(26) << "Dipo Wake Kick";
    if (Wq) fp << setw(26) << "Quad Wake Kick";
    if (FB) fp << setw(26) << "Feedback Kick";
    fp << endl;
    fp.setf(fp.left | fp.showpos | fp.scientific);
    for (auto i=0; i<ave.size(); ++i){
        fp << setw(26) << ave[i].xx;
        fp << setw(26) << ave[i].xl;
        fp << setw(26) << ave[i].de;
        fp << setw(26) << ave[i].ss;
        fp << setw(26) << std[i].xx;
        fp << setw(26) << std[i].xl;
        fp << setw(26) << std[i].de;
        fp << setw(26) << std[i].ss;
        if (Wl) fp << setw(26) << Wlkick[i];
        if (Wd) fp << setw(26) << Wdkick[i];
        if (Wq) fp << setw(26) << Wqkick[i];
        if (FB) fp << setw(26) << FBkick[i];
        fp << endl;
    }
    fp.close();
}

void Results_t::from_file(const char* filename)
{
	ifstream fp(filename);
	if (fp.fail()) return;

    auto g_bool = [](string& cmd){return (cmd.compare("true")==0) ? true:false;};

	double d1(0.0), d2(0.0), d3(0.0), d4(0.0);
  	string line;
	unsigned long line_count = 0;
	while (getline(fp, line)) {
  		line_count++;
  		istringstream ss(line);
		char c = ss.get();
		while (c == ' ') c = ss.get();
  		if (c == '#' || c == '\n') continue;
  		else if (c == '%') {
			string cmd;
	  		ss >> cmd;
            if (cmd.compare("number_of_turns") == 0){ss >> nturns; reserve_memory();}
            else if (cmd.compare("calc_statistics_every") == 0){ss >> calc_every; reserve_memory();}
            else if (cmd.compare("print_in_screen") == 0){ss >> cmd; print_in_screen = g_bool(cmd);}
            else if (cmd.compare("print_in_screen_every") == 0){ss >> print_every;}
            else if (cmd.compare("save_bunch") == 0){ss >> cmd; save_bunch = g_bool(cmd);}
            else if (cmd.compare("save_bunch_every") == 0){ss >> save_bunch_every;}
            else if (cmd.compare("save_distribution_xx") == 0){ss >> cmd; save_distribution_xx = g_bool(cmd);}
            else if (cmd.compare("save_distribution_xl") == 0){ss >> cmd; save_distribution_xl = g_bool(cmd);}
            else if (cmd.compare("save_distribution_de") == 0){ss >> cmd; save_distribution_de = g_bool(cmd);}
            else if (cmd.compare("save_distribution_ss") == 0){ss >> cmd; save_distribution_ss = g_bool(cmd);}
            else if (cmd.compare("save_distributions_every") == 0){ss >> save_distributions_every;}
            else if (cmd.compare("keep_feedback_kicks") == 0){ss >> cmd; FB = g_bool(cmd); reserve_memory();}
            else if (cmd.compare("keep_wake_long_kicks") == 0){ss >> cmd; Wl = g_bool(cmd); reserve_memory();}
            else if (cmd.compare("keep_wake_dipo_kicks") == 0){ss >> cmd; Wd = g_bool(cmd); reserve_memory();}
            else if (cmd.compare("keep_wake_quad_kicks") == 0){ss >> cmd; Wq = g_bool(cmd); reserve_memory();}
            continue;
  		}
		ss.unget();
        ss >> d1; ss >> d2; ss >> d3; ss >> d4;
        ave.push_back(Particle_t(d1, d2, d3, d4));
        ss >> d1; ss >> d2; ss >> d3; ss >> d4;
        std.push_back(Particle_t(d1, d2, d3, d4));
        if (Wl) {ss >> d1; Wlkick.push_back(d1);}
        if (Wd) {ss >> d1; Wdkick.push_back(d1);}
        if (Wq) {ss >> d1; Wqkick.push_back(d1);}
        if (FB) {ss >> d1; FBkick.push_back(d1);}
	}
	fp.close();
}
