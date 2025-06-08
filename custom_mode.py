# upgraded_custom_mode.py
import sys
import os
import subprocess
import threading
import time
from datetime import datetime

from PyQt5.QtWidgets import (QMainWindow, QApplication, QMessageBox, QInputDialog,
                             QFileDialog, QVBoxLayout, QLabel, QHBoxLayout, QWidget)
from PyQt5.QtCore import Qt

from custom_mode_ui import Ui_CustomModeWindow

try:
    import cv2
except ImportError:
    cv2 = None

class CustomModeApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CustomModeWindow()
        self.ui.setupUi(self)

        self.ui.btnListApps.clicked.connect(self.list_apps)
        self.ui.btnStartApp.clicked.connect(self.start_app)
        self.ui.btnStopApp.clicked.connect(self.stop_app)

        self.ui.btnListProcesses.clicked.connect(self.list_processes)
        self.ui.btnStartProcess.clicked.connect(self.start_process)
        self.ui.btnStopProcess.clicked.connect(self.stop_process)

        self.ui.btnStartKeylogger.clicked.connect(self.start_keylogger)
        self.ui.btnStopKeylogger.clicked.connect(self.stop_keylogger)

        self.ui.btnRestart.clicked.connect(self.restart_system)
        self.ui.btnShutdown.clicked.connect(self.shutdown_system)

        self.ui.btnGetFile.clicked.connect(self.get_file_content)

        self.ui.btnCapturePhoto.clicked.connect(self.capture_photo)
        self.ui.btnRecordVideo.clicked.connect(self.record_video)

        #self.ui.btnSystemInfo.clicked.connect(self.show_system_info)

        self.keylogger_running = False
        self.keylogger_thread = None

        self.recording = False

    def append_output(self, text):
        timestamp = datetime.now().strftime("[%H:%M:%S]")
        self.ui.textEditOutput.append(f"{timestamp} {text}")

    def list_apps(self):
        self.append_output("Listing installed apps (demo)...")
        apps = ["Chrome", "Notes", "Visual Studio Code", "Spotify"]
        self.append_output("Installed apps:\n" + "\n".join(apps))


    def start_app(self):
        app_name, ok = QInputDialog.getText(self, "Start App", "Enter app name to start:")
        if ok and app_name.strip():
            self.append_output(f"Starting app: {app_name}")
            try:
                if sys.platform == 'darwin':  # macOS
                    result = subprocess.run(['open', '-a', app_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    if result.returncode == 0:
                        self.append_output("Started successfully.")
                    else:
                        self.append_output(f"Error: {result.stderr.decode().strip()}")
                elif os.name == 'nt':
                    os.startfile(app_name)
                    self.append_output("Started successfully.")
                else:
                    subprocess.Popen(app_name.strip().split())
                    self.append_output("Started successfully.")
            except Exception as e:
                self.append_output(f"Error: {e}")


    def stop_app(self):
        app_name, ok = QInputDialog.getText(self, "Stop App", "Enter app name to stop:")
        if ok and app_name.strip():
            self.append_output(f"Stopping app: {app_name}")
            try:
                if sys.platform == 'darwin':  # macOS
                    script = f'tell application "{app_name}" to quit'
                    result = subprocess.run(['osascript', '-e', script], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                    if result.returncode == 0:
                        self.append_output(f"{app_name} stopped.")
                    else:
                        self.append_output(f"Failed to stop {app_name}: {result.stderr.decode().strip()}")
                elif os.name == 'nt':
                    cmd = f'taskkill /IM {app_name}.exe /F'
                    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    if result.returncode == 0:
                        self.append_output(f"{app_name} stopped.")
                    else:
                        self.append_output(f"Failed to stop {app_name}.\n{result.stderr}")
                else:
                    cmd = ['pkill', '-f', app_name]
                    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    if result.returncode == 0:
                        self.append_output(f"{app_name} stopped.")
                    else:
                        self.append_output(f"Failed to stop {app_name}. Maybe it's not running.")
            except Exception as e:
                self.append_output(f"Error: {e}")


    def list_processes(self):
        self.append_output("Listing running processes...")
        cmd = 'tasklist' if os.name == 'nt' else 'ps aux'
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.append_output(result.stdout or result.stderr)

    def start_process(self):
        process_name, ok = QInputDialog.getText(self, "Start Process", "Enter process name or path:")
        if ok and process_name.strip():
            try:
                subprocess.Popen(process_name.strip().split())
                self.append_output("Process started.")
            except Exception as e:
                self.append_output(f"Error: {e}")

    def stop_process(self):
        pid_str, ok = QInputDialog.getText(self, "Stop Process", "Enter process PID to stop:")
        if ok and pid_str.strip().isdigit():
            pid = int(pid_str.strip())
            try:
                if os.name == 'nt':
                    cmd = f'taskkill /PID {pid} /F'
                    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                    self.append_output(result.stdout or result.stderr)
                else:
                    os.kill(pid, 9)
                    self.append_output(f"Process {pid} stopped.")
            except Exception as e:
                self.append_output(f"Error: {e}")

    def keylogger_worker(self):
        self.append_output("Keylogger started. Logging keys...")
        while self.keylogger_running:
            time.sleep(2)
            self.append_output("[Keylogger] Simulated log...")

    def start_keylogger(self):
        if not self.keylogger_running:
            self.keylogger_running = True
            self.keylogger_thread = threading.Thread(target=self.keylogger_worker, daemon=True)
            self.keylogger_thread.start()
        else:
            self.append_output("Keylogger is already running.")

    def stop_keylogger(self):
        if self.keylogger_running:
            self.keylogger_running = False
            self.keylogger_thread.join()
            self.append_output("Keylogger stopped.")
        else:
            self.append_output("Keylogger is not running.")

    def restart_system(self):
        reply = QMessageBox.question(self, 'Restart', 'Restart system?', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.system("shutdown /r /t 1" if os.name == 'nt' else "sudo reboot")

    def shutdown_system(self):
        reply = QMessageBox.question(self, 'Shutdown', 'Shutdown system?', QMessageBox.Yes | QMessageBox.No)
        if reply == QMessageBox.Yes:
            os.system("shutdown /s /t 1" if os.name == 'nt' else "sudo shutdown now")

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

    def capture_photo(self):
        if cv2 is None:
            self.append_output("OpenCV not installed.")
            return
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            self.append_output("Cannot open webcam.")
            return
        ret, frame = cap.read()
        if ret:
            filename = f"photo_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(filename, frame)
            self.append_output(f"Photo saved as {filename}")
        cap.release()
        cv2.destroyAllWindows()

    def record_video(self):
        if cv2 is None:
            self.append_output("OpenCV not installed.")
            return
        duration = self.ui.spinBoxRecordSec.value()
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            self.append_output("Cannot open webcam.")
            return
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        filename = f"video_{datetime.now().strftime('%Y%m%d_%H%M%S')}.avi"
        out = cv2.VideoWriter(filename, fourcc, 20.0, (640, 480))

        self.append_output(f"Recording for {duration} seconds...")
        start_time = time.time()
        while int(time.time() - start_time) < duration:
            ret, frame = cap.read()
            if ret:
                out.write(frame)
            else:
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        self.append_output(f"Video saved as {filename}")

    def show_system_info(self):
        self.append_output("Fetching system info...")
        if os.name == 'nt':
            cmd = "systeminfo"
        else:
            cmd = "uname -a"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.append_output(result.stdout or result.stderr)

    def list_usb_devices(self):
        self.append_output("Listing connected USB devices...")
        if os.name == 'nt':
            cmd = "wmic path CIM_LogicalDevice where ""Description like '%USB%'"" get /value"
        else:
            cmd = "lsusb"
        result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        self.append_output(result.stdout or result.stderr)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CustomModeApp()
    window.show()
    sys.exit(app.exec_())
