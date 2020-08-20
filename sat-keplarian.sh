#!/bin/bash

timestamp=$(date +"%d%m%y-%H%M%S")

filename="keps-${timestamp}.txt"

# different sources for TLE

#curl https://www.amsat.org/tle/current/nasabare.txt > ${filename}
curl https://celestrak.com/NORAD/elements/amateur.txt > ${filename}