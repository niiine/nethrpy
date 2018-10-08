#!/usr/bin/env python3

import sys
from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle("nethr")

ui_window = Ui_MainWindow()
ui_window.setupUi(window)

window.show()

sys.exit(app.exec_())
