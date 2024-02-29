#!/bin/bash
# This script sends a JSON POST request to a URL and displays the body of the response

# Check if the file is a valid JSON
if python3 -m json.tool "$2" > /dev/null 2>&1; then
    curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
else
    echo -n "Not a valid JSON"
fi
