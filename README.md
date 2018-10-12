## AutoRNP -- Automated repair of High Floating-Point Errors in Numerical Libraries

AutoRNP is a dynamic analysis tool for automated detecting and repairing high floating-point errors in numerical programs.
It includes following functions:

* Detecting high floating-point errors in a numerical program
* Generating piecewise quradraic functions to approximate the corresponding true mathematical function of the numerical program.
* Producing patch according to the piecewise quradraic functions
* Applying patch on the numerical program and testing the repaired program

AutoRNP is still pretty early in development, we had applied it on 20 numerical programs in GSL(GNU Scientific Library), 
and successfully repair 19 of 20.  
While AutoRNP is presented under the one-dimensional context, 
for future work, we plan to extend AutoRNP to be generally applicable to numerical program of higher dimensions.

AutoRNP is licensed under GPLv3. If that doesn't work for your use case, let us know, and we're happy to talk about licensing under other terms.

### Requirements

* python 2.7.14. You can install it by following commonds (on ubuntu):
    
    
        $ sudo add-apt-repository ppa:jonathonf/python-2.7
        
        $ sudo apt-get update
        
        $ sudo apt-get install python2.7
    
        $ python --version

* gsl-2.1 

    Download from the link below and Install (on ubuntu)::


        http://mirrors.ustc.edu.cn/gnu/gsl/

        $ ./configure | make | make install

* pygsl-2.3.0 (Install it later, see Installation Instructions). 

    Download from the link below:


        https://sourceforge.net/projects/pygsl/files/pygsl/





### Installation Instructions
The project was developed on a 64-bit linux platform (ubuntu 16.04 LTS). 
After cloning the repo, you should do following steps:

* Into the root directory of AutoRNP, and run "./autofig.sh" to 
install the required python package (details in file "requirements.txt") and configure the benchmarks.

* Install pygsl-2.3.0 (on ubuntu), before installing pygsl, gsl must be installed first:


        $ python setup.py build
        
        $ python setup.py install
 




### Running

To repeat the experiments on 20 GSL functions, just run "./run4GSL.sh", and all results will be generated and stored under "/experiments"

You can also configure the parameters of experiments by editing the file "repairGSL.py" in "/experiments".