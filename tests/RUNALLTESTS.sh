#!/bin/bash

#Note: due to line below using 'ls' (unreccomended), files cannot contain spaces. Other special characters are untested.
files=`ls *.py`

cd C:\\Users\\szymj\\Desktop\\Consume

index=0
for f in $files
do
	cd C:\\Users\\szymj\\Desktop\\Consume
	f=${f%".py"}
	
	if [ "$f" != '__init__' ]
	then
		index=$((index+1))
		printf "$index "
		python -m "tests.$f"
	fi
done

$SHELL
