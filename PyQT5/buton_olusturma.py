import sys
from PyQt5 import QtWidgets, QtGui


def window():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()

    pencere.setWindowTitle('PyQt Ders 2')
    button = QtWidgets.QPushButton(pencere)
    button.setText('Bir Buton')
    etiket = QtWidgets.QLabel(pencere)
    etiket.setText('Merhaba PyQt5')

    etiket.move(200, 30)
    button.move(200, 60)
    pencere.setGeometry(100, 100, 500, 500)

    pencere.show()
    sys.exit(app.exec_())


window()
