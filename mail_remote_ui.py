from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
        MainWindow.setStyleSheet("background-color: #2c3e50;")  # Màu nền chính

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Nút Back
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 20, 100, 40))
        self.pushButton.setText("⬅ Back")
        self.pushButton.setStyleSheet("""
            QPushButton {
                background-color: #e74c3c;
                color: white;
                font-weight: bold;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #c0392b;
            }
        """)

        # Nút Choose mail remote
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 20, 200, 40))
        self.pushButton_2.setText("📧 Choose Mail Remote")
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                background-color: #27ae60;
                color: white;
                font-weight: bold;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #1e8449;
            }
        """)

        # Label: Mail Requests
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 80, 200, 30))
        self.label.setText("📨 Mail Requests:")
        self.label.setStyleSheet("color: white; font: bold 14px 'Segoe UI';")

        # Khung nhập Mail Requests
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 110, 860, 230))
        self.textEdit.setStyleSheet("""
            QTextEdit {
                background-color: rgba(255, 255, 255, 0.95);
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                padding: 10px;
                font: 13px 'Consolas';
            }
        """)

        # Label: Processing Results
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 360, 200, 30))
        self.label_2.setText("⚙️ Processing Results:")
        self.label_2.setStyleSheet("color: white; font: bold 14px 'Segoe UI';")

        # Khung kết quả xử lý
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 390, 860, 250))
        self.textEdit_2.setStyleSheet("""
            QTextEdit {
                background-color: rgba(255, 255, 255, 0.95);
                border: 2px solid #bdc3c7;
                border-radius: 10px;
                padding: 10px;
                font: 13px 'Consolas';
            }
        """)

        MainWindow.setCentralWidget(self.centralwidget)

        # MenuBar và StatusBar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 900, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("📡 Gmail Remote Control")


# Để chạy giao diện thử:
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
