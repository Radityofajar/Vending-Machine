from PyQt5 import QtCore, QtGui, QtWidgets
import serial
import time

ser = serial.Serial('COM7', 9600)
time.sleep(2)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1210, 880)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.stok1 = QtWidgets.QPushButton(self.centralwidget)
        self.stok1.setGeometry(QtCore.QRect(20, 200, 200, 200))
        self.stok1.setObjectName("stok1")

        self.stok2 = QtWidgets.QPushButton(self.centralwidget)
        self.stok2.setGeometry(QtCore.QRect(190, 200, 200, 200))
        self.stok2.setObjectName("stok2")

        self.stok3 = QtWidgets.QPushButton(self.centralwidget)
        self.stok3.setGeometry(QtCore.QRect(360, 200, 200, 200))
        self.stok3.setObjectName("stok3")

        self.stok4 = QtWidgets.QPushButton(self.centralwidget)
        self.stok4.setGeometry(QtCore.QRect(530, 200, 200, 200))
        self.stok4.setObjectName("stok4")

        self.stok5 = QtWidgets.QPushButton(self.centralwidget)
        self.stok5.setGeometry(QtCore.QRect(700, 200, 200, 200))
        self.stok5.setObjectName("stok5")

        self.stok6 = QtWidgets.QPushButton(self.centralwidget)
        self.stok6.setGeometry(QtCore.QRect(870, 200, 200, 200))
        self.stok6.setObjectName("stok6")

        self.stok7 = QtWidgets.QPushButton(self.centralwidget)
        self.stok7.setGeometry(QtCore.QRect(1040, 200, 200, 200))
        self.stok7.setObjectName("stok7")

        self.stok8 = QtWidgets.QPushButton(self.centralwidget)
        self.stok8.setGeometry(QtCore.QRect(20, 370, 200, 200))
        self.stok8.setObjectName("stok8")

        self.stok9 = QtWidgets.QPushButton(self.centralwidget)
        self.stok9.setGeometry(QtCore.QRect(190, 370, 200, 200))
        self.stok9.setObjectName("stok9")

        self.stok10 = QtWidgets.QPushButton(self.centralwidget)
        self.stok10.setGeometry(QtCore.QRect(360, 370, 200, 200))
        self.stok10.setObjectName("stok10")

        self.stok11 = QtWidgets.QPushButton(self.centralwidget)
        self.stok11.setGeometry(QtCore.QRect(530, 370, 200, 200))
        self.stok11.setObjectName("stok11")

        self.stok12 = QtWidgets.QPushButton(self.centralwidget)
        self.stok12.setGeometry(QtCore.QRect(700, 370, 200, 200))
        self.stok12.setObjectName("stok12")

        self.stok13 = QtWidgets.QPushButton(self.centralwidget)
        self.stok13.setGeometry(QtCore.QRect(870, 370, 200, 200))
        self.stok13.setObjectName("stok13")

        self.stok14 = QtWidgets.QPushButton(self.centralwidget)
        self.stok14.setGeometry(QtCore.QRect(1040, 370, 200, 200))
        self.stok14.setObjectName("stok14")

        self.stok15 = QtWidgets.QPushButton(self.centralwidget)
        self.stok15.setGeometry(QtCore.QRect(20, 540, 200, 200))
        self.stok15.setObjectName("stok15")

        self.stok16 = QtWidgets.QPushButton(self.centralwidget)
        self.stok16.setGeometry(QtCore.QRect(190, 540, 200, 200))
        self.stok16.setObjectName("stok16")

        self.stok17 = QtWidgets.QPushButton(self.centralwidget)
        self.stok17.setGeometry(QtCore.QRect(360, 540, 200, 200))
        self.stok17.setObjectName("stok17")

        self.stok18 = QtWidgets.QPushButton(self.centralwidget)
        self.stok18.setGeometry(QtCore.QRect(530, 540, 200, 200))
        self.stok18.setObjectName("stok18")

        self.stok19 = QtWidgets.QPushButton(self.centralwidget)
        self.stok19.setGeometry(QtCore.QRect(700, 540, 200, 200))
        self.stok19.setObjectName("stok19")

        self.stok20 = QtWidgets.QPushButton(self.centralwidget)
        self.stok20.setGeometry(QtCore.QRect(870, 540, 200, 200))
        self.stok20.setObjectName("stok20")

        self.stok21 = QtWidgets.QPushButton(self.centralwidget)
        self.stok21.setGeometry(QtCore.QRect(1040, 540, 200, 200))
        self.stok21.setObjectName("stok21")

        self.stok22 = QtWidgets.QPushButton(self.centralwidget)
        self.stok22.setGeometry(QtCore.QRect(20, 710, 200, 200))
        self.stok22.setObjectName("stok22")

        self.stok23 = QtWidgets.QPushButton(self.centralwidget)
        self.stok23.setGeometry(QtCore.QRect(190, 710, 200, 200))
        self.stok23.setObjectName("stok23")

        self.stok24 = QtWidgets.QPushButton(self.centralwidget)
        self.stok24.setGeometry(QtCore.QRect(360, 710, 200, 200))
        self.stok24.setObjectName("stok24")

        self.stok25 = QtWidgets.QPushButton(self.centralwidget)
        self.stok25.setGeometry(QtCore.QRect(530, 710, 200, 200))
        self.stok25.setObjectName("stok25")

        self.stok26 = QtWidgets.QPushButton(self.centralwidget)
        self.stok26.setGeometry(QtCore.QRect(700, 710, 200, 200))
        self.stok26.setObjectName("stok26")

        self.stok27 = QtWidgets.QPushButton(self.centralwidget)
        self.stok27.setGeometry(QtCore.QRect(870, 710, 200, 200))
        self.stok27.setObjectName("stok27")

        self.stok28 = QtWidgets.QPushButton(self.centralwidget)
        self.stok28.setGeometry(QtCore.QRect(1040, 710, 200, 200))
        self.stok28.setObjectName("stok28")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(400, 70, 481, 81))
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

        self.stok1.setStyleSheet("background-image : url(coca cola.jpg);")
        self.stok1.resize(150, 150)
        stok_1 = 'a'
        self.stok1.clicked.connect(lambda: self.clickme(stok_1))

        self.stok2.setStyleSheet("background-image : url(sprite.jpg);")
        self.stok2.resize(150, 150)
        stok_2 = 'b'
        self.stok2.clicked.connect(lambda: self.clickme(stok_2))

        self.stok3.setStyleSheet("background-image : url(fanta.jpg);")
        self.stok3.resize(150, 150)
        stok_3 = 'c'
        self.stok3.clicked.connect(lambda: self.clickme(stok_3))

        self.stok4.setStyleSheet("background-image : url(pepsi.jpg);")
        self.stok4.resize(150, 150)
        stok_4 = 'd'
        self.stok4.clicked.connect(lambda: self.clickme(stok_4))

        self.stok5.setStyleSheet("background-image : url(coca cola.jpg);")
        self.stok5.resize(150, 150)
        stok_5 = 'e'
        self.stok5.clicked.connect(lambda: self.clickme(stok_5))

        self.stok6.setStyleSheet("background-image : url(sprite.jpg);")
        self.stok6.resize(150, 150)
        stok_6 = 'f'
        self.stok6.clicked.connect(lambda: self.clickme(stok_6))

        self.stok7.setStyleSheet("background-image : url(fanta.jpg);")
        self.stok7.resize(150, 150)
        stok_7 = 'g'
        self.stok7.clicked.connect(lambda: self.clickme(stok_7))

        self.stok8.setStyleSheet("background-image : url(pepsi.jpg);")
        self.stok8.resize(150, 150)
        stok_8 = 'h'
        self.stok8.clicked.connect(lambda: self.clickme(stok_8))

        self.stok9.setStyleSheet("background-image : url(coca cola.jpg);")
        self.stok9.resize(150, 150)
        stok_9 = 'i'
        self.stok9.clicked.connect(lambda: self.clickme(stok_9))

        self.stok10.setStyleSheet("background-image : url(sprite.jpg);")
        self.stok10.resize(150, 150)
        stok_10 = 'j'
        self.stok10.clicked.connect(lambda: self.clickme(stok_10))

        self.stok11.setStyleSheet("background-image : url(coca cola.jpg);")
        self.stok11.resize(150, 150)
        stok_11 = 'k'
        self.stok11.clicked.connect(lambda: self.clickme(stok_11))

        self.stok12.setStyleSheet("background-image : url(sprite.jpg);")
        self.stok12.resize(150, 150)
        stok_12 = 'l'
        self.stok12.clicked.connect(lambda: self.clickme(stok_12))

        self.stok13.setStyleSheet("background-image : url(fanta.jpg);")
        self.stok13.resize(150, 150)
        stok_13 = 'm'
        self.stok13.clicked.connect(lambda: self.clickme(stok_13))

        self.stok14.setStyleSheet("background-image : url(pepsi.jpg);")
        self.stok14.resize(150, 150)
        stok_14 = 'n'
        self.stok14.clicked.connect(lambda: self.clickme(stok_14))

        self.stok15.setStyleSheet("background-image : url(coca cola.jpg);")
        self.stok15.resize(150, 150)
        stok_15 = 'o'
        self.stok15.clicked.connect(lambda: self.clickme(stok_15))

        self.stok16.setStyleSheet("background-image : url(sprite.jpg);")
        self.stok16.resize(150, 150)
        stok_16 = 'p'
        self.stok16.clicked.connect(lambda: self.clickme(stok_16))

        self.stok17.setStyleSheet("background-image : url(fanta.jpg);")
        self.stok17.resize(150, 150)
        stok_17 = 'q'
        self.stok17.clicked.connect(lambda: self.clickme(stok_17))

        self.stok18.setStyleSheet("background-image : url(pepsi.jpg);")
        self.stok18.resize(150, 150)
        stok_18 = 'r'
        self.stok18.clicked.connect(lambda: self.clickme(stok_18))

        self.stok19.setStyleSheet("background-image : url(coca cola.jpg);")
        self.stok19.resize(150, 150)
        stok_19 = 's'
        self.stok19.clicked.connect(lambda: self.clickme(stok_19))

        self.stok20.setStyleSheet("background-image : url(sprite.jpg);")
        self.stok20.resize(150, 150)
        stok_20 = 't'
        self.stok20.clicked.connect(lambda: self.clickme(stok_20))

        self.stok21.setStyleSheet("background-image : url(coca cola.jpg);")
        self.stok21.resize(150, 150)
        stok_21 = 'u'
        self.stok21.clicked.connect(lambda: self.clickme(stok_21))

        self.stok22.setStyleSheet("background-image : url(sprite.jpg);")
        self.stok22.resize(150, 150)
        stok_22 = 'v'
        self.stok22.clicked.connect(lambda: self.clickme(stok_22))

        self.stok23.setStyleSheet("background-image : url(fanta.jpg);")
        self.stok23.resize(150, 150)
        stok_23 = 'w'
        self.stok23.clicked.connect(lambda: self.clickme(stok_23))

        self.stok24.setStyleSheet("background-image : url(pepsi.jpg);")
        self.stok24.resize(150, 150)
        stok_24 = 'x'
        self.stok24.clicked.connect(lambda: self.clickme(stok_24))

        self.stok25.setStyleSheet("background-image : url(coca cola.jpg);")
        self.stok25.resize(150, 150)
        stok_25 = 'y'
        self.stok25.clicked.connect(lambda: self.clickme(stok_25))

        self.stok26.setStyleSheet("background-image : url(sprite.jpg);")
        self.stok26.resize(150, 150)
        stok_26 = 'z'
        self.stok26.clicked.connect(lambda: self.clickme(stok_26))

        self.stok27.setStyleSheet("background-image : url(fanta.jpg);")
        self.stok27.resize(150, 150)
        stok_27 = 'A'
        self.stok27.clicked.connect(lambda: self.clickme(stok_27))

        self.stok28.setStyleSheet("background-image : url(pepsi.jpg);")
        self.stok28.resize(150, 150)
        stok_28 = 'B'
        self.stok28.clicked.connect(lambda: self.clickme(stok_28))

    def clickme(self, arg):
        print(arg)
        i = arg
        ser.write(i.encode())

        try:
            tersedia = ser.read(1).decode()
        except UnicodeDecodeError:
            tersedia = None
        print(tersedia)
        print(type(tersedia))
        if (tersedia == '1'):
            print('Stok barang tersedia')
            #konfirmasi
        elif(tersedia == '0'):
            print('Stok Habis')
            #back to mainWindow
        else:
            print("error")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
