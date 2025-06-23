from PyQt5 import QtWidgets, QtCore, QtGui
import os

def image_path(filename):
    return os.path.join(os.path.dirname(__file__), "images", filename)

def icon(filename):
    return QtGui.QIcon(image_path(filename))

class Ui_CustomModeWindow(object):
    def setupUi(self, CustomModeWindow):
        CustomModeWindow.setObjectName("CustomModeWindow")
        CustomModeWindow.resize(950, 600)
        CustomModeWindow.setWindowTitle("Custom Mode - Control Center")

        self.centralwidget = QtWidgets.QWidget(CustomModeWindow)
        main_layout = QtWidgets.QVBoxLayout(self.centralwidget)
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Taskbar
        self.taskbarWidget = QtWidgets.QWidget()
        self.taskbarWidget.setStyleSheet("background-color: #2c3e50; padding: 12px; border-radius: 8px;")
        taskbar_layout = QtWidgets.QHBoxLayout(self.taskbarWidget)
        taskbar_layout.setContentsMargins(10, 0, 10, 0)
        self.labelTitle = QtWidgets.QLabel("🔧 Custom Control Center")
        self.labelTitle.setStyleSheet("font-size: 18px; font-weight: bold; color: white;")
        taskbar_layout.addWidget(self.labelTitle)
        taskbar_layout.addStretch()
        main_layout.addWidget(self.taskbarWidget)

        # IP input
        ip_layout = QtWidgets.QHBoxLayout()
        self.lineEditServerIP = QtWidgets.QLineEdit()
        self.lineEditServerIP.setPlaceholderText("Enter server IP...")
        ip_layout.addWidget(QtWidgets.QLabel("Server IP:"))
        ip_layout.addWidget(self.lineEditServerIP)
        main_layout.addLayout(ip_layout)

        # Main content layout
        content_layout = QtWidgets.QHBoxLayout()

        # Sidebar
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
        self.btnProcesses = QtWidgets.QPushButton("  Processes")
        self.btnProcesses.setIcon(icon("process.png"))
        self.btnApps = QtWidgets.QPushButton("  Apps")
        self.btnApps.setIcon(icon("apps_icon.png"))
        self.btnFiles = QtWidgets.QPushButton("📁 Files")
        self.btnWebcam = QtWidgets.QPushButton("📷 Webcam")
        self.btnKeylogger = QtWidgets.QPushButton("  Keylogger")
        self.btnKeylogger.setIcon(icon("keylogger.png"))

        for btn in [self.btnSystem, self.btnProcesses, self.btnApps,
                    self.btnFiles, self.btnWebcam, self.btnKeylogger]:
            btn.setStyleSheet(button_style)
            main_sidebar_layout.addWidget(btn)

        main_sidebar_layout.addStretch()

        self.labelSchoolLogo = QtWidgets.QLabel()
        school_pixmap = QtGui.QPixmap(image_path("school_logo.png"))
        self.labelSchoolLogo.setPixmap(school_pixmap.scaled(160, 160, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        self.labelSchoolLogo.setAlignment(QtCore.Qt.AlignCenter)
        main_sidebar_layout.addStretch()
        main_sidebar_layout.addWidget(self.labelSchoolLogo, alignment=QtCore.Qt.AlignCenter)
        main_sidebar_layout.addSpacing(20)  # Giảm số này nếu muốn lệch lên cao hơn

        self.btnBackToMain = QtWidgets.QPushButton("⬅ Back to Main")
        self.btnBackToMain.setStyleSheet("""
            QPushButton {
                background-color: #3498db;
                color: white;
                font-size: 14px;
                padding: 10px;
                text-align: left;
                border: none;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }
        """)
        main_sidebar_layout.addWidget(self.btnBackToMain)

        self.sidebar.setFixedWidth(160)
        content_layout.addWidget(self.sidebar)

        # Pages
        self.stackedWidget = QtWidgets.QStackedWidget()
        content_layout.addWidget(self.stackedWidget)
        main_layout.addLayout(content_layout)

        # Pages
        self.pageSystem = self.create_system_page()
        self.pageProcesses = self.create_process_page()
        self.pageApps = self.create_apps_page()
        self.pageFiles = self.create_files_page()
        self.pageWebcam = self.create_webcam_page()
        self.pageKeylogger = self.create_keylogger_page()
        self.pageEmpty = QtWidgets.QWidget()

        for page in [self.pageSystem, self.pageProcesses, self.pageApps,
                     self.pageFiles, self.pageWebcam, self.pageKeylogger, self.pageEmpty]:
            self.stackedWidget.addWidget(page)

        CustomModeWindow.setCentralWidget(self.centralwidget)

        self.btnSystem.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        self.btnProcesses.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        self.btnApps.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btnFiles.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        self.btnWebcam.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(4))
        self.btnKeylogger.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(5))

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
        self.textOutputProcess = log_output
        layout.addWidget(log_label)
        layout.addWidget(log_output)
        return page

    def create_apps_page(self):
        page = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout(page)
        layout.setSpacing(10)  # 🔧 Giảm khoảng cách giữa các khối dọc

        # Info label
        label = QtWidgets.QLabel("💡 Start or stop apps by typing their exact name (e.g. chrome, notepad).")
        label.setStyleSheet("color: gray; font-size: 12px;")
        layout.addWidget(label)

        # List Apps Button
        self.btnListApps = QtWidgets.QPushButton("📄 List Apps")
        self.make_buttons_fixed([self.btnListApps])
        list_app_layout = QtWidgets.QHBoxLayout()
        list_app_layout.setContentsMargins(0, 0, 0, 0)
        list_app_layout.setSpacing(6)
        list_app_layout.addWidget(self.btnListApps)
        list_app_layout.addStretch()
        layout.addLayout(list_app_layout)

        # --- Start App Stack ---
        self.startStack = QtWidgets.QStackedWidget()

        # Start button only
        start_button_only = QtWidgets.QWidget()
        h1 = QtWidgets.QHBoxLayout(start_button_only)
        h1.setContentsMargins(0, 0, 0, 0)
        h1.setSpacing(6)
        self.btnStartAppOnly = QtWidgets.QPushButton("🟢 Start App")
        self.make_buttons_fixed([self.btnStartAppOnly])
        h1.addWidget(self.btnStartAppOnly)
        h1.addStretch()

        # Start with input
        start_input = QtWidgets.QWidget()
        h2 = QtWidgets.QHBoxLayout(start_input)
        h2.setContentsMargins(0, 0, 0, 0)
        h2.setSpacing(6)
        self.btnStartAppInput = QtWidgets.QPushButton("🟢 Start App")
        self.lineEditStartApp = QtWidgets.QLineEdit()
        self.lineEditStartApp.setPlaceholderText("Enter app name to start...")
        self.lineEditStartApp.setMinimumWidth(200)
        self.lineEditStartApp.setMinimumHeight(36)
        self.lineEditStartApp.setStyleSheet("font-size: 14px; padding: 6px;")
        self.make_buttons_fixed([self.btnStartAppInput])
        h2.addWidget(self.btnStartAppInput)
        h2.addWidget(self.lineEditStartApp)

        self.startStack.addWidget(start_button_only)
        self.startStack.addWidget(start_input)
        start_wrapper = QtWidgets.QWidget()
        start_layout = QtWidgets.QVBoxLayout(start_wrapper)
        start_layout.setContentsMargins(0, 0, 0, 0)
        start_layout.addWidget(self.startStack)
        self.startStack.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        layout.addWidget(start_wrapper)

        # --- Stop App Stack ---
        self.stopStack = QtWidgets.QStackedWidget()

        # Stop button only
        stop_button_only = QtWidgets.QWidget()
        h3 = QtWidgets.QHBoxLayout(stop_button_only)
        h3.setContentsMargins(0, 0, 0, 0)
        h3.setSpacing(6)
        self.btnStopAppOnly = QtWidgets.QPushButton("🔴 Stop App")
        self.make_buttons_fixed([self.btnStopAppOnly])
        h3.addWidget(self.btnStopAppOnly)
        h3.addStretch()

        # Stop with input
        stop_input = QtWidgets.QWidget()
        h4 = QtWidgets.QHBoxLayout(stop_input)
        h4.setContentsMargins(0, 0, 0, 0)
        h4.setSpacing(6)
        self.btnStopAppInput = QtWidgets.QPushButton("🔴 Stop App")
        self.lineEditStopApp = QtWidgets.QLineEdit()
        self.lineEditStopApp.setPlaceholderText("Enter app name to stop...")
        self.lineEditStopApp.setMinimumWidth(200)
        self.lineEditStopApp.setMinimumHeight(36)
        self.lineEditStopApp.setStyleSheet("font-size: 14px; padding: 6px;")
        self.make_buttons_fixed([self.btnStopAppInput])
        h4.addWidget(self.btnStopAppInput)
        h4.addWidget(self.lineEditStopApp)

        self.stopStack.addWidget(stop_button_only)
        self.stopStack.addWidget(stop_input)
        stop_wrapper = QtWidgets.QWidget()
        stop_layout = QtWidgets.QVBoxLayout(stop_wrapper)
        stop_layout.setContentsMargins(0, 0, 0, 0)
        stop_layout.addWidget(self.stopStack)
        self.stopStack.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        layout.addWidget(stop_wrapper)

        # --- Output Log ---
        log_label, log_output = self.create_output_log()
        self.textEditAppLog = log_output
        log_output.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        layout.addWidget(log_label)
        layout.addWidget(log_output)

        # --- Events ---
        self.btnStartAppOnly.clicked.connect(self.toggle_start_input)
        self.btnStartAppInput.clicked.connect(self.toggle_start_input)
        self.btnStopAppOnly.clicked.connect(self.toggle_stop_input)
        self.btnStopAppInput.clicked.connect(self.toggle_stop_input)

        return page

    def toggle_start_input(self):
        self.startStack.setCurrentIndex(1 if self.startStack.currentIndex() == 0 else 0)
        self.stopStack.setCurrentIndex(0)

    def toggle_stop_input(self):
        self.stopStack.setCurrentIndex(1 if self.stopStack.currentIndex() == 0 else 0)
        self.startStack.setCurrentIndex(0)

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