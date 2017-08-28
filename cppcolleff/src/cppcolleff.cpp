#include <cppcolleff/cppcolleff.h>

static int _generate_bunch_thread(
	const Ring_t& ring,
	my_PartVector& p,
	const unsigned int seed,
	const Interpola_t& idistr_interpol,
	const int init,
	const int final)
{
	const my_Dvector& idist = idistr_interpol.ref_to_xi();
	normal_distribution<double> espread_dist(0.0,ring.espread);
	exponential_distribution<double> emitx_dist(1/(2*ring.emitx));
	uniform_real_distribution<double> phix_dist(0.0,TWOPI);
	uniform_real_distribution<double> ss_dist(idist.front(),idist.back());
	default_random_engine gen(seed);

  	for (int i=init;i<final;++i){
	  		double&& emitx = emitx_dist(gen);
	  		double&& phix  = phix_dist(gen);
	  		double&& Ax    = sqrt(emitx/ring.betax);
	  		double&& Acosx = Ax*cos(phix);
	  		double&& Asinx = Ax*sin(phix);
	  		p[i].de = espread_dist(gen);
	  		p[i].ss = idistr_interpol.get_y(ss_dist(gen));
	  		p[i].xx =  Acosx*ring.betax          + ring.etax *p[i].de;
	  		p[i].xl = -Acosx*ring.alphax - Asinx + ring.etaxl*p[i].de;
  	}
	return 1;
}
void generate_bunch(const Ring_t& ring, Bunch_t& bun, ThreadPool& pool)
{
	Interpola_t idistr_interpol (ring.get_integrated_distribution());

	extern unsigned long seed;

	my_PartVector& p = bun.particles;
    unsigned int nr_th = get_num_threads();
	my_Ivector lims (get_bounds(0,p.size()));
	std::vector< std::future<int> > results;

	for (unsigned int i=0;i<nr_th;++i){
		results.emplace_back(pool.enqueue(
			_generate_bunch_thread, ref(ring), ref(p), seed,
  			ref(idistr_interpol), lims[i], lims[i+1]
		));
		seed++;
	}
    for(auto && result: results) result.get();

	bun.is_sorted = false;
}
void generate_bunch(const Ring_t& ring, Bunch_t& bun)
{
	ThreadPool pool (get_num_threads());
	return generate_bunch(ring, bun, pool);
}


static double get_residue(
	const my_Dvector& spos,
	const my_Dvector& distr,
	const my_Dvector& distr_old,
	ThreadPool& pool)
{
	double res (0.0);
	double ds (spos[1] - spos[0]);

	unsigned int nr_th = get_num_threads();
	my_Ivector lims (get_bounds(0, spos.size()));
	vector< std::future<double> > results;
	auto fun = [&](int ini, int fin){
		double r (0.0);
		for (int ii=ini;ii<fin;++ii){r += (distr[ii] - distr_old[ii]) * (distr[ii] - distr_old[ii]) * ds;}
		return r;};
	for (unsigned int i=0;i<nr_th;++i){
		results.emplace_back(pool.enqueue(fun, lims[i], lims[i+1]));
	}
	for(auto&& result: results) res += result.get();

	return res;
}
static my_Dvector _const_espread_iteration_Haissinski(
	const Ring_t ring,
	const my_Dvector KickF,
	const int niter,
	const my_Dvector distr_ini,
	ThreadPool& pool)
{
	my_Dvector distr_old (distr_ini);
	auto& cav_s = ring.cav.ref_to_xi();
	auto& cav_V = ring.cav.ref_to_yi();
	double residue_old (get_residue(cav_s, distr_old, my_Dvector(cav_s.size(),0.0), pool));
	int count (0);
	double&& ds = (cav_s[1]-cav_s[0]);

	unsigned int nr_th = get_num_threads();
	my_Ivector lims (get_bounds(0, cav_V.size()));
	vector< std::future<int> > res;
	while (true) {
		my_Dvector V (convolution_same(KickF, distr_old, pool)); // variable to be returned;

		// correct the scale of the convolution and add cavity to potential:
	    auto fun = [&](my_Dvector& V1, int ini, int fin)
	    {for (int i=ini;i<fin;++i){V1[i] *= ds; V1[i] += cav_V[i];}  return 1;};
	    for (unsigned int i=0;i<nr_th;++i){
	        res.emplace_back(pool.enqueue(fun, ref(V), lims[i], lims[i+1]));
	    }
	    for(auto&& result: res) result.get();
		res.clear();

		my_Dvector&& distr = ring.get_distribution(pool, V, cav_s);
		double&& residue = get_residue(cav_s, distr, distr_old, pool);

		if (residue < residue_old){if (residue < 1e-6) return V;}
		else {if (++count > niter) return my_Dvector ();};

		distr_old.swap(distr);
		swap(residue_old,residue);
	}
}


my_Dvector solve_Haissinski_get_potential(
	const Wake_t& wake,
	const Ring_t& ring,
	const double& Ib,
	const int niter,
	const my_Dvector distr_ini)
{
	ThreadPool pool (get_num_threads());
	return solve_Haissinski_get_potential(wake, ring, Ib, pool, niter, distr_ini);
}

my_Dvector solve_Haissinski_get_potential(
	const Wake_t& wake,
	const Ring_t& ring,
	const double& Ib,
	ThreadPool& pool,
	const int niter,
	const my_Dvector distr_ini)
{
	// get the wake function at the cavity longitudinal points (actually it is the kick)
	my_Dvector ini_distr (distr_ini);
	if (ini_distr.size() == 0) {ini_distr = ring.get_distribution();}

	auto& cav_s = ring.cav.ref_to_xi();
	my_Dvector&& KickF = wake.Wl.get_wake_at_points(cav_s, -Ib * ring.T0 / ring.energy);
	return _const_espread_iteration_Haissinski(ring, KickF, niter, distr_ini, pool);
}


double find_equilibrium_energy_spread(
	const Wake_t& wake,
	Ring_t& ring,
	const double& Ib,
	const int niter,
	const my_Dvector distr_ini)
{
	ThreadPool pool (get_num_threads());
	return find_equilibrium_energy_spread(wake, ring, Ib, pool, niter, distr_ini);
}

double find_equilibrium_energy_spread(
	const Wake_t& wake,
	Ring_t& ring,
	const double& Ib,
	ThreadPool& pool,
	const int niter,
	const my_Dvector distr_ini)
{
	// get the wake function at the cavity longitudinal points (actually it is the kick)
	auto& cav_s = ring.cav.ref_to_xi();
	my_Dvector&& KickF = wake.Wl.get_wake_at_points(cav_s, -Ib * ring.T0 / ring.energy);

	my_Dvector V (_const_espread_iteration_Haissinski(ring, KickF, niter, distr_ini, pool));

	// Now use bissection to get the equilibrium distribution if needed
	double final_espread (ring.espread);
	if ( V.empty() ) {
		double init_espread (ring.espread);
		// double delta_spread (ring.espread); //begin with a delta equal to the natural energy spread
		double delta_spread (1e-4);
		bool conv_once (false);

		while (delta_spread > 1e-5) {
			if (V.empty()) {
				if (conv_once) delta_spread /= 2;
				ring.espread += delta_spread;
			}
			else {
				conv_once = true;
				final_espread = ring.espread;
				delta_spread /= 2;
				ring.espread -= delta_spread;
			}
			// fprintf(stdout,"ok\n");
			V = _const_espread_iteration_Haissinski(ring, KickF, niter, distr_ini, pool);
			// fprintf(stdout,"ok2\n");
		}
		ring.espread = init_espread;
	}
	return final_espread;
}


void single_bunch_tracking(
    const Ring_t& ring,
    const Wake_t& wake,
    Feedback_t& fb,
    Bunch_t& bun,
    Results_t& results)
{
    //current dependent strength of the kick:
    const double kick_stren = ring.T0 / ring.energy * bun.Ib / bun.num_part;

	ThreadPool pool (get_num_threads());

    for (long n=0;n<results.get_nturns();n++){
        double&& xx_ave = results.calc_stats(bun, n, pool);
        /* convention: positive ss, means particle behind the sinchronous particle;
         First do single particle tracking:*/
        ring.track_one_turn(bun, n, pool);

        results.register_Wkicks(n, wake.apply_kicks(bun, kick_stren, ring.betax, pool));
        results.register_FBkick(n,   fb.apply_kick(bun, xx_ave,     ring.betax));
    }
    results.calc_stats(bun, results.get_nturns(), pool);
}


void multi_bunch_tracking(
	const Ring_t& ring,
	const Wake_t& long_range_wake,
	const Wake_t& short_range_wake,
	Feedback_t& fb,
	vector<Bunch_t>& buns,
	vector<Results_t>& results)
{

}
