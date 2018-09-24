#!/usr/bin/env bash
for i in `seq 1100 1100`
do
	echo $i
	for j in 3 2 1
	do
		python apply_patch.py -n $i -t $j
		python run_patch.py -n $i -t $j
	done
done
