#!/usr/bin/env python
#
# Test SDL_DS3231
# John C. Shovic, SwitchDoc Labs
# 08/03/2014
#
#

# imports

import sys
import time
import datetime
import random 
import ds3231
import os

dateToSet = time.strftime("%Y-%m-%d %H:%M:%S")
with open('/home/pi/DVR/DLogs/RTCBootTime.txt','a') as file:
    file.write('\nPi Time before Set : '+str(dateToSet))


rtc = ds3231.SDL_DS3231(1, 0x68)
dateToSet = rtc.read_datetime()
with open('/home/pi/DVR/DLogs/RTCBootTime.txt','a') as file:
    file.write(' || RTC Time : '+str(dateToSet))    


command = 'sudo date -s \"'+str(dateToSet)+'\"'
# print(command)
stream = os.popen(command)
# print(stream.read())
with open('/home/pi/DVR/DLogs/RTCBootTime.txt','a') as file:
    file.write(' || Pi Time after Set : '+str(stream.read()))

