#GUI (2 of 9) PyQt5 QLabels

import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First GUI app")
        self.setGeometry(750, 350, 500, 500)
        self.setWindowIcon(QIcon("C:/Users/morko/Downloads/randomPhoto.JPG"))

        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 26))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: red;" 
                            "background-color: cyan;" 
                            "font-weight: bold;" 
                            "font-style: italic;" 
                            "text-decoration: underline;"
                            )
#        label.setAlignment(Qt.AlignTop) # Align Top
#        label.setAlignment(Qt.AlignBottom) # Align Bottom
#        label.setAlignment(Qt.AlignVCenter) # Align Vertically to the center

#        label.setAlignment(Qt.AlignRight) # Align Right
#        label.setAlignment(Qt.AlignHCenter) # Align Horizontally to the center
#        label.setAlignment(Qt.AlignLeft) # Align Left
#        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # combination of horizontal and vertical positions
        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()