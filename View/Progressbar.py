import sys
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QColor, QPainter, QPen
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QLabel,
    QVBoxLayout
)

class Spinner(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._angle = 0

        self._timer = QTimer(self)
        self._timer.timeout.connect(self._rotate)
        self._timer.start(16) 
    
    def _rotate(self):
        self._angle = (self._angle + 6) % 360
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen(Qt.white, 4)
        painter.setPen(pen)

        rect = self.rect().adjusted(6, 6, -6, -6)
        painter.drawArc(rect, self._angle * 16, 270 * 16)


class LoadingOverlay(QWidget):
    def __init__(self, parent):
        super().__init__(parent)

        self.setAttribute(Qt.WA_NoSystemBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setGeometry(parent.rect())

        self.background_color = QColor(0, 0, 0, 160)


        self.container = QWidget(self)
        self.container.setAttribute(Qt.WA_TranslucentBackground)
        self.container.setGeometry(self.rect())

        layout = QVBoxLayout(self.container)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(12)
        layout.setAlignment(Qt.AlignCenter)

        self.spinner = Spinner(self.container)
        self.spinner.setFixedSize(64, 64)

        self.label = QLabel("Espere...", self.container)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet(
            "color: white; font-size: 14px; font-weight: 500;"
        )

        layout.addWidget(self.spinner)
        layout.addWidget(self.label)

        self.hide()

    def resizeEvent(self, event):
        self.setGeometry(self.parent().rect())
        self.container.setGeometry(self.rect())
        super().resizeEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.fillRect(self.rect(), self.background_color)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Overlay de carga")
        self.resize(900, 600)

        central = QLabel("Contenido principal de la aplicación")
        central.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(central)

        self.overlay = LoadingOverlay(self.centralWidget())
        self.overlay.show()

    def resizeEvent(self, event):
        self.overlay.resize(self.centralWidget().size())
        super().resizeEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
