from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutUsWindow(object):
    def setupUi(self, AboutUsWindow):
        AboutUsWindow.setObjectName("AboutUsWindow")
        AboutUsWindow.resize(700, 600)
        AboutUsWindow.setWindowTitle("About Us")
        AboutUsWindow.setStyleSheet("background-color: white;")

        self.centralwidget = QtWidgets.QWidget(AboutUsWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Title
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(150, 30, 400, 50))
        self.titleLabel.setText("👨‍💻 Meet the Team")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)

        # Info Label
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(50, 100, 600, 400))
        self.infoLabel.setStyleSheet("font-size: 14px;")
        self.infoLabel.setAlignment(QtCore.Qt.AlignTop)
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setOpenExternalLinks(True)  # 🔵 Cho phép click mở link
        self.infoLabel.setText(
            "<b>🛠 Project Description:</b><br>"
            "This remote control tool allows users to interact with and control a target computer via Gmail commands "
            "and custom functions. Developed as part of a university course project to demonstrate socket programming, "
            "threading, process control, and GUI design.<br><br>"
            
            "<b>👥 Team Members:</b><br>"
            "• Nguyễn Khang Hy – UI Designer & Gmail Integration<br>"
            "• Lê Đinh Nguyên Phong – System Developer & Socket Communication<br>"
            "• Phạm Hoàng Phúc – Process Control & Feature Integration<br><br>"

            "<b>📫 Contact Us:</b><br>"
            "• Facebook (Leader): <a href='https://www.facebook.com/phong.opg.2025' style='color:#1a73e8;'>facebook.com/phong.opg.2025</a><br>"
            "• Email: <a href='mailto:khanghy0604@gmail.com' style='color:#1a73e8;'>khanghy0604@gmail.com</a><br><br>"

            "<b>📍 Course:</b> Computer Networks – HCMUS<br>"
            "<b>📅 Semester:</b> 2025 - Term 3"
        )

        AboutUsWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(AboutUsWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 21))
        AboutUsWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(AboutUsWindow)
        AboutUsWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(AboutUsWindow)
