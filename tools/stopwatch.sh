#!/bin/sh

now=$(date +%s)sec
logFile="./stopwatch-${now}.log"

function log {
    echo "$1" | tee -a "${logFile}"
}

log "${now}"

while true; do 
    read
    log "$(TZ=UTC date --date now-$now +%H:%M:%S.%N)"
done
