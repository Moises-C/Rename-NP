from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QDir

class View:
    
    def __init__(self, ui):
        self.ui = ui
    
    def get_directory(self):
        return QFileDialog.getExistingDirectory(self.ui.centralwidget, "Selecciona el directorio de archivos NP.", QDir().homePath() )
        