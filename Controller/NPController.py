from PyQt5.QtWidgets import QMainWindow
from UI.interface import Ui_MainWindow
from View.ViewApp import View
from Model.Rename import Rename
import threading

class NPController(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.view = View(self.ui)
        self.signals()

    def signals(self):
        self.ui.search_directory_btn.clicked.connect(self.set_directory)
        self.ui.generate_files.clicked.connect(self.rename_files)
        
    def set_directory(self):
        self.ui.input_directory.setText(self.view.get_directory())
    
    def rename_files(self):
        root = self.ui.input_directory.text()
        node_origin = self.ui.node_origin.text()
        node_destin = self.ui.node_destin.text()
        def work():
            self.view.show_progress()
            if len(root) > 0 and len(node_origin) > 0 and len(node_destin):
                try:
                    self.rename = Rename(root, node_origin, node_destin)
                    self.rename.rename()
                    self.view.alert_succesfull()
                except BaseException as e:
                    self.view.hide_progress()
                    self.view.alert_unsuccessfull(e)
            else:
                self.view.alert_unsuccessfull(e)
            self.view.hide_progress()
        threading.Thread(target=work, daemon=True).start()