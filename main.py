#GUI (6 of 9) PyQt5 Checkboxes

import sys
from tkinter import Widget

from PyQt5.QtWidgets import (QMainWindow, QApplication, QLabel, QWidget, QBoxLayout, QHBoxLayout, QGridLayout,
                             QVBoxLayout, QPushButton, QCheckBox)
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        #self.setWindowTitle("First GUI app")
        self.setGeometry(750, 350, 500, 500)
        self.checkbox = QCheckBox("Are you a human being ?", self)
        #self.button = QPushButton("Click Here !", self)
        #self.setWindowIcon(QIcon("C:/Users/morko/Downloads/randomPhoto.JPG"))
        #self.label5 = QLabel("Hello", self)
        self.initUI()

    def initUI(self):
        self.checkbox.setStyleSheet("font-size: 20px;" "font-family: bold;")
        self.checkbox.setGeometry(10, 0, 300, 100)
        self.checkbox.setChecked(False)
        self.checkbox.stateChanged.connect(self.checkbox_changed)


    """ self.button.setGeometry(150, 150, 300, 300)
        self.button.setStyleSheet("font-size: 28px;")
        self.button.clicked.connect(self.on_click)
        self.label5.setGeometry(150, 300, 200, 100)
        self.label5.setStyleSheet("font-size: 50px;")
    """

    def checkbox_changed(self, state):
        print(state)
        if state == Qt.Checked:
        #if state == 2:
           print("You are a human being !")
        else:
            print("You don't like food")


"""
    def on_click(self):
        print("Button clicked !")
        self.button.setText("clicked")
        self.button.setDisabled(True)
        self.label5.setText("Goodbye")
"""




"""
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        label1 = QLabel("#1", self)

        label2 = QLabel("#2", self)

        label3 = QLabel("#3", self)

        label4 = QLabel("#4", self)

        label5 = QLabel("#5", self)

        label1.setStyleSheet("background-color: red")
        label2.setStyleSheet("background-color: blue")
        label3.setStyleSheet("background-color: green")
        label4.setStyleSheet("background-color: purple")
        label5.setStyleSheet("background-color: yellow")



        grid = QGridLayout()

        grid.addWidget(label1, 0, 0)
        grid.addWidget(label2, 0, 1)
        grid.addWidget(label3, 0, 2)
        grid.addWidget(label4, 1, 0)
        grid.addWidget(label5, 1, 2)

        central_widget.setLayout(grid)
"""
"""
        vbox= QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)
        vbox.addWidget(label5)

        central_widget.setLayout(vbox)
"""
"""
        hbox = QHBoxLayout()

        hbox.addWidget(label1)
        hbox.addWidget(label2)
        hbox.addWidget(label3)
        hbox.addWidget(label4)
        hbox.addWidget(label5)

        central_widget.setLayout(hbox)
"""



"""
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 26))
        label.setGeometry(0,0,500,100)
        label.setStyleSheet("color: red;" 
                            "background-color: cyan;" 
                            "font-weight: bold;" 
                            "font-style: italic;" 
                            "text-decoration: underline;"
                            )

        label2 = QLabel(self)
        label2.setGeometry(0, 0, 250, 250)

        pixmap = QPixmap("C:/Users/morko/Downloads/randomPhoto.JPG")
        label2.setPixmap(pixmap)
        label2.setScaledContents(True)


        label2.setGeometry((self.width() - label2.width()) // 2 , (self.height() - label2.height()) // 2, label2.width(), label.height())
"""
#        label.setAlignment(Qt.AlignTop) # Align Top
#        label.setAlignment(Qt.AlignBottom) # Align Bottom
#        label.setAlignment(Qt.AlignVCenter) # Align Vertically to the center

#        label.setAlignment(Qt.AlignRight) # Align Right
#        label.setAlignment(Qt.AlignHCenter) # Align Horizontally to the center
#        label.setAlignment(Qt.AlignLeft) # Align Left
#        label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # combination of horizontal and vertical positions
#        label.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()