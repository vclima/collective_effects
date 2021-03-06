#ifndef _RESULTS_H
#define _RESULTS_H

#include <cppcolleff/essentials.h>
#include <cppcolleff/Bunch.h>

class Results_t {
    private:
        unsigned long calc_every, print_every, save_bunch_every, save_distributions_every, nturns;
        bool FB, Wd, Wl, Wq;

        bool calc_this_turn(const long n) const
        {
            if (calc_every == 0) return false;
            if ((n % calc_every)==0 || n==nturns) return true;
            return false;
        }
        bool print_this_turn(const long n) const
        {
            if (!calc_this_turn(n) || !print_in_screen || print_every == 0) return false;
            if ((n % (calc_every*print_every))==0 || n==nturns) return true;
            return false;
        }
        bool save_bunch_this_turn(const long n) const
        {
            if (!save_bunch || save_bunch_every == 0) return false;
            if ((n % save_bunch_every)==0 || n==nturns) return true;
            return false;
        }
        bool save_distributions_this_turn(const long n) const
        {
            if (save_distributions_every == 0) return false;
            if (!save_distribution_xx && !save_distribution_xx &&
                !save_distribution_de && !save_distribution_ss) return false;
            if ((n % save_distributions_every)==0 || n==nturns) return true;
            return false;
        }
        void reserve_memory()
        {
            long np = nturns/calc_every + 2;
            ave.reserve(np);
            std.reserve(np);
            if (FB) FBkick.reserve(np); else FBkick.reserve(0);
            if (Wd) Wdkick.reserve(np); else Wdkick.reserve(0);
            if (Wq) Wqkick.reserve(np); else Wqkick.reserve(0);
            if (Wl) Wlkick.reserve(np); else Wlkick.reserve(0);
            for (int&& i=0; i<track_parts.size(); ++i)
            {
                track_parts[i].reserve(np);
                if (Wl) track_Wlkick[i].reserve(np); else track_Wlkick[i].reserve(0);
                if (Wd || Wq)track_Wtkick[i].reserve(np); else track_Wtkick[i].reserve(0);
            }
        }
        void initial_guess_distributions()
        {
            bins = my_Ivector(4,1000);
            min.push_back(-200e-6);
            min.push_back(-100e-6);
            min.push_back(-1e-2);
            min.push_back(-3e-2);
            for (auto&& m:min) max.push_back(-m);
        }
        void to_stream(ostream& fp, const bool isFile = true) const;
    public:
        bool save_bunch, print_in_screen, save_distribution_xx;
        bool save_distribution_xl, save_distribution_de, save_distribution_ss;
        bool save_moment_xx, save_moment_xl, save_moment_de, save_moment_ss;
        bool save_moment_xx2, save_moment_xl2, save_moment_de2, save_moment_ss2;
        my_PartMatrix track_parts;
        my_PartVector ave;
        my_PartVector std;
        my_Dvector min, max;
        my_Ivector bins;
        my_Dvector Wlkick, Wdkick, Wqkick, FBkick;  // kicks of wakes and feedback;
        my_Dmatrix track_Wlkick, track_Wtkick;
        Results_t (const unsigned long nt, const unsigned long eve = 1, const bool kicks = false):
            calc_every(eve), print_every(10L), save_bunch_every(0L), save_distributions_every(0L),
            nturns(nt), save_bunch(false), print_in_screen(true), save_distribution_xx(false),
            save_distribution_xl(false), save_distribution_de(false), save_distribution_ss(false),
            save_moment_xx(false), save_moment_xl(false), save_moment_de(false), save_moment_ss(false),
            save_moment_xx2(false), save_moment_xl2(false), save_moment_de2(false), save_moment_ss2(false),
            FB(kicks), Wd(kicks), Wq(kicks), Wl(kicks) {reserve_memory(); initial_guess_distributions();}
        ~Results_t() = default;

        void set_keepFB(const bool keep) {FB = keep; reserve_memory();}
        void set_keepWd(const bool keep) {Wd = keep; reserve_memory();}
        void set_keepWq(const bool keep) {Wq = keep; reserve_memory();}
        void set_keepWl(const bool keep) {Wl = keep; reserve_memory();}
        void set_nturns(const long nt){nturns = nt; reserve_memory();}
        void set_calc_every(const unsigned long eve){calc_every = eve; reserve_memory();}
        void set_print_every(const unsigned long eve){print_every = eve;}
        void set_save_bunch_every(const unsigned long eve){save_bunch_every = eve;}
        void set_save_distributions_every(const unsigned long eve){save_distributions_every = eve;}
        void set_nparticles_to_track(const int np = 0)
        {
            track_parts.resize(np);
            track_Wlkick.resize(np);
            track_Wtkick.resize(np);
            reserve_memory();
        }

        unsigned long get_nturns() const {return nturns;}
        unsigned long get_calc_every() const {return calc_every;}
        unsigned long get_print_every() const {return print_every;}
        unsigned long get_save_bunch_every() const {return save_bunch_every;}
        unsigned long get_save_distributions_every() const {return save_distributions_every;}
        double calc_stats(const Bunch_t& bun, const long turn, ThreadPool& pool);
        double calc_stats(const Bunch_t& bun, const long turn);
        void register_Wkicks(const long turn, const my_Dvector& kik);
        void register_FBkick(const long turn, const double& kik);

        void to_file(const char* filename) const;
        void from_file(const char* filename);
        void show_properties() const;
};

#endif
