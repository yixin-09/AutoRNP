#!/usr/bin/env bash
python apply_patch.py -n $1 -t $2 -i $3
python run_patch.py -n $1 -t $2 -i $3

