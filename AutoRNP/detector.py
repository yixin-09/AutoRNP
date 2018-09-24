from DEMC import *
from PTB import *
import basic_function as bf

def searchMaxErr(rf,pf,inpdm,fnm,limit_time,limit_n):
    # DEMC: find the input max_x that trigger the maximum floating-point in a input domain
    res = DEMC(rf, pf, inpdm, fnm, limit_n, limit_time)
    return res

def detectHighErrs(ret, level, mean_error,rf,pf):
    max_x = ret[1]
    max_error = ret[0]
    #calculate the threshold
    th = np.log2(max_error) - np.max([np.log2(mean_error), 0.0])
    th = np.power(2, (th * level + np.max([np.log2(mean_error), 0.0])))
    #PTB: find the input interval includes the inputs higher than an give threshold
    bound = pointToBound(th, rf, pf, max_x)
    #Partition the bound into small intervals to keep same ulp value in each interval
    bound_l = bf.bound_partition(bound)
    return max_x, bound, bound_l, th

