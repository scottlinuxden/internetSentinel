# Internet Sentinel
![Internet Sentinel](assets/internet_sentinel_hardware_front_view.png?raw=true "InternetSentinel")

Internet Sentinel is a software and hardware solution that monitors the Internet connection in a Local Area Network 
and if not ON-LINE (checked via Internet Server ping) will power cycle an attached cable modem via the connected 
IoT Power Relay from Digital-loggers.com.  Also performs a speed test of your Internet connection and will power 
cycle your cable modem if the download speed reported is below a threshold.  This will attempt to get a faster 
connection to the ISP. Voice notifications are possible with a set of speakers that connect to the headphone jack 
of the RPI.

## Features
* Internet Service Monitoring (Power Cycles attached cable modem if any of the following is true):
  * No ping response from configurable Internet Server (Google 8.0.8.8 is default)
  * Internet speed test to best closest server is below a download floor threshold in Mbps
* Internet Speed Test with the following statistics reported:
  * Ping time in milliseconds
  * Download speed in Mbps
  * Upload speed in Mbps
  * Closest and Best Server to perform speed test
* Overall Internet Connection Status
  * Status of the Internet connection
  * Date/Time of the Last issue with the Internet connection
  * Current status of the Internet Sentinel Device such as conducting a speed test or pinging Internet Server
* Supported User Interface Themes
  * Dark (display backlight dimmed to 45%)
  * Light (full display backlight)
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
(Amazon was chosen since they had all the parts needed however parts are available elsewhere.)
Raspberry Pi 4 - https://www.amazon.com/dp/B07TLDTRYF/ref=cm_sw_em_r_mt_dp_U_DtCZEb9FHF451
32 GB Micro SD Card - https://www.amazon.com/dp/B06XWN9Q99/ref=cm_sw_em_r_mt_dp_U_5ECZEbB89KJWA
RPI Touchscreen Case - https://www.amazon.com/dp/B07WXK38YM/ref=cm_sw_em_r_mt_dp_U_vuCZEb07MR7HY
Touchscreen Display - https://www.amazon.com/dp/B0153R2A9I/ref=cm_sw_em_r_mt_dp_U_2tCZEbT87HJ67
Jumper wires (female connector and male pin on other end) - https://www.amazon.com/dp/B07GD2BWPY/ref=cm_sw_em_r_mt_dp_U_VuCZEbRXVE5CQ
Speakers - https://www.amazon.com/dp/B07SZ8CVWB/ref=cm_sw_em_r_mt_dp_U_GsCZEbZHWPGDJ
IoT Power Relay - https://www.amazon.com/dp/B00WV7GMA2/ref=cm_sw_em_r_mt_dp_U_pvCZEbP4FEGWJ

# Hardware Construction
## Raspberry Pi and Touchscreen Display Assembly
### Front View
![Internet Sentinel Front View](assets/internet_sentinel_hardware_front_view.png?raw=true "InternetSentinelFrontView")

### Top View
![Internet Sentinel Top View](assets/internet_sentinel_hardware_top_view.png?raw=true "InternetSentinelTopView")

### Rear View
![Internet Sentinel Rear View](assets/internet_sentinel_hardware_rear_view.png?raw=true "InternetSentinelRearView")

* Install Raspbian OS on the 32 GB Micro SD card using the following Windows or Mac OS X [Raspberry Pi Imager software](https://www.raspberrypi.org/downloads/)
* Choose the Raspberry Pi OS 32-bit version to install on the Micro SD card
* Insert the Micro SD card into the Raspberry Pi Micro SD card slot
* Following the [directions](https://smarticase.com/pages/smartipi-touch-2-setup-1) to install the RPI in the 
RPI Touchscreen case with the Touchscreen Display.
* Connect the speakers to a RPI USB port and headphone jack.
* Connect the IoT Power Relay to the RPI as described below in next section.

## IoT Power Relay Connections
* Remove the IoT Power Relay green phoenix connector.  The entire light green connector block pulls out to expose
screw terminals that need loosened and male jumper wire pin of both wires inserted. 
* Connect the two jumper wires (male jumper wire pin) to the connector via the screw terminals and connect the female 
ends of the wires to the RPI GPIO header as described below (See diagram below of exact location of GPIO header pins):
  * Connect the RPI header BCM 23 pin to the + side of the IoT Power Relay green phoenix connector.
  * Connect RPI header ground pin 14 next to and to the left of BCM 23 to the - side of the IoT Power Relay green phoenix
connector.
* Insert the internet device (cable modem) plug into the IoT Power Relay outlet marked NORMALLY ON.
* Complete the Software Installation steps below.

See link below for more info on the IoT Power Relay
https://www.digital-loggers.com/iotfaqs.html

### Raspberry Pi GPIO Pin and IoT Power Relay Connections
The pins marked by a red box in the diagram are connected via the jumper wires to the IoT Power Relay:

![Raspberry Pi Pinout Diagram](assets/raspberrypi_gpio_pinout.png?raw=true "RaspberryPiPinoutDiagram")

# Software Installation
![Internet Sentinel Application](assets/internet_sentinel_screenshot.png?raw=true "InternetSentinelScreenshot")

## Application Files
* Install the Internet Sentinel application software in this repository by cloning the repository files to the folder
/home/pi/internetSentinel on the Raspberry Pi.

## Operating System and Python Dependent Files
* The following application dependent packages need to be installed by performing the following:
  * sudo apt-get update
  * sudo apt-get install qt5-default pyqt5-dev pyqt5-dev-tools
  * sudo apt-get install espeak
  * sudo apt-get install gnome-keyring
  * sudo pip3 install secretstorage dbus-python
  * sudo pip3 install speedtest-cli
  * sudo pip3 install num2words
  * sudo pip3 install keyring
  * sudo apt-get install seahorse

* Configure RPI to wait for network on-line before booting.  Make sure you have the RPI connected to a LAN
wireless access point, router, or switch via CAT5e or higher Wired Ethernet cable then:
  * Select Boot-Options menu
  * Select Wait for Network at Boot
  * Select Yes

* Add Internet Sentinel to startup when RPI boots by doing the following:
  * At command prompt enter the following to edit the autostart file:
  * sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
  * Add the following lines to bottom of the file:
  * @xset s off
  * @xset -dpms
  * @xset s noblank
  * @/usr/bin/python3 /home/pi/internetSentinel/internetSentinel.py
  * Save the file by depressing Ctrl-X
  
## Desktop Launcher
* Install the desktop icon application launcher:
  * cp /home/pi/internetSentinel/internetSentinel.desktop /home/pi/Desktop

* Select the File Manager Icon (looks like a folder) in the desktop menubar
  * Select Edit on File Manager menu bar
  * Select Preferences menu item
  * Select General Tab
  * Select checkbox next to "Do not ask option on executable launch"
  * Exit out of File Manager

## Optional Email Notification Configuration
* Edit the file internet_sentinel.ini
  * Edit the line 'smtp_server' by setting it to the email server hostname that you use for your email account
  * Edit the line 'smtp_server_port' by setting it to the email server port that you use for your email account
  
* Enter the following command to add your gmail login username and password pair in the Gnome keyring
  * python3 set_email_login_credentials.py
    
* Run the gnome keyring application below at a terminal prompt to set the default 'Login' keyring password
  * seahorse
  ![Seahorse](assets/seahorse_application_window.png?raw=true "InternetSentinel")
  * Select the 'Login' keyring in list on left to change password
  * Select the 'email_login_username' to change the email login server username
  * Select the 'email_login_password' to change the email login server password
* If you reboot the RPI you will need to enter this 'Login' keyring password then you can run Internet Sentinel

## Final Steps
* Reboot the RPI via the following command:
  * sudo /sbin/reboot

## Acknowledgements
I would like to mention the following people whose software was used in this application:
* [Stefan Holstein Analogue Gauge Widget PyQt](https://github.com/StefanHol/AnalogGaugeWidgetPyQt)
* [Alexander Huszagh Breeze StyleSheets](https://github.com/Alexhuszagh/BreezeStyleSheets)
* [Matt Martz Speedtest-cli](https://github.com/sivel/speedtest-cli)

