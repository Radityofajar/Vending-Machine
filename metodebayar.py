# import sys
# import serial
# import time
import sistemqr
import sistemtap

from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *


class MetodeBayar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Metode Pembayaran")
        self.setGeometry(455, 200, 450, 350)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # widgets of top layout #
        # self.paymentSysImg = QLabel()
        # self.img = QPixmap('qrcode.png')
        # self.paymentSysImg.setPixmap(self.img)
        self.titleText = QLabel("Pilih Metode Pembayaran")

        # widgets of bottom layout #
        # self.qrBtn = QPushButton(self)
        # self.qrBtn.setGeometry(QtCore.QRect(65, 100, 150, 150))
        # self.qrBtn.setStyleSheet("background-image : url(scan.jpg);")
        # self.qrBtn.resize(120, 120)
        self.qrBtn = QPushButton("Scan QR Code")
        self.qrBtn.clicked.connect(self.funcSistemQR)

        # self.tapBtn = QPushButton(self)
        # self.tapBtn.setGeometry(QtCore.QRect(65, 100, 150, 150))
        # self.tapBtn.setStyleSheet("background-image : url(tap.jpg);")
        # self.tapBtn.resize(120, 120)
        self.tapBtn = QPushButton("Tap Card")
        self.tapBtn.clicked.connect(self.funcSistemTap)

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()

        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        # add widgets #
        # widget of toplayout #
        # self.topLayout.addWidget(self.paymentSysImg)
        self.topLayout.addWidget(self.titleText)
        self.topFrame.setLayout(self.topLayout)

        # widget of form layout #
        self.bottomLayout.addRow(QLabel(""), self.qrBtn)
        self.bottomLayout.addRow(QLabel(""), self.tapBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        #
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)

    def funcSistemQR(self):
        self.newSys = sistemqr.SistemQR()
        self.close()

    def funcSistemTap(self):
        self.newSys = sistemtap.SistemTap()
        self.close()

if __name__ == "__main__":
   import sys
   App = QApplication(sys.argv)
   Window = MetodeBayar()
   sys.exit(App.exec_())