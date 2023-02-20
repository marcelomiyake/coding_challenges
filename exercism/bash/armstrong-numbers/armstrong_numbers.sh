#!/usr/bin/env bash

number=$1
exponent=${#number}
sum=0
for ((i = 0; i < $exponent; i++)); do
  ((sum = $sum + ${number:$i:1} ** $exponent))
done
if [ "$sum" = "$number" ]; then
  echo "true"
else
  echo "false"
fi
