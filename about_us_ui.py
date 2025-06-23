from PyQt5 import QtCore, QtGui, QtWidgets
import os

def image_path(filename):
    return os.path.join(os.path.dirname(__file__), "images", filename)

class Ui_AboutUsWindow(object):
    def setupUi(self, AboutUsWindow):
        AboutUsWindow.setObjectName("AboutUsWindow")
        AboutUsWindow.resize(800, 900)
        AboutUsWindow.setWindowTitle("About Us")
        AboutUsWindow.setStyleSheet("background-color: #f0f2f5;")

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setWidgetResizable(True)

        self.scrollWidget = QtWidgets.QWidget()
        self.scrollArea.setWidget(self.scrollWidget)

        self.main_layout = QtWidgets.QVBoxLayout(self.scrollWidget)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(25)

        self.backButton = QtWidgets.QPushButton("⬅ Back")
        self.backButton.setFixedSize(100, 40)
        self.backButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.backButton.setStyleSheet("""
            QPushButton {
                background-color: #ff3b30;
                color: white;
                font-weight: bold;
                border: none;
                border-radius: 12px;
                padding-left: 10px;
            }
            QPushButton:hover {
                background-color: #e53e3e;
            }
        """)
        self.backButton.clicked.connect(self.goBack)

        self.main_layout.addSpacing(20)
        backFrame = QtWidgets.QFrame()
        backLayout = QtWidgets.QHBoxLayout(backFrame)
        backLayout.setContentsMargins(20, 0, 0, 0)
        backLayout.setAlignment(QtCore.Qt.AlignLeft)
        backLayout.addWidget(self.backButton)

        self.main_layout.addWidget(backFrame)


        self.addSchoolLogo()

        self.titleLabel = QtWidgets.QLabel("👨‍💻 Meet the Team")
        self.titleLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titleLabel.setStyleSheet("font-size: 26px; font-weight: bold; color: #222;")
        self.main_layout.addWidget(self.titleLabel)

        self.projectLabel = QtWidgets.QLabel()
        self.projectLabel.setWordWrap(True)
        self.projectLabel.setStyleSheet("""
            font-size: 14px;
            color: #333;
            line-height: 1.6;
            background-color: #ffffff;
            border-radius: 10px;
            padding: 15px;
            border: 1px solid #ddd;
        """)
        self.projectLabel.setText(
            "<b>🛠 Project Description:</b><br>"
            "A simple remote-control tool using Gmail for command exchange and system interaction."
        )
        self.main_layout.addWidget(self.projectLabel)

        self.member_cards = []
        self.avatar_buttons = []
        self.addAvatarsAndShortInfo()

        for member in self.team_members:
            card = self.createMemberCard(member)
            self.main_layout.addWidget(card)
            self.member_cards.append(card)

        self.footerLabel = QtWidgets.QLabel()
        self.footerLabel.setStyleSheet("font-size: 13px; color: #444; padding: 10px;")
        self.footerLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.footerLabel.setText(
            "<b>🎓 Course:</b> Computer Networks – HCMUS<br>"
            "<b>📅 Semester:</b> 2025 - Term 3<br>"
            "<b>👨‍🏫 Class:</b> 24C06"
        )
        self.main_layout.addWidget(self.footerLabel)

        AboutUsWindow.setCentralWidget(self.scrollArea)
        self.menubar = QtWidgets.QMenuBar(AboutUsWindow)
        AboutUsWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutUsWindow)
        AboutUsWindow.setStatusBar(self.statusbar)
        QtCore.QMetaObject.connectSlotsByName(AboutUsWindow)

    def addSchoolLogo(self):
        logoRow = QtWidgets.QHBoxLayout()
        logoRow.setAlignment(QtCore.Qt.AlignCenter)
        logoRow.setSpacing(20)

        # Trường hợp ảnh logo hơi dọc (giống ảnh bạn gửi)
        logo = QtWidgets.QLabel()
        pixmap = QtGui.QPixmap(image_path("school_logo.png"))
        logo.setPixmap(pixmap.scaled(110, 130, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation))
        logo.setAlignment(QtCore.Qt.AlignCenter)
        logoRow.addWidget(logo)

        # Text bên phải
        textBox = QtWidgets.QVBoxLayout()
        textBox.setAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        textBox.setSpacing(2)
        
        fitLabel = QtWidgets.QLabel("fit@hcmus")
        fitLabel.setStyleSheet("font-size: 28px; font-weight: bold; color: #003399;")  # xanh đậm hơn

        vnuLabel = QtWidgets.QLabel("VNUHCM - UNIVERSITY OF SCIENCE")
        vnuLabel.setStyleSheet("font-size: 13px; font-weight: bold; color: #333333; text-transform: uppercase;")

        facultyLabel = QtWidgets.QLabel("FACULTY OF INFORMATION TECHNOLOGY")
        facultyLabel.setStyleSheet("font-size: 13px; font-weight: bold; color: #333333; text-transform: uppercase;")

        for lbl in [fitLabel, vnuLabel, facultyLabel]:
            lbl.setAlignment(QtCore.Qt.AlignLeft)

        textBox.addWidget(fitLabel)
        textBox.addWidget(vnuLabel)
        textBox.addWidget(facultyLabel)

        logoRow.addLayout(textBox)
        self.main_layout.addLayout(logoRow)

        # Dòng lớp học phía dưới
        classLabel = QtWidgets.QLabel("Class: Graduation topic on computer network")
        classLabel.setAlignment(QtCore.Qt.AlignCenter)
        classLabel.setStyleSheet("font-size: 16px; color: #222; font-weight: 500; margin-top: 10px;")
        self.main_layout.addWidget(classLabel)

    def addAvatarsAndShortInfo(self):
        self.team_members = [
            {
                "name": "Nguyễn Khang Hy",
                "id": "24127280",
                "role": "UI Designer & Gmail Integration",
                "email": "khanghy0604@gmail.com",
                "github": "https://github.com/nguyenkhanghy",
                "facebook": "https://facebook.com/khanghy204",
                "avatar": "hy.png"
            },
            {
                "name": "Lê Đinh Nguyên Phong",
                "id": "24127215",
                "role": "System Developer & Socket Communication",
                "email": "phong.opg@gmail.com",
                "github": "https://github.com/46thanft",
                "facebook": "https://www.facebook.com/phong.opg.2025",
                "avatar": "phong.png"
            },
            {
                "name": "Phạm Hoàng Phúc",
                "id": "24127502",
                "role": "Process Control & Feature Integration",
                "email": "phucpro104@gmail.com",
                "github": "https://github.com/hoangfish",
                "facebook": "https://www.facebook.com/fish.hoang.2025",
                "avatar": "phuc.png"
            },
        ]

        rowLayout = QtWidgets.QHBoxLayout()
        rowLayout.setSpacing(30)
        rowLayout.setAlignment(QtCore.Qt.AlignCenter)

        for i, member in enumerate(self.team_members):
            card = QtWidgets.QFrame()
            card.setFixedWidth(180)
            card.setStyleSheet("""
                QFrame {
                    background-color: #ffffff;
                    border: 1px solid #ccc;
                    border-radius: 12px;
                }
            """)
            cardLayout = QtWidgets.QVBoxLayout(card)
            cardLayout.setAlignment(QtCore.Qt.AlignCenter)
            cardLayout.setContentsMargins(10, 10, 10, 10)

            avatarBtn = QtWidgets.QPushButton()
            pixmap = QtGui.QPixmap(image_path(member["avatar"]))
            avatarBtn.setIcon(QtGui.QIcon(pixmap))
            avatarBtn.setIconSize(QtCore.QSize(100, 100))
            avatarBtn.setFixedSize(110, 110)
            avatarBtn.setStyleSheet("border: none;")
            avatarBtn.clicked.connect(lambda _, idx=i: self.scrollToCard(idx))

            idLabel = QtWidgets.QLabel(f"{member['id']}")
            idLabel.setAlignment(QtCore.Qt.AlignCenter)
            idLabel.setStyleSheet("font-size: 14px; font-weight: bold; color: #222;")

            nameLabel = QtWidgets.QLabel(member["name"])
            nameLabel.setAlignment(QtCore.Qt.AlignCenter)
            nameLabel.setStyleSheet("font-size: 13px; color: #333;")

            github_user = member['github'].split('/')[-1]
            githubLabel = QtWidgets.QLabel(f"GitHub: <a href='{member['github']}'>{github_user}</a>")
            githubLabel.setOpenExternalLinks(True)
            githubLabel.setAlignment(QtCore.Qt.AlignCenter)
            githubLabel.setStyleSheet("font-size: 12px; color: #1a73e8;")

            cardLayout.addWidget(avatarBtn)
            cardLayout.addSpacing(5)
            cardLayout.addWidget(idLabel)
            cardLayout.addWidget(nameLabel)
            cardLayout.addWidget(githubLabel)

            rowLayout.addWidget(card)

        self.main_layout.addLayout(rowLayout)

    def createMemberCard(self, member):
        card = QtWidgets.QFrame()
        card.setStyleSheet("""
            background-color: white;
            border-radius: 12px;
            padding: 16px;
            border: 1px solid #e0e0e0;
        """)
        layout = QtWidgets.QVBoxLayout(card)
        layout.setSpacing(8)

        name_label = QtWidgets.QLabel(f"👤 Name: {member['name']}")
        name_label.setStyleSheet("font-size: 16px; font-weight: bold; color: #222;")

        id_label = QtWidgets.QLabel(f"🎓 Student ID: {member['id']}")
        role_label = QtWidgets.QLabel(f"🧩 Role: {member['role']}")

        email_label = QtWidgets.QLabel()
        email_label.setText(f"📧 Email: <a href='mailto:{member['email']}' style='color:#1a73e8;'>{member['email']}</a>")
        email_label.setOpenExternalLinks(True)

        github_label = QtWidgets.QLabel()
        github_label.setText(f"🐱 GitHub: <a href='{member['github']}' style='color:#1a73e8;'>{member['github']}</a>")
        github_label.setOpenExternalLinks(True)

        facebook_label = QtWidgets.QLabel()
        facebook_label.setText(f"📘 Facebook: <a href='{member['facebook']}' style='color:#1a73e8;'>{member['facebook']}</a>")
        facebook_label.setOpenExternalLinks(True)

        for label in [id_label, role_label, email_label, github_label, facebook_label]:
            label.setStyleSheet("font-size: 13px; color: #444;")

        layout.addWidget(name_label)
        layout.addWidget(id_label)
        layout.addWidget(role_label)
        layout.addWidget(email_label)
        layout.addWidget(github_label)
        layout.addWidget(facebook_label)

        return card

    def scrollToCard(self, index):
        widget = self.member_cards[index]
        scrollBar = self.scrollArea.verticalScrollBar()
        y = widget.pos().y()
        scrollBar.setValue(y)

    def goBack(self):
        window = self.backButton.window()
        if window:
            window.close()