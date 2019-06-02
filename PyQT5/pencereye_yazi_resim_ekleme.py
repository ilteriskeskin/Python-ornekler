import sys
from PyQt5 import QtWidgets, QtGui

def window():
    app = QtWidgets.QApplication(sys.argv)
    pencere = QtWidgets.QWidget()
    
    pencere.setWindowTitle('PyQt Ders 1')
    etiket1 = QtWidgets.QLabel(pencere)
    etiket2 = QtWidgets.QLabel(pencere)
    
    etiket1.setText("Burası Etiket")
    etiket1.move(200, 30)
    
    etiket2.setPixmap(QtGui.QPixmap('img/pyqt.png'))
    etiket2.move(70, 100)

    pencere.setGeometry(100, 100, 1500, 1500)
    
    pencere.show()
    sys.exit(app.exec_())

window()
