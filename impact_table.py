from qgis.PyQt.QtWidgets import *
from .impact_table_dialog import Ui_dlgImpacts


class DlgTable(QDialog, Ui_dlgImpacts):
    def __init__(self):
        super(DlgTable, self).__init__()
        self.setupUi(self)
        
        #chamge the second column width make it bigger
        self.tblImpacts.setColumnWidth(1, 325)

