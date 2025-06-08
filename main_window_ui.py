# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setWindowTitle("Remote Control - Dashboard")

        # Background màu trắng
        MainWindow.setStyleSheet("background-color: white;")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(200, 50, 400, 50))
        self.titleLabel.setText("REMOTE CONTROL SYSTEM")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Gmail Remote Button
        self.btn_gmail = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gmail.setGeometry(QtCore.QRect(300, 150, 200, 50))
        self.btn_gmail.setText("📧 Gmail Remote")
        self.btn_gmail.setStyleSheet("background-color: #26c6da; color: white; font-size: 16px; border-radius: 10px;")

        # Custom Mode Button
        self.btn_custom = QtWidgets.QPushButton(self.centralwidget)
        self.btn_custom.setGeometry(QtCore.QRect(300, 230, 200, 50))
        self.btn_custom.setText("🛠️ Custom Mode")
        self.btn_custom.setStyleSheet("background-color: #26a69a; color: white; font-size: 16px; border-radius: 10px;")

        # About Us Button
        self.btn_about = QtWidgets.QPushButton(self.centralwidget)
        self.btn_about.setGeometry(QtCore.QRect(300, 310, 200, 50))
        self.btn_about.setText("👨‍💻 About Us")
        self.btn_about.setStyleSheet("background-color: #7e57c2; color: white; font-size: 16px; border-radius: 10px;")

        MainWindow.setCentralWidget(self.centralwidget)

        # Menubar and Statusbar (optional)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
