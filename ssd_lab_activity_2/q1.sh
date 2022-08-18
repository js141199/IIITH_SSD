#!/bin/bash

read filePath

lines=$(wc -l < $filePath)

n=$((lines/2))

if (( lines%2 == 1 ))
then
	n=$((n+1))
fi

awk '{ if(NR=='$n') print $0 }' $filePath

