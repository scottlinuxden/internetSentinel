# Internet Sentinel Application
![Internet Sentinel Applicatin](assets/internet_sentinel_screenshot.png?raw=true "InternetSentinelScreenshot")

Internet Sentinel is a software and hardware solution that monitors the Internet connection in a Local Area Network 
and if not ON-LINE (checked via Internet Server ping) will power cycle an attached cable modem via the connected 
IoT Power Relay from Digital-loggers.com.  Will aslo performs a speed test of your Internet connection and will power 
cycle your cable modem if the download speed reported is below a threshold to attempt to get a faster connection to 
the ISP. Voice notifications are possible with a set of speakers that connect to the headphone jack of the RPI.

## Features
* Internet Service Monitoring (Power Cycles attached cable modem if any of the following is true)
  * No ping response from configurable Internet Server (Google 8.0.8.8 is default)
  * Internet speed test to best closest server is below a download floor threshold in Mbps
* Internet Speed Test with the following statistics reported
  * Ping time in milliseconds
  * Download speed in Mbps
  * Upload speed in Mbps
  * Closest and Best Server to perform speed test
* Overall Internet Connection Status
  * Status of the Internet connection
  * Date/Time of the Last issue with the Internet connection
  * Current status of the Internet Sentinel Device such as conducting a speed test or pinging Internet Server
* Supported User Interface Themes
  * Dark
  * Light
* Manual Controls to:
  * Reset the Internet Connection
  * Reboot the Internet Sentinel Device
* Configuration
  * Download Floor value in Mbps at which time Internet Sentinel resets the Internet Connection
  * Reset Delay in seconds to power off the cable modem before powering it on
  * Voice Notifications setting to enable voice notifications of issue with Internet Connection
  * Internet Server to ping to determine if Internet connection is On-line
  * Frequency in seconds to test the speed of the Internet connection
  
# Equipment list
(Amazon was chosen since they had all the parts needed. Parts are available elsewhere.)
Raspberry Pi 4 - https://www.amazon.com/dp/B07TLDTRYF/ref=cm_sw_em_r_mt_dp_U_DtCZEb9FHF451
32 GB Micro SD Card - https://www.amazon.com/dp/B06XWN9Q99/ref=cm_sw_em_r_mt_dp_U_5ECZEbB89KJWA
RPI Touchscreen Case - https://www.amazon.com/dp/B07WXK38YM/ref=cm_sw_em_r_mt_dp_U_vuCZEb07MR7HY
Touchscreen Display - https://www.amazon.com/dp/B0153R2A9I/ref=cm_sw_em_r_mt_dp_U_2tCZEbT87HJ67
Jumper wires (female connector and male pin on other end) - https://www.amazon.com/dp/B07GD2BWPY/ref=cm_sw_em_r_mt_dp_U_VuCZEbRXVE5CQ
Speakers - https://www.amazon.com/dp/B07SZ8CVWB/ref=cm_sw_em_r_mt_dp_U_GsCZEbZHWPGDJ
IoT Power Relay - https://www.amazon.com/dp/B00WV7GMA2/ref=cm_sw_em_r_mt_dp_U_pvCZEbP4FEGWJ

# Hardware Construction
## Raspberry Pi and Touchscreen Display Assembly
* Install Raspbian on the 32 GB Micro SD card using the following software:
  [Raspberry Pi Imager software][https://www.raspberrypi.org/downloads/]
* Following the directions to install the RPI in the RPI Touchscreen case with the Touchscreen Display.
## IoT Power Relay
See link below for more info on the IoT Power Relay
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

# Software Installation
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

## Acknowledgements
I would like to mention the following people and software used in thie application:
* [Stefan Holstein Analogue Gauge Widget PyQt][https://github.com/StefanHol/AnalogGaugeWidgetPyQt]
* [Alexander Huszagh Breeze StyleSheets][https://github.com/Alexhuszagh/BreezeStyleSheets]
* [Matt Martz Speedtest-cli][https://github.com/sivel/speedtest-cli]

