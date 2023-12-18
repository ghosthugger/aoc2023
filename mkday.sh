#!/bin/bash

zpd=$(printf "%02d" $1)
mkdir $zpd
#cp -R template $zpd
#sed -i "s/template/day$zpd/g" $zpd/Cargo.toml

# Download input
# Put this in .cookie.txt
#  # Netscape HTTP Cookie File
#  .adventofcode.com    TRUE    /    FALSE    0    session    <token-copied-from-browser-devtools>
curl -o $zpd/input.txt --cookie .cookie.txt https://adventofcode.com/2023/day/$1/input
cp dayX.py $zpd/day$1.py
touch $zpd/day$1-2.py
touch $zpd/input-small.txt

