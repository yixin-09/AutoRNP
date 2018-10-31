from detector import detectHighErrs
from detector import searchMaxErr
from extractor import iter_liner_build
import extractor as exr
from linerFinder import generate_fitting
import basic_function as bf
from GenPatch import covertToC
from GenPatch import combCovertToC
from GenPatch import patch_generate
import os
import signal
import time


class TimeoutError (RuntimeError):
    pass

def handler (signum, frame):
    raise TimeoutError()

signal.signal (signal.SIGALRM, handler)

def derivingApproximation(th,bound_l,rf,name,filename,inp):
    bound_idx = 0
    num_line = 0
    save_line = []
    exr.glob_point_l = []
    for bound in bound_l:
        temp_ploy_fit = ''
        n = int(bf.getFPNum(bound[0], bound[1]))
        ori_bound = bound
        print bound
        print
        print "%.12e" % float(bf.getFPNum(bound[0], bound[1]))
        # To make sure the length of bound less than a value (1e12)
        limit_of_bound = 1e12
        samll_bound_l = []
        ulp_x = bf.getulp(bound[0])
        # Step2: linear iterative approximation
        # partition the bound according to the limit_of_bound
        if n / limit_of_bound > 2.0:
            temp_bound0 = bound[0]
            temp_dis = limit_of_bound * ulp_x
            while (temp_bound0 + temp_dis < bound[1]):
                if (inp<temp_bound0 + temp_dis)&(inp>temp_bound0):
                    samll_bound_l.append([temp_bound0, inp])
                    samll_bound_l.append([inp, temp_bound0 + temp_dis])
                else:
                    samll_bound_l.append([temp_bound0, temp_bound0 + temp_dis])
                temp_bound0 = temp_bound0 + temp_dis
            samll_bound_l.append([temp_bound0, bound[1]])
            print len(samll_bound_l)
            print bound
            i = 0
            for idx_b in samll_bound_l:
                i = i + 1
                iter_liner_build(th, idx_b, rf, n)
        else:
            if (inp<bound[1])&(inp>bound[0]):
                iter_liner_build(th, [bound[0],inp], rf, n)
                iter_liner_build(th, [inp,bound[1]], rf, n)
            else:
                iter_liner_build(th, bound, rf, n)
        if len(exr.glob_point_l) >= 30:
            temp_ploy_fit = generate_fitting(exr.glob_point_l)
        covertToC(exr.glob_point_l, n, name, bound_idx, filename,ori_bound,temp_ploy_fit)
        save_line=save_line+exr.glob_point_l
        num_line = num_line+len(exr.glob_point_l)
        bound_idx = bound_idx + 1
        exr.glob_point_l = []
    return save_line,num_line



def main(rf,pf,level, rd_seed, mean_error, inpdm, fnm, limit_time, limit_n, num, password,max_ret):
    print "Begin repair the function "+fnm
    # generate file to store patch files
    filename = "../experiments/experiment_results/repair_results" + str(num) + "/test" + repr(int(level * 10))
    if not os.path.exists(filename):
        os.makedirs(filename)
    # generate file to save lines
    line_filename = "../experiments/experiment_results/repair_results" + str(num) + "/lines" + repr(int(level * 10))
    if not os.path.exists(line_filename):
        os.makedirs(line_filename)
    if not os.path.exists(filename + "/patch"):
        os.makedirs(filename + "/patch")
    # generate shell scripts to apply patches
    if os.path.exists(filename + "/patch/patch_cmd.sh"):
        os.remove(filename + "/patch/patch_cmd.sh")
    f = open(filename + "/patch/patch_cmd.sh", "w")
    f.write("#!/usr/bin/env bash\n")
    f.close()
    sudoPassword = password
    command = 'chmod 777 ' + filename + "/patch/patch_cmd.sh"
    os.system('echo %s|sudo -S %s' % (sudoPassword, command))
    # make sure remove the old patch
    if os.path.exists(filename + '/patch_of_' + fnm + ".c"):
        os.remove(filename + '/patch_of_' + fnm + ".c")
    # A list to store the results we want to save, e.g. the repair time, the size of bound
    res = []
    res.append(fnm)
    if max_ret == []:
        max_ret = searchMaxErr(rf,pf,inpdm,fnm,limit_time,limit_n)
    else:
	searchMaxErr(rf,pf,inpdm,fnm,limit_time,limit_n)
    num_line = 0
    staTime = time.time()
    try:
        signal.alarm(limit_time)
        # call the detector to find I_err
	print "Executing the PTB algorithm"
        max_x, bound, bound_l, th = detectHighErrs(max_ret, level, mean_error, rf, pf)
        t1 = time.time() - staTime
        res.append(th)
        res.append(t1)
        res.append(bound)
        bound_distance = bf.getFPNum(bound[0], bound[1])
        res.append(bound_distance)
        ori_bound = bound
        print bound
        print "The size of bound is: %.8e" % bound_distance
        # call the derivingApproximation to produce approximation and produce patch
        save_lines, num_line = derivingApproximation(th, bound_l, rf, fnm, filename, max_x)
        bf.save_line_list(line_filename + '/' + fnm + '.txt', save_lines)
        combCovertToC(bound_l, fnm, len(bound_l), filename)
        temp_t = time.time() - staTime
        res.append(temp_t)
        patch_generate(ori_bound, fnm, filename)
        total_time = time.time() - staTime
        res.append(total_time)
        res.append(rd_seed)
        print "Repair time: " + str(total_time)
        print "patch is generate, the name is " + 'patch_of_' + fnm + ".c"
        size_file = 0.0
        if os.path.exists(filename + '/patch_of_' + fnm + ".c"):
            size_file = os.path.getsize(filename + '/patch_of_' + fnm + ".c")
        res.append(size_file)
        res.append(num_line)
        bf.glob_point_l = []
        return res
    except TimeoutError:
        print 'timeout'
        res.append(0.0)
        res.append(0.0)
        res.append(rd_seed)
        res.append(0)
        res.append(0.0)
        res.append(0.0)
        return res


