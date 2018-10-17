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



        #init urlaub_count which is the counter for which array needs to be shown/hidden
        global urlaub_count
        urlaub_count = 0

        #init urlaub_array
        global urlaub_array
        urlaub_array = [
        [self.ui.label_urlaub_von_2,
        self.ui.label_urlaub_bis_2,
        self.ui.date_urlaub_bis_2,
        self.ui.date_urlaub_von_2],

        [self.ui.label_urlaub_von_3,
        self.ui.label_urlaub_bis_3,
        self.ui.date_urlaub_bis_3,
        self.ui.date_urlaub_von_3],

        [self.ui.label_urlaub_von_4,
        self.ui.label_urlaub_bis_4,
        self.ui.date_urlaub_bis_4,
        self.ui.date_urlaub_von_4],

        [self.ui.label_urlaub_von_5,
        self.ui.label_urlaub_bis_5,
        self.ui.date_urlaub_bis_5,
        self.ui.date_urlaub_von_5],

        [self.ui.label_urlaub_von_6,
        self.ui.label_urlaub_bis_6,
        self.ui.date_urlaub_bis_6,
        self.ui.date_urlaub_von_6],

        [self.ui.label_urlaub_von_7,
        self.ui.label_urlaub_bis_7,
        self.ui.date_urlaub_bis_7,
        self.ui.date_urlaub_von_7],

        [self.ui.label_urlaub_von_8,
        self.ui.label_urlaub_bis_8,
        self.ui.date_urlaub_bis_8,
        self.ui.date_urlaub_von_8],

        [self.ui.label_urlaub_von_9,
        self.ui.label_urlaub_bis_9,
        self.ui.date_urlaub_bis_9,
        self.ui.date_urlaub_von_9]
        ]

        #hide labels urlaub 2-9
        self.init_hide_urlaub()


        #help button
        self.ui.button_help.clicked.connect(self.set_help_text)

        #about button
        self.ui.button_about.clicked.connect(self.set_about_text)


        self.ui.button_urlaub_hinzufuegen.clicked.connect(self.show_urlaub)
        self.ui.button_urlaub_entfernen.clicked.connect(self.hide_urlaub)


    def set_help_text(self):
        self.ui.text_dialog.setText("Sonderzeiten = alles, was von der Netto - Arbeitszeit abgezogen werden muss. (Krankheit/Meeting etc)\nFeiertage müssen nicht beachtet - werden, da sie automatisch berechnet werden.\n(Momentan nur RLP Feiertage, Option für andere - Bundesländer wird irgendwann hinzugefügt.")

    def set_about_text(self):
        self.ui.text_dialog.setText("Kontaktemail: nine.github@gmail.com\nKontaktwebsite: https://github.com/strahlii\nSourcecode: https://github.com/strahlii/nethrpy")

    def show_urlaub(self):
        global urlaub_count
        global urlaub_array
        for e in urlaub_array[urlaub_count]:
            e.show()
        urlaub_count +=1

    def hide_urlaub(self):
        global urlaub_count
        global urlaub_array
        for e in urlaub_array[urlaub_count]:
            e.hide()
        urlaub_count -=1

    def init_hide_urlaub(self):
        global urlaub_array
        for i in urlaub_array:
            for e in i:
                e.hide()


window = MainWindow()

window.show()



sys.exit(app.exec_())
