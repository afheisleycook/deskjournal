from PyQt6.QtWidgets import (QApplication, QWidget,QTextEdit,QPushButton,QPlainTextEdit,QLabel)
import sys
import sqlite3
app = sqlite3.connect("app.db")
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(10,10,300, 400)
        self.show()
        self.ltitle = QLabel(self)
        self.ltitle.setText("enter a title")
        self.ltitle.show()




app = QApplication(sys.argv)
main = MainWindow()
sys.exit(app.exec())


