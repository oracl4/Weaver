from PyQt5.QtWidgets import *

import views.MainWindow as MW
import views.IronCathWindow as ICW
import views.SteelCathWindow as SCW
import views.IronThicWindow as ITW
import views.SteelThicWindow as STW
import views.WallCathResult as WCR
import views.WallThicResult as WTR

import Calculator as calc
import re

class Controller():
    def __init__(self):
        pass

    def showPopup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Error")
        msg.setText("Please Enter the Right Input!")
        x = msg.exec_()

    def show_MainWindow(self):
        self._MainWindow = MW.MainWindow()
        self._MainWindow.switch_window.connect(self.change_InputWindows)
        self._MainWindow.show()

    def change_InputWindows(self, text):
        if(text == "ICW"):
            self._ICWWindow = ICW.IronCathWindowLay()
            self._ICWWindow.switch_window.connect(self.change_OutputWindows)
            self._MainWindow.close()
            self._ICWWindow.show()

        elif(text == "SCW"):
            self._SCWWindow = SCW.SteelCathWindowLay()
            self._SCWWindow.switch_window.connect(self.change_OutputWindows)
            self._MainWindow.close()
            self._SCWWindow.show()

        elif(text == "ITW"):
            self._ITWWindow = ITW.IronThicWindowLay()
            self._ITWWindow.switch_window.connect(self.change_OutputWindows)
            self._MainWindow.close()
            self._ITWWindow.show()

        elif(text == "STW"):
            self._STWWindow = STW.SteelThicWindowLay()
            self._STWWindow.switch_window.connect(self.change_OutputWindows)
            self._MainWindow.close()
            self._STWWindow.show()

    def change_OutputWindows(self, text):
        # Home Button
        if(text == "HICW"):
            self._ICWWindow.close()
            self.show_MainWindow()

        elif(text == "HSCW"):
            self._SCWWindow.close()
            self.show_MainWindow()

        elif(text == "HITW"):
            self._ITWWindow.close()
            self.show_MainWindow()

        elif(text == "HSTW"):
            self._STWWindow.close()
            self.show_MainWindow()

        # Calculate Button
        elif(text == "OICW"):
            # Get Input
            PipeSegment = self._ICWWindow.PipeSegment.text()
            PipeSegment = PipeSegment.replace(',', '.')

            CPResult = self._ICWWindow.CPResult.text()
            CPResult = CPResult.replace(',', '.')

            # Check Input
            if( (re.match('.', PipeSegment) == None) or
                (re.match('^-?[0-9]\d*(\.\d+)?$', CPResult) == None) ):
                self.showPopup()
            else:
                # Calculate
                CathOutput = calc.calculateCath(CPResult)
                self._OWCath = WCR.WallCathWindowLay(PipeSegment, CathOutput)
                self._OWCath.sendInput(PipeSegment, CPResult)
                self._OWCath.switch_window.connect(self.change_FinalWindows)
                self._ICWWindow.close()
                self._OWCath.show()

        elif(text == "OSCW"):
            # Get Input
            PipeSegment = self._SCWWindow.PipeSegment.text()
            PipeSegment = PipeSegment.replace(',', '.')

            CPResult = self._SCWWindow.CPResult.text()
            CPResult = CPResult.replace(',', '.')

            # Check Input
            if( (re.match('.', PipeSegment) == None) or
                (re.match('^-?[0-9]\d*(\.\d+)?$', CPResult) == None) ):
                self.showPopup()
            else:
                # Calculate
                CathOutput = calc.calculateCath(CPResult)
                self._OWCath = WCR.WallCathWindowLay(PipeSegment, CathOutput)
                self._OWCath.sendInput(PipeSegment, CPResult)
                self._OWCath.switch_window.connect(self.change_FinalWindows)
                self._SCWWindow.close()
                self._OWCath.show()

        elif(text == "OITW"):
            # Get Input
            PipeSegment = self._ITWWindow.PipeSegment.text()
            PipeSegment = PipeSegment.replace(',', '.')

            ObjectClass = self._ITWWindow.ObjectClass.currentText()

            NPS = self._ITWWindow.NPS.currentText()

            ClassNumber = self._ITWWindow.ClassNumber.currentText()

            DesignPressure = self._ITWWindow.DesignPressure.text()
            DesignPressure = DesignPressure.replace(',', '.')

            CorrAllo = self._ITWWindow.CorrAllo.text()
            CorrAllo = CorrAllo.replace(',', '.')

            UTResult = self._ITWWindow.UTResult.text()
            UTResult = UTResult.replace(',', '.')

            # Check Input
            if( (re.match('.', PipeSegment) == None) or
                (re.match('.', DesignPressure) == None) or
                (re.match('.', CorrAllo) == None) or
                (re.match('.', UTResult) == None) ):
                self.showPopup()
            else:
                # Calculate
                SMYS, WallOutput, NomWallOutput, ReqWallOutput, CorDepthOutput = calc.calculateIT(PipeSegment, ObjectClass, NPS, ClassNumber, DesignPressure, CorrAllo, UTResult)
                self._OWThic = WTR.WallThicWindowLay(PipeSegment, WallOutput, NomWallOutput, ReqWallOutput,
                                                     CorDepthOutput)
                self._OWThic.sendDataInputIron(PipeSegment, ObjectClass, NPS, ClassNumber, DesignPressure, CorrAllo,
                                               UTResult, SMYS, WallOutput, NomWallOutput, ReqWallOutput, CorDepthOutput)
                self._OWThic.switch_window.connect(self.change_FinalWindows)
                self._ITWWindow.close()
                self._OWThic.show()

        elif(text == "OSTW"):
            # Get Input
            PipeSegment = self._STWWindow.PipeSegment.text()
            PipeSegment = PipeSegment.replace(',', '.')

            FluidType = self._STWWindow.FluidType.currentText()

            Location = self._STWWindow.Location.currentText()

            ObjectClass = self._STWWindow.ObjectClass.currentText()

            Specification = self._STWWindow.Specification.currentText()

            Grade = self._STWWindow.Grade.currentText()

            NPS = self._STWWindow.NPS.currentText()

            SCH = self._STWWindow.SCH.currentText()

            DesignPressure = self._STWWindow.DesignPressure.text()
            DesignPressure = DesignPressure.replace(',', '.')

            DesignTemp = self._STWWindow.DesignTemp.text()
            DesignTemp = DesignTemp.replace(',', '.')

            CorrAllo = self._STWWindow.CorrAllo.text()
            CorrAllo = CorrAllo.replace(',', '.')

            ManTol = self._STWWindow.ManTol.text()
            ManTol = ManTol.replace(',', '.')

            UTResult = self._STWWindow.UTResult.text()
            UTResult = UTResult.replace(',', '.')

            # Check Input
            if( (re.match('.', PipeSegment) == None) or
                (re.match('.', ObjectClass) == None) or
                (re.match('.', Specification) == None) or
                (re.match('.', Grade) == None) or
                (re.match('.', DesignPressure) == None) or
                (re.match('.', DesignTemp) == None) or
                (re.match('.', CorrAllo) == None) or
                (re.match('.', ManTol) == None) or
                (re.match('.', UTResult) == None) ):
                self.showPopup()
            else:
                # Calculate
                SMYS, WeldJointFact, DesignFact, AlloStressPsi, Td, NomWallOutput, ReqWallOutput, CorDepthOutput, WallOutput = calc.calculateST(PipeSegment, FluidType, Location, ObjectClass, Specification, Grade, NPS, SCH, DesignPressure, DesignTemp, CorrAllo, ManTol, UTResult)
                self._OWThic = WTR.WallThicWindowLay(PipeSegment, WallOutput, NomWallOutput, ReqWallOutput, CorDepthOutput)
                self._OWThic.sendDataInputSteel(PipeSegment, FluidType, Location, ObjectClass, Specification, Grade, NPS, SCH, DesignPressure,
                      DesignTemp, CorrAllo, ManTol, UTResult, SMYS, WeldJointFact, DesignFact, AlloStressPsi, Td,
                      NomWallOutput, ReqWallOutput, CorDepthOutput, WallOutput)
                self._OWThic.switch_window.connect(self.change_FinalWindows)
                self._STWWindow.close()
                self._OWThic.show()

    def change_FinalWindows(self, text):
        if(text == "HOWC"):
            self._OWCath.close()
            self.show_MainWindow()

        elif(text == "HOWT"):
            self._OWThic.close()
            self.show_MainWindow()