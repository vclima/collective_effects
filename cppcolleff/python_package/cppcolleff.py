# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.8
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_cppcolleff', [dirname(__file__)])
        except ImportError:
            import _cppcolleff
            return _cppcolleff
        if fp is not None:
            try:
                _mod = imp.load_module('_cppcolleff', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _cppcolleff = swig_import_helper()
    del swig_import_helper
else:
    import _cppcolleff
del version_info
try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.


def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr_nondynamic(self, class_type, name, static=1):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    if (not static):
        return object.__getattr__(self, name)
    else:
        raise AttributeError(name)

def _swig_getattr(self, class_type, name):
    return _swig_getattr_nondynamic(self, class_type, name, 0)


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object:
        pass
    _newclass = 0



_cppcolleff.TWOPI_swigconstant(_cppcolleff)
TWOPI = _cppcolleff.TWOPI

_cppcolleff.light_speed_swigconstant(_cppcolleff)
light_speed = _cppcolleff.light_speed

def set_num_threads(nr):
    return _cppcolleff.set_num_threads(nr)
set_num_threads = _cppcolleff.set_num_threads
class Particle_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Particle_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Particle_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["xx"] = _cppcolleff.Particle_t_xx_set
    __swig_getmethods__["xx"] = _cppcolleff.Particle_t_xx_get
    if _newclass:
        xx = _swig_property(_cppcolleff.Particle_t_xx_get, _cppcolleff.Particle_t_xx_set)
    __swig_setmethods__["xl"] = _cppcolleff.Particle_t_xl_set
    __swig_getmethods__["xl"] = _cppcolleff.Particle_t_xl_get
    if _newclass:
        xl = _swig_property(_cppcolleff.Particle_t_xl_get, _cppcolleff.Particle_t_xl_set)
    __swig_setmethods__["de"] = _cppcolleff.Particle_t_de_set
    __swig_getmethods__["de"] = _cppcolleff.Particle_t_de_get
    if _newclass:
        de = _swig_property(_cppcolleff.Particle_t_de_get, _cppcolleff.Particle_t_de_set)
    __swig_setmethods__["ss"] = _cppcolleff.Particle_t_ss_set
    __swig_getmethods__["ss"] = _cppcolleff.Particle_t_ss_get
    if _newclass:
        ss = _swig_property(_cppcolleff.Particle_t_ss_get, _cppcolleff.Particle_t_ss_set)

    def __init__(self, *args):
        this = _cppcolleff.new_Particle_t(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cppcolleff.delete_Particle_t
    __del__ = lambda self: None
Particle_t_swigregister = _cppcolleff.Particle_t_swigregister
Particle_t_swigregister(Particle_t)
cvar = _cppcolleff.cvar

class Interpola_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Interpola_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Interpola_t, name)
    __repr__ = _swig_repr

    def __init__(self, *args):
        this = _cppcolleff.new_Interpola_t(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cppcolleff.delete_Interpola_t
    __del__ = lambda self: None

    def set_x(self, xref):
        return _cppcolleff.Interpola_t_set_x(self, xref)

    def set_y(self, yref):
        return _cppcolleff.Interpola_t_set_y(self, yref)

    def set_xy(self, xref, yref):
        return _cppcolleff.Interpola_t_set_xy(self, xref, yref)

    def ref_to_xi(self):
        return _cppcolleff.Interpola_t_ref_to_xi(self)

    def ref_to_yi(self):
        return _cppcolleff.Interpola_t_ref_to_yi(self)

    def get_y(self, x):
        return _cppcolleff.Interpola_t_get_y(self, x)
Interpola_t_swigregister = _cppcolleff.Interpola_t_swigregister
Interpola_t_swigregister(Interpola_t)


def bounds_for_threads(parts, ini, final):
    return _cppcolleff.bounds_for_threads(parts, ini, final)
bounds_for_threads = _cppcolleff.bounds_for_threads

def convolution_full(vec1, vec2):
    return _cppcolleff.convolution_full(vec1, vec2)
convolution_full = _cppcolleff.convolution_full

def convolution_full_orig(vec1, vec2):
    return _cppcolleff.convolution_full_orig(vec1, vec2)
convolution_full_orig = _cppcolleff.convolution_full_orig

def convolution_same(vec1, vec2):
    return _cppcolleff.convolution_same(vec1, vec2)
convolution_same = _cppcolleff.convolution_same

def convolution_same_orig(vec1, vec2):
    return _cppcolleff.convolution_same_orig(vec1, vec2)
convolution_same_orig = _cppcolleff.convolution_same_orig
class Bunch_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Bunch_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Bunch_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["is_sorted"] = _cppcolleff.Bunch_t_is_sorted_set
    __swig_getmethods__["is_sorted"] = _cppcolleff.Bunch_t_is_sorted_get
    if _newclass:
        is_sorted = _swig_property(_cppcolleff.Bunch_t_is_sorted_get, _cppcolleff.Bunch_t_is_sorted_set)
    __swig_setmethods__["num_part"] = _cppcolleff.Bunch_t_num_part_set
    __swig_getmethods__["num_part"] = _cppcolleff.Bunch_t_num_part_get
    if _newclass:
        num_part = _swig_property(_cppcolleff.Bunch_t_num_part_get, _cppcolleff.Bunch_t_num_part_set)
    __swig_setmethods__["Ib"] = _cppcolleff.Bunch_t_Ib_set
    __swig_getmethods__["Ib"] = _cppcolleff.Bunch_t_Ib_get
    if _newclass:
        Ib = _swig_property(_cppcolleff.Bunch_t_Ib_get, _cppcolleff.Bunch_t_Ib_set)
    __swig_setmethods__["particles"] = _cppcolleff.Bunch_t_particles_set
    __swig_getmethods__["particles"] = _cppcolleff.Bunch_t_particles_get
    if _newclass:
        particles = _swig_property(_cppcolleff.Bunch_t_particles_get, _cppcolleff.Bunch_t_particles_set)

    def __init__(self, *args):
        this = _cppcolleff.new_Bunch_t(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cppcolleff.delete_Bunch_t
    __del__ = lambda self: None

    def generate_bunch(self):
        return _cppcolleff.Bunch_t_generate_bunch(self)

    def general_sort(self):
        return _cppcolleff.Bunch_t_general_sort(self)

    def insertion_sort(self):
        return _cppcolleff.Bunch_t_insertion_sort(self)

    def selection_sort(self):
        return _cppcolleff.Bunch_t_selection_sort(self)

    def sort(self):
        return _cppcolleff.Bunch_t_sort(self)
Bunch_t_swigregister = _cppcolleff.Bunch_t_swigregister
Bunch_t_swigregister(Bunch_t)

class Ring_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Ring_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Ring_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["harm_num"] = _cppcolleff.Ring_t_harm_num_set
    __swig_getmethods__["harm_num"] = _cppcolleff.Ring_t_harm_num_get
    if _newclass:
        harm_num = _swig_property(_cppcolleff.Ring_t_harm_num_get, _cppcolleff.Ring_t_harm_num_set)
    __swig_setmethods__["betax"] = _cppcolleff.Ring_t_betax_set
    __swig_getmethods__["betax"] = _cppcolleff.Ring_t_betax_get
    if _newclass:
        betax = _swig_property(_cppcolleff.Ring_t_betax_get, _cppcolleff.Ring_t_betax_set)
    __swig_setmethods__["alphax"] = _cppcolleff.Ring_t_alphax_set
    __swig_getmethods__["alphax"] = _cppcolleff.Ring_t_alphax_get
    if _newclass:
        alphax = _swig_property(_cppcolleff.Ring_t_alphax_get, _cppcolleff.Ring_t_alphax_set)
    __swig_setmethods__["etax"] = _cppcolleff.Ring_t_etax_set
    __swig_getmethods__["etax"] = _cppcolleff.Ring_t_etax_get
    if _newclass:
        etax = _swig_property(_cppcolleff.Ring_t_etax_get, _cppcolleff.Ring_t_etax_set)
    __swig_setmethods__["etaxl"] = _cppcolleff.Ring_t_etaxl_set
    __swig_getmethods__["etaxl"] = _cppcolleff.Ring_t_etaxl_get
    if _newclass:
        etaxl = _swig_property(_cppcolleff.Ring_t_etaxl_get, _cppcolleff.Ring_t_etaxl_set)
    __swig_setmethods__["tunex"] = _cppcolleff.Ring_t_tunex_set
    __swig_getmethods__["tunex"] = _cppcolleff.Ring_t_tunex_get
    if _newclass:
        tunex = _swig_property(_cppcolleff.Ring_t_tunex_get, _cppcolleff.Ring_t_tunex_set)
    __swig_setmethods__["chromx"] = _cppcolleff.Ring_t_chromx_set
    __swig_getmethods__["chromx"] = _cppcolleff.Ring_t_chromx_get
    if _newclass:
        chromx = _swig_property(_cppcolleff.Ring_t_chromx_get, _cppcolleff.Ring_t_chromx_set)
    __swig_setmethods__["tunex_shift"] = _cppcolleff.Ring_t_tunex_shift_set
    __swig_getmethods__["tunex_shift"] = _cppcolleff.Ring_t_tunex_shift_get
    if _newclass:
        tunex_shift = _swig_property(_cppcolleff.Ring_t_tunex_shift_get, _cppcolleff.Ring_t_tunex_shift_set)
    __swig_setmethods__["circum"] = _cppcolleff.Ring_t_circum_set
    __swig_getmethods__["circum"] = _cppcolleff.Ring_t_circum_get
    if _newclass:
        circum = _swig_property(_cppcolleff.Ring_t_circum_get, _cppcolleff.Ring_t_circum_set)
    __swig_setmethods__["mom_comp"] = _cppcolleff.Ring_t_mom_comp_set
    __swig_getmethods__["mom_comp"] = _cppcolleff.Ring_t_mom_comp_get
    if _newclass:
        mom_comp = _swig_property(_cppcolleff.Ring_t_mom_comp_get, _cppcolleff.Ring_t_mom_comp_set)
    __swig_setmethods__["T0"] = _cppcolleff.Ring_t_T0_set
    __swig_getmethods__["T0"] = _cppcolleff.Ring_t_T0_get
    if _newclass:
        T0 = _swig_property(_cppcolleff.Ring_t_T0_get, _cppcolleff.Ring_t_T0_set)
    __swig_setmethods__["energy"] = _cppcolleff.Ring_t_energy_set
    __swig_getmethods__["energy"] = _cppcolleff.Ring_t_energy_get
    if _newclass:
        energy = _swig_property(_cppcolleff.Ring_t_energy_get, _cppcolleff.Ring_t_energy_set)
    __swig_setmethods__["emitx"] = _cppcolleff.Ring_t_emitx_set
    __swig_getmethods__["emitx"] = _cppcolleff.Ring_t_emitx_get
    if _newclass:
        emitx = _swig_property(_cppcolleff.Ring_t_emitx_get, _cppcolleff.Ring_t_emitx_set)
    __swig_setmethods__["espread"] = _cppcolleff.Ring_t_espread_set
    __swig_getmethods__["espread"] = _cppcolleff.Ring_t_espread_get
    if _newclass:
        espread = _swig_property(_cppcolleff.Ring_t_espread_get, _cppcolleff.Ring_t_espread_set)
    __swig_setmethods__["cav"] = _cppcolleff.Ring_t_cav_set
    __swig_getmethods__["cav"] = _cppcolleff.Ring_t_cav_get
    if _newclass:
        cav = _swig_property(_cppcolleff.Ring_t_cav_get, _cppcolleff.Ring_t_cav_set)

    def __init__(self):
        this = _cppcolleff.new_Ring_t()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cppcolleff.delete_Ring_t
    __del__ = lambda self: None

    def get_distribution(self, *args):
        return _cppcolleff.Ring_t_get_distribution(self, *args)

    def get_integrated_distribution(self, *args):
        return _cppcolleff.Ring_t_get_integrated_distribution(self, *args)

    def track_one_turn(self, bun):
        return _cppcolleff.Ring_t_track_one_turn(self, bun)
Ring_t_swigregister = _cppcolleff.Ring_t_swigregister
Ring_t_swigregister(Ring_t)

class Results_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Results_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Results_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["to_file"] = _cppcolleff.Results_t_to_file_set
    __swig_getmethods__["to_file"] = _cppcolleff.Results_t_to_file_get
    if _newclass:
        to_file = _swig_property(_cppcolleff.Results_t_to_file_get, _cppcolleff.Results_t_to_file_set)
    __swig_setmethods__["print_screen"] = _cppcolleff.Results_t_print_screen_set
    __swig_getmethods__["print_screen"] = _cppcolleff.Results_t_print_screen_get
    if _newclass:
        print_screen = _swig_property(_cppcolleff.Results_t_print_screen_get, _cppcolleff.Results_t_print_screen_set)
    __swig_setmethods__["ave"] = _cppcolleff.Results_t_ave_set
    __swig_getmethods__["ave"] = _cppcolleff.Results_t_ave_get
    if _newclass:
        ave = _swig_property(_cppcolleff.Results_t_ave_get, _cppcolleff.Results_t_ave_set)
    __swig_setmethods__["std"] = _cppcolleff.Results_t_std_set
    __swig_getmethods__["std"] = _cppcolleff.Results_t_std_get
    if _newclass:
        std = _swig_property(_cppcolleff.Results_t_std_get, _cppcolleff.Results_t_std_set)
    __swig_setmethods__["Wlkick"] = _cppcolleff.Results_t_Wlkick_set
    __swig_getmethods__["Wlkick"] = _cppcolleff.Results_t_Wlkick_get
    if _newclass:
        Wlkick = _swig_property(_cppcolleff.Results_t_Wlkick_get, _cppcolleff.Results_t_Wlkick_set)
    __swig_setmethods__["Wdkick"] = _cppcolleff.Results_t_Wdkick_set
    __swig_getmethods__["Wdkick"] = _cppcolleff.Results_t_Wdkick_get
    if _newclass:
        Wdkick = _swig_property(_cppcolleff.Results_t_Wdkick_get, _cppcolleff.Results_t_Wdkick_set)
    __swig_setmethods__["FBkick"] = _cppcolleff.Results_t_FBkick_set
    __swig_getmethods__["FBkick"] = _cppcolleff.Results_t_FBkick_get
    if _newclass:
        FBkick = _swig_property(_cppcolleff.Results_t_FBkick_get, _cppcolleff.Results_t_FBkick_set)

    def __init__(self, *args):
        this = _cppcolleff.new_Results_t(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cppcolleff.delete_Results_t
    __del__ = lambda self: None

    def set_keepFB(self, keep):
        return _cppcolleff.Results_t_set_keepFB(self, keep)

    def set_keepWd(self, keep):
        return _cppcolleff.Results_t_set_keepWd(self, keep)

    def set_keepWl(self, keep):
        return _cppcolleff.Results_t_set_keepWl(self, keep)

    def set_every(self, eve):
        return _cppcolleff.Results_t_set_every(self, eve)

    def set_nturns(self, nt):
        return _cppcolleff.Results_t_set_nturns(self, nt)

    def get_nturns(self):
        return _cppcolleff.Results_t_get_nturns(self)

    def calc_stats(self, bun, turn):
        return _cppcolleff.Results_t_calc_stats(self, bun, turn)

    def register_Wkicks(self, turn, kik):
        return _cppcolleff.Results_t_register_Wkicks(self, turn, kik)

    def register_FBkick(self, turn, kik):
        return _cppcolleff.Results_t_register_FBkick(self, turn, kik)

    def dump_bunch_to_file(self, bun, filename):
        return _cppcolleff.Results_t_dump_bunch_to_file(self, bun, filename)
Results_t_swigregister = _cppcolleff.Results_t_swigregister
Results_t_swigregister(Results_t)

class Feedback_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Feedback_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Feedback_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["track"] = _cppcolleff.Feedback_t_track_set
    __swig_getmethods__["track"] = _cppcolleff.Feedback_t_track_get
    if _newclass:
        track = _swig_property(_cppcolleff.Feedback_t_track_get, _cppcolleff.Feedback_t_track_set)
    __swig_setmethods__["npoints"] = _cppcolleff.Feedback_t_npoints_set
    __swig_getmethods__["npoints"] = _cppcolleff.Feedback_t_npoints_get
    if _newclass:
        npoints = _swig_property(_cppcolleff.Feedback_t_npoints_get, _cppcolleff.Feedback_t_npoints_set)
    __swig_setmethods__["delay"] = _cppcolleff.Feedback_t_delay_set
    __swig_getmethods__["delay"] = _cppcolleff.Feedback_t_delay_get
    if _newclass:
        delay = _swig_property(_cppcolleff.Feedback_t_delay_get, _cppcolleff.Feedback_t_delay_set)
    __swig_setmethods__["phase"] = _cppcolleff.Feedback_t_phase_set
    __swig_getmethods__["phase"] = _cppcolleff.Feedback_t_phase_get
    if _newclass:
        phase = _swig_property(_cppcolleff.Feedback_t_phase_get, _cppcolleff.Feedback_t_phase_set)
    __swig_setmethods__["freq"] = _cppcolleff.Feedback_t_freq_set
    __swig_getmethods__["freq"] = _cppcolleff.Feedback_t_freq_get
    if _newclass:
        freq = _swig_property(_cppcolleff.Feedback_t_freq_get, _cppcolleff.Feedback_t_freq_set)
    __swig_setmethods__["gain"] = _cppcolleff.Feedback_t_gain_set
    __swig_getmethods__["gain"] = _cppcolleff.Feedback_t_gain_get
    if _newclass:
        gain = _swig_property(_cppcolleff.Feedback_t_gain_get, _cppcolleff.Feedback_t_gain_set)
    __swig_setmethods__["satur"] = _cppcolleff.Feedback_t_satur_set
    __swig_getmethods__["satur"] = _cppcolleff.Feedback_t_satur_get
    if _newclass:
        satur = _swig_property(_cppcolleff.Feedback_t_satur_get, _cppcolleff.Feedback_t_satur_set)
    __swig_setmethods__["bpmbeta"] = _cppcolleff.Feedback_t_bpmbeta_set
    __swig_getmethods__["bpmbeta"] = _cppcolleff.Feedback_t_bpmbeta_get
    if _newclass:
        bpmbeta = _swig_property(_cppcolleff.Feedback_t_bpmbeta_get, _cppcolleff.Feedback_t_bpmbeta_set)
    __swig_setmethods__["kikbeta"] = _cppcolleff.Feedback_t_kikbeta_set
    __swig_getmethods__["kikbeta"] = _cppcolleff.Feedback_t_kikbeta_get
    if _newclass:
        kikbeta = _swig_property(_cppcolleff.Feedback_t_kikbeta_get, _cppcolleff.Feedback_t_kikbeta_set)

    def __init__(self):
        this = _cppcolleff.new_Feedback_t()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cppcolleff.delete_Feedback_t
    __del__ = lambda self: None

    def apply_kick(self, bun, xx_mean, betax):
        return _cppcolleff.Feedback_t_apply_kick(self, bun, xx_mean, betax)
Feedback_t_swigregister = _cppcolleff.Feedback_t_swigregister
Feedback_t_swigregister(Feedback_t)

class WakePl(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, WakePl, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, WakePl, name)
    __repr__ = _swig_repr
    __swig_setmethods__["general"] = _cppcolleff.WakePl_general_set
    __swig_getmethods__["general"] = _cppcolleff.WakePl_general_get
    if _newclass:
        general = _swig_property(_cppcolleff.WakePl_general_get, _cppcolleff.WakePl_general_set)
    __swig_setmethods__["resonator"] = _cppcolleff.WakePl_resonator_set
    __swig_getmethods__["resonator"] = _cppcolleff.WakePl_resonator_get
    if _newclass:
        resonator = _swig_property(_cppcolleff.WakePl_resonator_get, _cppcolleff.WakePl_resonator_set)
    __swig_setmethods__["W"] = _cppcolleff.WakePl_W_set
    __swig_getmethods__["W"] = _cppcolleff.WakePl_W_get
    if _newclass:
        W = _swig_property(_cppcolleff.WakePl_W_get, _cppcolleff.WakePl_W_set)
    __swig_setmethods__["wr"] = _cppcolleff.WakePl_wr_set
    __swig_getmethods__["wr"] = _cppcolleff.WakePl_wr_get
    if _newclass:
        wr = _swig_property(_cppcolleff.WakePl_wr_get, _cppcolleff.WakePl_wr_set)
    __swig_setmethods__["Rs"] = _cppcolleff.WakePl_Rs_set
    __swig_getmethods__["Rs"] = _cppcolleff.WakePl_Rs_get
    if _newclass:
        Rs = _swig_property(_cppcolleff.WakePl_Rs_get, _cppcolleff.WakePl_Rs_set)
    __swig_setmethods__["Q"] = _cppcolleff.WakePl_Q_set
    __swig_getmethods__["Q"] = _cppcolleff.WakePl_Q_get
    if _newclass:
        Q = _swig_property(_cppcolleff.WakePl_Q_get, _cppcolleff.WakePl_Q_set)

    def __init__(self):
        this = _cppcolleff.new_WakePl()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cppcolleff.delete_WakePl
    __del__ = lambda self: None

    def get_wake_at_points(self, spos, stren):
        return _cppcolleff.WakePl_get_wake_at_points(self, spos, stren)
WakePl_swigregister = _cppcolleff.WakePl_swigregister
WakePl_swigregister(WakePl)

class Wake_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, Wake_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, Wake_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["Wd"] = _cppcolleff.Wake_t_Wd_set
    __swig_getmethods__["Wd"] = _cppcolleff.Wake_t_Wd_get
    if _newclass:
        Wd = _swig_property(_cppcolleff.Wake_t_Wd_get, _cppcolleff.Wake_t_Wd_set)
    __swig_setmethods__["Wq"] = _cppcolleff.Wake_t_Wq_set
    __swig_getmethods__["Wq"] = _cppcolleff.Wake_t_Wq_get
    if _newclass:
        Wq = _swig_property(_cppcolleff.Wake_t_Wq_get, _cppcolleff.Wake_t_Wq_set)
    __swig_setmethods__["Wl"] = _cppcolleff.Wake_t_Wl_set
    __swig_getmethods__["Wl"] = _cppcolleff.Wake_t_Wl_get
    if _newclass:
        Wl = _swig_property(_cppcolleff.Wake_t_Wl_get, _cppcolleff.Wake_t_Wl_set)

    def __init__(self):
        this = _cppcolleff.new_Wake_t()
        try:
            self.this.append(this)
        except Exception:
            self.this = this
    __swig_destroy__ = _cppcolleff.delete_Wake_t
    __del__ = lambda self: None

    def apply_kicks(self, bun, stren, betax):
        return _cppcolleff.Wake_t_apply_kicks(self, bun, stren, betax)
Wake_t_swigregister = _cppcolleff.Wake_t_swigregister
Wake_t_swigregister(Wake_t)


def generate_bunch(*args):
    return _cppcolleff.generate_bunch(*args)
generate_bunch = _cppcolleff.generate_bunch

def solve_Haissinski(wake, ring, Ib):
    return _cppcolleff.solve_Haissinski(wake, ring, Ib)
solve_Haissinski = _cppcolleff.solve_Haissinski

def do_tracking(ring, wake, fb, bun, results):
    return _cppcolleff.do_tracking(ring, wake, fb, bun, results)
do_tracking = _cppcolleff.do_tracking
class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _cppcolleff.delete_SwigPyIterator
    __del__ = lambda self: None

    def value(self):
        return _cppcolleff.SwigPyIterator_value(self)

    def incr(self, n=1):
        return _cppcolleff.SwigPyIterator_incr(self, n)

    def decr(self, n=1):
        return _cppcolleff.SwigPyIterator_decr(self, n)

    def distance(self, x):
        return _cppcolleff.SwigPyIterator_distance(self, x)

    def equal(self, x):
        return _cppcolleff.SwigPyIterator_equal(self, x)

    def copy(self):
        return _cppcolleff.SwigPyIterator_copy(self)

    def next(self):
        return _cppcolleff.SwigPyIterator_next(self)

    def __next__(self):
        return _cppcolleff.SwigPyIterator___next__(self)

    def previous(self):
        return _cppcolleff.SwigPyIterator_previous(self)

    def advance(self, n):
        return _cppcolleff.SwigPyIterator_advance(self, n)

    def __eq__(self, x):
        return _cppcolleff.SwigPyIterator___eq__(self, x)

    def __ne__(self, x):
        return _cppcolleff.SwigPyIterator___ne__(self, x)

    def __iadd__(self, n):
        return _cppcolleff.SwigPyIterator___iadd__(self, n)

    def __isub__(self, n):
        return _cppcolleff.SwigPyIterator___isub__(self, n)

    def __add__(self, n):
        return _cppcolleff.SwigPyIterator___add__(self, n)

    def __sub__(self, *args):
        return _cppcolleff.SwigPyIterator___sub__(self, *args)
    def __iter__(self):
        return self
SwigPyIterator_swigregister = _cppcolleff.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class my_Ivector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, my_Ivector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, my_Ivector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cppcolleff.my_Ivector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cppcolleff.my_Ivector___nonzero__(self)

    def __bool__(self):
        return _cppcolleff.my_Ivector___bool__(self)

    def __len__(self):
        return _cppcolleff.my_Ivector___len__(self)

    def __getslice__(self, i, j):
        return _cppcolleff.my_Ivector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cppcolleff.my_Ivector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cppcolleff.my_Ivector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cppcolleff.my_Ivector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cppcolleff.my_Ivector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cppcolleff.my_Ivector___setitem__(self, *args)

    def pop(self):
        return _cppcolleff.my_Ivector_pop(self)

    def append(self, x):
        return _cppcolleff.my_Ivector_append(self, x)

    def empty(self):
        return _cppcolleff.my_Ivector_empty(self)

    def size(self):
        return _cppcolleff.my_Ivector_size(self)

    def swap(self, v):
        return _cppcolleff.my_Ivector_swap(self, v)

    def begin(self):
        return _cppcolleff.my_Ivector_begin(self)

    def end(self):
        return _cppcolleff.my_Ivector_end(self)

    def rbegin(self):
        return _cppcolleff.my_Ivector_rbegin(self)

    def rend(self):
        return _cppcolleff.my_Ivector_rend(self)

    def clear(self):
        return _cppcolleff.my_Ivector_clear(self)

    def get_allocator(self):
        return _cppcolleff.my_Ivector_get_allocator(self)

    def pop_back(self):
        return _cppcolleff.my_Ivector_pop_back(self)

    def erase(self, *args):
        return _cppcolleff.my_Ivector_erase(self, *args)

    def __init__(self, *args):
        this = _cppcolleff.new_my_Ivector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _cppcolleff.my_Ivector_push_back(self, x)

    def front(self):
        return _cppcolleff.my_Ivector_front(self)

    def back(self):
        return _cppcolleff.my_Ivector_back(self)

    def assign(self, n, x):
        return _cppcolleff.my_Ivector_assign(self, n, x)

    def resize(self, *args):
        return _cppcolleff.my_Ivector_resize(self, *args)

    def insert(self, *args):
        return _cppcolleff.my_Ivector_insert(self, *args)

    def reserve(self, n):
        return _cppcolleff.my_Ivector_reserve(self, n)

    def capacity(self):
        return _cppcolleff.my_Ivector_capacity(self)
    __swig_destroy__ = _cppcolleff.delete_my_Ivector
    __del__ = lambda self: None
my_Ivector_swigregister = _cppcolleff.my_Ivector_swigregister
my_Ivector_swigregister(my_Ivector)

class my_Dvector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, my_Dvector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, my_Dvector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cppcolleff.my_Dvector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cppcolleff.my_Dvector___nonzero__(self)

    def __bool__(self):
        return _cppcolleff.my_Dvector___bool__(self)

    def __len__(self):
        return _cppcolleff.my_Dvector___len__(self)

    def __getslice__(self, i, j):
        return _cppcolleff.my_Dvector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cppcolleff.my_Dvector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cppcolleff.my_Dvector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cppcolleff.my_Dvector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cppcolleff.my_Dvector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cppcolleff.my_Dvector___setitem__(self, *args)

    def pop(self):
        return _cppcolleff.my_Dvector_pop(self)

    def append(self, x):
        return _cppcolleff.my_Dvector_append(self, x)

    def empty(self):
        return _cppcolleff.my_Dvector_empty(self)

    def size(self):
        return _cppcolleff.my_Dvector_size(self)

    def swap(self, v):
        return _cppcolleff.my_Dvector_swap(self, v)

    def begin(self):
        return _cppcolleff.my_Dvector_begin(self)

    def end(self):
        return _cppcolleff.my_Dvector_end(self)

    def rbegin(self):
        return _cppcolleff.my_Dvector_rbegin(self)

    def rend(self):
        return _cppcolleff.my_Dvector_rend(self)

    def clear(self):
        return _cppcolleff.my_Dvector_clear(self)

    def get_allocator(self):
        return _cppcolleff.my_Dvector_get_allocator(self)

    def pop_back(self):
        return _cppcolleff.my_Dvector_pop_back(self)

    def erase(self, *args):
        return _cppcolleff.my_Dvector_erase(self, *args)

    def __init__(self, *args):
        this = _cppcolleff.new_my_Dvector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _cppcolleff.my_Dvector_push_back(self, x)

    def front(self):
        return _cppcolleff.my_Dvector_front(self)

    def back(self):
        return _cppcolleff.my_Dvector_back(self)

    def assign(self, n, x):
        return _cppcolleff.my_Dvector_assign(self, n, x)

    def resize(self, *args):
        return _cppcolleff.my_Dvector_resize(self, *args)

    def insert(self, *args):
        return _cppcolleff.my_Dvector_insert(self, *args)

    def reserve(self, n):
        return _cppcolleff.my_Dvector_reserve(self, n)

    def capacity(self):
        return _cppcolleff.my_Dvector_capacity(self)
    __swig_destroy__ = _cppcolleff.delete_my_Dvector
    __del__ = lambda self: None
my_Dvector_swigregister = _cppcolleff.my_Dvector_swigregister
my_Dvector_swigregister(my_Dvector)

class my_PartVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, my_PartVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, my_PartVector, name)
    __repr__ = _swig_repr

    def iterator(self):
        return _cppcolleff.my_PartVector_iterator(self)
    def __iter__(self):
        return self.iterator()

    def __nonzero__(self):
        return _cppcolleff.my_PartVector___nonzero__(self)

    def __bool__(self):
        return _cppcolleff.my_PartVector___bool__(self)

    def __len__(self):
        return _cppcolleff.my_PartVector___len__(self)

    def __getslice__(self, i, j):
        return _cppcolleff.my_PartVector___getslice__(self, i, j)

    def __setslice__(self, *args):
        return _cppcolleff.my_PartVector___setslice__(self, *args)

    def __delslice__(self, i, j):
        return _cppcolleff.my_PartVector___delslice__(self, i, j)

    def __delitem__(self, *args):
        return _cppcolleff.my_PartVector___delitem__(self, *args)

    def __getitem__(self, *args):
        return _cppcolleff.my_PartVector___getitem__(self, *args)

    def __setitem__(self, *args):
        return _cppcolleff.my_PartVector___setitem__(self, *args)

    def pop(self):
        return _cppcolleff.my_PartVector_pop(self)

    def append(self, x):
        return _cppcolleff.my_PartVector_append(self, x)

    def empty(self):
        return _cppcolleff.my_PartVector_empty(self)

    def size(self):
        return _cppcolleff.my_PartVector_size(self)

    def swap(self, v):
        return _cppcolleff.my_PartVector_swap(self, v)

    def begin(self):
        return _cppcolleff.my_PartVector_begin(self)

    def end(self):
        return _cppcolleff.my_PartVector_end(self)

    def rbegin(self):
        return _cppcolleff.my_PartVector_rbegin(self)

    def rend(self):
        return _cppcolleff.my_PartVector_rend(self)

    def clear(self):
        return _cppcolleff.my_PartVector_clear(self)

    def get_allocator(self):
        return _cppcolleff.my_PartVector_get_allocator(self)

    def pop_back(self):
        return _cppcolleff.my_PartVector_pop_back(self)

    def erase(self, *args):
        return _cppcolleff.my_PartVector_erase(self, *args)

    def __init__(self, *args):
        this = _cppcolleff.new_my_PartVector(*args)
        try:
            self.this.append(this)
        except Exception:
            self.this = this

    def push_back(self, x):
        return _cppcolleff.my_PartVector_push_back(self, x)

    def front(self):
        return _cppcolleff.my_PartVector_front(self)

    def back(self):
        return _cppcolleff.my_PartVector_back(self)

    def assign(self, n, x):
        return _cppcolleff.my_PartVector_assign(self, n, x)

    def resize(self, *args):
        return _cppcolleff.my_PartVector_resize(self, *args)

    def insert(self, *args):
        return _cppcolleff.my_PartVector_insert(self, *args)

    def reserve(self, n):
        return _cppcolleff.my_PartVector_reserve(self, n)

    def capacity(self):
        return _cppcolleff.my_PartVector_capacity(self)
    __swig_destroy__ = _cppcolleff.delete_my_PartVector
    __del__ = lambda self: None
my_PartVector_swigregister = _cppcolleff.my_PartVector_swigregister
my_PartVector_swigregister(my_PartVector)

# This file is compatible with both classic and new-style classes.


