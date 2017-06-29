#!/bin/bash

program=$1
runOn=$2
result=0
shift 2

for i in $@; do # For each threshold
  resultNew=`python2.7 $program $runOn $i` # Get the accuracy
  improve="$resultNew > $result"
  #improve=$improve|bc
  improve=`bc <<< $improve` # Boolean greater than
  if [ $improve -eq 1 ] # If the accuracy beats all past accuracies
  then
	result=$resultNew # Save the new best accuracy
	thr=$i # Save the new best threshold
  fi
done

echo The best threshold is $thr with accuracy $result
