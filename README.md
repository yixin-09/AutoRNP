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

### Installation Instructions
