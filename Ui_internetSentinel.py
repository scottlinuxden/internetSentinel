# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/rsdavis/Documents/internetSentinel/internetSentinel.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InternetSentinelDialog(object):
    def setupUi(self, InternetSentinelDialog):
        InternetSentinelDialog.setObjectName("InternetSentinelDialog")
        InternetSentinelDialog.resize(800, 460)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InternetSentinelDialog.sizePolicy().hasHeightForWidth())
        InternetSentinelDialog.setSizePolicy(sizePolicy)
        InternetSentinelDialog.setMinimumSize(QtCore.QSize(800, 460))
        InternetSentinelDialog.setMaximumSize(QtCore.QSize(800, 460))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        InternetSentinelDialog.setFont(font)
        self.verticalLayout = QtWidgets.QVBoxLayout(InternetSentinelDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.uLabel = QtWidgets.QLabel(InternetSentinelDialog)
        self.uLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.uLabel.setFont(font)
        self.uLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uLabel.setObjectName("uLabel")
        self.verticalLayout_6.addWidget(self.uLabel)
        self.uploadLabel = QtWidgets.QLabel(InternetSentinelDialog)
        self.uploadLabel.setMinimumSize(QtCore.QSize(0, 40))
        self.uploadLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.uploadLabel.setFont(font)
        self.uploadLabel.setText("")
        self.uploadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uploadLabel.setObjectName("uploadLabel")
        self.verticalLayout_6.addWidget(self.uploadLabel)
        self.gridLayout.addLayout(self.verticalLayout_6, 0, 2, 1, 1)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.dLabel = QtWidgets.QLabel(InternetSentinelDialog)
        self.dLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.dLabel.setFont(font)
        self.dLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dLabel.setObjectName("dLabel")
        self.verticalLayout_5.addWidget(self.dLabel)
        self.downloadLabel = QtWidgets.QLabel(InternetSentinelDialog)
        self.downloadLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.downloadLabel.setFont(font)
        self.downloadLabel.setText("")
        self.downloadLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.downloadLabel.setObjectName("downloadLabel")
        self.verticalLayout_5.addWidget(self.downloadLabel)
        self.gridLayout.addLayout(self.verticalLayout_5, 0, 1, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pLabel = QtWidgets.QLabel(InternetSentinelDialog)
        self.pLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.pLabel.setFont(font)
        self.pLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pLabel.setObjectName("pLabel")
        self.verticalLayout_2.addWidget(self.pLabel)
        self.pingLabel = QtWidgets.QLabel(InternetSentinelDialog)
        self.pingLabel.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(25)
        self.pingLabel.setFont(font)
        self.pingLabel.setText("")
        self.pingLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pingLabel.setObjectName("pingLabel")
        self.verticalLayout_2.addWidget(self.pingLabel)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.horizontalLayout_4.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_10.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_8 = QtWidgets.QLabel(InternetSentinelDialog)
        self.label_8.setMinimumSize(QtCore.QSize(0, 50))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_10.addWidget(self.label_8)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setContentsMargins(5, -1, -1, -1)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.testServerLabel = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.testServerLabel.setFont(font)
        self.testServerLabel.setText("")
        self.testServerLabel.setObjectName("testServerLabel")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.testServerLabel)
        self.lniLabel = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lniLabel.setFont(font)
        self.lniLabel.setObjectName("lniLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lniLabel)
        self.lastNetworkIssueDateLabel = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lastNetworkIssueDateLabel.setFont(font)
        self.lastNetworkIssueDateLabel.setText("")
        self.lastNetworkIssueDateLabel.setObjectName("lastNetworkIssueDateLabel")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lastNetworkIssueDateLabel)
        self.isLabel = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.isLabel.setFont(font)
        self.isLabel.setObjectName("isLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.isLabel)
        self.internetStatusLabel = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.internetStatusLabel.setFont(font)
        self.internetStatusLabel.setText("")
        self.internetStatusLabel.setObjectName("internetStatusLabel")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.internetStatusLabel)
        self.verticalLayout_10.addLayout(self.formLayout_2)
        self.horizontalLayout_5.addLayout(self.verticalLayout_10)
        self.speedometerWidget = AnalogGaugeWidget(InternetSentinelDialog)
        self.speedometerWidget.setMinimumSize(QtCore.QSize(200, 200))
        self.speedometerWidget.setMaximumSize(QtCore.QSize(200, 200))
        self.speedometerWidget.setObjectName("speedometerWidget")
        self.horizontalLayout_5.addWidget(self.speedometerWidget)
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_12.addWidget(self.label)
        self.resetInternetConnectionPushButton = QtWidgets.QPushButton(InternetSentinelDialog)
        self.resetInternetConnectionPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.resetInternetConnectionPushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.resetInternetConnectionPushButton.setFont(font)
        self.resetInternetConnectionPushButton.setObjectName("resetInternetConnectionPushButton")
        self.verticalLayout_12.addWidget(self.resetInternetConnectionPushButton, 0, QtCore.Qt.AlignHCenter)
        self.rebootSystemPushButton = QtWidgets.QPushButton(InternetSentinelDialog)
        self.rebootSystemPushButton.setMinimumSize(QtCore.QSize(0, 40))
        self.rebootSystemPushButton.setMaximumSize(QtCore.QSize(120, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.rebootSystemPushButton.setFont(font)
        self.rebootSystemPushButton.setObjectName("rebootSystemPushButton")
        self.verticalLayout_12.addWidget(self.rebootSystemPushButton, 0, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(InternetSentinelDialog)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        self.label_5.setFont(font)
        self.label_5.setText("")
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_12.addWidget(self.label_5)
        self.horizontalLayout_5.addLayout(self.verticalLayout_12)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.configLabel = QtWidgets.QLabel(InternetSentinelDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configLabel.sizePolicy().hasHeightForWidth())
        self.configLabel.setSizePolicy(sizePolicy)
        self.configLabel.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.configLabel.setFont(font)
        self.configLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.configLabel.setObjectName("configLabel")
        self.verticalLayout_7.addWidget(self.configLabel)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.formLayout_3.setContentsMargins(5, -1, 5, -1)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_6 = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.downloadFloorSpinBox = QtWidgets.QSpinBox(InternetSentinelDialog)
        self.downloadFloorSpinBox.setMinimumSize(QtCore.QSize(0, 23))
        self.downloadFloorSpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.downloadFloorSpinBox.setMaximum(100)
        self.downloadFloorSpinBox.setObjectName("downloadFloorSpinBox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.downloadFloorSpinBox)
        self.label_18 = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.resetDelaySpinBox = QtWidgets.QSpinBox(InternetSentinelDialog)
        self.resetDelaySpinBox.setMinimumSize(QtCore.QSize(30, 23))
        self.resetDelaySpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.resetDelaySpinBox.setFont(font)
        self.resetDelaySpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.resetDelaySpinBox.setMaximum(60)
        self.resetDelaySpinBox.setObjectName("resetDelaySpinBox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.resetDelaySpinBox)
        self.label_11 = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.notificationsCheckBox = QtWidgets.QCheckBox(InternetSentinelDialog)
        self.notificationsCheckBox.setMinimumSize(QtCore.QSize(0, 23))
        self.notificationsCheckBox.setText("")
        self.notificationsCheckBox.setChecked(True)
        self.notificationsCheckBox.setObjectName("notificationsCheckBox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.notificationsCheckBox)
        self.label_13 = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout_10.setContentsMargins(-1, -1, 3, -1)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.pingHostOctet1SpinBox = QtWidgets.QSpinBox(InternetSentinelDialog)
        self.pingHostOctet1SpinBox.setMinimumSize(QtCore.QSize(0, 23))
        self.pingHostOctet1SpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pingHostOctet1SpinBox.setFont(font)
        self.pingHostOctet1SpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pingHostOctet1SpinBox.setMaximum(255)
        self.pingHostOctet1SpinBox.setProperty("value", 8)
        self.pingHostOctet1SpinBox.setObjectName("pingHostOctet1SpinBox")
        self.horizontalLayout_10.addWidget(self.pingHostOctet1SpinBox)
        self.label_15 = QtWidgets.QLabel(InternetSentinelDialog)
        self.label_15.setMinimumSize(QtCore.QSize(10, 10))
        self.label_15.setMaximumSize(QtCore.QSize(10, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_10.addWidget(self.label_15)
        self.pingHostOctet2SpinBox = QtWidgets.QSpinBox(InternetSentinelDialog)
        self.pingHostOctet2SpinBox.setMinimumSize(QtCore.QSize(0, 23))
        self.pingHostOctet2SpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pingHostOctet2SpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pingHostOctet2SpinBox.setProperty("value", 8)
        self.pingHostOctet2SpinBox.setObjectName("pingHostOctet2SpinBox")
        self.horizontalLayout_10.addWidget(self.pingHostOctet2SpinBox)
        self.label_16 = QtWidgets.QLabel(InternetSentinelDialog)
        self.label_16.setMinimumSize(QtCore.QSize(10, 0))
        self.label_16.setMaximumSize(QtCore.QSize(10, 16777215))
        self.label_16.setSizeIncrement(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_10.addWidget(self.label_16)
        self.pingHostOctet3SpinBox = QtWidgets.QSpinBox(InternetSentinelDialog)
        self.pingHostOctet3SpinBox.setMinimumSize(QtCore.QSize(0, 23))
        self.pingHostOctet3SpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pingHostOctet3SpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pingHostOctet3SpinBox.setProperty("value", 8)
        self.pingHostOctet3SpinBox.setObjectName("pingHostOctet3SpinBox")
        self.horizontalLayout_10.addWidget(self.pingHostOctet3SpinBox)
        self.label_17 = QtWidgets.QLabel(InternetSentinelDialog)
        self.label_17.setMinimumSize(QtCore.QSize(10, 0))
        self.label_17.setMaximumSize(QtCore.QSize(10, 16777215))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_10.addWidget(self.label_17)
        self.pingHostOctet4SpinBox = QtWidgets.QSpinBox(InternetSentinelDialog)
        self.pingHostOctet4SpinBox.setMinimumSize(QtCore.QSize(0, 23))
        self.pingHostOctet4SpinBox.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pingHostOctet4SpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.pingHostOctet4SpinBox.setMinimum(-3)
        self.pingHostOctet4SpinBox.setProperty("value", 8)
        self.pingHostOctet4SpinBox.setObjectName("pingHostOctet4SpinBox")
        self.horizontalLayout_10.addWidget(self.pingHostOctet4SpinBox)
        self.formLayout_3.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_10)
        self.label_4 = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.testFrequencySpinBox = QtWidgets.QSpinBox(InternetSentinelDialog)
        self.testFrequencySpinBox.setMinimumSize(QtCore.QSize(0, 23))
        self.testFrequencySpinBox.setAlignment(QtCore.Qt.AlignCenter)
        self.testFrequencySpinBox.setObjectName("testFrequencySpinBox")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.testFrequencySpinBox)
        self.verticalLayout_7.addLayout(self.formLayout_3)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setContentsMargins(-1, -1, 5, -1)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_2 = QtWidgets.QLabel(InternetSentinelDialog)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_8.addWidget(self.label_2)
        self.statusPlainTextEdit = QtWidgets.QPlainTextEdit(InternetSentinelDialog)
        self.statusPlainTextEdit.setMaximumSize(QtCore.QSize(16777215, 140))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.statusPlainTextEdit.setFont(font)
        self.statusPlainTextEdit.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.statusPlainTextEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.statusPlainTextEdit.setReadOnly(True)
        self.statusPlainTextEdit.setObjectName("statusPlainTextEdit")
        self.verticalLayout_8.addWidget(self.statusPlainTextEdit, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(InternetSentinelDialog)
        QtCore.QMetaObject.connectSlotsByName(InternetSentinelDialog)

    def retranslateUi(self, InternetSentinelDialog):
        _translate = QtCore.QCoreApplication.translate
        InternetSentinelDialog.setWindowTitle(_translate("InternetSentinelDialog", "Internet Sentinel"))
        self.uLabel.setText(_translate("InternetSentinelDialog", "UPLOAD (Mbps)"))
        self.uploadLabel.setToolTip(_translate("InternetSentinelDialog", "Upload speed of files to the Test Server over internet connection"))
        self.dLabel.setText(_translate("InternetSentinelDialog", "DOWNLOAD (Mbps)"))
        self.downloadLabel.setToolTip(_translate("InternetSentinelDialog", "Download speed of files from the Test Server over internet connection"))
        self.pLabel.setText(_translate("InternetSentinelDialog", "PING (ms)"))
        self.pingLabel.setToolTip(_translate("InternetSentinelDialog", "Time in milliseconds to ping the Test Server"))
        self.label_8.setText(_translate("InternetSentinelDialog", "STATISTICS"))
        self.label_3.setText(_translate("InternetSentinelDialog", "SERVER:"))
        self.testServerLabel.setToolTip(_translate("InternetSentinelDialog", "Test Server used in last Internet speed test"))
        self.lniLabel.setText(_translate("InternetSentinelDialog", "LAST ISSUE:"))
        self.lastNetworkIssueDateLabel.setToolTip(_translate("InternetSentinelDialog", "Last Network Issue Date and Time"))
        self.isLabel.setText(_translate("InternetSentinelDialog", "INTERNET:"))
        self.internetStatusLabel.setToolTip(_translate("InternetSentinelDialog", "Current Internet Connection Status (ON-LINE or OFF-LINE)"))
        self.speedometerWidget.setToolTip(_translate("InternetSentinelDialog", "Graphical representation of Internet Download Speed to Test Server"))
        self.label.setText(_translate("InternetSentinelDialog", "MANUAL CONTROLS"))
        self.resetInternetConnectionPushButton.setToolTip(_translate("InternetSentinelDialog", "Power cycle the Internet device off wait RESET DELAY seconds and power device on"))
        self.resetInternetConnectionPushButton.setText(_translate("InternetSentinelDialog", "RESET INTERNET"))
        self.rebootSystemPushButton.setToolTip(_translate("InternetSentinelDialog", "Reboot the internet Sentinel Device"))
        self.rebootSystemPushButton.setText(_translate("InternetSentinelDialog", "REBOOT SYSTEM"))
        self.configLabel.setText(_translate("InternetSentinelDialog", "CONFIGURATION"))
        self.label_6.setText(_translate("InternetSentinelDialog", "DOWNLOAD FLOOR (Mbps):"))
        self.downloadFloorSpinBox.setToolTip(_translate("InternetSentinelDialog", "Minimum Internet Speed before Internet Device is power cycled"))
        self.label_18.setText(_translate("InternetSentinelDialog", "RESET DELAY (secs):"))
        self.resetDelaySpinBox.setToolTip(_translate("InternetSentinelDialog", "Time between power cycling the internet device down then up"))
        self.label_11.setText(_translate("InternetSentinelDialog", "VOICE NOTIFICATIONS:"))
        self.notificationsCheckBox.setToolTip(_translate("InternetSentinelDialog", "Check to announce Internet issues via voice."))
        self.label_13.setText(_translate("InternetSentinelDialog", "PING HOST:"))
        self.pingHostOctet1SpinBox.setToolTip(_translate("InternetSentinelDialog", "IP Address of Internet Server to test if Internet is up and on-line"))
        self.label_15.setText(_translate("InternetSentinelDialog", "."))
        self.pingHostOctet2SpinBox.setToolTip(_translate("InternetSentinelDialog", "IP Address of Internet Server to test if Internet is up and on-line"))
        self.label_16.setText(_translate("InternetSentinelDialog", "."))
        self.pingHostOctet3SpinBox.setToolTip(_translate("InternetSentinelDialog", "IP Address of Internet Server to test if Internet is up and on-line"))
        self.label_17.setText(_translate("InternetSentinelDialog", "."))
        self.pingHostOctet4SpinBox.setToolTip(_translate("InternetSentinelDialog", "IP Address of Internet Server to test if Internet is up and on-line"))
        self.label_4.setText(_translate("InternetSentinelDialog", "TEST FREQUENCY (mins):"))
        self.testFrequencySpinBox.setToolTip(_translate("InternetSentinelDialog", "Time to wait before testing Internet Speed thru ISP"))
        self.label_2.setText(_translate("InternetSentinelDialog", "STATUS"))
        self.statusPlainTextEdit.setToolTip(_translate("InternetSentinelDialog", "Current Internet connection status information"))
from analoggaugewidget import AnalogGaugeWidget
