#!/bin/bash

timestamp=$(date +"%d%m%y-%H%M%S")

filename="satslist-${timestamp}.txt"

curl http://www.ne.jp/asahi/hamradio/je9pel/satslist.htm > ${filename}
