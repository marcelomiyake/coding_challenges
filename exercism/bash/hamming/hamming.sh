#!/usr/bin/env bash

strandA=$1
strandB=$2
hammingDistance=0

if [ "$#" -ne 2 ]; then
  echo "Usage: hamming.sh <string1> <string2>"
  exit 1
fi

if [ "${#strandA}" != "${#strandB}" ]; then
  echo "strands must be of equal length"
  exit 1
fi

for ((i = 0; i < ${#strandA}; i++)); do
  if [ "${strandA:$i:1}" != "${strandB:$i:1}" ]; then
    let hammingDistance=$hammingDistance+1
  fi
done
echo $hammingDistance
