# AutoRNP -- Automated Repair of High Floating-Point Errors in Numerical Libraries

AutoRNP is a dynamic analysis tool for automatically detecting and repairing high floating-point errors in numerical programs.
It includes following functions:

* Detecting high floating-point errors in a numerical program
* Generating piecewise quadratic functions to approximate the corresponding mathematical 
function that the numerical program attempts to implement.
* Producing patches according to the piecewise quadratic functions
* Applying patches on the numerical programs and testing the repaired program

AutoRNP is still under development, We had applied it on 20 numerical programs in GSL(GNU Scientific Library), 
and successfully repair 19 of 20.  
While AutoRNP is presented under the one-dimensional context, 
for future work, we plan to extend AutoRNP to be generally applicable to numerical programs of higher dimensions (over inputs).

AutoRNP is licensed under GPLv3. If that doesn't work for your use case, please contact with us, and we are glad to talk about licensing under other terms.

## Requirements

* python 2.7.14. 

    You can install it by following commands (on Ubuntu):
    
    
        $ sudo add-apt-repository ppa:jonathonf/python-2.7        
        $ sudo apt-get update        
        $ sudo apt-get install python2.7
        $ python --version

* gsl-2.1 

    Download from the link below and install (on Ubuntu)::


        http://mirrors.ustc.edu.cn/gnu/gsl/
        $ ./configure | make | make install

* mpfr 3.1.2-1

    Install:
    
        sudo apt-get install libmpfr-dev
    

* pygsl-2.3.0 

    Download from the link below:


        https://sourceforge.net/projects/pygsl/files/pygsl/

## Installation Instructions
The project was developed on a 64-bit Linux platform (ubuntu 16.04 LTS). 
After cloning the repo, you need to do the following steps:

* Into the root directory, and run "./autofig.sh" to 
install the required python package (see details in file "requirements.txt") and configure the benchmarks.

* Install pygsl-2.3.0 (on Ubuntu), and note that gsl must be installed before installing pygsl:


        $ python setup.py config
        $ python setup.py build
        $ sudo python setup.py install
 





## Running

The following are the instructions and explanations for the experments in the POPL 2019 paper:

    Efficient Automated Repair of High Floating-Point Errors in Numerical Libraries

In Section 5 of the paper, we propose an experimental
evaluation of our approach implemented by the new tool AutoRNP:
the main goal of following instructions is to repeat this experimental
evaluation.

The main structure of this project is as follows:
  * AutoRNP          --> source code of our tool
  * benchmarks       --> source code of 20 GSL functions that
                         our experiments were conducted on
  * experiments      --> scripts for repeating our experiments
  * paper_data       --> original experimental results
                         presented in our paper by AutoRNP
  * HBG              --> scripts and data for experiments on HBG           

Run the shell script:

$ ./run4GSL.sh

After a few hours (around 3 hours), experimental results will
be produced under the directory "/experiments".
Note: please change the system password "hello" in "experiments/repairGSL.py", "experiments/run_patch.py" and 
"experiments/apply_patch.py" to your own system password.


### Structure of experimental results:

The main structure of the experimental results (in "/experiments") is as follows:

    - experiments/detecting_results
        - DEMC              --> includes the detecting results by
                                our DEMC algorithm.
        - Detecting results are store in "DEMC/[function_name].xls"
          for each GSL function (e.g. "DEMC/gsl_sf_airy_Ai.xls").
          In [function_name].xls:
              -- "max_error": the maximum floating-point error by
                 DEMC.
              -- "input": the corresponding input that trigger
                 the maximum error.
              -- "execute time": the execution time of detecting
                 algorithm.
              -- "interval": the input interval includes the "input".
              -- "f1_n": the execution number of fitness1 function.
              -- "f2_n": the execution number of fitness2 function.
              -- "random seed": the random seed.
              -- "count" : repeat times of detecting method (i.e. 0..n)
              -- "gl_time": the execution time of differential
                 evolution algorithm


    - experiments/experiment_results
        - repair_results1  --> includes the approximations of the
                               original mathematical functions
                               and patches
            -- line+X      --> includes the approximations of the
                               original mathematical functions.
                               We store the approximations in format of
                               python list which cannot be understand
                               in text.
            -- test+X      --> includes the patches.
            (Note: X is in {1,2,3} which respectively corresponds to
            three repair thresholds {high, middle, low} in our paper,)
            -- A patch includes two files:
                 + patch_of_[function_name].c, e.g., patch_of_gsl_sf_airy_Ai.c,
                   which saves the C code repesentation of the
                   approximations of the original mathematical
                   functions. The file is to implement the
                   approximation to repair high floating-point
                   error in the original GSL functions.
                 + patch_of_[function_name], e.g., patch_of_gsl_sf_airy_Ai,
                   which is the patch file generate by "diff"
                   command. The file is to buid a new branch in
                   the source code of GSL function to call the
                   function in patch_of_[function_name].c .


    - table_results   --> includes the Excel tables storing
                          most experimental data
    - Experimental results are store in "table_results/experiment_results_total1.xls"
      In experiment_results_total1.xls:
          -- "program": the name of GSL functions.
          -- "Threshold": the repair threshold.
          -- "Bound": the repaired input interval
          -- "Bound_distance": the number of floating-point number
             in "Bound"
          -- "random_seed":random seed
          -- "PTB": the execution time of PTB algorithm
          -- "Repair": the execution time of Repair
          -- "Total": the total execution time
          -- "Patch size": the size of patch in Byte (e.g. 1000B)
          -- "Line number": the number of pieces of piecewise
             quaradic function that used to repair errors.
          -- Success rate: Testing results are also stored in the
	         table in column AF-AW, the two most important columns
	         are AJ and AT, AJ shows the success rate before repair,
             AT shows the success rate after repair. The success
             rate represents the proportion of the sample points
             that meet the repair threshold. After repair, the
             value in AT will equal to 1.0 for 19 of 20 GSL
             functions which means all the sample points meet
             the repair threshold after repairing for the 19 GSL
             functions.

#### Analyzing results:

Using the python script "plot_res.py" under the root directory
, we can plot the results stored in the Excel tables. Most of
similar tables and figures in our paper will produced in the same
directory as "plot_res.py", shell command is below:

$ python plot_res.py -f "experiments/experiment_results/table_results/experiment_results_total1.xls"

The illustration of produced tables and figures are following:

    * "benchmarks.xls":
        - Table 1 in our paper, shows the name and maximum error of subjects.
    * "benchAndResults.xls":
        - Table 2 in our paper, shows the repair time and success
          rate of repair.
    * "Hig_max.eps", "Mid_max.eps", "low_max.eps"
      "Hig_avg.eps", "Hig_avg.eps", "low_avg.eps":
        - Fig. 12 in our paper, shows the accuracy improving for
          three level repair. Each row represents the improvement
          in accuracy achieved by AutoNRP on a single benchmark.
          The thick arrow starts at the accuracy of the program
          before repair, and ends at the accuracy of the program
          after repair. A \textbf{triangle} is drawn at the value
          of error threshold for each subject . A \textbf{pentagram}
          is drawn at the value of mean error of each subject in its
          whole input domain.
    * "th2time2bound.eps":
        - Fig. 13 in our paper, shows the log2 value of repair
          time and size of the repaired input interval for each
          subject under three repair threshold.
    * "timeOverheadb.eps":
        - Fig. 14(a) in our paper, shows the cumulative distribution
          of the slowdown for subjects after repaired over the repaired
          input interval.
    * "timeOverheadW.eps":
        - Fig. 14(b) in our paper, shows the cumulative distribution
          of the slowdown for subjects after repaired over the whole
          input domain.
    * "storage.xls":
        - Table. 4 in our paper, shows the storage overhead by the
          size of patch file.


#### Analyzing results in "paper_data":

Original experimental results  on AutoRNP in our paper are mainly
store in the excel table "paper_data/experiment_results/table_results/experiment_results_total630.xls",
so run the command below, you can get the most of same tables and
figures in our paper

    $ python plot_res.py -f "paper_data/experiment_results/table_results/experiment_results_total630.xls"

### RUN HBG ON THE 20 FUNCTIONS
To run HBG on the 20 functions, please first install herbie (http://herbie.uwplse.org/doc/latest/installing.html) under the directory "HBG".

In the directory "HBG",
We have already collected the floating-point expressions that were
produced by Herbgrind when running on the 20 GSL functions. Files
store those expressions are named "High_level.fpcore", "Middle_level.fpcore"
and "Low_level.fpcore". We put those files in the directory "HBG/experiments".
In the directory "HBG", reviewers can run the following command to
use Herbie to improve those floating-point expressions:

    $ ./HBG_herbie_test.sh

After a few hours (more than 10 hours), results for each file will
be produced in three directories: "graphsHigh", "graphsMiddle",
"graphsLow" in the directory "HBG/experiments", and reviewers
can open the file "report.html" in each directory to view the
results reported by Herbie.
