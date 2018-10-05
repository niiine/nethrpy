#!/usr/bin/env python3

import sys
from qtpy import QtWidgets

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QMainWindow()
window.setWindowTitle("nethr")

button = QtWidgets.QPushButton(window)
button.show()

window.show()

sys.exit(app.exec_())
