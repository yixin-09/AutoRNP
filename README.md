## AutoRNP -- Automated Repair of High Floating-Point Errors in Numerical Libraries

AutoRNP is a dynamic analysis tool for automated detecting and repairing high floating-point errors in numerical programs.
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

### Requirements

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

### Installation Instructions
The project was developed on a 64-bit Linux platform (ubuntu 16.04 LTS). 
After cloning the repo, you need to do the following steps:

* Into the root directory of AutoRNP, and run "./autofig.sh" to 
install the required python package (see details in file "requirements.txt") and configure the benchmarks.

* Install pygsl-2.3.0 (on Ubuntu), and note that gsl must be installed before installing pygsl:


        $ python setup.py config
        $ python setup.py build
        $ sudo python setup.py install
 





### Running

To repeat the experiments on 20 GSL functions, just run "./run4GSL.sh" under the root directory of  AutoRNP, 
and all results will be produced and stored in "/experiments"

You can also configure the parameters of experiments by editing the file "repairGSL.py" in "/experiments".