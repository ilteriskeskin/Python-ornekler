import sys
from PyQt5.QtWidgets import QWidget, QApplication, QRadioButton, QLabel, QPushButton, QVBoxLayout


class Pencere(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.radio_yazisi = QLabel('Favori Programlama Dilin Hangisi?')
        self.java = QRadioButton('Java')
        self.python = QRadioButton('Python')
        self.cpp = QRadioButton('C++')
        self.ruby = QRadioButton('Ruby')

        self.yazi_alani = QLabel('')
        self.button = QPushButton('Gönder')
        self.temizle = QPushButton('Temizle')

        v_box = QVBoxLayout()
        v_box.addWidget(self.radio_yazisi)
        v_box.addWidget(self.java)
        v_box.addWidget(self.python)
        v_box.addWidget(self.cpp)
        v_box.addWidget(self.ruby)
        v_box.addStretch()
        v_box.addWidget(self.yazi_alani)
        v_box.addWidget(self.button)
        v_box.addWidget(self.temizle)

        self.setLayout(v_box)
        self.setWindowTitle('Radio Button')

        self.button.clicked.connect(lambda : self.click(self.java.isChecked(), self.python.isChecked(), self.cpp.isChecked(), self.ruby.isChecked(), self.yazi_alani))
        self.temizle.clicked.connect(self.clear)
        self.show()

    def click(self, java, python, cpp, ruby, yazi_alani):
        if java:
            yazi_alani.setText('Java Dili Favorin')
        if python:
            yazi_alani.setText('Python Dili Favorin')
        if cpp:
            yazi_alani.setText('C++ Dili Favorin')
        if ruby:
            yazi_alani.setText('Ruby Dili Favorin')
    def clear(self):
        self.yazi_alani.clear()

app = QApplication(sys.argv)
pencere = Pencere()
sys.exit(app.exec_())
