from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

import Printer as pr

class WallThicWindowLay(QMainWindow):
    switch_window = QtCore.pyqtSignal(str)

    PipeSegment, FluidType, Location, ObjectClass, Specification, Grade, NPS, SCH = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
    DesignPressure, DesignTemp, CorrAllo, ManTol, UTResult, SMYS, WeldJointFact, DesignFact = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]
    AllowStress, TempDerating, NomWallThick, MinWallThick, CorrDepth, WallThick = ["N/A", "N/A", "N/A", "N/A", "N/A", "N/A"]

    def __init__(self, PipeSegment, WallOutput, NomWallOutput, ReqWallOutput, CorDepthOutput):
        super().__init__()
        loadUi(ApplicationContext().get_resource('WallThicResult.ui'), self)
        qssFile = open(ApplicationContext().get_resource('Style.qss')).read()

        # Button Handler
        self.HomeButton.clicked.connect(self.goHome)
        self.PrintButton.clicked.connect(self.printResult)

        # Label Handler
        # Pipe Segment
        OutputStyled = """<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600;">""" + str(
            PipeSegment) + """</span></p></body></html>"""
        self.PipeSegment.setText(OutputStyled)
        self.PipeSegment.setStyleSheet(qssFile)

        OutputStyled = """<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600;">""" + str(
            WallOutput) + """</span></p></body></html>"""
        self.WallOutput.setText(OutputStyled)
        self.WallOutput.setStyleSheet(qssFile)

        # Wall Output
        OutputStyled = """<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600;">""" + str(
            WallOutput) + """</span></p></body></html>"""
        self.WallOutput.setText(OutputStyled)
        self.WallOutput.setStyleSheet(qssFile)

        # Nominal Wall Output
        OutputStyled = """<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600;">""" + str(
            NomWallOutput) + """</span></p></body></html>"""
        self.NomWallOutput.setText(OutputStyled)
        self.NomWallOutput.setStyleSheet(qssFile)

        # Required Wall Output
        OutputStyled = """<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600;">""" + str(
            ReqWallOutput) + """</span></p></body></html>"""
        self.ReqWallOutput.setText(OutputStyled)
        self.ReqWallOutput.setStyleSheet(qssFile)

        # Corrosion Depth Output
        OutputStyled = """<html><head/><body><p align="center"><span style=" font-size:10pt; font-weight:600;">""" + str(
            CorDepthOutput) + """</span></p></body></html>"""
        self.CorDepthOutput.setText(OutputStyled)
        self.CorDepthOutput.setStyleSheet(qssFile)

    @pyqtSlot()
    def goHome(self):
        self.switch_window.emit("HOWT")

    @pyqtSlot()
    def sendDataInputIron(self, PipeSegment, ObjectClass, NPS, ClassNumber, DesignPressure, CorrAllo, UTResult, SMYS, WallOutput, NomWallOutput, ReqWallOutput, CorDepthOutput):
        self.PipeSegment = PipeSegment
        self.ObjectClass = ObjectClass
        self.Grade = ClassNumber
        self.NPS = NPS
        self.DesignPressure = DesignPressure
        self.CorrAllo = CorrAllo
        self.UTResult = UTResult
        self.SMYS = SMYS
        self.NomWallThick = NomWallOutput
        self.MinWallThick = ReqWallOutput
        self.CorrDepth = CorDepthOutput
        self.WallThick = WallOutput

    @pyqtSlot()
    def sendDataInputSteel(self, PipeSegment, FluidType, Location, ObjectClass, Specification, Grade, NPS, SCH, DesignPressure,
                      DesignTemp, CorrAllo, ManTol, UTResult, SMYS, WeldJointFact, DesignFact, AlloStressPsi, Td,
                      NomWallOutput, ReqWallOutput, CorDepthOutput, WallOutput):
        self.PipeSegment = PipeSegment
        self.FluidType = FluidType
        self.Location = Location
        self.ObjectClass = ObjectClass
        self.Specification = Specification
        self.Grade = Grade
        self.NPS = NPS
        self.SCH = SCH
        self.DesignPressure = DesignPressure
        self.DesignTemp = DesignTemp
        self.CorrAllo = CorrAllo
        self.ManTol = ManTol
        self.UTResult = UTResult
        self.SMYS = SMYS
        self.WeldJointFact = WeldJointFact
        self.DesignFact = DesignFact
        self.AllowStress = AlloStressPsi
        self.TempDerating = Td
        self.NomWallThick = NomWallOutput
        self.MinWallThick = ReqWallOutput
        self.CorrDepth = CorDepthOutput
        self.WallThick = WallOutput

    @pyqtSlot()
    def printResult(self):
        pr.printThicResult(self.PipeSegment, self.FluidType, self.Location, self.ObjectClass, self.Specification, self.Grade, self.NPS, self.SCH,
                                   self.DesignPressure, self.DesignTemp, self.CorrAllo, self.ManTol, self.UTResult, self.SMYS, self.WeldJointFact, self.DesignFact,
                                   self.AllowStress, self.TempDerating, self.NomWallThick, self.MinWallThick, self.CorrDepth, self.WallThick)
