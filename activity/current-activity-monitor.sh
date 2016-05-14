#!/usr/bin/env bash

# REST_API_URL="https://trello.com/1/list/56acc96e751324399cea0ce1/cards"
# JSON_JQ_EXTRACTOR=".[0].name"
# POLLING_INTERVAL=10

REST_API_URL="https://api.github.com/repos/tsoding/voronoi-diagram/issues?labels=in+progress"
JSON_JQ_EXTRACTOR=".[0].title"
POLLING_INTERVAL=60

set -x

while true; do
    curl -s "$REST_API_URL" > in-progress.json
    echo -n "Current Activity: " > current-activity.txt
    if [ $(jq -r "$JSON_JQ_EXTRACTOR != null" in-progress.json) == "true" ]; then
        jq -r "$JSON_JQ_EXTRACTOR" in-progress.json >> current-activity.txt
    else
        echo "Farting" >> current-activity.txt
    fi
    sleep "$POLLING_INTERVAL"
done
