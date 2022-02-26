
Use the command given below to set up RTC on raspberry pi

```wget -o https://raw.githubusercontent.com/adnan6336/RaspberryPiCodes/main/RTCCode/rtcInstall ; sudo bash rtcInstall```

*After successfull installation, use one of the command given below to set up the time for the first time only*

*set time using internet*

```sudo python3 /home/pi/DVR/Scripts/setRTCTime.py -i```

*set time manually*

```sudo python3 /home/pi/DVR/Scripts/setRTCTime.py```
