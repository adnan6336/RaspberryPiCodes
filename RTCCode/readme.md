
Use the command given below to set up RTC on raspberry pi

```wget -o https://raw.githubusercontent.com/adnan6336/RaspberryPiCodes/main/RTCCode/rtcInstall ; sudo bash rtcInstall```

*After successfull installation you must reboot by typing*

``` sudo reboot ```

*Then use one of the command given below to set up the time for the first time only*

*set time using internet*

```sudo python3 /home/pi/DVR/Scripts/setRTCTime.py -i```

*set time manually*

```sudo python3 /home/pi/DVR/Scripts/setRTCTime.py```

*Note the installation failed due to time out then one possible solution would be to first set your time in order to get the installation files from github.
for that, try this command.*

``` sudo date -s "yyyy-mm-dd"```
