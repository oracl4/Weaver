from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

import Printer as pr

class WallCathWindowLay(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)
    [PipeSegment, CPResult] = [0, 0]

    def __init__(self, PipeSegment, WallOutput):
        super().__init__()
        loadUi(ApplicationContext().get_resource('WallCathResult.ui'), self)
        qssFile = open(ApplicationContext().get_resource('Style.qss')).read()
        
        # Button Handler
        self.HomeButton.clicked.connect(self.goHome)
        self.PrintButton.clicked.connect(self.printResult)

        # Label Handler
        # Pipe Segment
        OutputStyled = """<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600;">""" + str(PipeSegment) + """</span></p></body></html>"""
        self.PipeSegment.setText(OutputStyled)
        self.PipeSegment.setStyleSheet(qssFile)

        OutputStyled = """<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600;">""" + str(WallOutput) + """</span></p></body></html>"""
        self.WallOutput.setText(OutputStyled)
        self.WallOutput.setStyleSheet(qssFile)

    @pyqtSlot()
    def goHome(self):
        self.switch_window.emit("HOWC")

    @pyqtSlot()
    def sendInput(self, PipeSegment, CPResult):
        self.PipeSegment = PipeSegment
        self.CPResult = CPResult

    @pyqtSlot()
    def printResult(self):
        doc = QtGui.QTextDocument()
        doc.setHtml(self.WallOutput.text())
        CPStatus = doc.toPlainText()

        pr.printCathodicResult(self.CPResult, CPStatus)