#!/bin/sh
/usr/local/bin/julius \
	-h /home/pi/julius/dictation-kit-4.5/model/phone_m/jnas-tri-3k16-gid.binhmm \
	-hlist /home/pi/julius/dictation-kit-4.5/model/phone_m/logicalTri \
	-input mic \
	-48 \
	-gram /home/pi/julius/sample2
