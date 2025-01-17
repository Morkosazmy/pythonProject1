#GUI (1 of 7) PyQt5

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI app")
        self.setGeometry(750, 350, 500, 500)
        self.setWindowIcon(QIcon("C:/Users/morko/Downloads/randomPhoto.JPG"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()