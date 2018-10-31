from detector import detectHighErrs
import basic_function as bf
from mpmath import *
import numpy as np
from scipy.optimize import differential_evolution
from scipy.optimize import minimize


#line_search + error compensation


#Build line with error compensation
def covetBoundTline(rf, bound, disbd):
    x0 = bound[0]
    x1 = bound[1]
    try:
        y0 = rf(bound[0])
    except (ValueError, ZeroDivisionError, OverflowError, Warning, TypeError):
        y0 = rf(bound[0]+bf.getulp(bound[0]))
    try:
        y1 = rf(bound[1])
    except (ValueError, ZeroDivisionError, OverflowError, Warning, TypeError):
        y1 = rf(bound[1]-bf.getulp(bound[1]))
    ulp_x0 = bf.getulp(x0)
    y1 = float(y1)
    y0 = float(y0)
    k = (y1 - y0) / (x1 - x0)
    delta_val = k * ulp_x0
    if bf.getulp(y1) < bf.getulp(y0):
        s_y = y1
        s_x = x1
        e_x = x0
        e_y = y0
    else:
        s_y = y0
        s_x = x0
        e_x = x1
        e_y = y1
    l_fun = lambda x: (x - s_x) * k + s_y
    if disbd == 2.0:
        return [(s_x, s_y), delta_val, bf.getMidDistance(x1, x0), 1.0, 1.0, x1, (x1, x0),(e_x, e_y)]
    glob_fitness_fun = np.frompyfunc(lambda x: bf.fitness_fun(rf,l_fun,x), 1, 1)
    # ret = differential_evolution(glob_fitness_fun,popsize=15, bounds=[bound])
    mid_point = x0 + (x1 - x0) / 2.0
    ret = minimize(glob_fitness_fun,[mid_point], bounds=[bound])
    mid_b = ret.x[0]
    if 1.0/glob_fitness_fun(mid_point) -1.0/ret.fun>0:
        mid_b = mid_point
        print "replace"
    max_err = float(rf(mid_point)) - l_fun(mid_point)
    estimate_max_error = (mid_point - x0) * (mid_point - x1)
    curve_k = float(max_err / estimate_max_error)
    if curve_k == 0.0:
        curve_k = 1.0
    return [(s_x, s_y), delta_val, bf.getMidDistance(x1, x0), 1.0,curve_k, mid_b, (x1, x0),
            (e_x, e_y)]


#produce the quadratic function
def lineAproFun(kb_val, x):
    i = kb_val[0]
    j = kb_val[7]
    if x == j[0]:
        return j[1]
    dv = kb_val[1]
    ulp_x = bf.getulp(x)
    if kb_val[4] == 0:
        compen = 0
    else:
        compen = (x-i[0])*(x-j[0]) * kb_val[4]
    rs = (x - i[0]) / ulp_x * dv + i[1] + compen
    return float(rs)


# iterative refine algorithm
glob_point_l = []
iter_nums = 0
iter_count = 0
def iter_liner_build(th, bound, rf, n):
    mp.dps = 30
    global glob_point_l
    global iter_nums
    disbd = bf.getFPNum(bound[0], bound[1])
    if disbd == 1:
        return 0
    kb_val = covetBoundTline(rf, bound, disbd)
    if disbd == 2:
        print kb_val
        glob_point_l.append(kb_val)
        return 0
    shadowFun = lambda x: lineAproFun(kb_val, x)
    glob_fitness_fun = np.frompyfunc(lambda x: bf.fitness_fun(rf, shadowFun, x), 1, 1)
    ret = differential_evolution(glob_fitness_fun, popsize=np.min([disbd, 15]), bounds=[bound])
    if ret.fun == 0:
        print ret.fun
        print ret.x
    max_err = 1.0 / glob_fitness_fun(ret.x[0])
    mid_point = kb_val[5]
    if max_err <= np.floor(th):
        glob_point_l.append(kb_val)
        return 0
    else:
        iter_liner_build(th, [bound[0], mid_point], rf, n)
        iter_liner_build(th, [mid_point, bound[1]], rf, n)





