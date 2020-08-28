import sys
# import serial
# import time

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PaymentSys(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Payment System")
        self.setGeometry(500, 200, 350, 350)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()

    def widgets(self):
        # widgets of top layout #
        self.paymentSysImg = QLabel()
        self.img = QPixmap('qrcode.png')
        self.paymentSysImg.setPixmap(self.img)
        self.titleText = QLabel("Scan QR Code")

        # widgets of bottom layout #
        self.yesBtn = QPushButton("Transaksi Berhasil")
        yes_btn = 'Y'
        self.yesBtn.clicked.connect(lambda: self.clickme2(yes_btn))

        self.noBtn = QPushButton("Transaksi Gagal")
        no_btn = 'N'
        self.noBtn.clicked.connect(lambda: self.clickme2(no_btn))

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QHBoxLayout()
        self.bottomLayout = QFormLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        # add widgets #
        # widget of toplayout #
        self.topLayout.addWidget(self.paymentSysImg)
        self.topLayout.addWidget(self.titleText)
        self.topFrame.setLayout(self.topLayout)

        # widget of form layout #
        self.bottomLayout.addRow(QLabel(""), self.yesBtn)
        self.bottomLayout.addRow(QLabel(""), self.noBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        #########
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)

    def clickme2(self, arg):
        print(arg)

        self.close()

if __name__ == "__main__":
   import sys
   App = QApplication(sys.argv)
   Window = PaymentSys()
   sys.exit(App.exec_())
