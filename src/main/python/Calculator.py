from fbs_runtime.application_context.PyQt5 import ApplicationContext
import pandas as pd

def calculateCath(CPResult):
    result = float(CPResult)
    if (result <= -1.1):
        respons = "ANODE POTENTIAL"
    elif (result <= -0.95):
        respons = "VERY GOOD"
    elif (result <= -0.85):
        respons = "GOOD"
    elif (result <= -0.8):
        respons = "OKAY"
    elif (result <= -0.7):
        respons = "BAD"
    elif (result >= -0.7):
        respons = "NO PROTECTION"
    return respons


def calculateIT(PipeSegment, Class, NPS, ClassNumber, DesignPressure, CorrAllo, UTResult):
    # Read Datasheet
    IronPress = pd.read_csv(ApplicationContext().get_resource("""datasheet\Iron\IronPress.csv"""), sep=';')
    IronThick = pd.read_csv(ApplicationContext().get_resource("""datasheet\Iron\IronThick.csv"""), sep=';')

    # Normalize NaN with Zero
    IronPress = IronPress.fillna(0)
    IronThick = IronThick.fillna(0)

    # Find Outside Diameter
    if (Class == "Pressure"):
        rowSelect = IronPress.loc[IronPress['PipeSize'] == str(NPS)]
    elif (Class == "Thickness"):
        rowSelect = IronThick.loc[IronThick['PipeSize'] == str(NPS)]

    OutDia = float(rowSelect['OutDia'])

    # Specified Min. Yield Strength
    SMYS = 42000

    # Design Pressure Wall Thickness 
    TMin = float((float(DesignPressure) * OutDia) / (2 * float(SMYS)))

    # Nominal Wall Thickness (NPS)
    TN = TMin + float(CorrAllo)

    # Nom. Wall Thickness (Calc)
    if (Class == "Pressure"):
        rowSelect = IronPress.loc[IronPress['PipeSize'] == str(NPS)]
    elif (Class == "Thickness"):
        rowSelect = IronThick.loc[IronThick['PipeSize'] == str(NPS)]

    column = str(ClassNumber)
    columnSelect = rowSelect[column]

    # Find the Output
    NomWallOutput = float(columnSelect)
    ReqWallOutput = TN
    CorDepthOutput = NomWallOutput - float(UTResult)

    # Find the Status
    if (float(UTResult) <= 0.2 * float(ReqWallOutput)):
        WallOutput = "NEED REPLACEMENT"
    elif (float(UTResult) <= 0.4 * float(ReqWallOutput)):
        WallOutput = "BAD"
    elif (float(UTResult) <= 0.6 * float(ReqWallOutput)):
        WallOutput = "OKAY"
    elif (float(UTResult) <= 0.8 * float(ReqWallOutput)):
        WallOutput = "GOOD"
    elif (float(UTResult) >= 0.8 * float(ReqWallOutput)):
        WallOutput = "VERY GOOD"

    # Normalize Output 3 Decimals
    NomWallOutput = str(f"{(round(NomWallOutput, 3)):.3f}").replace('.', ',')
    ReqWallOutput = str(f"{(round(ReqWallOutput, 3)):.3f}").replace('.', ',')
    CorDepthOutput = str(f"{(round(CorDepthOutput, 3)):.3f}").replace('.', ',')

    return SMYS, WallOutput, NomWallOutput, ReqWallOutput, CorDepthOutput


def calculateST(PipeSegment, FluidType, Location, ObjectClass, Specification, Grade, NPS, SCH, DesignPressure, DesignTemp, CorrAllo, ManTol, UTResult):
    # Read Datasheet
    SteelPress = pd.read_csv(ApplicationContext().get_resource("""datasheet\Steel\SteelPressure.csv"""), sep='\t')
    SteelNPS = pd.read_csv(ApplicationContext().get_resource("""datasheet\Steel\SteelNPS.csv"""), sep='\t')
    SteelPress = SteelPress.fillna(0)
    SteelNPS = SteelNPS.fillna(0)

    # Find Specified Min. Yield Strength
    rowSelect = SteelPress[(SteelPress['Class'] == str(ObjectClass)) & (SteelPress['Spec'] == str(Specification)) & (SteelPress['Grade'] == str(Grade))]
    SMYS = float(rowSelect['SMYSPsi'])

    # Weld Joint Factor
    WeldJointFact = float(rowSelect['WeldJoint'])

    # Design Factor
    if(str(Location) == "Class 1"):
        DesignFact = 0.72
    elif(str(Location) == "Class 2"):
        DesignFact = 0.6
    elif(str(Location) == "Class 3"):
        DesignFact = 0.5
    elif(str(Location) == "Class 4"):
        DesignFact = 0.4
    elif(str(Location) == "Offshore"):
        DesignFact = 0.72

    # Allowable Stress Psi
    AlloStressPsi = float(SMYS * WeldJointFact * DesignFact)

    # Find Outside Diameter (Inch)
    OutDiaRow = SteelNPS.loc[SteelNPS['NPS'] == str(NPS)]
    OutDiaInch = str(OutDiaRow.iloc[0]['ODInch']).replace(',', '.')
    OutDiaInch = float(OutDiaInch)

    # Design Pressure Wall Thickness
    TMin = (float(DesignPressure) * OutDiaInch) / (2 * AlloStressPsi)

    # Nominal Wall Thickness (Top)
    TnTop = TMin + float(CorrAllo)

    # Temperature Derating
    Td = float((( -0.033 / 50.0) * ((float(DesignTemp) - 250.0))) + 1.0)

    # Nominal Wall Thickness (Bot)
    TnBot = (float(DesignPressure) * OutDiaInch) / (2.0 * AlloStressPsi * Td)

    # Requirement Wall Thickness
    TReq = TnBot * (100.0 / (100.0 - float(ManTol))) + float(CorrAllo)

    # Nominal Wall Thicknes (Calc)
    column = str(SCH)
    columnSelect = str(OutDiaRow.iloc[0][column]).replace(',', '.')

    # Convert to Inch
    TnCalc = float(columnSelect) / 25.4
    NomWallOutput = TnCalc

    # Get the ReqWall Output
    if(FluidType == "Gas"):
        ReqWallOutput = TnTop
    elif(FluidType == "Liquid"):
        ReqWallOutput = TReq

    # Corrosion Depth
    CorDepthOutput = NomWallOutput - float(UTResult)

    # Find the Status
    if (float(UTResult) <= 0.2 * float(ReqWallOutput)):
        WallOutput = "NEED REPLACEMENT"
    elif (float(UTResult) <= 0.4 * float(ReqWallOutput)):
        WallOutput = "BAD"
    elif (float(UTResult) <= 0.6 * float(ReqWallOutput)):
        WallOutput = "OKAY"
    elif (float(UTResult) <= 0.8 * float(ReqWallOutput)):
        WallOutput = "GOOD"
    elif (float(UTResult) >= 0.8 * float(ReqWallOutput)):
        WallOutput = "VERY GOOD"

    # Normalize Output 3 Decimals
    NomWallOutput = str(f"{(round(NomWallOutput, 3)):.3f}").replace('.', ',')
    ReqWallOutput = str(f"{(round(ReqWallOutput, 3)):.3f}").replace('.', ',')
    CorDepthOutput = str(f"{(round(CorDepthOutput, 3)):.3f}").replace('.', ',')

    return SMYS, WeldJointFact, DesignFact, AlloStressPsi, Td, NomWallOutput, ReqWallOutput, CorDepthOutput, WallOutput
