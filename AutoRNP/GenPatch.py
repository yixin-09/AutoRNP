import sys
import basic_function as bf
import os



def exists_in_file(filename,s):
    exists = 0
    fo = open(filename)
    line = fo.readline()
    # Loop until EOF
    while line != '':
        # Search for string in line
        index = line.find(s)
        if (index != -1):
            exists = 1
            break
        # Read next line
        line = fo.readline()
    # Close the files
    fo.close()
    return exists

def line_in_file(filename,s):
    fo = open(filename)
    line = fo.readline()
    # Initialize counter for line number
    line_no = 1
    exists = 0
    # Loop until EOF
    while line != '':
        # Search for string in line
        index = line.find(s)
        if (index != -1):
            insert_line = line_no + 1
            break
        # Read next line
        line = fo.readline()
        # Increment line counter
        line_no += 1
    # Close the files
    fo.close()
    return insert_line

def patch_generate(ori_bound, name, ori_filename):
    if name in [u'gsl_sf_zeta', u'gsl_sf_eta']:
        x = "s"
    else:
        x = "x"
    print "Generate patch"
    ori_filename = ori_filename+"/"
    orig_stdout = sys.stdout
    filename = "../benchmarks/GSL_function/" + name + '_patch.txt'
    f = open(filename, 'w')
    sys.stdout = f
    print "#include \"patch_of_" + name + ".c\""
    print "if(("+x+"<=" + repr(ori_bound[1]) + ")&&("+x+">=" + repr(ori_bound[0]) + ")){"
    print " result->val = accuracy_improve_patch_of_" + name + "("+x+");"
    print " result->err = GSL_DBL_EPSILON * fabs(result->val);"
    print " return GSL_SUCCESS;"
    print "}"
    sys.stdout = orig_stdout
    f.close()
    f = open(filename, "r")
    contents = f.readlines()
    f.close()
    fun_name = "EVAL_RESULT("+name+"_e"+"("
    cfun_name = name+"_e"
    search_path = "../benchmarks/GSL_function/specfunc4patch/"
    if not os.path.exists(search_path):
        search_path = "."
    source_list = os.listdir(search_path)
    insert_line = 0
    # Repeat for each file in the directory
    insert_fname = ""
    for fname in source_list:
        exists = exists_in_file(search_path + fname, fun_name)
        if exists == 1:
            if name in [u'gsl_sf_psi', u'gsl_sf_psi_1']:
                cfun_name = 'int '+cfun_name
            insert_line = line_in_file(search_path + fname, cfun_name)
            insert_fname = fname
    patch_name = name+"_patch.c"
    cp_cmd = "cp -f "+ "../benchmarks/GSL_function/specfunc4patch/" + insert_fname+" "+ori_filename+"patch/" + patch_name
    os.system(cp_cmd)
    f = open(ori_filename+"patch/" +patch_name, "r")
    new_contents = f.readlines()
    f.close()
    for j in range(1,len(contents)):
        new_contents.insert(insert_line," "+contents[j])
        insert_line = insert_line + 1
    new_contents.insert(25, contents[0])
    f = open(ori_filename+"patch/" + patch_name, "w")
    new_contents = "".join(new_contents)
    f.write(new_contents)
    f.close()
    gen_path_cmd = "diff -Naur "+ "../benchmarks/GSL_function/specfunc4patch/" + insert_fname+" "+ori_filename+"patch/" +patch_name + "> "+ori_filename+"patch/" +"patch_of_" + name
    os.system(gen_path_cmd)
    cp_back = "cp -f "+ ori_filename+"patch/" +patch_name + " " + "../benchmarks/GSL_function/specfunc4patch/" + insert_fname
    os.system(cp_back)
    rm_code = "rm " + ori_filename+"patch/" +patch_name
    os.system(rm_code)
    osname = os.path.dirname(os.getcwd())
    apply_patch = "patch " + osname+"/benchmarks/gsl_src/gsl-2.1-repair/specfunc/"+insert_fname + " "+"patch_of_" + name+"\n"
    f = open(ori_filename + "patch/patch_cmd.sh", "a")
    f.write(apply_patch)
    f.close()

def covertToC(glob_l,n,name,idx,filename,bound,temp_ploy_fit):
    print "Cover To C code"
    orig_stdout = sys.stdout
    name = 'patch_of_'+name
    len_glob = len(glob_l)
    x_0 = bound[0]
    ulp_x = bf.getulp(glob_l[0][0][0])
    temp_n = 0.0
    temp_n_max = 0.0
    f = open(filename+'/'+name+'.c', 'a')
    name = name.split("gsl_")[1]
    sys.stdout = f
    print 'static double array_x_'+name+'_'+str(idx)+'['+ str(len_glob) + '] = {'
    for i in glob_l:
        print "%.18e," % i[0][0]
    print '};'
    print 'static double array_y_'+name+'_'+str(idx)+'[' + str(len_glob) + '] = {'
    for i in glob_l:
        print "%.18e," % i[0][1]
    print '};'
    print 'static double array_e_y_' + name + '_' + str(idx) + '[' + str(len_glob) + '] = {'
    for i in glob_l:
        print "%.18e," % i[7][1]
    print '};'
    print 'static double array_detla_'+name+'_'+str(idx)+'[' + str(len_glob) + '] = {'
    for i in glob_l:
        print "%.18e," % i[1]
    print '};'
    print 'static double array_idx_'+name+'_'+str(idx)+'[' + str(len_glob+1) + '] = {'
    print "%.18e," % temp_n
    for i in glob_l:
        print "%.18e," % (i[2]+temp_n)
        temp_n = i[2]+temp_n
    print '};'
    # print 'static double array_maxX_' + str(idx) + '[' + str(len_glob) + '] = {'
    # for i in glob_l:
    #     print "%.15e," % (i[3]+temp_n_max)
    #     temp_n_max = (i[2]+temp_n_max)
    # print '};'
    print 'static double array_maxE_' +name+'_'+ str(idx) + '[' + str(len_glob) + '] = {'
    for i in glob_l:
        print "%.18e," % i[4]
    print '};'
    print "double accuracy_improve_patch_of_gsl_"+name+'_'+str(idx)+"(double x)"
    print "{"
    print " long int n = "+str(n)+";"
    print " int len_glob = "+str(len_glob)+";"
    print " double ulp_x = " + repr(ulp_x)+";"
    print " double x_0 = " + repr(x_0)+";"
    print " double compen = 0.0;"
    print " double n_x = ((x-x_0)/ulp_x);"
    if temp_ploy_fit == '':
        # print " int idx = floor(n_x*len_glob/n);"
        print " int idx = floor(len_glob/2);"
    else:
        print temp_ploy_fit
        print " if(idx>=len_glob){"
        print "         idx = len_glob-1;"
        print " }"
    print " while((idx>=0)&&(idx<len_glob)){"
    print "     if((n_x>array_idx_"+name+'_'+str(idx)+"[idx])&&(n_x<array_idx_"+name+'_'+str(idx)+"[idx+1])){"
    print "         compen = ulp_x*ulp_x * (n_x-array_idx_"+name+'_'+str(idx)+"[idx+1])*(n_x-array_idx_"+name+'_'+str(idx)+"[idx])*array_maxE_"+name+'_'+str(idx)+"[idx];"
    print "         return (x-array_x_"+name+'_'+str(idx)+"[idx])/ulp_x*array_detla_"+name+'_'+str(idx)+"[idx]+array_y_"+name+'_'+str(idx)+"[idx]+compen;"
    print "     }"
    print "     else if(n_x<array_idx_"+name+'_'+str(idx)+"[idx]){"
    print "         idx = idx - 1;"
    print "     }"
    print "     else if(n_x>array_idx_"+name+'_'+str(idx)+"[idx+1]){"
    print "         idx = idx + 1;"
    print "     }"
    print "     else if(x==array_x_"+name+'_'+str(idx)+"[idx]){"
    print "         return array_y_"+name+'_'+str(idx)+"[idx];"
    print "     }"
    print "     else{"
    print "         return array_e_y_"+name+'_'+str(idx)+"[idx];"
    print "     }"
    print " }"
    print "}"
    sys.stdout = orig_stdout
    f.close()



def combCovertToC(bound_l,name,bl,filename):
    print "Cover To C code"
    orig_stdout = sys.stdout
    name = 'patch_of_' + name
    f = open(filename +'/'+name + '.c', 'a')
    idx = 0
    sys.stdout = f
    print "double accuracy_improve_" + name +"(double x)"
    print "{"
    for i in bound_l:
        print "if(x<="+repr(i[1])+"){"
        print " return accuracy_improve_" + name + '_' + str(idx) + "(x);"
        print "}"
        idx = idx+1
    print "}"
    sys.stdout = orig_stdout
    f.close()
