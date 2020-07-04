import datetime
import os
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import internetSpeedTest
import resetInternetConnection
from Ui_internetSentinel import Ui_InternetSentinelDialog
import breeze_resources

ORGANIZATION_NAME = 'LinXden'
ORGANIZATION_DOMAIN = 'linxden.com'
APPLICATION_NAME = 'Internet Sentinel'

VERSION = "1.0.0"

PYTHON_DEBUG = False

INSTALLATION_DIRECTORY = "/home/pi/internetSentinel"

if PYTHON_DEBUG:
    pyqtRemoveInputHook()


def get_pid_file():
    """
    Gets the PID from the Internet Sentinel PID file which is created when the program is executed
    Returns: PID from the file

    """
    pid = None
    try:
        with open('%s/internet_sentinel.pid' % INSTALLATION_DIRECTORY, 'r') as pid_file:
            pid = int(pid_file.readline().strip())
    except:
        pass
    return pid


def is_programming_running():
    """
    Determines if the Internet Sentinel application is running and if so returns result
    Returns: True if the Internet Sentinel application is running and False otherwise

    """
    is_running = False
    if get_pid_file() is not None:
        try:
            os.kill(get_pid_file(), 0)
        except OSError:
            pass
        else:
            is_running = True

    return is_running


class InternetSentinel(QDialog):
    """
    Main Dialog Window for the Internet Sentinel
    """

    def __init__(self, application, parent=None):
        """
        Initialize the Internet Sentinel Application and GUI
        Args:
            parent: Parent widget of this dialog
        """

        self.application = application

        QDialog.__init__(self, parent)
        self.generate_pid_file()

        # create USK Key Creator Dialog
        self.ui = Ui_InternetSentinelDialog()

        # manifest UI
        self.ui.setupUi(self)

        self.settings = QSettings()

        self.themes = ['Dark', 'Light']
        self.ui.themeComboBox.addItems(self.themes)

        self.ui.themeComboBox.setCurrentIndex(self.ui.themeComboBox.findText(
            self.settings.value('settings/theme', 'Dark', type=str)))

        theme = self.ui.themeComboBox.currentText()
        self.set_theme(theme)

        self.setWindowTitle("%s (Version: %s)" % (APPLICATION_NAME, VERSION))

        self.ui.speedometerWidget.set_NeedleColor(0,0,255,255)
        self.ui.speedometerWidget.set_CenterPointColor(0,0,255)
        self.ui.speedometerWidget.set_ScaleValueColor(255,255,255,255)
        self.ui.speedometerWidget.value_min = 0
        self.ui.speedometerWidget.value_max = 100
        self.ui.speedometerWidget.scala_main_count = 10
        self.ui.speedometerWidget.set_MinValue(0)
        self.ui.speedometerWidget.set_MaxValue(100)
        self.ui.speedometerWidget.update_value(0)
        self.ui.speedometerWidget.set_enable_value_text()
        self.ui.speedometerWidget.set_gauge_color_inner_radius_factor(917)
        self.ui.speedometerWidget.set_gauge_color_outer_radius_factor(1000)
        self.ui.speedometerWidget.set_scale_polygon_colors([[.00, Qt.green],
                                                            [.1, Qt.yellow],
                                                            [.15, Qt.red],
                                                            [1, Qt.transparent]])
        self.ui.speedometerWidget.set_DisplayValueColor(255,255,255,255)
        self.ui.themeComboBox.currentTextChanged.connect(self.theme_changed)
        self.ui.resetDelaySpinBox.setValue(self.settings.value('settings/reset_delay', 30, type=int))
        self.ui.resetDelaySpinBox.setMinimum(15)
        self.ui.resetDelaySpinBox.valueChanged.connect(self.reset_delay_changed)
        self.ui.downloadFloorSpinBox.setValue(self.settings.value('settings/download_floor', 10, type=int))
        self.ui.downloadFloorSpinBox.setMinimum(1)
        self.ui.downloadFloorSpinBox.valueChanged.connect(self.download_floor_changed)
        self.ui.testFrequencySpinBox.setMinimum(1)
        self.ui.testFrequencySpinBox.setValue(self.settings.value('settings/test_frequency', 1, type=int))
        self.ui.testFrequencySpinBox.valueChanged.connect(self.test_frequency_changed)
        self.ui.notificationsCheckBox.setChecked(self.settings.value('settings/notifications', True, type=bool))
        self.ui.notificationsCheckBox.stateChanged.connect(self.notifications_changed)
        ping_host_ip_address = self.settings.value('settings/ping_host_ip_address', '8.8.8.8', type=str)
        self.set_ping_host_ip_address(ping_host_ip_address)
        self.ui.pingHostOctet4SpinBox.valueChanged.connect(self.ping_host_changed)
        self.ui.pingHostOctet3SpinBox.valueChanged.connect(self.ping_host_changed)
        self.ui.pingHostOctet2SpinBox.valueChanged.connect(self.ping_host_changed)
        self.ui.pingHostOctet1SpinBox.valueChanged.connect(self.ping_host_changed)

        self.ui.pingLabel.setText('0')
        self.ui.downloadLabel.setText('0')
        self.ui.uploadLabel.setText('0')
        self.ui.testServerLabel.setText('')
        self.ui.lastNetworkIssueDateLabel.setText(self.settings.value('settings/last_issue',
                                                                      datetime.datetime.today().strftime(
                                                                          "%m/%d/%Y %H:%M:%S"),
                                                                      type=str))
        self.ui.internetStatusLabel.setText('')
        self.ui.resetInternetConnectionPushButton.clicked.connect(self.reset_internet_connection)
        self.ui.rebootSystemPushButton.clicked.connect(self.reboot_system)
        self.reset_internet_connection_worker = None
        self.speed_test_worker = None
        # resetInternetConnection.initialize_gpio_pins()

        # self.set_alert("Checking internet in %d minute(s)" % int(self.ui.testFrequencySpinBox.value()))
        # QTimer.singleShot(int(self.ui.testFrequencySpinBox.value()) * 60 * 1000, self.conduct_speed_test)
        self.internet_offline = False
        self.conduct_speed_test()

    def set_theme(self, name):
        file = QFile(":/%s.qss" % name.lower())
        file.open(QFile.ReadOnly | QFile.Text)
        stream = QTextStream(file)
        self.application.setStyleSheet(stream.readAll())
        file.close()
        if name.upper() == 'DARK':
            self.ui.speedometerWidget.set_NeedleColor(0, 0, 255, 255)
            self.ui.speedometerWidget.set_ScaleValueColor(255, 255, 255, 255)
            self.ui.speedometerWidget.set_DisplayValueColor(255, 255, 255, 255)
            os.system('sudo sh -c "echo 100 > /sys/class/backlight/rpi_backlight/brightness"')
        else:
            self.ui.speedometerWidget.set_NeedleColor(0, 0, 0, 255)
            self.ui.speedometerWidget.set_ScaleValueColor(0, 0, 0, 255)
            self.ui.speedometerWidget.set_DisplayValueColor(0, 0, 0, 255)
            os.system('sudo sh -c "echo 255 > /sys/class/backlight/rpi_backlight/brightness"')

    def theme_changed(self):
        self.set_theme(self.ui.themeComboBox.currentText())
        self.settings.setValue('settings/theme', self.ui.themeComboBox.currentText())

    def test_frequency_changed(self):
        """
        User has changed the Test Frequency on the GUI and speed test worker is made aware of this
        Returns: None

        """
        self.speed_test_worker.set_test_frequency(int(self.ui.testFrequencySpinBox.value()))
        self.settings.setValue('settings/test_frequency', self.ui.testFrequencySpinBox.value())

    def notifications_changed(self):
        """
        User has changed the Voice Notifications option on the GUI and speed test worker is made aware of this
        Returns: None

        """
        self.speed_test_worker.set_notifications(self.ui.notificationsCheckBox.isChecked())
        self.settings.setValue('settings/notifications', self.ui.notificationsCheckBox.isChecked())

    def reset_delay_changed(self):
        self.settings.setValue('settings/reset_delay', self.ui.resetDelaySpinBox.value())

    def download_floor_changed(self):
        self.settings.setValue('settings/download_floor', self.ui.downloadFloorSpinBox.value())

    def ping_host_changed(self):
        """
        User has changed the Ping Host IP Address on the GUI and speed test worker is made aware of this
        Returns: None

        """
        ping_host = self.get_ping_host_ip_address()
        self.speed_test_worker.set_ping_host(ping_host)
        self.settings.setValue('settings/ping_host_ip_address', self.get_ping_host_ip_address())

    def set_ping_host_ip_address(self, ip_address):
        """
        Set the Ping Host IP address octets on the GUI from an IP address string
        Args:
            ip_address: ip address string to use to set the GUI Ping Host IP Address octets

        Returns: None

        """
        tokens = ip_address.split('.')
        self.ui.pingHostOctet1SpinBox.setValue(int(tokens[0]))
        self.ui.pingHostOctet2SpinBox.setValue(int(tokens[1]))
        self.ui.pingHostOctet3SpinBox.setValue(int(tokens[2]))
        self.ui.pingHostOctet4SpinBox.setValue(int(tokens[3]))

    def get_ping_host_ip_address(self):
        """
        Gets the Ping Host IP Address from Ping Host IP Address Octets on the GUI
        Returns: Ping Host IP Address as a string

        """
        ping_host_ip_address = self.ui.pingHostOctet1SpinBox.text() + '.' + \
                               self.ui.pingHostOctet2SpinBox.text() + '.' + \
                               self.ui.pingHostOctet3SpinBox.text() + '.' + \
                               self.ui.pingHostOctet4SpinBox.text()
        return ping_host_ip_address

    def conduct_speed_test(self):
        """
        Start up an Internet Speed Test Worker Thread to monitor the Internet connection
        Returns: None

        """
        ping_host_ip_address = self.get_ping_host_ip_address()

        self.speed_test_worker = internetSpeedTest.Worker(
            ping_host_ip_address=ping_host_ip_address,
            notifications=self.ui.notificationsCheckBox.isChecked(),
            test_frequency=int(self.ui.testFrequencySpinBox.text()))

        self.speed_test_worker.alert_handler.connect(self.set_alert)
        self.speed_test_worker.test_results_handler.connect(self.update_test_results)
        self.speed_test_worker.start()

    @pyqtSlot(str)
    def set_alert(self, alert_message):
        """
        Sets the scrolling alert message area on the GUI to include alert_message
        Args:
            alert_message: message to prepend to the alert area

        Returns: None

        """
        timestamp = datetime.datetime.today().strftime("%m/%d/%Y %H:%M:%S")
        alert = timestamp + ":" + alert_message + '\n'
        cursor = QTextCursor(self.ui.statusPlainTextEdit.document())
        cursor.setPosition(0)
        self.ui.statusPlainTextEdit.setTextCursor(cursor)
        self.ui.statusPlainTextEdit.insertPlainText(alert)

    @pyqtSlot(float, float, float, str)
    def update_test_results(self, download_speed, upload_speed, ping_time, server):
        """
        Qt Slot to update the Internet Speed Test results information on the GUI
        Args:
            download_speed: download speed results for best test server in Mbps
            upload_speed: upload speed results to best test server in Mbps
            ping_time: elapsed time in ms to ping the best test server determined by the internet speed test
            server: server name used for the internet speed test or status of the test such as
            internet down, internet unrecoverable, internet reset, or internet speed test

        Returns: None

        """

        self.ui.downloadLabel.setText("%.2f" % download_speed)
        self.ui.uploadLabel.setText("%.2f" % upload_speed)
        self.ui.pingLabel.setText("%.2f" % ping_time)
        if int(download_speed) > self.ui.speedometerWidget.get_value_max():
            self.ui.speedometerWidget.set_MaxValue(int(download_speed))
        self.ui.speedometerWidget.update_value(int(download_speed))

        if server == 'internet unrecoverable':
            self.ui.internetStatusLabel.setText('OFF-LINE')
            self.internet_offline = True
            self.ui.lastNetworkIssueDateLabel.setText(datetime.datetime.today().strftime("%m/%d/%Y %H:%M:%S"))
            self.set_alert("ERROR: Internet connection has not been restored after first attempt. Will keep trying."
                           "Check Internet Device and wiring and/or call ISP to troubleshoot.")
            if self.ui.notificationsCheckBox.isChecked():
                self.speak("Internet connection had not be restored after first attempt, "
                           "Check Internet Device and wiring and/or call ISP to troubleshoot. "
                           "Will keep trying.")

        elif server == 'internet reset':
            self.ui.internetStatusLabel.setText('OFF-LINE')
            self.ui.lastNetworkIssueDateLabel.setText(datetime.datetime.today().strftime("%m/%d/%Y %H:%M:%S"))
            # self.set_alert("ERROR: Internet connection is down")
            # if self.ui.notificationsCheckBox.isChecked():
            #     os.system('espeak -ven-us -g6 -s150 "Internet connection is down, '
            #               'resetting internet connection" 2>/dev/null')
            self.internet_offline = True

        elif server == 'internet down':
            self.ui.internetStatusLabel.setText('OFF-LINE')
            self.internet_offline = True
            self.ui.lastNetworkIssueDateLabel.setText(datetime.datetime.today().strftime("%m/%d/%Y %H:%M:%S"))
            self.set_alert("ERROR: Internet connection is down")
            if self.ui.notificationsCheckBox.isChecked():
                self.speak("Internet connection is down, resetting internet connection")
                self.email_alert("Internet connection is down, resetting internet connection.")
                self.reset_internet_connection()

        elif server == 'internet speed test':
            self.speed_test_worker.conduct_speed_test(run_immediately=True)

        elif server != '':
            server = server.strip()
            if len(server) > 20:
                server = server[:20] + '...'
            self.ui.testServerLabel.setText(server)
            if int(download_speed) < int(self.ui.downloadFloorSpinBox.text()):
                self.ui.internetStatusLabel.setText('OFF-LINE')
                self.internet_offline = True
                self.set_alert("INFO: Download speed of %.2f is less than download floor, resetting internet connection")
                if self.ui.notificationsCheckBox.isChecked():
                    self.speak("Download speed of %.2f is less than download floor, "
                               "resetting internet connection" % download_speed)
                    self.ui.lastNetworkIssueDateLabel.setText(datetime.datetime.today().strftime("%m/%d/%Y %H:%M:%S"))
                    self.reset_internet_connection()
            else:
                self.ui.internetStatusLabel.setText('ON-LINE')
                if self.internet_offline:
                    self.internet_offline = False
                    if self.ui.notificationsCheckBox.isChecked():
                        self.speak("Internet is back on-line")
                        self.email_alert("Internet is back on-line")

    def speak(self, text):
        language = '-ven-us'
        command = 'espeak -ven-us -g6 -s150 "' + text + '" --stdout | aplay'
        os.system(command)

    def email_alert(self, alert):
        pass

    def reset_internet_connection(self):
        """
        Starts a Reset Internet Connection Worker thread to perform the task of power cycling the connected
        internet device such a cable modem
        Returns: None
        """
        self.ui.lastNetworkIssueDateLabel.setText(datetime.datetime.today().strftime("%m/%d/%Y %H:%M:%S"))
        self.reset_internet_connection_worker = resetInternetConnection.Worker(
            reset_delay=int(self.ui.resetDelaySpinBox.text()),
            test_server_ip_address=self.get_ping_host_ip_address(),
            internet_device_power_on_wait_time=5*60,
            notifications=self.ui.notificationsCheckBox.isChecked())

        self.reset_internet_connection_worker.test_status_handler.connect(self.update_test_results)
        self.reset_internet_connection_worker.alert_handler.connect(self.set_alert)
        self.reset_internet_connection_worker.start()

    def reboot_system(self):
        """
        Reboots the Internet Sentinel device
        Returns: None

        """
        response = QMessageBox.information(self,
                                           "Reboot Confirmation",
                                           "Rebooting this device will stop Internet monitoring and power cycle this device",
                                           QMessageBox.Ok |
                                           QMessageBox.Cancel,
                                           QMessageBox.Ok)

        if response == QMessageBox.Ok:
            if self.ui.notificationsCheckBox.isChecked():
                os.system('sudo sh -c "echo 255 > /sys/class/backlight/rpi_backlight/brightness"')
                self.speak("Rebooting Internet Sentinel Device")
            os.system("sudo /sbin/reboot")

    def generate_pid_file(self):
        """
        Generates a PID file that includes the process ID of the Internet Sentinel application when it was started
        Returns: None

        """
        with open('%s/internet_monitor.pid' % INSTALLATION_DIRECTORY, 'w') as pid_file:
            pid_file.write("%d\n" % os.getpid())

    def closeEvent(self, event):
        """
        When users selects the X on the Dialog Window the application settings are save to uSD card
        Args:
            event: application close event which is ignored

        Returns: None

        """
        os.system('sudo sh -c "echo 255 > /sys/class/backlight/rpi_backlight/brightness"')
        self.settings.setValue('settings/reset_delay', self.ui.resetDelaySpinBox.value())
        self.settings.setValue('settings/download_floor', self.ui.downloadFloorSpinBox.value())
        self.settings.setValue('settings/test_frequency', self.ui.testFrequencySpinBox.value())
        self.settings.setValue('settings/notifications', self.ui.notificationsCheckBox.isChecked())
        self.settings.setValue('settings/ping_host_ip_address', self.get_ping_host_ip_address())
        self.settings.setValue('settings/last_issue', self.ui.lastNetworkIssueDateLabel.text())
        self.settings.sync()


if __name__ == "__main__":

    if is_programming_running():
        sys.exit(0)

    QCoreApplication.setApplicationName(ORGANIZATION_NAME)
    QCoreApplication.setOrganizationDomain(ORGANIZATION_DOMAIN)
    QCoreApplication.setApplicationName(APPLICATION_NAME)

    app = QApplication(sys.argv)

    #QApplication.setStyle(QStyleFactory.create("Cleanlooks"))
    #QApplication.setPalette(QApplication.style().standardPalette())
    window = InternetSentinel(application=app, parent=None)
    window.show()
    sys.exit(app.exec_())

