import sys
import metodebayar
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
import sqlite3
import updateproduct
import updatescreen
import serial
import time

con=sqlite3.connect("products.db")
cur=con.cursor()

#ser = serial.Serial('COM9', 115200)
#time.sleep(2)


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Product Manager")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(0,0,1080,1920)
        self.setFixedSize(self.size())
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.UI)
        self.timer.start(15000)
        self.UI()
        self.showFullScreen()

    def UI(self):
        #self.toolBar()
        self.tabWidget()
        self.widgets()
        self.layouts()
        #self.displayProducts()

    def toolBar(self):
        self.tb=self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        self.addProduct=QAction(QIcon('icons/add.png'),"Add Product",self)
        self.tb.addAction(self.addProduct)
        self.tb.addSeparator()

        self.addMember=QAction(QIcon('icons/users.png'), "Add Member", self)
        self.tb.addAction(self.addMember)
        self.tb.addSeparator()

        self.sellProduct=QAction(QIcon('icons/sell.png'), "Sell Product", self)
        self.tb.addAction(self.sellProduct)
        self.tb.addSeparator()

    def tabWidget(self):
        self.tabs=QTabWidget()
        self.setCentralWidget(self.tabs)
        self.tab1=QWidget()
        self.tab2=QWidget()
        self.tab3=QWidget()
        self.tabs.addTab(self.tab1,"Products")
        self.tabs.addTab(self.tab2,"Details")
        self.tabs.addTab(self.tab3,"Setup")

    def widgets(self):
        self.productsTable = QTableWidget()
        self.productsTable.setColumnCount(6)
        self.productsTable.setHorizontalHeaderItem(0, QTableWidgetItem("Product Id"))
        self.productsTable.setHorizontalHeaderItem(1, QTableWidgetItem("Product Name"))
        self.productsTable.setHorizontalHeaderItem(2, QTableWidgetItem("Manufacturer"))
        self.productsTable.setHorizontalHeaderItem(3, QTableWidgetItem("Price"))
        self.productsTable.setHorizontalHeaderItem(4, QTableWidgetItem("Quota"))
        self.productsTable.setHorizontalHeaderItem(5, QTableWidgetItem("Availablity"))

        self.searchText=QLabel("Search")
        self.searchEntry=QLineEdit()
        self.searchEntry.setPlaceholderText("Search for Products")
        self.searchButton=QPushButton("Search")

        self.Allproduct=QRadioButton("All Products")
        self.Availableproduct=QRadioButton("Available")
        self.NotAvailableproduct=QRadioButton("Not Available")
        self.listButton=QPushButton("List")

        self.Upload = QWidget()
        self.Upload.setObjectName("Upload")

        self.uploadPhoto = QPushButton(self.Upload)
        self.uploadPhoto.setObjectName("Upload Photo")
        self.uploadPhoto.setGeometry(QRect(20, 200, 200, 200))
        self.uploadPhoto.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/addmember.png);")
        self.uploadPhoto.resize(255, 255)
        self.uploadPhoto.clicked.connect(self.funcUploadProduct)

        self.uploadVideo = QPushButton(self.Upload)
        self.uploadVideo.setObjectName("Upload Photo")
        self.uploadVideo.setGeometry(QRect(400, 200, 200, 200))
        self.uploadVideo.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/addmember.png);")
        self.uploadVideo.resize(255, 255)
        self.uploadVideo.clicked.connect(self.funcUploadScreensaver)

        self.label_photo = QLabel(self.Upload)
        self.label_photo.setGeometry(QRect(45, 400, 200, 200))
        font = QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(50)
        self.label_photo.setFont(font)
        self.label_photo.setObjectName("label_photo")
        self.label_photo.setText("<html><head/><body><p align=\"center\">Update Product</p></body></html>")

        self.label_video = QLabel(self.Upload)
        self.label_video.setGeometry(QRect(400, 400, 300, 200))
        font = QFont()
        font.setFamily("Myriad Pro Light")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(50)
        self.label_video.setFont(font)
        self.label_video.setObjectName("label_photo")
        self.label_video.setText("<html><head/><body><p align=\"center\">Upload Screensaver</p></body></html>")

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")

        #self.label_5 = QLabel(self.centralwidget)
        #self.label_5.setGeometry(QRect(320, 20, 481, 81))
        #font = QFont()
        #font.setFamily("Myriad Pro Light")
        #font.setPointSize(36)
        #font.setBold(True)
        #font.setWeight(75)
        #self.label_5.setFont(font)
        #self.label_5.setObjectName("label_5")
        #self.label_5.setText("<html><head/><body><p align=\"center\">Vending Machine</p></body></html>")

        self.stok1 = QPushButton(self.centralwidget)
        self.stok1.setGeometry(QRect(20, 200, 200, 200))
        self.stok1.setObjectName("stok1")
        self.stok1.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/stok1.jpg);")
        self.stok1.resize(200, 200)
        stok_1 = 'a'
        self.stok1.clicked.connect(lambda: self.clickme(stok_1))
        self.stok1.clicked.connect(self.funcPaymentSys)

        self.stok2 = QPushButton(self.centralwidget)
        self.stok2.setGeometry(QRect(300, 200, 200, 200))
        self.stok2.setObjectName("stok2")
        self.stok2.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok2.jpg);")
        self.stok2.resize(200, 200)
        stok_2 = 'b'
        self.stok2.clicked.connect(lambda: self.clickme(stok_2))
        self.stok2.clicked.connect(self.funcPaymentSys)

        self.stok3 = QPushButton(self.centralwidget)
        self.stok3.setGeometry(QRect(580, 200, 200, 200))
        self.stok3.setObjectName("stok3")
        self.stok3.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok3.jpg);")
        self.stok3.resize(200, 200)
        stok_3 = 'c'
        self.stok3.clicked.connect(lambda: self.clickme(stok_3))
        self.stok3.clicked.connect(self.funcPaymentSys)

        self.stok4 = QPushButton(self.centralwidget)
        self.stok4.setGeometry(QRect(860, 200, 200, 200))
        self.stok4.setObjectName("stok4")
        self.stok4.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/stok4.jpg);")
        self.stok4.resize(200, 200)
        stok_4 = 'd'
        self.stok4.clicked.connect(lambda: self.clickme(stok_4))
        self.stok4.clicked.connect(self.funcPaymentSys)

        self.stok5 = QPushButton(self.centralwidget)
        self.stok5.setGeometry(QRect(20, 445, 200, 200))
        self.stok5.setObjectName("stok5")
        self.stok5.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok5.jpg);")
        self.stok5.resize(200, 200)
        stok_5 = 'e'
        self.stok5.clicked.connect(lambda: self.clickme(stok_5))
        self.stok5.clicked.connect(self.funcPaymentSys)

        self.stok6 = QPushButton(self.centralwidget)
        self.stok6.setGeometry(QRect(300, 445, 200, 200))
        self.stok6.setObjectName("stok6")
        self.stok6.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok6.jpg);")
        self.stok6.resize(200, 200)
        stok_6 = 'f'
        self.stok6.clicked.connect(lambda: self.clickme(stok_6))
        self.stok6.clicked.connect(self.funcPaymentSys)

        self.stok7 = QPushButton(self.centralwidget)
        self.stok7.setGeometry(QRect(580, 445, 200, 200))
        self.stok7.setObjectName("stok7")
        self.stok7.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok7.jpg);")
        self.stok7.resize(200, 200)
        stok_7 = 'g'
        self.stok7.clicked.connect(lambda: self.clickme(stok_7))
        self.stok7.clicked.connect(self.funcPaymentSys)

        self.stok8 = QPushButton(self.centralwidget)
        self.stok8.setGeometry(QRect(860, 445, 200, 200))
        self.stok8.setObjectName("stok8")
        self.stok8.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok8.jpg);")
        self.stok8.resize(200, 200)
        stok_8 = 'h'
        self.stok8.clicked.connect(lambda: self.clickme(stok_8))
        self.stok8.clicked.connect(self.funcPaymentSys)

        self.stok9 = QPushButton(self.centralwidget)
        self.stok9.setGeometry(QRect(20, 690, 200, 200))
        self.stok9.setObjectName("stok9")
        self.stok9.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok9.jpg);")
        self.stok9.resize(200, 200)
        stok_9 = 'i'
        self.stok9.clicked.connect(lambda: self.clickme(stok_9))
        self.stok9.clicked.connect(self.funcPaymentSys)

        self.stok10 = QPushButton(self.centralwidget)
        self.stok10.setGeometry(QRect(300, 690, 200, 200))
        self.stok10.setObjectName("stok10")
        self.stok10.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok10.jpg);")
        self.stok10.resize(200, 200)
        stok_10 = 'j'
        self.stok10.clicked.connect(lambda: self.clickme(stok_10))
        self.stok10.clicked.connect(self.funcPaymentSys)

        self.stok11 = QPushButton(self.centralwidget)
        self.stok11.setGeometry(QRect(580, 690, 200, 200))
        self.stok11.setObjectName("stok11")
        self.stok11.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok11.jpg);")
        self.stok11.resize(200, 200)
        stok_11 = 'k'
        self.stok11.clicked.connect(lambda: self.clickme(stok_11))
        self.stok11.clicked.connect(self.funcPaymentSys)

        self.stok12 = QPushButton(self.centralwidget)
        self.stok12.setGeometry(QRect(860, 690, 200, 200))
        self.stok12.setObjectName("stok12")
        self.stok12.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok12.jpg);")
        self.stok12.resize(200, 200)
        stok_12 = 'l'
        self.stok12.clicked.connect(lambda: self.clickme(stok_12))
        self.stok12.clicked.connect(self.funcPaymentSys)

        self.stok13 = QPushButton(self.centralwidget)
        self.stok13.setGeometry(QRect(20, 935, 200, 200))
        self.stok13.setObjectName("stok13")
        self.stok13.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok13.jpg);")
        self.stok13.resize(200, 200)
        stok_13 = 'm'
        self.stok13.clicked.connect(lambda: self.clickme(stok_13))
        self.stok13.clicked.connect(self.funcPaymentSys)

        self.stok14 = QPushButton(self.centralwidget)
        self.stok14.setGeometry(QRect(300, 935, 200, 200))
        self.stok14.setObjectName("stok14")
        self.stok14.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok14.jpg);")
        self.stok14.resize(200, 200)
        stok_14 = 'n'
        self.stok14.clicked.connect(lambda: self.clickme(stok_14))
        self.stok14.clicked.connect(self.funcPaymentSys)

        self.stok15 = QPushButton(self.centralwidget)
        self.stok15.setGeometry(QRect(580, 935, 200, 200))
        self.stok15.setObjectName("stok15")
        self.stok15.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok15.jpg);")
        self.stok15.resize(200, 200)
        stok_15 = 'o'
        self.stok15.clicked.connect(lambda: self.clickme(stok_15))
        self.stok15.clicked.connect(self.funcPaymentSys)

        self.stok16 = QPushButton(self.centralwidget)
        self.stok16.setGeometry(QRect(860, 935, 200, 200))
        self.stok16.setObjectName("stok16")
        self.stok16.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok16.jpg);")
        self.stok16.resize(200, 200)
        stok_16 = 'p'
        self.stok16.clicked.connect(lambda: self.clickme(stok_16))
        self.stok16.clicked.connect(self.funcPaymentSys)

        self.stok17 = QPushButton(self.centralwidget)
        self.stok17.setGeometry(QRect(20, 1180, 200, 200))
        self.stok17.setObjectName("stok17")
        self.stok17.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok17.jpg);")
        self.stok17.resize(200, 200)
        stok_17 = 'q'
        self.stok17.clicked.connect(lambda: self.clickme(stok_17))
        self.stok17.clicked.connect(self.funcPaymentSys)

        self.stok18 = QPushButton(self.centralwidget)
        self.stok18.setGeometry(QRect(300, 1180, 200, 200))
        self.stok18.setObjectName("stok18")
        self.stok18.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok18.jpg);")
        self.stok18.resize(200, 200)
        stok_18 = 'r'
        self.stok18.clicked.connect(lambda: self.clickme(stok_18))
        self.stok18.clicked.connect(self.funcPaymentSys)

        self.stok19 = QPushButton(self.centralwidget)
        self.stok19.setGeometry(QRect(580, 1180, 200, 200))
        self.stok19.setObjectName("stok19")
        self.stok19.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok19.jpg);")
        self.stok19.resize(200, 200)
        stok_19 = 's'
        self.stok19.clicked.connect(lambda: self.clickme(stok_19))
        self.stok19.clicked.connect(self.funcPaymentSys)

        self.stok20 = QPushButton(self.centralwidget)
        self.stok20.setGeometry(QRect(860, 1180, 200, 200))
        self.stok20.setObjectName("stok20")
        self.stok20.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok20.jpg);")
        self.stok20.resize(200, 200)
        stok_20 = 't'
        self.stok20.clicked.connect(lambda: self.clickme(stok_20))
        self.stok20.clicked.connect(self.funcPaymentSys)

        self.stok21 = QPushButton(self.centralwidget)
        self.stok21.setGeometry(QRect(20, 1425, 200, 200))
        self.stok21.setObjectName("stok21")
        self.stok21.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok21.jpg);")
        self.stok21.resize(200, 200)
        stok_21 = 'u'
        self.stok21.clicked.connect(lambda: self.clickme(stok_21))
        self.stok21.clicked.connect(self.funcPaymentSys)

        self.stok22 = QPushButton(self.centralwidget)
        self.stok22.setGeometry(QRect(300, 1425, 200, 200))
        self.stok22.setObjectName("stok22")
        self.stok22.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok22.jpg);")
        self.stok22.resize(200, 200)
        stok_22 = 'v'
        self.stok22.clicked.connect(lambda: self.clickme(stok_22))
        self.stok22.clicked.connect(self.funcPaymentSys)

        self.stok23 = QPushButton(self.centralwidget)
        self.stok23.setGeometry(QRect(580, 1425, 200, 200))
        self.stok23.setObjectName("stok23")
        self.stok23.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok23.jpg);")
        self.stok23.resize(200, 200)
        stok_23 = 'w'
        self.stok23.clicked.connect(lambda: self.clickme(stok_23))
        self.stok23.clicked.connect(self.funcPaymentSys)

        self.stok24 = QPushButton(self.centralwidget)
        self.stok24.setGeometry(QRect(860, 1425, 200, 200))
        self.stok24.setObjectName("stok24")
        self.stok24.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok24.jpg);")
        self.stok24.resize(200, 200)
        stok_24 = 'x'
        self.stok24.clicked.connect(lambda: self.clickme(stok_24))
        self.stok24.clicked.connect(self.funcPaymentSys)

        self.stok25 = QPushButton(self.centralwidget)
        self.stok25.setGeometry(QRect(20, 1670, 200, 200))
        self.stok25.setObjectName("stok25")
        self.stok25.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok25.jpg);")
        self.stok25.resize(200, 200)
        stok_25 = 'y'
        self.stok25.clicked.connect(lambda: self.clickme(stok_25))
        self.stok25.clicked.connect(self.funcPaymentSys)

        self.stok26 = QPushButton(self.centralwidget)
        self.stok26.setGeometry(QRect(300, 1670, 200, 200))
        self.stok26.setObjectName("stok26")
        self.stok26.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok26.jpg);")
        self.stok26.resize(200, 200)
        stok_26 = 'z'
        self.stok26.clicked.connect(lambda: self.clickme(stok_26))
        self.stok26.clicked.connect(self.funcPaymentSys)

        self.stok27 = QPushButton(self.centralwidget)
        self.stok27.setGeometry(QRect(580, 1670, 200, 200))
        self.stok27.setObjectName("stok27")
        self.stok27.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok27.jpg);")
        self.stok27.resize(200, 200)
        stok_27 = 'A'
        self.stok27.clicked.connect(lambda: self.clickme(stok_27))
        self.stok27.clicked.connect(self.funcPaymentSys)

        self.stok28 = QPushButton(self.centralwidget)
        self.stok28.setGeometry(QRect(860, 1670, 200, 200))
        self.stok28.setObjectName("stok28")
        self.stok28.setStyleSheet(
            "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/stok28.jpg);")
        self.stok28.resize(200, 200)
        stok_28 = 'B'
        self.stok28.clicked.connect(lambda: self.clickme(stok_28))
        self.stok28.clicked.connect(self.funcPaymentSys)

    def layouts(self):
        self.mainLayout=QHBoxLayout()
        self.setupMainLayout=QHBoxLayout()
        self.mainLeftLayout=QVBoxLayout()
        self.mainRightLayout=QVBoxLayout()
        self.rightTopLayout=QHBoxLayout()
        self.rightMiddleLayout=QHBoxLayout()
        self.topGroupBox=QGroupBox("Search Box")
        self.middleGroupBox=QGroupBox("List Box")

        self.mainLeftLayout.addWidget(self.productsTable)

        self.rightTopLayout.addWidget(self.searchText)
        self.rightTopLayout.addWidget(self.searchEntry)
        self.rightTopLayout.addWidget(self.searchButton)
        self.topGroupBox.setLayout(self.rightTopLayout)

        self.rightMiddleLayout.addWidget(self.Allproduct)
        self.rightMiddleLayout.addWidget(self.Availableproduct)
        self.rightMiddleLayout.addWidget(self.NotAvailableproduct)
        self.rightMiddleLayout.addWidget(self.listButton)
        self.middleGroupBox.setLayout(self.rightMiddleLayout)

        self.mainRightLayout.addWidget(self.topGroupBox)
        self.mainRightLayout.addWidget(self.middleGroupBox)
        self.mainLayout.addLayout(self.mainLeftLayout, 70)
        self.mainLayout.addLayout(self.mainRightLayout, 30)
        self.tab2.setLayout(self.mainLayout)

        self.memberMainLayout=QHBoxLayout()
        self.memberMainLayout.addWidget(self.centralwidget)
        self.memberMainLayout.addLayout(self.memberMainLayout)
        self.tab1.setLayout(self.memberMainLayout)

        self.setupMainLayout=QHBoxLayout()
        self.setupMainLayout.addWidget(self.Upload)
        self.setupMainLayout.addLayout(self.setupMainLayout)
        self.tab3.setLayout(self.setupMainLayout)

    def clickme(self, arg):
        print(arg)
        i = arg
        #ser.write(i.encode())

    def funcPaymentSys(self):
        #pass
        self.newSys = metodebayar.MetodeBayar()
        #self.newSys = metodebayar.MetodeBayar(ser)

    def funcUploadProduct(self):
        self.newProduct=updateproduct.UpdateProduct()

    def funcUploadScreensaver(self):
        self.newSS=updatescreen.UpdateScreen()

'''''
    def displayProducts(self):
        for i in reversed(range(self.productsTable.rowCount())):
            self.productsTable.removeRow(i)

        query = cur.execute("SELECT product_ID,product_name,product_manufacturer,product_price,product_quota,product_availability FROM products")

        for row_data in query:
            row_number = self.productsTable.rowCount()
            self.productsTable.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.productsTable.setItem(row_number, column_number, QTableWidgetItem(str(data)))
'''
def main():
    App=QApplication(sys.argv)
    window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
