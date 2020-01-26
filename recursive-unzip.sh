#!/bin/bash
export TARGET=target.zip

while :
do
    export RESULT=$(unzip $TARGET 2>&1)
    export TARGET=$(echo $RESULT | cut -d' ' -f4) # get inside file name
done
