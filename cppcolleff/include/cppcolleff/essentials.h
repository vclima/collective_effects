
#ifndef _ESSENTIALS_H
#define _ESSENTIALS_H

// IO
#include <iostream>
#include <iomanip> //std::setw
#include <fstream>
#include <sstream>
#include <cstdio> //std::sprintf std::fprintf
#include <string> //std::string.c_str()
//Utilities:
#include <vector>
#include <utility> //std::swap
#include <random>  //std::generator and some distributions
#include <cmath> //std::sqrt std::sin std::cos
#include <complex>
//parallelization
#include <parallel/algorithm> //std::sort
#include <omp.h>
#include <cppcolleff/ThreadPool/ThreadPool.h>

using namespace std;

#define TWOPI  6.28318530717959
#define light_speed 299792458.0         // [m/s]   - definition

typedef vector<int> my_Ivector;
typedef vector<double> my_Dvector;
typedef vector<complex<double>> my_Cvector;

extern unsigned long seed;
extern int num_threads;

void set_num_threads(int nr);
int get_num_threads();
void set_seed_num(int nr);
unsigned long get_seed();
my_Ivector get_bounds(const int ini, const int fin);
my_Ivector get_bounds(const int ini, const int fin, const int nr);


class Particle_t {
public:
    double xx, xl, de, ss;
    Particle_t():xx(0.0),xl(0.0),de(0.0),ss(0.0) {};
    Particle_t(const Particle_t& p){xx=p.xx; xl=p.xl; de=p.de; ss=p.ss;}
    Particle_t(
        const double x,
        const double l,
        const double e,
        const double s): xx(x),xl(l),de(e),ss(s) {};
    Particle_t(const double ini): xx(ini),xl(ini),de(ini),ss(ini) {};
    Particle_t(const long ini): xx(ini),xl(ini),de(ini),ss(ini) {};
    ~Particle_t() = default;
    Particle_t& operator += (const Particle_t& b)
                {xx += b.xx; xl += b.xl; de += b.de; ss += b.ss; return *this;}
    Particle_t& operator -= (const Particle_t& b)
                {xx -= b.xx; xl -= b.xl; de -= b.de; ss -= b.ss; return *this;}
    Particle_t& operator *= (const Particle_t& b)
                {xx *= b.xx; xl *= b.xl; de *= b.de; ss *= b.ss; return *this;}
    Particle_t& operator /= (const Particle_t& b)
                {xx /= b.xx; xl /= b.xl; de /= b.de; ss /= b.ss; return *this;}
    template <class T> Particle_t& operator += (const T& b)
                            {xx += b; xl += b; de += b; ss += b; return *this;}
    template <class T> Particle_t& operator -= (const T& b)
                            {xx -= b; xl -= b; de -= b; ss -= b; return *this;}
    template <class T> Particle_t& operator *= (const T& b)
                            {xx *= b; xl *= b; de *= b; ss *= b; return *this;}
    template <class T> Particle_t& operator /= (const T& b)
                            {xx /= b; xl /= b; de /= b; ss /= b; return *this;}
    template <class T> Particle_t operator + (const T& b) const
                            {Particle_t c = *this; c += b; return c;}
    template <class T> Particle_t operator - (const T& b) const
                            {Particle_t c = *this; c -= b; return c;}
    template <class T> Particle_t operator * (const T& b) const
                            {Particle_t c = *this; c *= b; return c;}
    template <class T> Particle_t operator / (const T& b) const
                            {Particle_t c = *this; c /= b; return c;}
};

// Particle_t operator + (const Particle_t& p) {return p;}
// Particle_t operator - (const Particle_t& p) {return p*(-1.0);}
// template <class T> Particle_t operator + (const T& b, const Particle_t& p)
//                         {return p + b;}
// template <class T> Particle_t operator - (const T& b, const Particle_t& p)
//                         {return p*(-1.0) + b;}
// template <class T> Particle_t operator * (const T& b, const Particle_t& p)
//                         {return p*b;}

inline Particle_t sqrt(const Particle_t& p)
{
    Particle_t c;
    c.xx = sqrt(p.xx);
    c.xl = sqrt(p.xl);
    c.de = sqrt(p.de);
    c.ss = sqrt(p.ss);
    return c;
}

typedef vector<Particle_t> my_PartVector;

class Interpola_t {
private:
    my_Dvector xi, yi;
    my_Dvector dy, b; // pre-calculation for interpolation;
    double dx, offset;
    bool equally_spaced;
    void check_consistency();
    void initialize_interp() {
        dx = xi[1] - xi[0];
        offset = xi[0]/dx;
        for (int i=0;i<xi.size()-1;++i){
            dy.push_back(  (yi[i+1]-yi[i]) / (xi[i+1]-xi[i])  );
            b.push_back(  yi[i]   -   dy.back() * xi[i]   );
        }
    }
public:
    //Interpola_t(my_Dvector&& xref, my_Dvector&& yref) {xi = move(xref); yi = move(yref);check_consistency();}
    Interpola_t(my_Dvector& xref, my_Dvector& yref):
    xi(xref), yi(yref) {check_consistency();initialize_interp();}
    Interpola_t() = default;
    ~Interpola_t() = default;
    void set_x(my_Dvector& xref){xi=xref; check_consistency(); initialize_interp();}
    void set_y(my_Dvector& yref){yi=yref; check_consistency(); initialize_interp();}
    void set_xy(my_Dvector& xref, my_Dvector& yref){xi=xref; yi=yref; check_consistency(); initialize_interp();}
    const my_Dvector& ref_to_xi() const {return xi;}
    const my_Dvector& ref_to_yi() const {return yi;}
    bool empty() const {return xi.empty();}

    inline double get_y(const double& x) const
    {
        if      (x > xi.back())  {return 0.0;}
        else if (x < xi.front()) {return 0.0;}

        unsigned int i;
        if (equally_spaced){i = (unsigned int) (x/dx - offset);}
        else {for (i=0;i<xi.size();++i){if (x<xi[i]){break;}}}

        return dy[i] * x + b[i];
    }
};

my_Dvector convolution_full(const my_Dvector& vec1, const my_Dvector& vec2);
my_Dvector convolution_full(const my_Dvector& vec1, const my_Dvector& vec2, ThreadPool& pool);
my_Dvector convolution_full_orig(const my_Dvector& vec1, const my_Dvector& vec2);
my_Dvector convolution_full_orig(const my_Dvector& vec1, const my_Dvector& vec2, ThreadPool& pool);

// this function follows matlab's convention of same, not numpy's:
my_Dvector convolution_same(const my_Dvector& vec1, const my_Dvector& vec2);
my_Dvector convolution_same(const my_Dvector& vec1, const my_Dvector& vec2, ThreadPool& pool);
my_Dvector convolution_same_orig(const my_Dvector& vec1, const my_Dvector& vec2);
my_Dvector convolution_same_orig(const my_Dvector& vec1, const my_Dvector& vec2, ThreadPool& pool);

#endif
