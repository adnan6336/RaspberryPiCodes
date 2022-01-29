#!/usr/bin/env python

import sys
import time
import datetime
import random 
import ds3231
import os

rtc = ds3231.SDL_DS3231(1, 0x68)
dateToSet = rtc.read_datetime()


command = str(dateToSet)
print(command)



