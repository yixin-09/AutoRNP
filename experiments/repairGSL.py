import os
import xlwt
import numpy as np
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from AutoRNP.main import main
import AutoRNP.basic_function as bf
from Onevbench import *
from xlutils.copy import copy
import xlrd
import time



# the mean error for 20 GSL functions
mean_error_l = [2025112.1182000001, 234074.52411000003, 58280.480090000005, 135074.27234000002, 6.13516, \
                4.252680000000001, 1.0, 1.0, 12.22451, 1.90654, 1.5652000000000001, \
                1.5652800000000002, 1.83165, 10664.568519999999, 2.2533299999999996, 1.0, \
                2.02422, 1.0, 11.60261, 37.64867999999999]

def refresh():
    command = "rm -rf ../benchmarks/GSL_function/specfunc4patch/"
    command2 = "cp -R ../benchmarks/GSL_function/specfunc/. ../benchmarks/GSL_function/specfunc4patch/"
    os.system(command)
    os.system(command2)


def create_excel(table_name):
    book = xlwt.Workbook()
    sheet = book.add_sheet("sheet1")
    sheet.write(0, 0, "Programs")
    sheet.write(0, 1, "Threshold")
    sheet.write(0, 2, "Bound")
    sheet.write(0, 3, "Bound_distance")
    sheet.write(0, 4, "Before")
    sheet.write(0, 5, "After")
    sheet.write(0, 6, "PTB")
    sheet.write(0, 7, "Repair")
    sheet.write(0, 8, "Total")
    sheet.write(0, 9, "Patch Size")
    sheet.write(0, 10, "Line number")
    book.save(table_name)


def testBasedThreshold(num,fun_id,repair_enable,level,limit_time,rd_seed):
    filename = "experiment_results/table_results/"
    if not os.path.exists(filename):
        os.makedirs(filename)
    print "Random seed is :"+ str(rd_seed)
    i = fun_id*3
    #change it to youself password
    password = "hello"
    refresh()
    rf = rfl[fun_id]
    pf = gfl[fun_id]
    mean_error = mean_error_l[fun_id]
    inpdm = input_domain[fun_id][0]
    fnm = ngfl_fname[fun_id]
    limit_n = 100
    limit_n = 1
    # generate the inputs and max error in our paper
    inp = test_inp[fun_id]
    max_err= bf.getFPNum(rf(inp),pf(inp))
    max_ret=[max_err,inp]
    res = main(rf, pf, level, rd_seed, mean_error, inpdm, fnm, limit_time, limit_n, num, password,max_ret)
    ln = [0, 3, 2, 1]
    k = ln[int(level*10)]
    table_name = "experiment_results/table_results/experiment_results_total" + str(num) + ".xls"
    if not os.path.exists(table_name):
        create_excel(table_name)
    old_excel = xlrd.open_workbook(table_name, formatting_info=True)
    new_excel = copy(old_excel)
    sheet = new_excel.get_sheet(0)
    sheet.write(i + k, 0, res[0])
    sheet.write(i + k, 1, res[1])
    sheet.write(i + k, 2, str(res[3]))
    sheet.write(i + k, 3, res[4])
    sheet.write(i + k, 4, rd_seed)
    sheet.write(i + k, 5, "After")
    sheet.write(i + k, 6, res[2])
    sheet.write(i + k, 7, res[5])
    sheet.write(i + k, 8, res[6])
    sheet.write(i + k, 9, res[8])
    sheet.write(i + k, 10, res[9])
    new_excel.save(table_name)
    if repair_enable==1:
        print "begin repair original program and testing"
        test_time = time.time()
        cmd = "./run_experiment.sh " + str(num) + " " + str(int(level*10)) + " " + str(fun_id)
        test_time2 = time.time()-test_time
        print "The testing time is : " + repr(test_time2)
        os.system(cmd)
    else:
        print "Patch is generated"

st_time = time.time()
rd_seed = np.random.randint(0, 1e8, 1)[0]
np.random.seed(rd_seed)
repair_enable = 1
num = 1
for i in range(0,20):
    limit_time = 3600 * 3
    if i == 14 :
        # if you want to repair the gsl_sf_psi_1 function, change the time to more than 8 hours
        limit_time = 100
    print "*****************************************************"
    testBasedThreshold(num,i,repair_enable,0.1,limit_time,rd_seed)
    testBasedThreshold(num,i,repair_enable,0.2,limit_time,rd_seed)
    testBasedThreshold(num,i,repair_enable,0.3,limit_time,rd_seed)
print "Total time is :" + repr(time.time()-st_time)


