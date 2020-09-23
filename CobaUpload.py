from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import *
import sys, os
import sqlite3
from PIL import Image



con = sqlite3.connect('database.db')
cur = con.cursor()
defaultImg = "shop.png"


class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Data")
        self.setGeometry(0,0,1080,1920)
        self.UI()
        self.showFullScreen()

    def UI(self):
        self.mainDesign()
        self.layouts()
    
    # def closeEvent(self, event):
        # self.main = Main()
        
    def mainDesign(self):
        self.setStyleSheet("background-color: white")

        cur.execute("SELECT harga FROM database")
        stok = cur.fetchall()
        
        #for stok in stok:
         #   self.stok(str(database[0]) + "-" + database[2] + " " + database[1] + " " + database[3])
        
        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")


        # self.label_5 = QLabel(self.centralwidget)
        # self.label_5.setGeometry(QRect(320, 20, 481, 81))
        # font = QFont()
        # font.setFamily("Myriad Pro Light")
        # font.setPointSize(36)
        # font.setBold(True)
        # font.setWeight(75)
        # self.label_5.setFont(font)
        # self.label_5.setObjectName("label_5")
        # self.label_5.setText("<html><head/><body><p align=\"center\">Vending Machine</p></body></html>")

        self.label1 = QLabel(self.centralwidget)
        self.label1.setGeometry(QRect(20, 20, 200, 200))
        self.label1.setStyleSheet('font-size: 20pt; font-family: Arial Bold;')
        self.label1.setText ("Rp" + str(stok[0][0]))

        global dataList
        for i in range(0, 28):
            data = (ser.readline().split()[0].decode("ascii"))
            dataList[i] = data        
        
        self.stok1 = QPushButton(self.centralwidget)
        self.stok1.setGeometry(QRect(20, 200, 200, 200))
        self.stok1.setObjectName("stok1")
        if (dataList[0] == '0'):
            self.stok1.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/stok1.jpg);")
            self.stok1.resize(200, 200)
            stok_1 = 'a'
            self.stok1.clicked.connect(lambda: self.clickme(stok_1))
            self.stok1.clicked.connect(self.funcPaymentSys)
        else:
            self.stok1.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/no.jpg);")
            self.stok1.resize(200, 200)

        self.stok2 = QPushButton(self.centralwidget)
        self.stok2.setGeometry(QRect(300, 200, 200, 200))
        self.stok2.setObjectName("stok2")
        if (dataList[1] == '0'):
            self.stok2.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok2.jpg);")
            self.stok2.resize(200, 200)
            stok_2 = 'b'
            self.stok2.clicked.connect(lambda: self.clickme(stok_2))
            self.stok2.clicked.connect(self.funcPaymentSys)
        else:
            self.stok2.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok2.resize(200, 200)

        self.stok3 = QPushButton(self.centralwidget)
        self.stok3.setGeometry(QRect(580, 200, 200, 200))
        self.stok3.setObjectName("stok3")
        if (dataList[2] == '0'):
            self.stok3.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok3.jpg);")
            self.stok3.resize(200, 200)
            stok_3 = 'c'
            self.stok3.clicked.connect(lambda: self.clickme(stok_3))
            self.stok3.clicked.connect(self.funcPaymentSys)
        else:
            self.stok3.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok3.resize(200, 200)

        self.stok4 = QPushButton(self.centralwidget)
        self.stok4.setGeometry(QRect(860, 200, 200, 200))
        self.stok4.setObjectName("stok4")
        if (dataList[3] == '0'):
            self.stok4.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/stok4.jpg);")
            self.stok4.resize(200, 200)
            stok_4 = 'd'
            self.stok4.clicked.connect(lambda: self.clickme(stok_4))
            self.stok4.clicked.connect(self.funcPaymentSys)
        else:
            self.stok4.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/no.jpg);")
            self.stok4.resize(200, 200)

        self.stok5 = QPushButton(self.centralwidget)
        self.stok5.setGeometry(QRect(20, 445, 200, 200))
        self.stok5.setObjectName("stok5")
        if (dataList[4] == '0'):
            self.stok5.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok5.jpg);")
            self.stok5.resize(200, 200)
            stok_5 = 'e'
            self.stok5.clicked.connect(lambda: self.clickme(stok_5))
            self.stok5.clicked.connect(self.funcPaymentSys)
        else:
            self.stok5.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok5.jpg);")
            self.stok5.resize(200, 200)

        self.stok6 = QPushButton(self.centralwidget)
        self.stok6.setGeometry(QRect(300, 445, 200, 200))
        self.stok6.setObjectName("stok6")
        if (dataList[5] == '0'):
            self.stok6.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok6.jpg);")
            self.stok6.resize(200, 200)
            stok_6 = 'f'
            self.stok6.clicked.connect(lambda: self.clickme(stok_6))
            self.stok6.clicked.connect(self.funcPaymentSys)
        else:
            self.stok6.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok6.resize(200, 200)

        self.stok7 = QPushButton(self.centralwidget)
        self.stok7.setGeometry(QRect(580, 445, 200, 200))
        self.stok7.setObjectName("stok7")
        if (dataList[6] == '0'):
            self.stok7.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok7.jpg);")
            self.stok7.resize(200, 200)
            stok_7 = 'g'
            self.stok7.clicked.connect(lambda: self.clickme(stok_7))
            self.stok7.clicked.connect(self.funcPaymentSys)
        else:
            self.stok7.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok7.resize(200, 200)

        self.stok8 = QPushButton(self.centralwidget)
        self.stok8.setGeometry(QRect(860, 445, 200, 200))
        self.stok8.setObjectName("stok8")
        if (dataList[7] == '0'):
            self.stok8.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok8.jpg);")
            self.stok8.resize(200, 200)
            stok_8 = 'h'
            self.stok8.clicked.connect(lambda: self.clickme(stok_8))
            self.stok8.clicked.connect(self.funcPaymentSys)
        else:
            self.stok8.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok8.resize(200, 200)

        self.stok9 = QPushButton(self.centralwidget)
        self.stok9.setGeometry(QRect(20, 690, 200, 200))
        self.stok9.setObjectName("stok9")
        if (dataList[8] == '0'):
            self.stok9.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok9.jpg);")
            self.stok9.resize(200, 200)
            stok_9 = 'i'
            self.stok9.clicked.connect(lambda: self.clickme(stok_9))
            self.stok9.clicked.connect(self.funcPaymentSys)
        else:
            self.stok9.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok9.resize(200, 200)

        self.stok10 = QPushButton(self.centralwidget)
        self.stok10.setGeometry(QRect(300, 690, 200, 200))
        self.stok10.setObjectName("stok10")
        if (dataList[9] == '0'):
            self.stok10.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok10.jpg);")
            self.stok10.resize(200, 200)
            stok_10 = 'j'
            self.stok10.clicked.connect(lambda: self.clickme(stok_10))
            self.stok10.clicked.connect(self.funcPaymentSys)
        else:
            self.stok10.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok10.resize(200, 200)

        self.stok11 = QPushButton(self.centralwidget)
        self.stok11.setGeometry(QRect(580, 690, 200, 200))
        self.stok11.setObjectName("stok11")
        if (dataList[10] == '0'):
            self.stok11.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok11.jpg);")
            self.stok11.resize(200, 200)
            stok_11 = 'k'
            self.stok11.clicked.connect(lambda: self.clickme(stok_11))
            self.stok11.clicked.connect(self.funcPaymentSys)
        else:
            self.stok11.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok11.resize(200, 200)

        self.stok12 = QPushButton(self.centralwidget)
        self.stok12.setGeometry(QRect(860, 690, 200, 200))
        self.stok12.setObjectName("stok12")
        if (dataList[11] == '0'):
            self.stok12.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok12.jpg);")
            self.stok12.resize(200, 200)
            stok_12 = 'l'
            self.stok12.clicked.connect(lambda: self.clickme(stok_12))
            self.stok12.clicked.connect(self.funcPaymentSys)
        else:
            self.stok12.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok12.resize(200, 200)

        self.stok13 = QPushButton(self.centralwidget)
        self.stok13.setGeometry(QRect(20, 935, 200, 200))
        self.stok13.setObjectName("stok13")
        if (dataList[12] == '0'):
            self.stok13.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok13.jpg);")
            self.stok13.resize(200, 200)
            stok_13 = 'm'
            self.stok13.clicked.connect(lambda: self.clickme(stok_13))
            self.stok13.clicked.connect(self.funcPaymentSys)
        else:
            self.stok13.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok13.resize(200, 200)

        self.stok14 = QPushButton(self.centralwidget)
        self.stok14.setGeometry(QRect(300, 935, 200, 200))
        self.stok14.setObjectName("stok14")
        if (dataList[13] == '0'):
            self.stok14.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok14.jpg);")
            self.stok14.resize(200, 200)
            stok_14 = 'n'
            self.stok14.clicked.connect(lambda: self.clickme(stok_14))
            self.stok14.clicked.connect(self.funcPaymentSys)
        else:
            self.stok14.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok14.resize(200, 200)

        self.stok15 = QPushButton(self.centralwidget)
        self.stok15.setGeometry(QRect(580, 935, 200, 200))
        self.stok15.setObjectName("stok15")
        if (dataList[14] == '0'):
            self.stok15.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok15.jpg);")
            self.stok15.resize(200, 200)
            stok_15 = 'o'
            self.stok15.clicked.connect(lambda: self.clickme(stok_15))
            self.stok15.clicked.connect(self.funcPaymentSys)
        else:
            self.stok15.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok15.resize(200, 200)

        self.stok16 = QPushButton(self.centralwidget)
        self.stok16.setGeometry(QRect(860, 935, 200, 200))
        self.stok16.setObjectName("stok16")
        if (dataList[15] == '0'):
            self.stok16.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok16.jpg);")
            self.stok16.resize(200, 200)
            stok_16 = 'p'
            self.stok16.clicked.connect(lambda: self.clickme(stok_16))
            self.stok16.clicked.connect(self.funcPaymentSys)
        else:
            self.stok16.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok16.resize(200, 200)

        self.stok17 = QPushButton(self.centralwidget)
        self.stok17.setGeometry(QRect(20, 1180, 200, 200))
        self.stok17.setObjectName("stok17")
        if (dataList[16] == '0'):
            self.stok17.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok17.jpg);")
            self.stok17.resize(200, 200)
            stok_17 = 'q'
            self.stok17.clicked.connect(lambda: self.clickme(stok_17))
            self.stok17.clicked.connect(self.funcPaymentSys)
        else:
            self.stok17.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok17.resize(200, 200)

        self.stok18 = QPushButton(self.centralwidget)
        self.stok18.setGeometry(QRect(300, 1180, 200, 200))
        self.stok18.setObjectName("stok18")
        if (dataList[17] == '0'):
            self.stok18.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok18.jpg);")
            self.stok18.resize(200, 200)
            stok_18 = 'r'
            self.stok18.clicked.connect(lambda: self.clickme(stok_18))
            self.stok18.clicked.connect(self.funcPaymentSys)
        else:
            self.stok18.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok18.resize(200, 200)

        self.stok19 = QPushButton(self.centralwidget)
        self.stok19.setGeometry(QRect(580, 1180, 200, 200))
        self.stok19.setObjectName("stok19")
        if (dataList[18] == '0'):
            self.stok19.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok19.jpg);")
            self.stok19.resize(200, 200)
            stok_19 = 's'
            self.stok19.clicked.connect(lambda: self.clickme(stok_19))
            self.stok19.clicked.connect(self.funcPaymentSys)
        else:
            self.stok19.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok19.resize(200, 200)

        self.stok20 = QPushButton(self.centralwidget)
        self.stok20.setGeometry(QRect(860, 1180, 200, 200))
        self.stok20.setObjectName("stok20")
        if (dataList[19] == '0'):
            self.stok20.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok20.jpg);")
            self.stok20.resize(200, 200)
            stok_20 = 't'
            self.stok20.clicked.connect(lambda: self.clickme(stok_20))
            self.stok20.clicked.connect(self.funcPaymentSys)
        else:
            self.stok20.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok20.resize(200, 200)

        self.stok21 = QPushButton(self.centralwidget)
        self.stok21.setGeometry(QRect(20, 1425, 200, 200))
        self.stok21.setObjectName("stok21")
        if (dataList[20] == '0'):
            self.stok21.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok21.jpg);")
            self.stok21.resize(200, 200)
            stok_21 = 'u'
            self.stok21.clicked.connect(lambda: self.clickme(stok_21))
            self.stok21.clicked.connect(self.funcPaymentSys)
        else:
            self.stok21.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok21.resize(200, 200)

        self.stok22 = QPushButton(self.centralwidget)
        self.stok22.setGeometry(QRect(300, 1425, 200, 200))
        self.stok22.setObjectName("stok22")
        if (dataList[21] == '0'):
            self.stok22.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok22.jpg);")
            self.stok22.resize(200, 200)
            stok_22 = 'v'
            self.stok22.clicked.connect(lambda: self.clickme(stok_22))
            self.stok22.clicked.connect(self.funcPaymentSys)
        else:
            self.stok22.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok22.resize(200, 200)

        self.stok23 = QPushButton(self.centralwidget)
        self.stok23.setGeometry(QRect(580, 1425, 200, 200))
        self.stok23.setObjectName("stok23")
        if (dataList[22] == '0'):
            self.stok23.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok23.jpg);")
            self.stok23.resize(200, 200)
            stok_23 = 'w'
            self.stok23.clicked.connect(lambda: self.clickme(stok_23))
            self.stok23.clicked.connect(self.funcPaymentSys)
        else:
            self.stok23.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok23.resize(200, 200)

        self.stok24 = QPushButton(self.centralwidget)
        self.stok24.setGeometry(QRect(860, 1425, 200, 200))
        self.stok24.setObjectName("stok24")
        if (dataList[23] == '0'):
            self.stok24.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok24.jpg);")
            self.stok24.resize(200, 200)
            stok_24 = 'x'
            self.stok24.clicked.connect(lambda: self.clickme(stok_24))
            self.stok24.clicked.connect(self.funcPaymentSys)
        else:
            self.stok24.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok24.resize(200, 200)

        self.stok25 = QPushButton(self.centralwidget)
        self.stok25.setGeometry(QRect(20, 1670, 200, 200))
        self.stok25.setObjectName("stok25")
        if (dataList[24] == '0'):
            self.stok25.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok25.jpg);")
            self.stok25.resize(200, 200)
            stok_25 = 'y'
            self.stok25.clicked.connect(lambda: self.clickme(stok_25))
            self.stok25.clicked.connect(self.funcPaymentSys)
        else:
            self.stok25.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok25.resize(200, 200)

        self.stok26 = QPushButton(self.centralwidget)
        self.stok26.setGeometry(QRect(300, 1670, 200, 200))
        self.stok26.setObjectName("stok26")
        if (dataList[25] == '0'):
            self.stok26.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok26.jpg);")
            self.stok26.resize(200, 200)
            stok_26 = 'z'
            self.stok26.clicked.connect(lambda: self.clickme(stok_26))
            self.stok26.clicked.connect(self.funcPaymentSys)
        else:
            self.stok26.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok26.resize(200, 200)

        self.stok27 = QPushButton(self.centralwidget)
        self.stok27.setGeometry(QRect(580, 1670, 200, 200))
        self.stok27.setObjectName("stok27")
        if (dataList[26] == '0'):
            self.stok27.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok27.jpg);")
            self.stok27.resize(200, 200)
            stok_27 = 'A'
            self.stok27.clicked.connect(lambda: self.clickme(stok_27))
            self.stok27.clicked.connect(self.funcPaymentSys)
        else:
            self.stok27.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok27.resize(200, 200)

        self.stok28 = QPushButton(self.centralwidget)
        self.stok28.setGeometry(QRect(860, 1670, 200, 200))
        self.stok28.setObjectName("stok28")
        if (dataList[27] == '0'):
            self.stok28.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok28.jpg);")
            self.stok28.resize(200, 200)
            stok_28 = 'B'
            self.stok28.clicked.connect(lambda: self.clickme(stok_28))
            self.stok28.clicked.connect(self.funcPaymentSys)
        else:
            self.stok28.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            self.stok28.resize(200, 200)
        
        self.setup = QPushButton(self.centralwidget)
        self.setup.setGeometry(QtCore.QRect(950, 10, 100, 100))
        self.setup.setObjectName("setup")
        self.setup.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(setup.jpg);")
        self.setup.resize(100, 100)
        self.setup.clicked.connect(self.funcLogIn)

    def layouts(self):
        # layouts
        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.centralwidget)
        #self.mainLayout.addLayout(self.mainLayout)

        # set main window layout
        self.setLayout(self.mainLayout)

    def funcPaymentSys(self):
        self.newSys = PaymentSys()
        self.close()

    def funcLogIn(self):
        self.newSys = LogIn()
        self.close()

    # def funcRefresh(self):
        # pass

    def clickme(self, arg):
        print(arg)
        i = arg
        # ser.write(i.encode())


class PaymentSys(QWidget):
    def __init__(self):
        super().__init__()
        # self.serial = serial
        self.setWindowTitle("Payment System")
        self.setGeometry(375, 750, 350, 350)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()
        
    #def closeEvent(self, event):
     #   self.main = Main()

    def widgets(self):
        self.setStyleSheet("background-color: white")
        # widgets of top layout
        self.paymentSysImg = QLabel()
        self.img = QPixmap('qrcode.png')
        self.paymentSysImg.setPixmap(self.img)
        self.titleText = QLabel("Scan QR Code")

        # widgets of bottom layout
        self.yesBtn = QPushButton("Transaksi Berhasil")
        self.yesBtn.setStyleSheet("background-color: blue")
        yes_btn = 'Y'
        self.yesBtn.clicked.connect(lambda: self.clickme2(yes_btn))

        self.noBtn = QPushButton("Transaksi Gagal")
        self.noBtn.setStyleSheet("background-color: blue")
        no_btn = 'N'
        self.noBtn.clicked.connect(lambda: self.clickme2(no_btn))

    def layouts(self):
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QHBoxLayout()
        self.topFrame = QFrame()
        self.bottomFrame = QFrame()

        # add widgets #
        # widget of toplayout #
        self.topLayout.addWidget(self.paymentSysImg)
        self.topLayout.addWidget(self.titleText)
        self.topFrame.setLayout(self.topLayout)

        # widget of form layout #
        self.bottomLayout.addWidget(self.yesBtn)
        self.bottomLayout.addWidget(self.noBtn)
        self.bottomFrame.setLayout(self.bottomLayout)

        #
        self.mainLayout.addWidget(self.topFrame)
        self.mainLayout.addWidget(self.bottomFrame)
        self.setLayout(self.mainLayout)

    def clickme2(self, arg):
        print(arg)
        y = arg
        # ser.write(y.encode())
        self.close()


class LogIn(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon('icons/members.png'))
        self.setGeometry(0,0,1200,1890)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        self.widgets()
        self.layouts()


    def widgets(self):
        self.setStyleSheet("background-color: white")
        
        self.masuk = QWidget()
        
        # widget of top layout
        self.username = QLabel(self.masuk)
        self.username.setText("Username: ")
        self.username.setGeometry(QtCore.QRect(400, 650, 100, 30))
                                  
        self.usernameEntry = QLineEdit(self.masuk)
        self.usernameEntry.setPlaceholderText("Enter Username")
        self.usernameEntry.setGeometry(QtCore.QRect(500, 650, 250, 30))
        
        self.password = QLabel(self.masuk)
        self.password.setText("Password: ")
        self.password.setGeometry(QtCore.QRect(400, 700, 100, 30))

        self.passwordEntry = QLineEdit(self.masuk)
        self.passwordEntry.setPlaceholderText("Enter Password")
        self.passwordEntry.setGeometry(QtCore.QRect(500, 700, 250, 30))
        self.passwordEntry.setEchoMode(1)

        self.enterBtn = QPushButton(self.masuk)
        self.enterBtn.setText("Enter")
        self.enterBtn.setStyleSheet("background-color: orange")
        self.enterBtn.setGeometry(QtCore.QRect(530, 750, 100, 30))
        self.enterBtn.clicked.connect(self.funcSetup)

        self.cancelBtn = QPushButton(self.masuk)
        self.cancelBtn.setText("Cancel")
        self.cancelBtn.setStyleSheet("background-color: orange")
        self.cancelBtn.setGeometry(QtCore.QRect(650, 750, 100, 30))
        self.cancelBtn.clicked.connect(self.funcCancel)

    def layouts(self):
        self.topLayout = QHBoxLayout()

        # add widget
        self.topLayout.addWidget(self.masuk)
        self.setLayout(self.topLayout)

    def funcSetup(self):
        if self.usernameEntry.text() == 'vendingmachine' and self.passwordEntry.text() == 'kei':
            self.addSys = AddSetup()
            self.close()
        else:
            pass

    def funcCancel(self):
        self.close()


class AddSetup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Setup")
        self.setWindowIcon(QIcon('icons/setup.png'))
        self.setGeometry(505, 250, 1080, 1920)
        self.setFixedSize(self.size())
        self.UI()
        self.showFullScreen()

    def UI(self):
        self.tabWidget()
        self.widgets()
        self.layouts()
        self.getProduct()
        self.displayFirstRecord()
        

    # def closeEvent(self, event):
        # self.main = Main()
        
    def tabWidget(self):
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.addTab(self.tab1, "Upload")
        self.tabs.addTab(self.tab2, "Details")

    def widgets(self):
        self.setStyleSheet("background-color: white")
        
        self.upload = QWidget()
        
        # widget of bottom layout
        self.photoBtn = QPushButton(self.upload)
        self.photoBtn.setText("Upload Image")
        self.photoBtn.setStyleSheet("background-color: orange")
        self.photoBtn.setGeometry(QtCore.QRect(200, 775, 300, 300))
        self.photoBtn.clicked.connect(self.uploadImg)

        self.videoBtn = QPushButton(self.upload)
        self.videoBtn.setText("Upload Video")
        self.videoBtn.setStyleSheet("background-color: orange")
        self.videoBtn.setGeometry(QtCore.QRect(600, 775, 300, 300))
        # self.videoBtn.clicked.connect(self.uploadVideo)

        self.submitBtn = QPushButton(self.upload)
        self.submitBtn.setText("Submit")
        self.submitBtn.setStyleSheet("background-color: orange")
        self.submitBtn.setGeometry(QtCore.QRect(750, 1100, 150, 80))
        self.submitBtn.clicked.connect(self.submit)
        
        # self.details = QWidget()
        self.productList = QListWidget()
        self.productList.itemClicked.connect(self.singleClick)
        self.addBtn = QPushButton("Add")
        self.addBtn.setStyleSheet("background-color: orange; font-size: 10pt")
        self.addBtn.clicked.connect(self.addProduct)
        
        self.deleteBtn = QPushButton("Delete")
        self.deleteBtn.setStyleSheet("Background-color: orange; font-size: 10pt")
        self.deleteBtn.clicked.connect(self.deleteProduct)
        
        self.updateBtn = QPushButton("Update")
        self.updateBtn.setStyleSheet("background-color: orange; font-size: 10pt")
        self.updateBtn.clicked.connect(self.updateProduct)

    def layouts(self):
        self.uploadLayout = QHBoxLayout()
        # self.topLayout = QHBoxLayout()

        # add widget
        self.uploadLayout.addWidget(self.upload)
        
        self.tab1.setLayout(self.uploadLayout)
        
        self.mainLayout = QHBoxLayout()
        self.leftLayout = QFormLayout()
        self.rightMainLayout = QVBoxLayout()
        self.rightTopLayout = QHBoxLayout()
        self.rightBottomLayout = QHBoxLayout()
        
        # child layout
        self.rightMainLayout.addLayout(self.rightTopLayout)
        self.rightMainLayout.addLayout(self.rightBottomLayout)
        
        self.mainLayout.addLayout(self.leftLayout, 60)
        self.mainLayout.addLayout(self.rightMainLayout, 40)
        
        # add widget to layout
        self.rightTopLayout.addWidget(self.productList)
        self.rightBottomLayout.addWidget(self.addBtn)
        self.rightBottomLayout.addWidget(self.deleteBtn)
        self.rightBottomLayout.addWidget(self.updateBtn)
        
        #setting main window layout
        self.tab2.setLayout(self.mainLayout)

    def uploadImg(self):
        global defaultImg
        size = (200, 200)
        self.filename, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")
        if ok:
            # print(self.filename)
            defaultImg = os.path.basename(self.filename)
            # print(defaultImg)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("img/{0}".format(defaultImg))
            
    # def uploadVideo
        # pass

    def submit(self):
        self.close()
        self.main = Main()
        
    def addProduct(self):
        self.newProduct = AddProduct()
        self.close()
        
    def getProduct(self):
        query = "SELECT id, name, kuantitas, harga FROM database"
        database = cur.execute(query).fetchall()
        for database in database:
            self.productList.addItem(str(database[0]) + "-" + database[2] + " " + database[1] + " " + database[3])
            
    def displayFirstRecord(self):
        query = "SELECT * FROM database ORDER BY ROWID ASC LIMIT 1"
        database = cur.execute(query).fetchone()
        img = QLabel()
        img.setPixmap(QPixmap("img/" + database[4]))
        name = QLabel(database[2])
        kuantitas = QLabel(database[1])
        harga = QLabel(database[3])
        
        self.leftLayout.setVerticalSpacing(20)
        
        self.leftLayout.addRow("", img)
        self.leftLayout.addRow("Name: ", name)
        self.leftLayout.addRow("Kuantitas: ", kuantitas)
        self.leftLayout.addRow("Harga: ", harga)
        
    def singleClick(self):
        for i in reversed(range(self.leftLayout.count())):
            widget = self.leftLayout.takeAt(i).widget()
            
            if widget is not None:
                widget.deleteLater()
                
        database = self.productList.currentItem().text()
        id = database.split("-")[0]
        query = ("SELECT * FROM database WHERE id =?")
        product = cur.execute(query, (id,)).fetchone()  # single item tuple = (1,)
        
        img = QLabel()
        img.setPixmap(QPixmap("img/" + product[4]))
        name = QLabel(product[2])
        kuantitas = QLabel(product[1])
        harga = QLabel(product[3])
        
        self.leftLayout.setVerticalSpacing(20)
        
        self.leftLayout.addRow("", img)
        self.leftLayout.addRow("Name: ", name)
        self.leftLayout.addRow("Kuantitas: ", kuantitas)
        self.leftLayout.addRow("Harga: ", harga)
        
    def deleteProduct(self):
        if self.productList.selectedItems():
            product = self.productList.currentItem().text()
            id = product.split("-")[0]
            mbox = QMessageBox.question(self, "Warning", "Are you sure to delete this product?", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if mbox == QMessageBox.Yes:
                try:
                    query = "DELETE FROM database WHERE id =?"
                    cur.execute(query, (id,))
                    con.commit()
                    QMessageBox.information(self, "Information", "Product has been deleted")
                    self.close()
                    self.main = Main()
                    
                except:
                    QMessageBox.information(self, "Warning!", "Product has not been deleted")
                    
        else:
            QMessageBox.information(self, "Warning!", "Please select a product to delete")
            
    def updateProduct(self):
        global product_id
        if self.productList.selectedItems():
            product = self.productList.currentItem().text()
            product_id = product.split("-")[0]
            self.updateWindow = UpdateProduct()
            self.close()
            
        else:
            QMessageBox.information(self, "Warning!", "Please select a product to update")
        
class UpdateProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Product")
        self.setGeometry(500, 70, 350, 550)
        self.UI()
        self.showFullscreen()
        
    def UI(self):
        self.getProduct()
        self.mainDesign()
        self.layouts()
        
    def closeEvent(self, event):
        self.main = Main()
        
    def getProduct(self):
        global product_id
        query = "SELECT * FROM database WHERE id =?"
        database = cur.execute(query, (product_id,)).fetchone()
        self.name = database[2]
        self.kuantitas = database[1]
        self.harga = database[3]
        self.img = database[4]
        
    def mainDesign(self):
        self.setStyleSheet("background-color: white; font-size: 12pt; font-family: Times")
        
        # top layout
        self.title = QLabel("Update Product")
        self.title.setStyleSheet('font-size: 20pt; font-family: Arial Bold;')
        self.addImg = QLabel()
        self.addImg.setPixmap(QPixmap("img/{}".format(self.img)))
        
        #bottom layout
        self.nameLbl = QLabel("Name: ")
        self.nameEntry = QLineEdit()
        self.nameEntry.setText(self.name)
        
        self.kuantitasLbl = QLabel("Kuantitas: ")
        self.kuantitasEntry = QLineEdit()
        self.kuantitasEntry.setText(self.kuantitas)
        
        self.hargaLbl = QLabel("Harga: ")
        self.hargaEntry = QLineEdit()
        self.hargaEntry.setText(self.harga)
        
        self.imgLbl = QLabel("Picture: ")
        self.imgBtn = QPushButton("Browse")
        self.imgBtn.setStyleSheet("backgorund-color: orange; font-size: 10pt")
        self.imgBtn.clicked.connect(self.uploadImg)
        
        self.upBtn = QPushButton("Update")
        self.upBtn.setStyleSheet("backgorund-color: orange; font-size: 10pt")
        self.upBtn.clicked.connect(self.updateProduct)
        
    def layouts(self):
        # main layout
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()
        
        # child layout
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)
        
        # add widget
        # top layout
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.addImg)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(100, 10, 10, 30)
        
        # bottom layout
        self.bottomLayout.addRow(self.nameLbl, self, nameEntry)
        self.bottomLayout.addRow(self.kuantitasLbl, self.kuantitasEntry)
        self.bottomLayout.addRow(self.hargaLbl, self.hargaEntry)
        self.bottomLayout.addRow(self.imgLbl, self.imgBtn)
        self.bottomLayour.addRow("", self.upBtn)
        
        # setting layout
        self.setLayout(self.mainLayout)
        
    def uploadImg(self):
        global defaultImg
        size = (200, 200)
        self.filename, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")
        if ok:
            defaultImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("img/{0}".format(defaultImg))
            
    def updateProduct(self):
        global defaultImg
        global product_id
        name = self.nameEntry.text()
        kuantitas = self.kuantitasEntry.text()
        harga = self.hargaEntry.text()
        img = defaultImg
        
        if (name and kuantitas and harga and img != ""):
            try:
                query = "UPDATE database set name =?, kuantitas =?, harga =?, img =? WHERE id =?"
                cur.execute(query, (name, kuantitas, harga, img, product_id))
                con.commit()
                QMessageBox.information(self, "Success", "Product has been updated")
                self.close()
                self.main = Main()
                
            except:
                QMessageBox.information(self, "Warning!", "Product has not been updated")
                
        else:
            QMessageBox.information(self, "Warning!", "Fields can not be empty")
            
class AddProduct(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Product")
        self.setGeometry(500, 70, 350, 550)
        self.UI()
        self.showFullScreen()

    def UI(self):
        self.mainDesign()
        self.layouts()

    #def closeEvent(self, event):
     #   self.main = Main()

    def mainDesign(self):
        self.setStyleSheet("background-color: white; font-size: 12pt; font-family: Times")
        # top layout
        self.title = QLabel("Add Product")
        self.title.setStyleSheet('font-size: 20pt; font-family: Arial Bold;')
        self.addImg = QLabel()
        self.addImg.setPixmap(QPixmap("icons/shop.png"))

        # bottom layout
        self.nameLbl = QLabel("Name: ")
        self.nameEntry = QLineEdit()
        self.nameEntry.setPlaceholderText("Enter Product Name")

        self.kuantitasLbl = QLabel("Kuantitas: ")
        self.kuantitasEntry = QLineEdit()
        self.kuantitasEntry.setPlaceholderText("Enter Product Quantity")

        self.hargaLbl = QLabel("Harga: ")
        self.hargaEntry = QLineEdit()
        self.hargaEntry.setPlaceholderText("Enter Harga")

        self.imgLbl = QLabel("Picture: ")
        self.imgBtn = QPushButton("Browse")
        self.imgBtn.setStyleSheet("background-color: orange; font-size: 10pt")
        self.imgBtn.clicked.connect(self.uploadImg)

        self.doneBtn = QPushButton("Done")
        self.doneBtn.setStyleSheet("background-color: orange; font-size: 10pt")
        self.doneBtn.clicked.connect(self.addProduct)

    def layouts(self):
        # main layout
        self.mainLayout = QVBoxLayout()
        self.topLayout = QVBoxLayout()
        self.bottomLayout = QFormLayout()

        # add child layout
        self.mainLayout.addLayout(self.topLayout)
        self.mainLayout.addLayout(self.bottomLayout)

        # add widget
        # top layout
        self.topLayout.addStretch()
        self.topLayout.addWidget(self.title)
        self.topLayout.addWidget(self.addImg)
        self.topLayout.addStretch()
        self.topLayout.setContentsMargins(110, 10, 10, 30)

        # bottom layout
        self.bottomLayout.addRow(self.nameLbl, self.nameEntry)
        self.bottomLayout.addRow(self.kuantitasLbl, self.kuantitasEntry)
        self.bottomLayout.addRow(self.hargaLbl, self.hargaEntry)
        self.bottomLayout.addRow(self.imgLbl, self.imgBtn)
        self.bottomLayout.addRow("", self.doneBtn)

        # setting layout
        self.setLayout(self.mainLayout)

    def uploadImg(self):
        global defaultImg
        size = (200, 200)
        self.filename, ok = QFileDialog.getOpenFileName(self, "Upload Image", "", "Image Files (*.jpg *.png)")
        if ok:

            defaultImg = os.path.basename(self.filename)
            img = Image.open(self.filename)
            img = img.resize(size)
            img.save("img/{0}".format(defaultImg))

    def addProduct(self):
        global dafaultImg
        name = self.nameEntry.text()
        kuantitas = self.kuantitasEntry.text()
        harga = self.hargaEntry.text()
        img = defaultImg

        if (name and kuantitas and harga != ""):
            try:
                query = "INSERT INTO database (name, kuantitas, harga, img) VALUES(?,?,?,?)"
                cur.execute(query, (name, kuantitas, harga, img))
                con.commit()
                QMessageBox.information(self, "Success", "Product has been added")
                self.close()
                self.main = Main()

            except:
                QMessageBox.information(self, "Warning", "Product has not been added")

        else:
            QMessageBox.information(self, "Warning", "Fields can not be empty")

def main():
    App = QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
