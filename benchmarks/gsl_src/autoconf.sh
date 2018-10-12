#!/usr/bin/env bash
tar xvfz gsl-2.1.tar.gz
mv gsl-2.1 gsl-2.1-repair
cd gsl-2.1-repair
./configure
make
cd ..
cp -r gsl-2.1-repair gsl-2.1-src


