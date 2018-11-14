from pygsl.testing import sf
from mpmath import *

#This file stores all functions (20) that need to be repaired

#f1
gf1 = lambda x: sf.airy_Ai(x,0)
rf1 = lambda x: airyai(x)
ef1 = lambda x: sf.airy_Ai_e(x,0)

#f2
gf2 = lambda x: sf.airy_Bi(x,0)
rf2 = lambda x: airybi(x)
ef2 = lambda x: sf.airy_Bi_e(x,0)


#f3
gf3 = lambda x: sf.airy_Ai_deriv(x,0)
rf3 = lambda x: airyai(x,1)
ef3 = lambda x: sf.airy_Ai_deriv_e(x,0)

#f4
gf4 = lambda x: sf.airy_Bi_deriv(x,0)
rf4 = lambda x: airybi(x,1)
ef4 = lambda x: sf.airy_Bi_deriv_e(x,0)

#f5
gf5 = sf.bessel_J0
rf5 = lambda x: besselj(0,x)
ef5 = sf.bessel_J0_e

#f6
gf6 = sf.bessel_J1
rf6 = lambda x: besselj(1,x)
ef6 = sf.bessel_J1_e

#f7
gf7 = sf.bessel_Y0
rf7 = lambda x: bessely(0,x)
ef7 = sf.bessel_Y0_e

#f8
gf8 = sf.bessel_Y1
rf8 = lambda x: bessely(1,x)
ef8 = sf.bessel_Y1_e

#f9
gf9 = sf.clausen
rf9 = lambda x: clsin(2,x)
ef9 = sf.clausen_e

#f10
gf10 = sf.expint_Ei
rf10 = lambda x: ei(x)
ef10 = sf.expint_Ei_e

#f11
gf11 = sf.legendre_P2
rf11 = lambda x: legendre(2,x)
ef11 = sf.legendre_P2_e

#f12
gf12 = sf.legendre_P3
rf12 = lambda x: legendre(3,x)
ef12 = sf.legendre_P3_e

#f13
gf13 = sf.legendre_Q1
rf13 = lambda x: legenq(1,0,x,type=3).real
ef13 = sf.legendre_Q1_e

#f14
gf14 = sf.psi
rf14 = lambda x: digamma(x)
ef14 = sf.psi_e


#f15
gf15 = sf.psi_1
rf15 = lambda x: psi(1,x)
ef15 = sf.psi_1_e


#f16
gf16 = sf.Chi
rf16 = lambda x: chi(x)
ef16 = sf.Chi_e

#f17
gf17 = sf.Ci
rf17 = lambda x: ci(x)
ef17 = sf.Ci_e

#f18
gf18 = sf.lnsinh
rf18 = lambda x: log(sinh(x))
ef18 = sf.lnsinh_e

#f19
gf19 = sf.zeta
rf19 = lambda x: zeta(x)
ef19 = sf.zeta_e

#f20
gf20 = sf.eta
rf20 = lambda x: altzeta(x)
ef20 = sf.eta_e

input_domain = [[[-1000.0, 1000.0]], [[-1000.0, 1000.0]], [[-1000.0, 1000.0]], [[-1000.0, 1000.0]], [[-1e+100, 1e+100]], [[-1e+100, 1e+100]], [[-1e+10, 1e+10]], [[-1e+10, 1e+10]], [[-823549.6645, 823549.6645]], [[-701.8334146820821, 701.8334146820821]], [[-1e+100, 1e+100]], [[-1e+100, 1e+100]], [[-1, 1e+100]], [[-262144.0, 1e10]], [[-10, 10000000000.0]], [[-701.8334146820821, 701.8334146820821]], [[0, 823549.6645]], [[0, 1e+100]], [[-170, 1000]], [[-168, 100]]]
rfl = [rf1, rf2, rf3, rf4, rf5, rf6, rf7, rf8, rf9, rf10, rf11, rf12, rf13, rf14, rf15, rf16, rf17, rf18, rf19, rf20]
gfl = [gf1, gf2, gf3, gf4, gf5, gf6, gf7, gf8, gf9, gf10, gf11, gf12, gf13, gf14, gf15, gf16, gf17, gf18, gf19, gf20]
efl = [ef1, ef2, ef3, ef4, ef5, ef6, ef7, ef8, ef9, ef10, ef11, ef12, ef13, ef14, ef15, ef16, ef17, ef18, ef19, ef20]
nrfl_fname = [u'airyai(x)', u'airybi(x)', u'airyai(x,1)', u'airybi(x,1)', u'besselj(0,x)', u'besselj(1,x)', u'bessely(0,x)', u'bessely(1,x)', u'clsin(2,x)', u'ei(x)', u'legendre(2,x)', u'legendre(3,x)', u'legenq(1,0,x)', u'digamma(x)', u'psi(1,x)', u'chi(x)', u'ci(x)', u'log(sinh(x))', u'zeta(x)', u'altzeta(x)']
ngfl_fname = [u'gsl_sf_airy_Ai', u'gsl_sf_airy_Bi', u'gsl_sf_airy_Ai_deriv', u'gsl_sf_airy_Bi_deriv', u'gsl_sf_bessel_J0', u'gsl_sf_bessel_J1', u'gsl_sf_bessel_Y0', u'gsl_sf_bessel_Y1', u'gsl_sf_clausen', u'gsl_sf_expint_Ei', u'gsl_sf_legendre_P2', u'gsl_sf_legendre_P3', u'gsl_sf_legendre_Q1', u'gsl_sf_psi', u'gsl_sf_psi_1', u'gsl_sf_Chi', u'gsl_sf_Ci', u'gsl_sf_lnsinh', u'gsl_sf_zeta', u'gsl_sf_eta']
ngfl_fname_exe = [u'gsl_sf_airy_Ai_e', u'gsl_sf_airy_Bi_e', u'gsl_sf_airy_Ai_deriv_e', u'gsl_sf_airy_Bi_deriv_e', u'gsl_sf_bessel_J0_e', u'gsl_sf_bessel_J1_e', u'gsl_sf_bessel_Y0_e', u'gsl_sf_bessel_Y1_e', u'gsl_sf_clausen_e', u'gsl_sf_expint_Ei_e', u'gsl_sf_legendre_P2_e', u'gsl_sf_legendre_P3_e', u'gsl_sf_legendre_Q1_e', u'gsl_sf_psi_e', u'gsl_sf_psi_1_e', u'gsl_sf_Chi_e', u'gsl_sf_Ci_e', u'gsl_sf_lnsinh_e', u'gsl_sf_zeta_e', u'gsl_sf_eta_e']
sngfl_fname = [u'airy_Ai', u'airy_Bi', u'airy_Ai_deriv', u'airy_Bi_deriv', u'bessel_J0', u'bessel_J1', u'bessel_Y0', u'bessel_Y1', u'clausen', u'xpint_Ei', u'legendre_P2', u'legendre_P3', u'legendre_Q1', u'psi', u'psi_1', u'Chi', u'Ci', u'lnsinh', u'zeta', u'ta']
test_inp = [-434.01660980268616, -422.09671545328115, -324.4642927988943, -405.65023907608304, 200.2771557933324, 3.831705970207512, 3.957678419314858,30.618286491641115,-78.53981633974483, 0.3725074107813666, -0.5773502691896258, 0.7745966692414834, 0.8335565596009646, -1829.8739199136473, -7.999999999999999, 0.5238225713898643, 3.3841804225511862, 0.881373587019543, -3.9999999999999996, -1.9999999999999998]



