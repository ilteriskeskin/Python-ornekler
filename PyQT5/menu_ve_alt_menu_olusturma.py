import sys
from PyQt5.QtWidgets import QApplication, QAction, qApp, QMainWindow


class Menu(QMainWindow):
    def __init__(self):
        super().__init__()

        menu_bar = self.menuBar()
        dosya = menu_bar.addMenu('Dosya')
        duzenle = menu_bar.addMenu('Düzenle')

        dosya_ac = QAction('Dosya Aç', self)
        dosya_ac.setShortcut('Ctrl+o')

        dosya_kaydet = QAction('Dosya Kaydet', self)
        dosya_kaydet.setShortcut('Ctrl+s')

        cikis = QAction('Çıkış', self)
        cikis.setShortcut('Ctrl+q')

        dosya.addAction(dosya_ac)
        dosya.addAction(dosya_kaydet)
        dosya.addAction(cikis)

        ara_ve_degistir = duzenle.addMenu('Ara ve Değiştir')
        ara = QAction('Ara', self)
        degistir = QAction('Değiştir', self)
        temizle = QAction('Temizle', self)

        ara_ve_degistir.addAction(ara)
        ara_ve_degistir.addAction(degistir)
        duzenle.addAction(temizle)

        cikis.triggered.connect(self.cikis_yap)

        dosya.triggered.connect(self.response)

        self.setWindowTitle('Menüler')
        self.show()

    def cikis_yap(self):
        qApp.quit()

    def response(self, action):
        if action.text() == 'Dosya Aç':
            print('Dosya Aç seçildi')
        elif action.text() == 'Dosya Kaydet':
            print('Dosya Kaydet seçildi')
        elif action.text() == 'Çıkış':
            print('Çıkış seçildi')

app = QApplication(sys.argv)
menu = Menu()
sys.exit(app.exec_())