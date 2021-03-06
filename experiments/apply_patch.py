import os
import time
import sys,getopt
import xlrd
import ast
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import AutoRNP.basic_function as bf
from Onevbench import *


def sudo_cmd(cmd):
    sudoPassword = 'hello'
    os.system('echo %s|sudo -S %s' % (sudoPassword, cmd))

def read_bound_randomSeed(exname,filename,k,fun_id):
    data = xlrd.open_workbook(exname)
    table = data.sheets()[0]
    id_k = k
    ret_l = []
    for i in [fun_id]:
        bound = ast.literal_eval(table.row_values(i*3+k)[2])
        rd_seed = int(table.row_values(i*3+k)[4])
        th = float(table.row_values(i*3+k)[1])
        pf = gfl[fun_id]
        rf = rfl[fun_id]
        ipdm = input_domain[fun_id][0]
        ret= bf.testRepair(bound,rd_seed,pf,rf,th,ipdm)
        ret_l.append(ret)
        k = k+2
    bf.testResultsToTable(exname,ret_l,id_k,0,fun_id)
    cwd = os.getcwd()
    os.chdir(filename+"patch")
    os.system("./patch_cmd.sh > tmp_log")
    os.chdir(filename)
    os.getcwd()
    os.system("cp *.c "+"../../../../benchmarks/gsl_src/gsl-2.1-repair/specfunc")
    os.chdir(cwd)
    sudo_cmd("./make_install.sh > tmp_log")
    sudo_cmd("rm tmp_log")

def main():
    begin_time = time.time()
    opts, args = getopt.getopt(sys.argv[1:], "n:t:i:", ["times=","threshold=","fun_id="])
    num = 0
    th = 0
    status = 0
    fun_id = 0
    ln = [0,3,2,1]
    for o, a in opts:
        if o in ('-n'):
            num = int(a)
            print num
        elif o in ('-t'):
            th = int(a)
        elif o in ('-i'):
            fun_id = int(a)
        else:
            print 'unhandled option'
            sys.exit(3)
    table_name = 'experiment_results/table_results/experiment_results_total'+str(num)+'.xls'
    folder_name = os.getcwd()
    file_name = folder_name+'/experiment_results/repair_results'+str(num)+ '/test'+str(th)+'/'
    read_bound_randomSeed(table_name,
                          file_name, ln[th],fun_id)




if __name__ == "__main__":
    main()

