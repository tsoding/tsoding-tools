#!/bin/sh

if [ -z "$1" ]; then
    now=$(date +%s)sec
else
    now="$1"
fi

logFile="./stopwatch-${now}.log"

function log {
    echo "$1" | tee -a "${logFile}"
}

echo "${now}"

while true; do 
    read
    log "$(TZ=UTC date --date now-$now +%H:%M:%S.%N)"
done
