from PyQt5.QtWidgets import QMessageBox, QFileDialog
from PyQt5.QtCore import QDir
from View.Progressbar import LoadingOverlay

class View:
    
    def __init__(self, ui):
        self.ui = ui
        self.progressbar = LoadingOverlay(self.ui.centralwidget)

    def get_directory(self):
        return QFileDialog.getExistingDirectory(self.ui.centralwidget, "Selecciona el directorio de archivos NP.", QDir().homePath() )
    
    def alert_succesfull(self):
        QMessageBox.information(self.ui.centralwidget, "Finalizado", "Se concreto correctamente el renombrado de archivos.")
    
    def alert_unsuccessfull(self,e):
        QMessageBox.critical(self.ui.centralwidget, "Ha ocurrido un problema", f"{e}")
        
    def alert_empty_fields(self):
        QMessageBox.warning(self.ui.centralwidget, "Campos nulos", "Asegurate de haber llenado todos los campos.")
    
    def show_progress(self):
        self.progressbar.show()
    
    def hide_progress(self):
        self.progressbar.hide()