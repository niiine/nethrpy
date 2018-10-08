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

        #hide labels urlaub 2-4
        self.ui.label_urlaub_von_2.hide()
        self.ui.label_urlaub_von_3.hide()
        self.ui.label_urlaub_von_4.hide()
        self.ui.label_urlaub_bis_2.hide()
        self.ui.label_urlaub_bis_3.hide()
        self.ui.label_urlaub_bis_4.hide()

        #hide dates urlaub 2-4
        self.ui.date_urlaub_bis_2.hide()
        self.ui.date_urlaub_bis_3.hide()
        self.ui.date_urlaub_bis_4.hide()
        self.ui.date_urlaub_von_2.hide()
        self.ui.date_urlaub_von_3.hide()
        self.ui.date_urlaub_von_4.hide()

        self.ui.button_help.clicked.connect(self.set_help_text)

    def set_help_text(self):
        self.ui.text_dialog.setText("Sonderzeiten = alles, was von der Netto - Arbeitszeit abgezogen werden muss. (Krankheit/Meeting etc)\nFeiertage müssen nicht beachtet - werden, da sie automatisch berechnet werden.\n(Momentan nur RLP Feiertage, Option für andere - Bundesländer wird irgendwann hinzugefügt.")


window = MainWindow()

window.show()



sys.exit(app.exec_())
