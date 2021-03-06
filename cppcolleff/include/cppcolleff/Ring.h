#ifndef _RING_H
#define _RING_H

#include <random>  //std::generator and some distributions
#include <cmath> // std::sin std::cos
#include <cppcolleff/essentials.h>
#include <cppcolleff/Bunch.h>

class Ring_t{
    private:
        int _track_one_turn(
            my_PartVector& p,
            const unsigned int seed,
            const int init,
            const int final_) const;
        void to_stream(ostream& fp, const bool isFile = true) const;
    public:
        int harm_num;                              // harmonic number
        double betax, alphax, etax, etaxl,         // optical functions
               tunex, chromx, tunex_shift,         // tune related parameters
               circum, mom_comp, energy,           // general ring parameters
               damp_nume, damp_numx,               // equilibrium parameters
               emitx, espread, en_lost_rad;        // equilibrium parameters
        Interpola_t cav;                           // cavity parameters
        Ring_t():
            harm_num(864),
            betax(1.0), alphax(0.0), etax(0.0), etaxl(0.0),
            tunex(0.0), chromx(0.0), tunex_shift(0.0),
            circum(0.0), mom_comp(0.0), energy(0.0),
            damp_nume(2.0), damp_numx(1.0),
            emitx(0.0), espread(0.0), en_lost_rad(0.0){};
        ~Ring_t() = default;
        my_Dvector get_distribution(
            const my_Dvector& V = my_Dvector(),
            const my_Dvector& spos = my_Dvector()) const;
        my_Dvector get_distribution(
            ThreadPool& pool,
            const my_Dvector& V = my_Dvector(),
            const my_Dvector& spos = my_Dvector()) const;

        Interpola_t get_integrated_distribution(
            const my_Dvector& V = my_Dvector(),
            const my_Dvector& spos = my_Dvector()) const;

        void track_one_turn(Bunch_t& bun, int n) const;
        void track_one_turn(Bunch_t& bun, int n, ThreadPool& pool) const;

        void to_file(const char* filename) const;
        void from_file(const char* filename);
        void show_properties() const;
};

#endif
