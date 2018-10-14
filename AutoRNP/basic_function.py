import numpy as np
import math
from mpmath import *
import struct
import xlwt
from scipy.optimize import differential_evolution
import pickle
import time
from xlutils.copy import copy
import xlrd

mp.prec = 200

# the random seed pool for people can repeating our experiments on detecting high floating-ponit errors,
# users can change it by generating new random number.
rd_seed = [82547955,18805512,51059660,67951510,96673401,92529168,43798981,\
           77041498,99700547,46432894,47637490,44611437,39774397,41271573,\
           4645333,25792865,3175680,69902962,60120588,56215621,86667354,\
           74905104,94207956,38027412,8741397,12937909,1370902,43545965,\
           47452337,66102720,86237691,61455401,14149645,39284815,92388247,\
           55354625,59213294,89102079,21502948,94527829,91610400,26056364,\
           41300704,79553483,78203397,20052848,70074407,21862765,17505322,\
           49703457,51989781,63982162,54105705,73199553,27712144,14028450,\
           57895331,88862329,99534636,50330848,14753501,65359048,62069927,\
           73549214,16226155,56551595,14029581,12154538,38929924,19960712,\
           85095147,72225765,25708618,28371123,55480794,21371248,7507139,\
           80070951,61317037,83546642,41962927,83218340,4355823,6686600,\
           18774345,84066402,41611436,22633123,45560493,11142569,37733241,\
           67382830,56461630,59719238,65235752,6412769,69435498,94266224,2120562,14276357]




def floatToRawLongBits(value):
	return struct.unpack('Q', struct.pack('d', value))[0]

def longBitsToFloat(bits):
	return struct.unpack('d', struct.pack('Q', bits))[0]


def fdistribution_partition(in_min, in_max):
    tmp_l = []
    a = np.frexp(in_min)
    b = np.frexp(in_max)
    tmp_j = 0
    if (in_min < 0)&(in_max > 0):
        if in_min >= -1.0:
            tmp_l.append([in_min, 0])
        else:
            for i in range(1, a[1]+1):
                tmp_i = np.ldexp(-0.5, i)
                tmp_l.append([tmp_i, tmp_j])
                tmp_j = tmp_i
            if in_min != tmp_j:
                tmp_l.append([in_min, tmp_j])
        tmp_j = 0
        if in_max <= 1.0:
            tmp_l.append([0, in_max])
        else:
            for i in range(1, b[1]+1):
                tmp_i = np.ldexp(0.5, i)
                tmp_l.append([tmp_j, tmp_i])
                tmp_j = tmp_i
            if in_max != tmp_j:
                tmp_l.append([tmp_j, in_max])
    if (in_min < 0) & (0 >= in_max):
        if in_min >= -1:
            tmp_l.append([in_min, in_max])
            return tmp_l
        else:
            if in_max > -1:
                tmp_l.append([-1, in_max])
                tmp_j = -1.0
                for i in range(2, a[1] + 1):
                    tmp_i = np.ldexp(-0.5, i)
                    tmp_l.append([tmp_i, tmp_j])
                    tmp_j = tmp_i
                if in_min != tmp_j:
                    tmp_l.append([in_min, tmp_j])
            else:
                if a[1] == b[1]:
                    tmp_l.append([in_min, in_max])
                    return tmp_l
                else:
                    tmp_j = np.ldexp(-0.5, b[1]+1)
                    tmp_l.append([tmp_j, in_max])
                    if tmp_j != in_min:
                        for i in range(b[1]+2, a[1]+1):
                            tmp_i = np.ldexp(-0.5, i)
                            tmp_l.append([tmp_i, tmp_j])
                            tmp_j = tmp_i
                        if in_min != tmp_j:
                            tmp_l.append([in_min, tmp_j])
    if (in_min >= 0) & (in_max > 0):
        if in_max <= 1:
            tmp_l.append([in_min, in_max])
            return tmp_l
        else:
            if in_min < 1:
                tmp_l.append([in_min, 1])
                tmp_j = 1.0
                for i in range(2, b[1] + 1):
                    tmp_i = np.ldexp(0.5, i)
                    tmp_l.append([tmp_j, tmp_i])
                    tmp_j = tmp_i
                if in_max != tmp_j:
                    tmp_l.append([tmp_j, in_max])
            else:
                if a[1] == b[1]:
                    tmp_l.append([in_min, in_max])
                    return tmp_l
                else:
                    tmp_j = np.ldexp(0.5, a[1]+1)
                    tmp_l.append([in_min, tmp_j])
                    if tmp_j != in_max:
                        for i in range(a[1]+2, b[1]+1):
                            tmp_i = np.ldexp(0.5, i)
                            tmp_l.append([tmp_j, tmp_i])
                            tmp_j = tmp_i
                        if in_max != tmp_j:
                            tmp_l.append([tmp_j, in_max])
    return tmp_l


#calculate the condition number: a is input; b is output; f is the numerical program
def condition(a,b,f):
    try:
        if math.fabs(b) < 2.2250738585072014e-308:
            j = 4.94065645841e-324
        else:
            j = b*2.2e-16
        i = a*2.220446049250313e-15
        ab = (f(a + i) - b)
        y = math.fabs(ab*1e-1/j)
        return y
    except Warning:
        y = 1.0
        return y


#return the 1/condition
def fitness_fun1(rf,pf,inp):
    try:
        b = pf(inp)
        res = condition(inp, b, pf)
        if (res == 0.0)|(np.isnan(res))|(res>np.finfo(np.double).max):
            res = 1.0
        else:
            res = 1.0/res
        return float(res)
    except (ValueError, ZeroDivisionError, OverflowError, Warning,TypeError) as e:
        return 1.0

#get the FPNum between two floating-point numbers
def getFPNum(a,b):
    ia = floatToRawLongBits(np.abs(a))
    ib = floatToRawLongBits(np.abs(b))
    zo = floatToRawLongBits(0)
    if sign(a)!=sign(b):
        res = abs(ib-zo)+abs(ia-zo)
    else:
        res = abs(ib-ia)
    return int(res+1)

# return the 1.0/FPNum
def fitness_fun(rf, pf, inp):
    try:
        inp = float(inp)
        r_val = float(rf(inp))
        p_val = float(pf(inp))
        if math.fabs(p_val) > np.finfo(np.double).max:
            return 1.0
        if math.fabs(r_val) > np.finfo(np.double).max:
            return 1.0
    except (ValueError, ZeroDivisionError, OverflowError, Warning, TypeError):
        return 1.0
    res = float(getUlpError(r_val, p_val))
    if (res == 0.0) | (np.isnan(res)):
        res = 1.0
    else:
        res = 1.0 / res
    if res == 0.0:
        res = 1.0
    return float(res)


def getulp(x):
    x = float(x)
    k = frexp(x)[1]-1
    if x == 0.0:
        return pow(2, -1074)
    if (k<1023)&(k>-1022):
        return pow(2,k-52)
    else:
        return pow(2,-1074)



def getMidDistance(a,b):
    ia = floatToRawLongBits(np.abs(a))
    ib = floatToRawLongBits(np.abs(b))
    zo = floatToRawLongBits(0)
    if sign(a)!=sign(b):
        res = abs(ib-zo)+abs(ia-zo)
    else:
        res = abs(ib-ia)
    if (sign(a)==sign(b))&(ib == ia):
        return 0
    return int(res)


def max_errorOnPoint(rf,pf,inp,step):
    ulp_inp = getulp(inp)
    glob_fitness_fun = np.frompyfunc(lambda x: fitness_fun(rf, pf, x), 1, 1)
    bn = np.max([step*1e-5,100])
    ret = differential_evolution(glob_fitness_fun,popsize=10,bounds=[[inp-bn*ulp_inp,inp+bn*ulp_inp]])
    return 1.0/ret.fun,ret.x[0]


def output_err(t_l,name,name2):
    book = xlwt.Workbook()
    sheet = book.add_sheet("sheet1")
    sheet.write(0, 0, "functions")
    sheet.write(0, 1, "max_error")
    sheet.write(0, 2, "input")
    sheet.write(0, 3, "interval")
    sheet.write(0, 4, "execute time")
    sheet.write(0, 5, "f1_n")
    sheet.write(0, 6, "f2_n")
    sheet.write(0, 7, "random_seed")
    sheet.write(0, 8, "count")
    sheet.write(0, 9, "gl_time")
    n = 1
    for t in t_l:
        sheet.write(n,0,name2)
        for k in range(0,len(t)):
            sheet.write(n,k+1,repr(t[k]))
        n = n+1
    book.save(name+".xls")

def save_line_list(file_name,l):
    with open(file_name, "wb") as fp:
        pickle.dump(l, fp)


def bound_partition(bound):
    db = bound[0]
    ub = bound[1]
    bound_l = []
    tmp_b = bound[0]
    if getulp(db) != getulp(ub):
        sdb = np.sign(np.frexp(db)[0])
        edb = np.frexp(db)[1]
        sedb = np.sign(bound[0])
        print edb
        print sedb
        while (1):
            tmp_0 = 0.5 * sdb
            # print
            # print tmp_0
            # print edb
            if sedb > 0:
                edb = int(edb + sedb)
            up_b = np.ldexp(tmp_0, edb)
            if sedb < 0:
                edb = int(edb + sedb)
            print up_b
            if edb < -1022:
                print up_b
                edb = int(edb - sedb)
                print edb
                bound_l.append([tmp_b, 0])
                sdb = -1 * sdb
                sedb = -1 * sedb
            if up_b > bound[1]:
                if tmp_b != bound[1]:
                    bound_l.append([tmp_b, bound[1]])
                break
            if tmp_b != up_b:
                if getulp(tmp_b)==getulp(up_b):
                    bound_l.append([tmp_b, up_b])
                    ulp_b = getulp(up_b + getulp(up_b))
                    tmp_b = up_b + ulp_b
                else:
                    bound_l.append([tmp_b, up_b-getulp(tmp_b)])
                    tmp_b = up_b
    else:
        bound_l.append(bound)
    return bound_l


def getUlpError(a,b):
    try:
        ia = floatToRawLongBits(np.abs(a))
        ib = floatToRawLongBits(np.abs(b))
        zo = floatToRawLongBits(0)
        if sign(a)!=sign(b):
            res = abs(ib-zo)+abs(ia-zo)
        else:
            res = abs(ib-ia)
        return int(res+1)
    except (ValueError, ZeroDivisionError, OverflowError, Warning,TypeError):
        return 1.0


####################################################
# functions for testing module
#
####################################################

def random_test(pf,rf,bound,rd_seed,th):
    np.random.seed(rd_seed)
    dis_num = getFPNum(bound[0],bound[1])
    if dis_num<100000:
        num = dis_num
    else:
        num = 100000
    num = 1000
    X = np.random.uniform(bound[0], bound[1], num)
    err_l = []
    X_good = []
    X_bad = []
    start_time = time.time()
    errfun = np.frompyfunc(lambda x: getUlpError(rf(x), pf(x)), 1, 1)
    res_l = errfun(X)
    for i in res_l:
        dis_err = i
        err_l.append(dis_err)
        if dis_err - th <= 1.0:
            X_good.append((i, dis_err))
        else:
            X_bad.append((i, dis_err))
    test_time = time.time() - start_time
    g_num = len(X_good)
    success_rate = float(g_num) / float(num)
    mean_err = np.float_power(2, np.mean(np.log2(err_l)))
    max_err = np.max(err_l)
    return success_rate, mean_err, max_err, test_time

def test_pf(pf,inp):
    try:
        p_val = float(pf(inp))
    except (ValueError,ZeroDivisionError,OverflowError,Warning,TypeError):
        return 1.0

def just_run_pf(pf,bound,rd_seed):
    np.random.seed(rd_seed)
    limit_n = 10000000
    limit_n = 1000
    pf_array = np.frompyfunc(lambda x: test_pf(pf,x), 1, 1)
    dis_num = getFPNum(bound[0],bound[1])
    if dis_num<limit_n:
        num = dis_num
    else:
        num = limit_n
    X = np.random.uniform(bound[0], bound[1], num)
    start_time = time.time()
    pf_array(X)
    test_time1 = time.time() - start_time
    return test_time1


def find_max(pf,rf,bound):
    bound_distance = getFPNum(bound[0],bound[1])
    popsize = 15+int(np.max([np.log2(bound_distance/1e9),1.0]))*2
    glob_fitness_fun = np.frompyfunc(lambda x: fitness_fun(rf, pf, x), 1, 1)
    ret = differential_evolution(glob_fitness_fun, popsize=popsize,maxiter=2000,bounds=[bound])
    return [1/ret.fun,ret.x]

def testRepair(bound,rd_seed,pf,rf,th,ipdm):
    ret = find_max(pf,rf,bound)
    # ret = [[1.0],[1.0]]
    ret_t = random_test(pf,rf,bound,rd_seed,th)
    # ret_t = [0,0,0,0]
    rt1 = just_run_pf(pf,bound,rd_seed)
    rt2 = just_run_pf(pf,ipdm,rd_seed)
    return ret,ret_t,rt1,rt2

def testRepairMax(bound,rd_seed,i,th):
    begin_time = time.time()
    ret = find_max(i,bound)
    ex_t = time.time()-begin_time
    return ret,ex_t


def testResultsToTable(exname,ret_l,k,id,fun_id):
    old_excel = xlrd.open_workbook(exname, formatting_info=True)
    new_excel = copy(old_excel)
    ws = new_excel.get_sheet(0)
    ws.write(0,4,"random_seed")
    if id == 0:
        name1 = "Max_error_before"
        name2 = "Testing_time_before"
        name3 = "Average_error_before"
        name4 = "input"
        name5 = "success_rate_before"
        name6 = "random_test_time_badland"
        name7 = "random_test_time_whole"
        name8 = "random_max_error"
    else:
        name1 = "Max_error_after"
        name2 = "Testing_time_after"
        name3 = "Average_error_after"
        name4 = "input_after"
        name5 = "success_rate_after"
        name6 = "random_test_time_badland"
        name7 = "random_test_time_whole"
        name8 = "random_max_error"
    temp_id = id*10+31
    ws.write(0, temp_id,name1)
    ws.write(0, temp_id + 1,name2)
    ws.write(0, temp_id + 2, name3)
    ws.write(0, temp_id + 3, name4)
    ws.write(0, temp_id + 4, name5)
    ws.write(0, temp_id + 5, name6)
    ws.write(0, temp_id + 6, name7)
    ws.write(0, temp_id + 7, name8)
    for i in [fun_id]:
        ws.write(i*3+k,temp_id,str(ret_l[0][0][0]))
        ws.write(i*3+k,temp_id+1,ret_l[0][1][3])
        ws.write(i*3+k,temp_id+2,ret_l[0][1][1])
        ws.write(i*3+k,temp_id+3,str(ret_l[0][0][1][0]))
        ws.write(i*3+k,temp_id+4,str(ret_l[0][1][0]))
        ws.write(i*3+k,temp_id+5,str(ret_l[0][2]))
        ws.write(i*3+k,temp_id+6,str(ret_l[0][3]))
        ws.write(i*3+k,temp_id+7,str(ret_l[0][1][2]))
        k = k+2
    new_excel.save(exname)