from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class SteelThicWindowLay(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    # STW Window
    def __init__(self):
        super().__init__()
        loadUi(ApplicationContext().get_resource('SteelThicLayout.ui'), self)

        # Button Handler
        self.HomeButton.clicked.connect(self.goHome)
        self.CalculateButton.clicked.connect(self.calculateCath)
        self.ObjectClass.activated.connect(self.ChangeSpecFunc)
        self.Specification.activated.connect(self.ChangeGradeFunc)

    @pyqtSlot()
    def ChangeSpecFunc(self):
        ClassChanged = self.ObjectClass.currentText()
        self.Specification.clear()
        if ClassChanged == "Seamless":
            self.Specification.addItems(["S API 5L", "S ASTM A 53", "S ASTM A 106", "S ASTM A 333", "S ASTM A 524"])
        elif ClassChanged == "Submerged Arc":
            self.Specification.addItems(["DSA API 5L", "DSA ASTM A 381"])
        elif ClassChanged == "Electric Fusion":
            self.Specification.addItems(["EF ASTM A 134", "EF ASTM A 139", "EF ASTM A 671", "EF ASTM A 672"])
        elif ClassChanged == "Electric Resistance":
            self.Specification.addItems(["ERWAPI 5L", "ERW ASTM A 53", "ERW ASTM A 135", "ERW ASTM A 333"])
        elif ClassChanged == "Furnace Butt":
            self.Specification.addItems(["BW API 5L", "BW ASTM A 53"])
        self.ChangeGradeFunc()

    @pyqtSlot()
    def ChangeGradeFunc(self):
        SpecChanged = self.Specification.currentText()
        self.Grade.clear()
        # Seamless
        if SpecChanged == "S API 5L":
            self.Grade.addItems(["A25", "A", "B", "X42", "X46", "X52", "X56", "X60", "X65", "X70", "X80"])
        elif SpecChanged == "S ASTM A 53":
            self.Grade.addItems(["A", "B"])
        elif SpecChanged == "S ASTM A 106":
            self.Grade.addItems(["A", "B", "C"])
        elif SpecChanged == "S ASTM A 333":
            self.Grade.addItems(["6"])
        elif SpecChanged == "S ASTM A 524":
            self.Grade.addItems(["I", "H"])

        # Submerged Arc
        elif SpecChanged == "DSA API 5L":
            self.Grade.addItems(["A", "B", "X42", "X46", "X52", "X56", "X60", "X65", "X70", "X80"])
        elif SpecChanged == "DSA ASTM A 381":
            self.Grade.addItems(["Y35", "Y42", "Y46", "Y48", "Y50", "Y52", "Y60", "Y65"])

        # Electric Fusion
        elif SpecChanged == "EF ASTM A 134":
            self.Grade.addItems(["-"])
        elif SpecChanged == "EF ASTM A 139":
            self.Grade.addItems(["A", "B"])
        elif SpecChanged == "EF ASTM A 671":
            self.Grade.addItems(["-", "--"])
        elif SpecChanged == "EF ASTM A 672":
            self.Grade.addItems(["-", "--"])

        # Electric Resistance
        elif SpecChanged == "ERWAPI 5L":
            self.Grade.addItems(["A", "B", "X42", "X46", "X52", "X56", "X60", "X65", "X70", "X80"])
        elif SpecChanged == "ERW ASTM A 53":
            self.Grade.addItems(["A", "B"])
        elif SpecChanged == "ERW ASTM A 135":
            self.Grade.addItems(["A", "B"])
        elif SpecChanged == "ERW ASTM A 333":
            self.Grade.addItems(["6"])

        # Furnace Butt
        elif SpecChanged == "BW API 5L":
            self.Grade.addItems(["A25"])
        elif SpecChanged == "BW ASTM A 53":
            self.Grade.addItems(["-"])

    @pyqtSlot()
    def goHome(self):
        self.switch_window.emit("HSTW")

    @pyqtSlot()
    def calculateCath(self):
        self.switch_window.emit("OSTW")