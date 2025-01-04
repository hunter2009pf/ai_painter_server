import sys

from PySide6.QtCore import QSize, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("AI Painter")
        self.setFixedSize(QSize(800, 600))


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
