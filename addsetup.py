import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
# import sqlite3

# con = sqlite3.connect("products.db")
# cur = con.cursor()

class AddSetup(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Setup")
        self.setWindowIcon(QIcon('icons/setup.png'))
        self.setGeometry(505, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # widget of top layout #
        self.addSetupImg = QLabel()
        self.img = QPixmap('icons/setup.png')
        self.addSetupImg.setPixmap(self.img)
        self.titleText = QLabel("Setup")

        # widget of bottom layout #
        self.usernameEntry = QLineEdit()
        self.usernameEntry.setPlaceholderText("Username")
        self.passwordEntry = QLineEdit()
        self.passwordEntry.setPlaceholderText("Password")
        self.enterBtn = QPushButton("Enter")
        self.cancelBtn = QPushButton("Cancel")

        # widget of bottom layout #
        # self.photoBtn = QPushButton("Upload Photo")
        # self.photoBtn.clicked.connect(self.funcUploadPhoto)

        # self.videoBtn = QPushButton("Upload Video")
        # self.videoBtn.clicked.connect(self.funcUploadVideo)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()

        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        # add widgets #
        # widgets of top layout
        self.topLayout.addWidget(self.addSetupImg)
        self.topLayout.addWidget(self.titleText)
        self.topFrame.setLayout(self.topLayout)

        # widget of form layout
        self.topLayout.addRow(QLabel("Username: "), self.usernameEntry)
        self.topLayout.addRow(QLabel("Password: "), self.passwordEntry)
        self.topLayout.addRow(QLabel(""), self.enterBtn)
        self.topLayout.addRow(QLabel(""), self.cancelBtn)
        self.topFrame.setLayout(self.bottomLayout)

        # widget of bottom layout
        # self.bottomLayout.addWidget(self.photoBtn)
        # self.bottomLayout.addWidget(self.videoBtn)
        # self.bottomFrame.setLayout(self.bottomLayout)

        #
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
   import sys

   App = QApplication(sys.argv)
   Window = AddSetup()
   sys.exit(App.exec_())
