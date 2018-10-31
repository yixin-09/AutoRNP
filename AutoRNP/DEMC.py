#The implementation of DEMC algorithm
import basic_function as bf
import time,signal
from scipy.optimize import differential_evolution
from scipy.optimize import basinhopping
import warnings
import math
import numpy as np
import os

class TimeoutError (RuntimeError):
    pass

def handler (signum, frame):
    raise TimeoutError()

signal.signal (signal.SIGALRM, handler)

def produce_interval(x,k):
    a = bf.getulp(x)*1e14
    return [np.max([x-a,k[0]]),np.min([x+a,k[1]])]

warnings.filterwarnings('error')

def reduce_x(a,b,x):
    x = float(x)
    return (a+b+(b-a)*math.sin(x))/2.0

def DEMC(rf,pf,inpdm,fnm,limit_n,limit_time):
    st = time.time()
    file_name = "../experiments/detecting_results/DEMC/" + fnm
    if not os.path.exists("../experiments/detecting_results/DEMC/"):
        os.makedirs("../experiments/detecting_results/DEMC/")
    count = 0
    final_max = 0.0
    final_x = 0.0
    final_count1 = 0
    final_count2 = 0
    final_bound = []
    record_res_l = []
    dom_l = bf.fdistribution_partition(inpdm[0], inpdm[1])
    glob_fitness_con = np.frompyfunc(lambda x: bf.fitness_fun1(rf, pf, x), 1, 1)
    glob_fitness_real = np.frompyfunc(lambda x: bf.fitness_fun(rf, pf, x), 1, 1)
    try:
        print "Detecting possible maximum error by DEMC algorithm"
        signal.alarm(limit_time)
        while(count<limit_n):
            temp_st=time.time()
            count1 = 0
            count2 = 0
            rand_seed = bf.rd_seed[count]
            np.random.seed(rand_seed)
            res_l = []
            for k in dom_l:
                temp_max = 0.0
                temp_x = 0.0
                res = differential_evolution(glob_fitness_con, popsize=15, bounds=[k], polish=False, strategy='best1bin')
                x = res.x[0]
                count2 = count2+res.nfev
                err = 1.0/glob_fitness_real(x)
                if err > temp_max:
                    temp_max = err
                    temp_x = x
                temp = [temp_max, temp_x, k]
                res_l.append(temp)
            t1 = time.time() - temp_st
            # print t1
            res_l = sorted(res_l, reverse=True)
            temp_max = res_l[0][0]
            temp_x = res_l[0][1]
            bound = res_l[0][2]
            res_lr = []
            s_len = np.min([len(res_l), 10])
            # print res_l[0:s_len]
            # glob_fitness_real_temp = lambda x: x*x
            minimizer_kwargs = {"method":"Nelder-Mead"}
            for j in res_l[0:s_len]:
                gen_l = produce_interval(j[1], j[2])
                glob_fitness_real_temp = lambda x: bf.fitness_fun(rf, pf, reduce_x(gen_l[0],gen_l[1],x))
                # glob_fitness_real_temp = lambda x: bf.fitness_fun(rf, pf, x)
                x = math.asin((2*j[1]-gen_l[0]-gen_l[1])/(gen_l[1]-gen_l[0]))
                # x = j[1]
                res = basinhopping(glob_fitness_real_temp,x,stepsize=bf.getulp(x)*1e10,minimizer_kwargs=minimizer_kwargs,niter_success=10,niter=200)
                count1 = count1 + res.nfev
                # x = res.x[0]
                x = reduce_x(gen_l[0],gen_l[1],res.x[0])
                err = 1.0/res.fun
                temp = [err, x, gen_l]
                res_lr.append(temp)
                if err > temp_max:
                    temp_max = err
                    temp_x = x
                    bound = j[2]
            t2 = time.time() - temp_st
            temp_l = [temp_max,temp_x,bound,t2,count1,count2,rand_seed,count,t1]
            # print temp_l
            final_count1 = final_count1+count1
            final_count2 = final_count2+count2
            record_res_l.append(temp_l)
            count = count + 1
            if temp_max>final_max:
                final_max=temp_max
                final_x = temp_x
                final_bound = bound
        final_time = time.time()-st
        bf.output_err(record_res_l, file_name, fnm)
        return [final_max, final_x, final_bound, final_time,count,final_count1,final_count2]
    except TimeoutError:
        final_time = time.time() - st
        bf.output_err(record_res_l,file_name,fnm)
        return [final_max, final_x, final_bound, final_time,count,final_count1,final_count2]



