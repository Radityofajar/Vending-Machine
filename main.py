import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
# import sqlite3
import addsetup

# con = sqlite3.connect("products.db")
# cur = con.cursor()


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Vending Machine")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(10, 40, 1350, 750)

        self.UI()
        self.show()

    def UI(self):
        self.toolBar()

    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # Toolbar Buttons #
        # Menu #
        self.addMenu = QAction(QIcon('icons/shop.png'), "Shop", self)
        self.tb.addAction(self.addMenu)
        self.tb.addSeparator()

        # Setup #
        self.addSetup = QAction(QIcon('icons/setup.png'), "Setup", self)
        self.tb.addAction(self.addSetup)
        self.addSetup.triggered.connect(self.funcAddSetup)
        self.tb.addSeparator()

    def funcAddSetup(self):
        self.newSetup = addsetup.AddSetup()


def main():
    App=QApplication(sys.argv)
    Window = Main()
    sys.exit(App.exec_())

if __name__ == '__main__':
    import sys

    App = QApplication(sys.argv)
    Window = Main()
    sys.exit(App.exec_())