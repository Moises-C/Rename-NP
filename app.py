from PyQt5.QtWidgets import QApplication
from Controller.NPController import NPController
import qdarktheme
import sys


if __name__ == "__main__":
    qdarktheme.enable_hi_dpi()
    app = QApplication(sys.argv)
    qdarktheme.setup_theme("light")
    np = NPController()
    np.show()
    app.exec_()