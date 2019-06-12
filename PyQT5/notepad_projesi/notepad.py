import sys
import os
from PyQt5.QtWidgets import QWidget, QApplication, QTextEdit, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog


class Notepad(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.yazi_alani = QTextEdit()
        self.temizle = QPushButton('Temizle')
        self.ac = QPushButton('Aç')
        self.kaydet = QPushButton('Kaydet')

        h_box = QHBoxLayout()
        h_box.addWidget(self.temizle)
        h_box.addWidget(self.ac)
        h_box.addWidget(self.kaydet)

        v_box = QVBoxLayout()
        v_box.addWidget(self.yazi_alani)
        v_box.addLayout(h_box)

        self.setLayout(v_box)
        self.setWindowTitle('NotePad')

        self.temizle.clicked.connect(self.yaziyi_temizle)
        self.ac.clicked.connect(self.dosya_ac)
        self.kaydet.clicked.connect(self.dosya_kaydet)

        self.show()

    def yaziyi_temizle(self):
        self.yazi_alani.clear()

    def dosya_ac(self):
        dosya_ismi = QFileDialog.getOpenFileName(self, 'Dosya Aç', os.getenv('HOME'))
        with open(dosya_ismi[0], 'r') as file:
            self.yazi_alani.setText(file.read())

    def dosya_kaydet(self):
        dosya_ismi = QFileDialog.getSaveFileName(self, 'Dosya Kaydet', os.getenv('HOME'))
        with open(dosya_ismi[0], 'w') as file:
            file.write(self.yazi_alani.toPlainText())

app = QApplication(sys.argv)
notepad = Notepad()
sys.exit(app.exec_())
