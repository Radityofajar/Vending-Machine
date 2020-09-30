from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import *
import sys
import os
import sqlite3
from PIL import Image
import serial
import time

global ser
ser = serial.Serial('/dev/ttyUSB0', 115200, timeout=10, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS)
time.sleep(1)
con = sqlite3.connect('database.db')
cur = con.cursor()

defaultImg = "shop.png"
dataList = [0] * 28

class Main(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Data")
        self.setGeometry(0, 0, 1080, 1920)
        self.UI()
        self.show()

    def UI(self):

        self.mainDesign()
        self.layouts()

    def createStock(self, v, x, y, z, img):
        stok = QPushButton(self.centralwidget)
        stok.setGeometry(QRect(x, y, 200, 200))
        stok.setObjectName("stok" + str(v + 1))
        if(dataList[v] == '1'):
            stok.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px; background-image : url(img/" + str(img) + ".jpg);")
            stok.resize(200, 200)
            C = str(z)
            stok.clicked.connect(lambda: self.clickme(C))
            stok.clicked.connect(self.funcPaymentSys)
        else:
            stok.setStyleSheet(
                "border-style: outset; padding: 8px; border-radius: 10px;background-image : url(img/no.jpg);")
            stok.resize(200, 200)
    
    def createLabel(self, x, y, z):
        cur.execute("SELECT harga FROM database")
        stock = cur.fetchall()

        label = QLabel(self.centralwidget)
        label.setGeometry(QRect(x, y, 150, 50 ))
        label.setStyleSheet('font-size: 20pt; font-family: Arial Bold;')
        label.setText("Rp" + " " + str(stock[z][0]))
    
    def mainDesign(self):
        self.setStyleSheet("background-color: white")

        # for stok in stok:
        #   self.stok(str(database[0]) + "-" + database[2] + " " + database[1] + " " + database[3])

        r = 'R'
        ser.write(r.encode())

        time.sleep(0.3)

        print("sini")

        # time.sleep(0.3)

        for i in range(0, 28):
            data = (ser.readline().split()[0].decode("ascii"))
            print(data)
            dataList[i] = data

        self.centralwidget = QWidget()
        self.centralwidget.setObjectName("centralwidget")

        self.label = []
        self.stok = []

        for i in range (5):
            x = 80 + (i % 4) *280
            y = 400 + (i // 4) *245
            z = 0 + i

            self.label.append(self.createLabel(x, y, z))

        for i in range (28):
            v = 0 + i
            x = 40 + (i % 4) * 280
            y = 200 + (i // 4) * 245
            z = chr(ord('a') + i)
            img = 'stok' + str((i+1))

            self.stok.append(self.createStock( v, x, y, z, img))


        
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
        # self.mainLayout.addLayout(self.mainLayout)

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

    def closeEvent(self, event):
        self.main = Main()

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
        # self.main = Main()


class LogIn(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.setWindowIcon(QIcon('icons/members.png'))
        self.setGeometry(0, 0, 1200, 1890)
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
        # self.stok1.update()
        self.main = Main()
        self.close()
        


class AddSetup(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Setup")
        self.setWindowIcon(QIcon('icons/setup.png'))
        self.setGeometry(505, 250, 1080, 1920)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

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

        # setting main window layout
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
            mbox = QMessageBox.question(self, "Warning", "Are you sure to delete this product?",
                                        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
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
        self.show()

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

        # bottom layout
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
        self.bottomLayout.addRow(self.nameLbl, self.nameEntry)
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
        self.show()

    def UI(self):
        self.mainDesign()
        self.layouts()

    # def closeEvent(self, event):
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
