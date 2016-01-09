#!/bin/sh

PARAMETERS_FILE="$1"
TEMPLATE_FILE="$2"

echo "$(cat ./${PARAMETERS_FILE})\n\necho \"$(cat ./${TEMPLATE_FILE})\"" | sh
