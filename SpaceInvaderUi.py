import sys

from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QImage, QPixmap, QPainter, QColor
from PyQt5.uic import loadUi


class MyGui(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("TestGui.ui", self)
        self.test_button.clicked.connect(self.print_black_image)

    def print_image(self, new_image):
        pixmap = QPixmap.fromImage(new_image)
        self.image.setPixmap(pixmap)

    def print_black_image(self):
        new_image = QImage(self.image.size(), QImage.Format_Mono)
        new_image.fill(Qt.color0)
        self.print_image(new_image)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyGui()
    window.show()
    sys.exit(app.exec_())
