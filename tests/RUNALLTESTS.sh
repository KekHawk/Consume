#!/bin/bash

for f in *.py
do
	cd C:\\Users\\szymj\\Desktop\\Consume
	f=${f%".py"}
	
	if [ "$f" != '__init__' ]
	then
		#printf "Running: $f"
		python -m "tests.$f"
	fi
done

$SHELL
