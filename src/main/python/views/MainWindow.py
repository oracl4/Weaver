from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class MainWindow(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    # Main Window
    def __init__(self):
        super().__init__()
        loadUi(ApplicationContext().get_resource('MainLayout.ui'), self)

        # Button Handler
        self.ironCathodicButton.clicked.connect(self.createICW)
        self.ironThicknessButton.clicked.connect(self.createITW)
        self.steelCathodicButton.clicked.connect(self.createSCW)
        self.steelThicknessButton.clicked.connect(self.createSTW)
        
    # Button Function
    @pyqtSlot()
    def createICW(self):
        self.switch_window.emit("ICW")
    
    @pyqtSlot()
    def createITW(self):
        self.switch_window.emit("ITW")
    
    @pyqtSlot()
    def createSCW(self):
        self.switch_window.emit("SCW")

    @pyqtSlot()
    def createSTW(self):
        self.switch_window.emit("STW")