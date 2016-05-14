#!/usr/bin/env bash

REST_API_URL="https://trello.com/1/list/56acc96e751324399cea0ce1/cards"

set -x

while true; do
    curl -s "$REST_API_URL" > in-progress.json
    echo -n "Current Activity: " > current-activity.txt
    if [ $(jq -r ".[0].name != null" in-progress.json) == "true" ]; then
        jq -r ".[0].name" in-progress.json >> current-activity.txt
    else
        echo "Farting" >> current-activity.txt
    fi
    sleep 10
done
