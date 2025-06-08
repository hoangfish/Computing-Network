from PyQt5.QtWidgets import QApplication, QMainWindow
from mail_remote_ui import Ui_MainWindow
# from mail_reader import MailReader  # Tạm comment vì chưa có module này

class MailRemoteApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối nút
        self.ui.pushButton.clicked.connect(self.go_back)
        self.ui.pushButton_2.clicked.connect(self.choose_mail_remote)

    def choose_mail_remote(self):
        # Tạm thời hiện nội dung giả lập để test giao diện
        # reader = MailReader("khanghy0604@gmail.com", "Hy06042006")
        # content = reader.get_latest_command_mail()
        content = "Nội dung mail mới nhất giả lập"
        self.ui.textEdit.setText(content)

    def go_back(self):
        print("Quay lại!")

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = MailRemoteApp()
    window.show()
    sys.exit(app.exec_())
