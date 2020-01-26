#!/bin/bash

# plz follow file naming conventions
for ((i = 1000; i >= 1; i--))
do
    unzip $i.zip
done
