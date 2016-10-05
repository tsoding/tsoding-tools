#!/bin/bash

downTime=0

lastAccessTime=$(date +"%s")

while [ true ]; do
    if ! ping -c1 google.com >& /dev/null; then
        downTime=$(( $(date +"%s") - $lastAccessTime ))
    else
        downTime=0
        lastAccessTime=$(date +"%s")
    fi

    sleep 15

    if [ $downTime -ge 300 ]; then
        echo "alert"
    fi
done
