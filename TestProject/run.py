import sys
from PyQt5 import QtWidgets, QtGui
from MainWindowC import MainWindow

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
