#!/bin/bash

timestamp=$(date +"%d%m%y-%H%M%S")

filename="keps-${timestamp}.txt"

curl https://www.amsat.org/tle/current/nasabare.txt > ${filename}