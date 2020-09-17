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

    def closeEvent(self, event):
        self.main = Main()

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
        size = (120, 120)
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
    Window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
