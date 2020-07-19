
import time

import speedtest
from PyQt5.QtCore import *
from PyQt5.QtCore import pyqtSignal

import ping


class Worker(QThread):
    """Internet Sentinel Worker thread that monitors a ping host server and if
    on-line runs a speed test every test frequency minutes
    """
    alert_handler = pyqtSignal(str)
    test_results_handler = pyqtSignal(float, float, float, str)

    def __init__(self,
                 ping_host_ip_address,
                 notifications,
                 test_frequency,
                 parent=None):
        """
        Initialize the Internet Sentinel Worker Thread
        Args:
            ping_host_ip_address: IP address of Internet Server that is pinged to determine if Internet ON-LINE
            notifications: True if voice notifications on status of Internet connections and steps being taken to
            connect or False to turn off any voice notifications
            test_frequency: Number of minutes between Internet Speed tests
            parent: Qt parent Widget for this QThread
        """

        QThread.__init__(self, parent)

        self.servers = []
        # If you want to test against a specific server
        # servers = [1234]

        self.threads = None
        # If you want to use a single threaded test
        # threads = 1

        self.ping_host_ip_address = ping_host_ip_address
        self.notifications = notifications
        self.test_frequency = test_frequency
        self.monitor_internet = True
        self.start_time = time.time()
        self.internet_down = False

    def __del__(self):
        """
        Waits on the thread to complete if Worker thread is deleted
        Returns: None

        """
        self.wait()

    def get_elapsed_time(self):
        """
        Gets the elapsed time in seconds since last start time assignment
        Returns: elapsed time in seconds

        """
        delta_time = time.time() - self.start_time
        return delta_time

    def set_notifications(self, state):
        """
        Sets whether voice notifications should occur during a speed test
        Args:
            state: True if voice notifications should occur or False for no notifications

        Returns: None

        """
        self.notifications = state

    def set_test_frequency(self, frequency):
        """
        Sets the time between when internet speed tests should occur
        Args:
            frequency: time in seconds to test internet speed

        Returns: None

        """
        self.test_frequency = frequency

    def set_ping_host(self, host_ip_address):
        """
        Set ths ping host ip address to use for the Internet Speed Test
        Args:
            host_ip_address: ip address to use for the ping host

        Returns: None

        """
        self.ping_host_ip_address = host_ip_address

    def conduct_speed_test(self, run_immediately=False):
        """
        Pings the host set in ping_host_ip_address and if it is found
        executes a Speedtest with the best internet server option using speedtest python module
        Args:
            run_immediately: True to execute a speed test even if not time to do so which is specified
            by test_frequency

        Returns: None

        """

        if ping.host(self.ping_host_ip_address) == 'found':

            self.internet_down = False

            if run_immediately or (self.get_elapsed_time() >= (self.test_frequency * 60)):

                self.alert_handler.emit("SUCCESS: Ping host: %s was successfully contacted, starting speed test..." %
                                        self.ping_host_ip_address)
                try:
                    s = speedtest.Speedtest()
                    s.get_servers(self.servers)
                    s.get_best_server()
                    s.download(threads=self.threads)
                    s.upload(threads=self.threads)
                    # s.results.share()

                    results_dict = s.results.dict()
                    download_speed = results_dict['download'] / (1000.0 * 1000.0)
                    upload_speed = results_dict['upload'] / (1000.0 * 1000.0)
                    ping_time = results_dict['ping']
                    server = results_dict['server']['sponsor']

                    self.alert_handler.emit("SUCCESS: Best Test Server: %s, Internet speed recorded: "
                                            "Download %.2f Mbps, Upload %.2f Mbps, Ping Time: %.2f ms" %
                                            (server, download_speed, upload_speed, ping_time))
                    self.test_results_handler.emit(download_speed, upload_speed, ping_time, server)
                    self.start_time = time.time()
                except:
                    self.alert_handler.emit("ERROR: Internet speed test could not be conducted "
                                            "due to issue with test server")

            else:
                # delay 10 seconds before next ping
                time.sleep(10)

        else:
            if not self.internet_down:
                self.test_results_handler.emit(0.0, 0.0, 0.0, 'internet down')
                self.internet_down = True

    def run(self):
        """
        Run a speed test once thread instantiates and forever after that with a ping happening very 10 seconds
        to determine if internet is on-line or off-line and a speed test executed if elapsed time between tests
        is greater than the specified test frequency
        Returns: None

        """
        run_immediately = True
        while self.monitor_internet:
            self.conduct_speed_test(run_immediately=run_immediately)
            run_immediately = False
