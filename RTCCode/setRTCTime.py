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
import ntplib



while True:
    try:
        rtc = ds3231.SDL_DS3231(1, 0x68)
        if(len(sys.argv) > 1):
            if(sys.argv[1] == '-i'):
                print('Using Internet to set time')
                client=ntplib.NTPClient()
                response = client.request('pool.ntp.org')
                dateToSet = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(response.tx_time))
            else:
                print('wrong input')
                sys.exit()
        else:
            print('manually input to set time')
            print()
            x = input("Please input date and time (format: 2022-12-30 16:59:59): ")
            print()
            f = "%Y-%m-%d %H:%M:%S"
            datetime.datetime.strptime(x,f)
            dateToSet = x

        command = 'sudo date -s \"'+dateToSet+'\"'
#         print(command)
        stream = os.popen(command)
        time.sleep(1)
        rtc.write_now()
        time.sleep(0.5)
        print("Time Setup Completed! RTC Configured...")
        break
    except Exception as e:
        print(e)
        print("This is the incorrect format, must be in this format (format: 2022-12-30 16:59:59)")