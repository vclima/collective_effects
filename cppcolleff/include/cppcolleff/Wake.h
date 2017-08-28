#ifndef _WAKE_H
#define _WAKE_H

#include <thread>
#include <cppcolleff/essentials.h>
#include <cppcolleff/Bunch.h>

struct WakePl
{
    bool wake_function, wake_potential, resonator;
    Interpola_t  WF, WP;
    my_Dvector wr, Rs, Q;
    WakePl(): wake_function(false), wake_potential(false), resonator(false) {};
    ~WakePl() = default;
    my_Dvector get_wake_at_points(const my_Dvector& spos, const double& stren) const;
};

class Wake_t
{
    public:
        static const int LL = 0;
        static const int XD = 1;
        static const int XQ = 2;
        WakePl Wd, Wq, Wl;
        Wake_t() {};
        ~Wake_t() = default;
        my_Dvector apply_kicks(
            Bunch_t& bun,
            const double stren,
            const double betax,
            ThreadPool& pool) const;

    private:
        my_Dvector apply_wake_function_kick(
            my_PartVector& par,
            double stren,
            double strenT,
            ThreadPool& pool) const;

        double apply_wake_resonator_kick(
            my_PartVector& p,
            int Ktype, // 0 for longituinal, 1 dipolar, 2 for quadrupolar
            double stren,
            my_Ivector& lims,
            ThreadPool& pool) const;
};

#endif
