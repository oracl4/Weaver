from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class IronThicWindowLay(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    # ITW Window
    def __init__(self):
        super().__init__()
        loadUi(ApplicationContext().get_resource('IronThicLayout.ui'), self)

        # Button Handler
        self.HomeButton.clicked.connect(self.goHome)
        self.CalculateButton.clicked.connect(self.calculateCath)

    @pyqtSlot()
    def goHome(self):
        self.switch_window.emit("HITW")

    @pyqtSlot()
    def calculateCath(self):
        self.switch_window.emit("OITW")