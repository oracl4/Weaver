import pdfrw
from fbs_runtime.application_context.PyQt5 import ApplicationContext

def write_fillable_pdf(input_pdf_path, output_pdf_path, data_dict):
    ANNOT_KEY = '/Annots'
    ANNOT_FIELD_KEY = '/T'
    ANNOT_VAL_KEY = '/V'
    ANNOT_RECT_KEY = '/Rect'
    SUBTYPE_KEY = '/Subtype'
    WIDGET_SUBTYPE_KEY = '/Widget'

    template_pdf = pdfrw.PdfReader(input_pdf_path)
    annotations = template_pdf.pages[0][ANNOT_KEY]
    for annotation in annotations:
        if annotation[SUBTYPE_KEY] == WIDGET_SUBTYPE_KEY:
            if annotation[ANNOT_FIELD_KEY]:
                key = annotation[ANNOT_FIELD_KEY][1:-1]
                if key in data_dict.keys():
                    annotation.update(
                        pdfrw.PdfDict(V='{}'.format(data_dict[key]))
                    )
    template_pdf.Root.AcroForm.update(pdfrw.PdfDict(NeedAppearances=pdfrw.PdfObject('true')))
    pdfrw.PdfWriter().write(output_pdf_path, template_pdf)

def printCathodicResult(CPResult, CPStatus):
    data_dict = {
        'CPResult': CPResult,
        'CPStatus': CPStatus
    }

    INVOICE_TEMPLATE_PATH = ApplicationContext().get_resource("""input\cathodic-layout.pdf""")
    INVOICE_OUTPUT_PATH = ApplicationContext().get_resource("""output\cathodic-output.pdf""")
    write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)

def printThicResult(PipeSegment, FluidType, Location, ObjectClass, Specification, Grade, NPS, SCH,
                        DesignPressure, DesignTemp, CorrAllo, ManTol, UTResult, SMYS, WeldJointFact, DesignFact,
                        AllowStress, TempDerating, NomWallThick, MinWallThick, CorrDepth, WallThick
                        ):
    data_dict = {
        'FluidType': FluidType,
        'Location': Location,
        'Class': ObjectClass,
        'Specification': Specification,
        'Grade': Grade,
        'NPS': NPS,
        'SCH': SCH,
        'DesignTemp': DesignTemp,
        'DesignPress': DesignPressure,
        'CorrAllo': CorrAllo,
        'ManTol': ManTol,
        'SMYS': SMYS,
        'WeldJointFact': WeldJointFact,
        'DesignFact': DesignFact,
        'UTResult': UTResult,
        'AllowStress': AllowStress,
        'WeldJointFactX': WeldJointFact,
        'DesignFactX': DesignFact,
        'TempDerating': TempDerating,
        'NomWallThick': NomWallThick,
        'MinWallThick': MinWallThick,
        'CorrDepth': CorrDepth,
        'WallThick': WallThick,
    }

    INVOICE_TEMPLATE_PATH = ApplicationContext().get_resource("""input\wallthick-layout.pdf""")
    INVOICE_OUTPUT_PATH = ApplicationContext().get_resource("""output\wallthick-output.pdf""")
    write_fillable_pdf(INVOICE_TEMPLATE_PATH, INVOICE_OUTPUT_PATH, data_dict)