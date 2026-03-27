from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QMetaObject, Qt, Q_ARG, pyqtSlot
from UI.interface import Ui_MainWindow
from View.ViewApp import View
from Model.Rename import Rename
from Repository.ConsultRepository import ConsultRepository
from Model.ApiRest import API
import threading

class NPController(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view = View(self.ui)
        self.api = API()
        self.consult = ConsultRepository()
        self.signals()

    def get_references(self):
        self.api.get("clarion")

    def signals(self):
        self.ui.search_directory_btn.clicked.connect(self.set_directory)
        self.ui.generate_files.clicked.connect(self.rename_files)
        
    def set_directory(self):
        self.ui.input_directory.setText(self.view.get_directory())
    
    def rename_files(self):
        root = self.ui.input_directory.text()
        node_origin = self.ui.node_origin.text()
        node_destin = self.ui.node_destin.text()
        self.view.show_progress()
        def work():
            if len(root) > 0 and len(node_origin) > 0 and len(node_destin):
                try:
                    self.get_references()
                    self.rename = Rename(root, node_origin, node_destin)
                    self.rename.rename2(self.api.get_response()["references"])
                    if self.rename.get_count():
                        QMetaObject.invokeMethod(self, "alert_successfull", Qt.QueuedConnection, Q_ARG(object, self.rename.get_count())) 
                    else:
                        QMetaObject.invokeMethod(self, "zero_match", Qt.QueuedConnection) 
                except BaseException as e:
                    self.view.hide_progress()
                    self.view.alert_unsuccessfull(e)
            else:
                self.view.alert_unsuccessfull(e)
            QMetaObject.invokeMethod(self, "hide_progress", Qt.QueuedConnection)    
        threading.Thread(target=work, daemon=True).start()
    
    @pyqtSlot(object)
    def alert_successfull(self, count):
        self.view.alert_succesfull(count)

    @pyqtSlot()
    def hide_progress(self):
        self.view.hide_progress()

    @pyqtSlot()
    def zero_match(self):
        self.view.zero_match()