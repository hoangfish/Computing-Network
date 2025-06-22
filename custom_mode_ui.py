from PyQt5 import QtWidgets, QtCore, QtGui
import os

def icon(path):
    return QtGui.QIcon(os.path.join("icons", path))

class Ui_CustomModeWindow(object):
    def setupUi(self, CustomModeWindow):
        CustomModeWindow.setObjectName("CustomModeWindow")
        CustomModeWindow.resize(950, 600)
        CustomModeWindow.setWindowTitle("Custom Mode - Control Center")

        self.centralwidget = QtWidgets.QWidget(CustomModeWindow)
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # === Taskbar/Header with its own QWidget ===
        self.taskbarWidget = QtWidgets.QWidget()
        self.taskbarWidget.setStyleSheet("""
            background-color: #2c3e50;
            padding: 12px;
            border-radius: 8px;
        """)
        taskbar_layout = QtWidgets.QHBoxLayout(self.taskbarWidget)
        taskbar_layout.setContentsMargins(10, 0, 10, 0)

        self.labelTitle = QtWidgets.QLabel("🔧 Custom Control Center")
        self.labelTitle.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        taskbar_layout.addWidget(self.labelTitle)
        taskbar_layout.addStretch()

        main_layout.addWidget(self.taskbarWidget)


        # === IP Layout ===
        ip_layout = QtWidgets.QHBoxLayout()
        self.lineEditServerIP = QtWidgets.QLineEdit()
        self.lineEditServerIP.setPlaceholderText("Enter server IP...")
        ip_layout.addWidget(QtWidgets.QLabel("Server IP:"))
        ip_layout.addWidget(self.lineEditServerIP)
        main_layout.addLayout(ip_layout)

        # === Content Layout ===
        content_layout = QtWidgets.QHBoxLayout()

        # === Sidebar ===
        self.sidebar = QtWidgets.QWidget()
        main_sidebar_layout = QtWidgets.QVBoxLayout(self.sidebar)
        main_sidebar_layout.setContentsMargins(0, 0, 0, 0)
        main_sidebar_layout.setSpacing(8)

        button_style = """
            QPushButton {
                background-color: #2c3e50;
                color: white;
                font-size: 14px;
                padding: 10px;
                text-align: left;
                border: none;
            }
            QPushButton:hover {
                background-color: #34495e;
            }
        """

        self.btnSystem = QtWidgets.QPushButton("🖥️ System")
        process_icon_path = os.path.join(os.path.dirname(__file__), "process.png")
        self.btnProcesses = QtWidgets.QPushButton("  Processes")
        self.btnProcesses.setIcon(QtGui.QIcon(process_icon_path))
        self.btnApps = QtWidgets.QPushButton("  Apps")
        app_icon_path = os.path.join(os.path.dirname(__file__), "apps_icon.png")
        self.btnApps.setIcon(QtGui.QIcon(app_icon_path))
        self.btnFiles = QtWidgets.QPushButton("📁 Files")
        self.btnWebcam = QtWidgets.QPushButton("📷 Webcam")
        keylogger_icon_path = os.path.join(os.path.dirname(__file__), "keylogger.png")
        self.btnKeylogger = QtWidgets.QPushButton("  Keylogger")
        self.btnKeylogger.setIcon(QtGui.QIcon(keylogger_icon_path))

        top_btn_layout = QtWidgets.QVBoxLayout()
        for btn in [self.btnSystem, self.btnProcesses, self.btnApps,
                    self.btnFiles, self.btnWebcam, self.btnKeylogger]:
            btn.setStyleSheet(button_style)
            top_btn_layout.addWidget(btn)
        main_sidebar_layout.addLayout(top_btn_layout)

        logo_layout = QtWidgets.QVBoxLayout()
        logo_layout.addStretch()
        self.labelSchoolLogo = QtWidgets.QLabel()
        school_logo_path = os.path.join(os.path.dirname(__file__), "school_logo.png")
        school_pixmap = QtGui.QPixmap(school_logo_path)
        self.labelSchoolLogo.setPixmap(
            school_pixmap.scaled(160, 160, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
        )
        self.labelSchoolLogo.setAlignment(QtCore.Qt.AlignCenter)
        logo_layout.addWidget(self.labelSchoolLogo)
        logo_layout.addStretch()
        main_sidebar_layout.addLayout(logo_layout)

        self.btnBack = QtWidgets.QPushButton("🔙 Back")
        self.btnBack.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-size: 14px;
                padding: 10px;
                text-align: left;
                border: none;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)
        main_sidebar_layout.addWidget(self.btnBack, alignment=QtCore.Qt.AlignBottom)

        self.sidebar.setFixedWidth(160)
        content_layout.addWidget(self.sidebar)

        # === Pages ===
        self.stackedWidget = QtWidgets.QStackedWidget()
        content_layout.addWidget(self.stackedWidget)
        main_layout.addLayout(content_layout)

        self.pageSystem = self.create_system_page()
        self.pageProcesses = self.create_process_page()
        self.pageApps = self.create_apps_page()
        self.pageFiles = self.create_files_page()
        self.pageWebcam = self.create_webcam_page()
        self.pageKeylogger = self.create_keylogger_page()
        self.pageEmpty = QtWidgets.QWidget()

        self.stackedWidget.addWidget(self.pageSystem)
        self.stackedWidget.addWidget(self.pageProcesses)
        self.stackedWidget.addWidget(self.pageApps)
        self.stackedWidget.addWidget(self.pageFiles)
        self.stackedWidget.addWidget(self.pageWebcam)
        self.stackedWidget.addWidget(self.pageKeylogger)
        self.stackedWidget.addWidget(self.pageEmpty)

        CustomModeWindow.setCentralWidget(self.centralwidget)

        self.btnSystem.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btnProcesses.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btnApps.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btnFiles.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btnWebcam.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.btnKeylogger.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))
        self.btnBack.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(6))

    def create_output_log(self):
        label = QtWidgets.QLabel("📤 Output Log:")
        text_output = QtWidgets.QTextEdit()
        text_output.setReadOnly(True)
        text_output.setMinimumHeight(80)
        text_output.setStyleSheet("background-color: #f4f4f4; font-family: Consolas;")
        return label, text_output

    def make_buttons_fixed(self, buttons, width=120, height=36):
        for btn in buttons:
            btn.setFixedSize(width, height)

    def create_system_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        label = QtWidgets.QLabel("❗ Use these actions with caution. They will affect the entire system.")
        label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(label)
        self.btnRestart = QtWidgets.QPushButton("🔄 Restart")
        self.btnRestart.setIcon(icon("restart.png"))
        self.btnShutdown = QtWidgets.QPushButton("📴 Shutdown")
        self.btnShutdown.setIcon(icon("shutdown.png"))
        self.make_buttons_fixed([self.btnRestart, self.btnShutdown])
        layout.addWidget(self.btnRestart)
        layout.addWidget(self.btnShutdown)
        layout.addSpacing(15)
        log_label, log_output = self.create_output_log()
        self.textOutputSystem = log_output
        layout.addWidget(log_label)
        layout.addWidget(log_output)
        return page

    def create_process_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        label = QtWidgets.QLabel("📋 Manage system processes. View, start, or stop processes by name or PID.")
        label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(label)
        button_layout = QtWidgets.QHBoxLayout()
        self.btnListProcesses = QtWidgets.QPushButton("📄 List")
        self.btnStartProcess = QtWidgets.QPushButton("🟢 Start")
        self.btnStopProcess = QtWidgets.QPushButton("🔴 Stop")
        self.make_buttons_fixed([self.btnListProcesses, self.btnStartProcess, self.btnStopProcess])
        button_layout.addWidget(self.btnListProcesses)
        button_layout.addWidget(self.btnStartProcess)
        button_layout.addWidget(self.btnStopProcess)
        layout.addLayout(button_layout)
        self.tableProcesses = QtWidgets.QTableWidget()
        self.tableProcesses.setColumnCount(3)
        self.tableProcesses.setHorizontalHeaderLabels(['PID', 'Name', 'User'])
        self.tableProcesses.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableProcesses.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableProcesses.verticalHeader().setVisible(False)
        self.tableProcesses.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableProcesses.setSortingEnabled(True)
        self.tableProcesses.setMinimumHeight(180)
        self.tableProcesses.setMaximumHeight(200)
        header = self.tableProcesses.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        layout.addWidget(self.tableProcesses)
        layout.addSpacing(15)
        log_label, log_output = self.create_output_log()
        self.textOutputProcesses = log_output
        layout.addWidget(log_label)
        layout.addWidget(log_output)
        return page

    def create_apps_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        label = QtWidgets.QLabel("💡 Start or stop apps by typing their exact name (e.g. chrome, notepad).")
        label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(label)
        self.btnListApps = QtWidgets.QPushButton("📄 List Apps")
        self.btnStartApp = QtWidgets.QPushButton("🟢 Start App")
        self.btnStopApp = QtWidgets.QPushButton("🔴 Stop App")
        self.make_buttons_fixed([self.btnListApps, self.btnStartApp, self.btnStopApp])
        layout.addWidget(self.btnListApps)
        layout.addWidget(self.btnStartApp)
        layout.addWidget(self.btnStopApp)
        layout.addSpacing(15)
        log_label, log_output = self.create_output_log()
        self.textOutputApps = log_output
        layout.addWidget(log_label)
        layout.addWidget(log_output)
        return page

    def create_files_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        label = QtWidgets.QLabel("📄 Enter a full absolute file path (e.g. C:/Users/Name/Desktop/file.txt).")
        label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(label)
        self.lineEditFilePath = QtWidgets.QLineEdit()
        self.lineEditFilePath.setPlaceholderText("Enter file path...")
        self.btnGetFile = QtWidgets.QPushButton("📥 Get File Content")
        self.make_buttons_fixed([self.btnGetFile], width=160)
        layout.addWidget(self.lineEditFilePath)
        layout.addWidget(self.btnGetFile)
        layout.addSpacing(15)
        log_label, log_output = self.create_output_log()
        self.textOutputFiles = log_output
        layout.addWidget(log_label)
        layout.addWidget(log_output)
        return page

    def create_webcam_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        label = QtWidgets.QLabel("📷 Capture photo or record video using the target's webcam.")
        label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(label)
        self.btnCapturePhoto = QtWidgets.QPushButton("📸 Capture Photo")
        self.btnRecordVideo = QtWidgets.QPushButton("🎥 Record Video")
        self.spinBoxRecordSec = QtWidgets.QSpinBox()
        self.spinBoxRecordSec.setRange(1, 60)
        self.spinBoxRecordSec.setValue(5)
        self.spinBoxRecordSec.setMaximumWidth(100)
        self.make_buttons_fixed([self.btnCapturePhoto, self.btnRecordVideo], width=160)
        layout.addWidget(self.btnCapturePhoto)
        layout.addWidget(self.btnRecordVideo)
        duration_layout = QtWidgets.QHBoxLayout()
        duration_layout.addWidget(QtWidgets.QLabel("Duration (seconds):"))
        duration_layout.addWidget(self.spinBoxRecordSec)
        duration_layout.addStretch()
        layout.addLayout(duration_layout)
        layout.addSpacing(15)
        log_label, log_output = self.create_output_log()
        self.textOutputWebcam = log_output
        layout.addWidget(log_label)
        layout.addWidget(log_output)
        return page

    def create_keylogger_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        label = QtWidgets.QLabel("👁️ Keylogger will record keystrokes remotely.")
        label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(label)
        self.btnKeyLogger = QtWidgets.QPushButton("🔴 Start Keylogger")
        self.btnKeyLogger.setIcon(icon("keylogger.png"))
        self.make_buttons_fixed([self.btnKeyLogger], width=180)
        layout.addWidget(self.btnKeyLogger)
        layout.addSpacing(15)
        log_label, log_output = self.create_output_log()
        self.textOutputKeylogger = log_output
        layout.addWidget(log_label)
        layout.addWidget(log_output)
        return page
