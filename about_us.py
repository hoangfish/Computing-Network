from PyQt5.QtWidgets import QApplication, QMainWindow
from about_us_ui import Ui_AboutUsWindow

class AboutUsApp(QMainWindow):  # Đổi tên class thành AboutUsApp cho đồng nhất
    def __init__(self):
        super().__init__()
        self.ui = Ui_AboutUsWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    window = AboutUsApp()
    window.show()
    sys.exit(app.exec_())
