from PyQt5.QtWidgets import QApplication, QMainWindow
from main_window_ui import Ui_MainWindow

# Import các cửa sổ con
from mail_remote import MailRemoteApp
from custom_mode import CustomModeApp
from about_us import AboutUsApp

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối nút
        self.ui.btn_gmail.clicked.connect(self.open_gmail_remote)
        self.ui.btn_custom.clicked.connect(self.open_custom_mode)
        self.ui.btn_about.clicked.connect(self.open_about_us)

        # Khởi tạo biến để giữ cửa sổ con tránh bị garbage collection
        self.gmail_window = None
        self.custom_window = None
        self.about_window = None

    def open_gmail_remote(self):
        if self.gmail_window is None:
            self.gmail_window = MailRemoteApp()
        self.gmail_window.show()

    def open_custom_mode(self):
        if self.custom_window is None:
            self.custom_window = CustomModeApp()
        self.custom_window.show()

    def open_about_us(self):
        if self.about_window is None:
            self.about_window = AboutUsApp()
        self.about_window.show()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
