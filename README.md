# Internet Sentinel Application for the Raspberry Pi (RPI) that monitors the Internet connection
![Internet Sentinel Applicatin](assets/internet_sentinel_screenshot.png?raw=true "Internet Sentinel Screenshot")
in the Local Area Network and if not ON-LINE (Internet Server ping) will power cycle the cable
modem via the connected IoT Power Relay from Digital-loggers.com.  Will aslo performs a speed test
of your Internet connection and will power cycle your cable modem if the download speed reported is
below a threshold to attempt to get a faster connection to the ISP. Voice notifications are possible
with a set of speakers that connect to the headphone jack of the RPI.

## Equipment list (Amazon was chosen since they had all the parts needed. Parts are available elsewhere.)
Raspberry Pi 4 - https://www.amazon.com/dp/B07TLDTRYF/ref=cm_sw_em_r_mt_dp_U_DtCZEb9FHF451
32 GB Micro SD Card - https://www.amazon.com/dp/B06XWN9Q99/ref=cm_sw_em_r_mt_dp_U_5ECZEbB89KJWA
RPI Touchscreen Case - https://www.amazon.com/dp/B07WXK38YM/ref=cm_sw_em_r_mt_dp_U_vuCZEb07MR7HY
Touchscreen Display - https://www.amazon.com/dp/B0153R2A9I/ref=cm_sw_em_r_mt_dp_U_2tCZEbT87HJ67
Jumper wires (female connector and male pin on other end) - https://www.amazon.com/dp/B07GD2BWPY/ref=cm_sw_em_r_mt_dp_U_VuCZEbRXVE5CQ
Speakers - https://www.amazon.com/dp/B07SZ8CVWB/ref=cm_sw_em_r_mt_dp_U_GsCZEbZHWPGDJ
IoT Power Relay - https://www.amazon.com/dp/B00WV7GMA2/ref=cm_sw_em_r_mt_dp_U_pvCZEbP4FEGWJ

## Hardware Construction
See link below for more info and how to connect the RPI to the IoT Power Relay
https://www.digital-loggers.com/iotfaqs.html

Remove the IoT Power Relay green phoenix connector.  The entire light green connector block pulls out to expose
screw terminals that need loosened and male jumper wire pin inserted. Connect the two jumper wires (male jumper wire pin)
to the connector via the screw terminals and connect the female ends of the wires to the RPI GPIO header as
described below (See diagram below of exact location of GPIO header pins):
Connect the RPI header GPIO23 pin to the + side of the IoT Power Relay green phoenix connector.
Connect RPI header ground pin 14 next to and to the left of GPIO23 to the - side of the IoT Power Relay green phoenix
connector.
![Raspberry Pi Pinout Diagram](assets/raspberrypi_gpio_pinout.png?raw=true "RaspberryPiPinoutDiagram")

Insert the internet device (cable modem) plug into the IoT Power Relay outlet marked NORMALLY ON.

## Software Installation
Install the Internet Sentinel application software in this repository by cloning the repository files to the folder
/home/pi/internetSentinel on the Raspberry Pi.

The following application dependent packages need to be installed by performing the following:
sudo apt-get update
sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
sudo apt-get install espeak
sudo pip3 install speedtest-cli
sudo pip3 install num2words

Install the desktop icon application launcher:
cp /home/pi/internetSentinel/internetSentinel.desktop /home/pi/Desktop

Select the File Manager Icon (looks like a folder) in the desktop menubar
Select Edit on File Manager menu bar
Select Preferences menu item
Select General Tab
Select checkbox next to "Do not ask option on executable launch"
Exit out of File Manager

Configure RPI to wait for network on-line before booting.  Make sure you have the RPI connected to a LAN
wireless access point, router, or switch via CAT5e or higher Wired Ethernet cable then:
Select Boot-Options menu
Select Wait for Network at Boot
Select Yes

Add Internet Sentinel to startup when RPI boots by doing the following:
At command prompt enter the following to edit the autostart file:
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
Add the following line to bottom of the file:
@xset s off
@xset -dpms
@xset s noblank
@/usr/bin/python3 /home/pi/internetSentinel/internetSentinel.py
Save the file by depressing Ctrl-X

reboot the RPI via the following command:
/sbin/reboot

