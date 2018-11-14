#!/usr/bin/env bash
SECONDS=0
racket herbie/src/herbie.rkt report --timeout '10800' --threads "yes" experiments/High_level.fpcore experiments/graphsHigh/
racket herbie/src/herbie.rkt report --timeout '10800' --threads "yes" experiments/Middle_level.fpcore experiments/graphsMiddle/
racket herbie/src/herbie.rkt report --timeout '10800' --threads "yes" experiments/Low_level.fpcore experiments/graphsLow/
duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
