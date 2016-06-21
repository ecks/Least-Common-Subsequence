#!/bin/bash

for i in {1..5}
do
  perc=$(echo "$i*0.2" | bc)
  python randomize.py -i input -o input_1 -p $perc -P $perc 
  python queue_clear_stream.py -i input_1 -o vote_1
  python queue_clear_all.py -i input_1 -o vote_2
  output1=`python metric.py -i input -I vote_1`
  output2=`python metric.py -i input -I vote_2`
  echo $output1
  echo $output2
done
