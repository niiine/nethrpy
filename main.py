#!/usr/bin/env python3

import datetime
import sys
import holidays
from qtpy import QtWidgets

from ui.mainwindow import Ui_MainWindow

app = QtWidgets.QApplication(sys.argv)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle("nethr")




        #init urlaub_array
        global urlaub_array
        urlaub_array = [
        [self.ui.label_urlaub_von_1,
        self.ui.label_urlaub_bis_1,
        self.ui.date_urlaub_von_1,
        self.ui.date_urlaub_bis_1],

        [self.ui.label_urlaub_von_2,
        self.ui.label_urlaub_bis_2,
        self.ui.date_urlaub_von_2,
        self.ui.date_urlaub_bis_2],

        [self.ui.label_urlaub_von_3,
        self.ui.label_urlaub_bis_3,
        self.ui.date_urlaub_von_3,
        self.ui.date_urlaub_bis_3],

        [self.ui.label_urlaub_von_4,
        self.ui.label_urlaub_bis_4,
        self.ui.date_urlaub_von_4,
        self.ui.date_urlaub_bis_4],

        [self.ui.label_urlaub_von_5,
        self.ui.label_urlaub_bis_5,
        self.ui.date_urlaub_von_5,
        self.ui.date_urlaub_bis_5],

        [self.ui.label_urlaub_von_6,
        self.ui.label_urlaub_bis_6,
        self.ui.date_urlaub_von_6,
        self.ui.date_urlaub_bis_6],

        [self.ui.label_urlaub_von_7,
        self.ui.label_urlaub_bis_7,
        self.ui.date_urlaub_von_7,
        self.ui.date_urlaub_bis_7],

        [self.ui.label_urlaub_von_8,
        self.ui.label_urlaub_bis_8,
        self.ui.date_urlaub_von_8,
        self.ui.date_urlaub_bis_8],

        [self.ui.label_urlaub_von_9,
        self.ui.label_urlaub_bis_9,
        self.ui.date_urlaub_von_9,
        self.ui.date_urlaub_bis_9]
        ]

        #hide labels urlaub 2-9
        self.init_hide_urlaub()


        #help button functionality
        self.ui.button_help.clicked.connect(self.set_help_text)

        #about button functionality
        self.ui.button_about.clicked.connect(self.set_about_text)

        #was_ist_sonderzeit button functionality
        self.ui.button_was_ist_sonderzeit.clicked.connect(self.set_sonderzeit_text)

        #show urlaub and hide urlaub buttons functionality
        self.ui.button_urlaub_hinzufuegen.clicked.connect(self.show_urlaub)
        self.ui.button_urlaub_entfernen.clicked.connect(self.hide_urlaub)

        #nettostunden berechnen button functionality
        self.ui.button_nettostunden_berechnen.clicked.connect(self.calculate_nettohours)


    def set_help_text(self):
        self.ui.text_dialog.setText("Kontakt via About-Button\nFeiertage sind nicht zu beachten, da sie automatisiert eingerechnet werden.\n(Momentan nur RLP Feiertage, Option für andere Bundesländer wird irgendwann hinzugefügt.")

    def set_about_text(self):
        self.ui.text_dialog.setText("Kontaktemail: nine.github@gmail.com\nKontaktwebsite: https://github.com/strahlii\nSourcecode: https://github.com/strahlii/nethrpy")

    def set_sonderzeit_text(self):
        self.ui.text_dialog.setText("Sonderzeiten = alles, was von der Netto-Arbeitszeit abgezogen werden muss (Meeting etc)\nFalls nötig kann hier auch die Krankheitszeit in Stunden angegeben werden, wenn bei Urlaub kein Platz mehr dafür ist.")

    #asks which_urlaub_to_show(), then shows the 4 urlaub-widgets via the array urlaub_array
    def show_urlaub(self):
        i = self.which_urlaub_to_show()
        if i is not None:
            global urlaub_array
            for e in urlaub_array[i]:
                e.show()

    #see show_urlaub()
    def hide_urlaub(self):
        i = self.which_urlaub_to_hide()
        if i is not None:
            global urlaub_array
            for e in urlaub_array[i]:
                e.hide()

    #from 0 to 8 asks urlaub_array widget if its hidden, if yes, return the first one (lowest index)
    def which_urlaub_to_show(self):
        global urlaub_array
        for i in range(9):
            if urlaub_array[i][0].isHidden():
                return i
        return None

    #from 8 to 0 asks urlaub_array widget if its shown, if yes, return the last one (highest index)
    def which_urlaub_to_hide(self):
        global urlaub_array
        for i in reversed(range(9)):
            if urlaub_array[i][0].isHidden() == False:
                return i
        return None

    #hides every widget in urlaub_array
    def init_hide_urlaub(self):
        global urlaub_array
        for i in urlaub_array:
            if i is urlaub_array[0]:
                continue
            for e in i:
                e.hide()

    #starts nethr__init__
    def calculate_nettohours(self):
        self.nethr__init__()

    #gets all values to calculate the netto hours
    def nethr__init__(self):
        global urlaub_array
        urlaub_list = []
        QDateEdit = type(self.ui.date_urlaub_von_1)
        for i in urlaub_array:
            for e in i:
                obj_type = type(e)
                if obj_type is QDateEdit and e.isVisible():
                    urlaub_list.append(e.date().toPyDate())
        offh = self.ui.spin_sonderzeit.value()
        hperday_array = [self.ui.spin_montag.value(), self.ui.spin_dienstag.value(), self.ui.spin_mittwoch.value(), self.ui.spin_donnerstag.value(), self.ui.spin_freitag.value(), self.ui.spin_samstag.value(), self.ui.spin_sonntag.value()]
        start = self.ui.date_zeitraum_von.date().toPyDate()
        end = self.ui.date_zeitraum_bis.date().toPyDate()
        urlaub_list = self.crop_urlaub(start, end, urlaub_list)
        ger_holidays = holidays.CountryHoliday('DE', prov='RP')
        print(urlaub_list)

        self.calculate(start, end, hperday_array, urlaub_list, offh, ger_holidays)

    def crop_urlaub(self, start, end, urlaub_list):
        i=0
        while i+1 < len(urlaub_list):
            if urlaub_list[i] > end or urlaub_list[i+1] < start:
                del urlaub_list[i]
                del urlaub_list[i]
            else:
                if urlaub_list[i] < start:
                    urlaub_list[i] = start
                if urlaub_list[i+1] > end:
                    urlaub_list[i+1] = end
            i=i+2
        return urlaub_list



    def calculate(self, start, end, hperday_array, urlaub_list, offh, ger_holidays):
        nettoh = 0
        currday = start
        td = datetime.timedelta(days=1)
        while currday <= end:
            if currday not in ger_holidays:
                nettoh = nettoh + hperday_array[currday.weekday()]
            else:
                print(currday)
            currday = currday + td
        print(nettoh)

    def calc_holidays(self, start, end, hperday_array, urlaub_list, offh, ger_holidays):
       holiday_hours = 0
       i=0
       while i+1 < len(urlaub_list):
           holiday_start = urlaub_list[i]
           holiday_end = urlaub_list[i+1]
           i=i+2





window = MainWindow()

window.show()



sys.exit(app.exec_())
