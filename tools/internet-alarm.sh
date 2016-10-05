#!/bin/sh

set -xe

downTime=0

lastAccessTime=$(date +"%s")

while [ true ]; do
    if ! ping -c1 -W10 google.com >& /dev/null; then
        downTime=$(( $(date +"%s") - $lastAccessTime ))
    else
        downTime=0
        lastAccessTime=$(date +"%s")
    fi

    sleep 1

    if [ $downTime -ge 5 ]; then
        mpg123 "erro.mp3"
        exit 1
    fi
done
