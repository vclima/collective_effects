#include <cppcolleff/essentials.h>

unsigned long seed = 1;
int num_threads = 1;

void set_num_threads(int nr)
{
    num_threads = nr;
    omp_set_num_threads(nr);
}

int get_num_threads() { return num_threads;}

void set_seed_num(int nr) {seed = nr;}

my_Ivector get_bounds(const int ini, const int fin)
{
    return get_bounds(ini, fin, num_threads);
}

my_Ivector get_bounds(const int ini, const int fin, const int nr)
{
    my_Ivector bounds (nr+1,0);
    int incr = (fin-ini) / nr;
    int rem  = (fin-ini) % nr;
    int ad   = 0;
    int N = ini;
    for (auto& bnd:bounds) {
        bnd = N;
        if (rem-- > 0) {ad = 1;} else {ad = 0;}
        N += incr + ad;
    }
    return bounds;
}

void Interpola_t::check_consistency()
{
    if (xi.size() != yi.size()){
        fprintf(stdout,"yi must be the same size as xi.\n");
        exit(1);
    }

    equally_spaced = true;
    double ds0 = xi[1]-xi[0];
    for (auto i=1;i<xi.size(); ++i){
        double&& ds = (xi[i] - xi[i-1]);
        if (ds <= 0.0) {
            fprintf(stdout,"xi must be strictly increasing.\n");
            exit(1);
        }
        if (abs(ds - ds0) > abs(ds0)*1e-10) {equally_spaced = false;}
    }
}

// this function follows matlab's convention of same, not numpy's.
my_Dvector convolution_same_orig(const my_Dvector& vec1, const my_Dvector& vec2)
{
    ThreadPool pool (get_num_threads());
    return convolution_same_orig(vec1, vec2, pool);
}
my_Dvector convolution_same_orig(const my_Dvector& vec1, const my_Dvector& vec2, ThreadPool& pool)
{
    my_Dvector conv (vec1.size(),0.0);
    int init = vec2.size()/2;

    unsigned int nr_th = get_num_threads();
    my_Ivector lims (get_bounds(0,conv.size()));
    std::vector< std::future<int> > results;

    //lambda function
    auto func = [&](my_Dvector& v, int com, int ter)
    {
        for (int ii=com;ii<ter;++ii){
            for (int j=0,k=(ii+init);j<vec2.size() && k>=0;++j,--k){
                if (k<vec1.size()){ v[ii] += vec1[k]*vec2[j];}
            }
        }
        return 1;
    }; //
    for (unsigned int i=0;i<nr_th;++i) results.emplace_back(pool.enqueue(
                        func, ref(conv), lims[i], lims[i+1]));
    for(auto && result: results) result.get();

    return conv;
}
my_Dvector convolution_full_orig(const my_Dvector& vec1, const my_Dvector& vec2)
{
    ThreadPool pool (get_num_threads());
    return convolution_full_orig(vec1, vec2, pool);
}
my_Dvector convolution_full_orig(const my_Dvector& vec1, const my_Dvector& vec2, ThreadPool& pool)
{
    my_Dvector conv (vec1.size()+vec2.size()-1,0.0);

    unsigned int nr_th = get_num_threads();
	my_Ivector lims (get_bounds(0,conv.size()));
	std::vector< std::future<int> > results;

    //lambda function
    auto func = [&](my_Dvector& v, int com, int ter)
    {
        for (int ii=com;ii<ter;++ii){
            for (int j=0,k=ii;j<vec2.size() && k>=0;++j,--k){
                if (k<vec1.size()){ v[ii] += vec1[k]*vec2[j];}
            }
        }
        return 1;
    }; //
	for (unsigned int i=0;i<nr_th;++i) results.emplace_back(pool.enqueue(
                        func, ref(conv), lims[i], lims[i+1]));
    for(auto && result: results) result.get();

    return conv;
}


/* The functions below implement the convolutions just like above, but with an
optimization for the case when the vectors to be convoluted have zeros at the
beginning and end. The speedup is of the order o 16 times for the convolutions
between the wake function and the bunch distribution.*/
static void _trim_vec(const my_Dvector& vec, int& mini, int& maxi)
{
    bool minb (true), maxb (true);
    for (int i=0,j=vec.size(); i<vec.size(); ++i,--j){
        if (minb && (vec[i]  >1e-30 || vec[i]  <-1e-30)) {minb = false; mini = i;}
        if (maxb && (vec[j-1]>1e-30 || vec[j-1]<-1e-30)) {maxb = false; maxi = j;}
        if ((!minb) && (!maxb)) {break;}
    }
}

static void _convolution(const my_Dvector& vec1, const my_Dvector& vec2, my_Dvector& conv, int init, ThreadPool& pool)
{
    // To do the convolution I trim the beginning and ending points if they are zero (1e-30);
    int min1 (0), max1 (vec1.size());
    _trim_vec(vec1, min1, max1);

    int min2 (0), max2 (vec2.size());
    _trim_vec(vec2, min2, max2);

    int ini = max(min1+min2-init,0);
    int fin = min(int(conv.size()), max1 + max2 - 1);

    unsigned int nr_job = max((fin-ini)/100, min(32, fin-ini));
	my_Ivector lims (get_bounds(ini, fin, nr_job));
	std::vector< std::future<int> > results;

    //lambda function
    auto func = [&](my_Dvector& v, int com, int ter)
    {
        for (int ii=com;ii<ter;++ii){
            const int delta = max(ii+init-min2-max1,0);
            for (int j=min2+delta,k=(ii+init-min2-delta);j<max2 && k>=min1;++j,--k){
                v[ii] += vec1[k]*vec2[j];
            }
        }
        return 1;
    }; //

	for (unsigned int i=0;i<nr_job;++i) results.emplace_back(pool.enqueue(
        func, ref(conv), lims[i], lims[i+1]));
    for(auto && result: results) result.get();


}
// this function follows matlab's convention of same, not numpy's.
my_Dvector convolution_same(const my_Dvector& vec1, const my_Dvector& vec2)
{
    ThreadPool pool (get_num_threads());
    return convolution_same(vec1, vec2, pool);
}
my_Dvector convolution_same(const my_Dvector& vec1, const my_Dvector& vec2, ThreadPool& pool)
{
    my_Dvector conv (vec1.size(),0.0);
    int init = vec2.size()/2;

    _convolution(vec1, vec2, conv, init, pool);
    return conv;
}
my_Dvector convolution_full(const my_Dvector& vec1, const my_Dvector& vec2)
{
    ThreadPool pool (get_num_threads());
    return convolution_full(vec1, vec2, pool);
}
my_Dvector convolution_full(const my_Dvector& vec1, const my_Dvector& vec2, ThreadPool& pool)
{
    my_Dvector conv (vec1.size()+vec2.size()-1,0.0);
    int init (0);

    _convolution(vec1, vec2, conv, init, pool);
    return conv;
}
