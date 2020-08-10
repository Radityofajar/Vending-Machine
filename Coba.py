from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import serial
import time

ser = serial.Serial('COM8', 9600)
time.sleep(2)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.CocaCola = QtWidgets.QPushButton(self.centralwidget)
        self.CocaCola.setGeometry(QtCore.QRect(0, 280, 93, 28))
        self.CocaCola.setObjectName("CocaCola")

        self.Fanta = QtWidgets.QPushButton(self.centralwidget)
        self.Fanta.setGeometry(QtCore.QRect(210, 280, 93, 28))
        self.Fanta.setObjectName("Fanta")

        self.Pepsi = QtWidgets.QPushButton(self.centralwidget)
        self.Pepsi.setGeometry(QtCore.QRect(420, 280, 93, 28))
        self.Pepsi.setObjectName("Pepsi")

        self.Sprite = QtWidgets.QPushButton(self.centralwidget)
        self.Sprite.setGeometry(QtCore.QRect(630, 280, 93, 28))
        self.Sprite.setObjectName("Sprite")

        self.Fanta_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Fanta_2.setGeometry(QtCore.QRect(0, 490, 200, 200))
        self.Fanta_2.setObjectName("Fanta_2")

        self.Sprite_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Sprite_2.setGeometry(QtCore.QRect(210, 490, 200, 200))
        self.Sprite_2.setObjectName("Sprite_2")

        self.Pepsi_2 = QtWidgets.QPushButton(self.centralwidget)
        self.Pepsi_2.setGeometry(QtCore.QRect(420, 490, 200, 200))
        self.Pepsi_2.setObjectName("Pepsi_2")

        self.CocaCola_2 = QtWidgets.QPushButton(self.centralwidget)
        self.CocaCola_2.setGeometry(QtCore.QRect(630, 490, 200, 200))
        self.CocaCola_2.setObjectName("CocaCola_2")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(290, 70, 481, 81))
        font = QtGui.QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1118, 26))

        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_5.setText(
            _translate("MainWindow", "<html><head/><body><p align=\"center\">Vending Machine</p></body></html>"))

        self.CocaCola.setStyleSheet("background-image : url(coca cola.jpg);")
        self.CocaCola.resize(200,200)
        self.CocaCola.clicked.connect(self.clickme)

        self.Sprite.setStyleSheet("background-image : url(sprite.jpg);")
        self.Sprite.resize(200, 200)
        self.Sprite.clicked.connect(self.clickme)

        self.Fanta.setStyleSheet("background-image : url(fanta.jpg);")
        self.Fanta.resize(200, 200)
        self.Fanta.clicked.connect(self.clickme2)

        self.Pepsi.setStyleSheet("background-image : url(pepsi.jpg);")
        self.Pepsi.resize(200, 200)
        self.Pepsi.clicked.connect(self.clickme2)

        self.CocaCola_2.setStyleSheet("background-image : url(coca cola.jpg);")
        self.CocaCola_2.resize(200, 200)
        self.CocaCola_2.clicked.connect(self.clickme)

        self.Sprite_2.setStyleSheet("background-image : url(sprite.jpg);")
        self.Sprite_2.resize(200, 200)
        self.Sprite_2.clicked.connect(self.clickme)

        self.Fanta_2.setStyleSheet("background-image : url(fanta.jpg);")
        self.Fanta_2.resize(200, 200)
        self.Fanta_2.clicked.connect(self.clickme2)

        self.Pepsi_2.setStyleSheet("background-image : url(pepsi.jpg);")
        self.Pepsi_2.resize(200, 200)
        self.Pepsi_2.clicked.connect(self.clickme2)

    def clickme(self):
        print("1")
        user_input = '1'
        QMessageBox.about(self, "Transaksi", "Terbeli")
        if user_input == '1':
            ser.write(b'1')
            print("LED Nyala")

    def clickme2(self):
        print("0")
        user_input = '0'
        QMessageBox.about(self, "Transaksi", "Terbeli")
        if user_input == '0':
            ser.write(b'0')
            print("LED Mati")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
