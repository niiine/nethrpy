#!/usr/bin/env python3

import sys
from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("nethr")

window = MainWindow()

window.show()

sys.exit(app.exec_())
