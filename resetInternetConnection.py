
import os
import time

import RPi.GPIO as gpio
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal

import ping


def initialize_gpio_pins():
    """
    Initialize GPIO23 pin to be addressed via Broadcom Pin Numbers and set as an output pin
    Returns: None

    """
    gpio.setmode(gpio.BCM)
    gpio.setup(23, gpio.OUT)


class Worker(QThread):
    """
    Reset Internet Connection Worker Thread to control power relay to power cycle via
    outlet on power relay and wait for device to bring Internet ON-LINE
    """
    alert_handler = pyqtSignal(str)
    test_status_handler = pyqtSignal(float, float, float, str)

    def __init__(self,
                 reset_delay,
                 notifications,
                 test_server_ip_address,
                 internet_device_power_on_wait_time,
                 parent=None):
        """
        Initialize the Reset Internet Connection Worker Thread
        Args:
            reset_delay: time in seconds to pause between power off of internet device and power device on
            notifications: True if voice notifications of Internet status should be announced or False if not
            test_server_ip_address: IP address of system on Internet to ping to determine if Internet is ON-LINE
            internet_device_power_on_wait_time: time in seconds to test if Internet is ON-LINE before giving up on
            the reset
            parent: parent Qt object if applicable
        """

        QThread.__init__(self, parent)

        self.reset_delay = reset_delay
        self.notifications = notifications
        self.test_server_ip_address = test_server_ip_address
        self.internet_device_power_on_wait_time = internet_device_power_on_wait_time
        initialize_gpio_pins()

    def __del__(self):
        """
        Deletion of Worker thread will wait on thread to complete
        Returns: None

        """
        self.wait()

    def speak(self, text):
        language = '-ven-us'
        command = 'espeak -ven-us -g6 -s150 "' + text + '" --stdout | aplay'
        os.system(command)

    def get_elapsed_time(self, start_time):
        """
        Get elapsed time from current time - start time snapshot
        Args:
            start_time: start time to compute the elapsed time against

        Returns: elapsed time in seconds

        """
        delta_time = time.time() - start_time
        return delta_time

    def set_test_server_ip_address(self, test_server_ip_address):
        """
        Set the test server ip address if it is changed on GUI
        :param test_server_ip_address: ip address of internet server to ping
        :return: None
        """
        self.test_server_ip_address = test_server_ip_address

    def set_reset_delay(self, reset_delay):
        """
        Set reset delay in the reset connection worker if GUI update occurs for this configuration item
        Args:
            reset_delay: time in seconds between power off of internet device and power on

        Returns: None

        """
        self.reset_delay = reset_delay

    def reset_internet_connection(self):
        """
        Resets the Internet connection by power cycling an internet device connected to the attached power
        relay in the outlet marked "NORMALLY ON".
        Returns: None

        """
        self.alert_handler.emit("SUCCESS: Stopping internet connection with %d second delay" % self.reset_delay)
        self.test_status_handler.emit(0.0, 0.0, 0.0, 'internet reset')
        if self.notifications:
            self.speak('Stopping internet connection')
        gpio.output(23, gpio.HIGH)
        time.sleep(self.reset_delay)
        self.alert_handler.emit("SUCCESS: Starting internet connection")
        if self.notifications:
            self.speak('Starting internet connection')
        gpio.output(23, gpio.LOW)

        start_time = time.time()

        while True:

            if ping.host(self.test_server_ip_address) == 'not found':
                elapsed_time = self.get_elapsed_time(start_time)
                if elapsed_time >= self.internet_device_power_on_wait_time:
                    self.alert_handler.emit("ERROR: Internet connection is not on-line after %d seconds" %
                                            elapsed_time)
                    self.test_status_handler.emit(0.0, 0.0, 0.0, 'internet unrecoverable')
                    break

                else:
                    # wait 10 seconds and try to ping Internet server
                    time.sleep(10)

            else:
                elapsed_time = self.get_elapsed_time(start_time)
                self.alert_handler.emit("SUCCESS: Internet Test Server is on-line elapsed time: %d seconds, "
                                        "internet speed test scheduled to run" % elapsed_time)
                self.test_status_handler.emit(0.0, 0.0, 0.0, 'internet speed test')
                break

    def run(self):
        """
        Run method for Qt Thread that executes a power cycle on internet device
        Returns: None

        """
        self.reset_internet_connection()
        gpio.cleanup(23)
