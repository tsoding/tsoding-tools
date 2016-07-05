#!/usr/bin/env bash

## General parameters
POLLING_INTERVAL=10
GITHUB_PROJECT="tsoding/dimooper"
# GITHUB_PROJECT="rexim/Morganey"

# # Trello parameters
# REST_API_URL="https://trello.com/1/list/56acc96e751324399cea0ce1/cards"
# JSON_JQ_EXTRACTOR=".[0].name"

# # Github Parameters
REST_API_URL="https://api.github.com/repos/${GITHUB_PROJECT}/issues?access_token=$ACCESS_TOKEN&labels=in+progress"
JSON_JQ_EXTRACTOR=".[0].title"

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
