from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
import sys


# hidden translated text - httxt
class MainWindow(QMainWindow):
    def __init__(self, design_path, parent=None):
        QMainWindow.__init__(self, parent)
        uic.loadUi(design_path, self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow("page_designs/raw_page.ui")
    window.show()
    sys.exit(app.exec_())
