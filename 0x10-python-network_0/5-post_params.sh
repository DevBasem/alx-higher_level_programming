#!/bin/bash
# This script sends a POST request to the specified URL
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
