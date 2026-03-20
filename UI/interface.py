# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfacerKQWPa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    _instance = None
   
    def __new__(cls):
        if Ui_MainWindow._instance is None:
              Ui_MainWindow._instance  = object.__new__(cls)
        return Ui_MainWindow._instance     

    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 279)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(400, 279))
        MainWindow.setMaximumSize(QSize(400, 279))
        icon = QIcon()
        icon.addFile(u"img/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color: #f5f7fb;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_main = QFrame(self.centralwidget)
        self.frame_main.setObjectName(u"frame_main")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_main.sizePolicy().hasHeightForWidth())
        self.frame_main.setSizePolicy(sizePolicy1)
        self.frame_main.setMinimumSize(QSize(0, 0))
        self.frame_main.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: #1565C0;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #0D47A1;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #E0E0E0;\n"
"    color: #9E9E9E;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background-color: #1976D2;\n"
"    color: white;\n"
"    border: none;\n"
"    border-radius: 4px;\n"
"    padding: 8px 18px;\n"
"    font-weight: 600;\n"
"	font-family: \"Segoe UI\";\n"
"}\n"
"\n"
"QPushButton#search_directory_btn {\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QFrame{\n"
"	border-radius: 6px;\n"
"	background-color: white;\n"
"}\n"
"\n"
"QLabel{\n"
"	font-family: \"Segoe UI\";\n"
"}\n"
"\n"
"Line{\n"
"	background-color: #F7F7F7;\n"
"}\n"
"\n"
"#input_directory{\n"
"border-top-right-radius: None;\n"
"border-bottom-right-radius: None;\n"
"}\n"
"\n"
"#search_directory_btn{\n"
"border-top-left-radius: None;\n"
"border-bottom-left-radius: None;\n"
"border-top-right-radius: 4px;\n"
"border-bottom-right-radius: 4px;\n"
"}\n"
"\n"
"#frame_main{\n"
"	border: None"
                        ";\n"
"}\n"
"")
        self.frame_main.setFrameShape(QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.frame_main)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.frame_search_custom = QFrame(self.frame_main)
        self.frame_search_custom.setObjectName(u"frame_search_custom")
        sizePolicy1.setHeightForWidth(self.frame_search_custom.sizePolicy().hasHeightForWidth())
        self.frame_search_custom.setSizePolicy(sizePolicy1)
        self.frame_search_custom.setFrameShape(QFrame.NoFrame)
        self.frame_search_custom.setFrameShadow(QFrame.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_search_custom)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.input_directory = QLineEdit(self.frame_search_custom)
        self.input_directory.setObjectName(u"input_directory")
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        self.input_directory.setFont(font1)

        self.horizontalLayout_9.addWidget(self.input_directory)

        self.search_directory_btn = QPushButton(self.frame_search_custom)
        self.search_directory_btn.setObjectName(u"search_directory_btn")
        sizePolicy.setHeightForWidth(self.search_directory_btn.sizePolicy().hasHeightForWidth())
        self.search_directory_btn.setSizePolicy(sizePolicy)
        icon1 = QIcon()
        icon1.addFile(u"img/folder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_directory_btn.setIcon(icon1)
        self.search_directory_btn.setIconSize(QSize(16, 16))

        self.horizontalLayout_9.addWidget(self.search_directory_btn)


        self.verticalLayout.addWidget(self.frame_search_custom)

        self.frame_2 = QFrame(self.frame_main)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Plain)
        self.frame_2.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.verticalLayout_2.addWidget(self.label)

        self.node_origin = QLineEdit(self.frame_2)
        self.node_origin.setObjectName(u"node_origin")

        self.verticalLayout_2.addWidget(self.node_origin)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout_2.addWidget(self.label_2)

        self.node_destin = QLineEdit(self.frame_2)
        self.node_destin.setObjectName(u"node_destin")

        self.verticalLayout_2.addWidget(self.node_destin)


        self.verticalLayout.addWidget(self.frame_2)

        self.generate_files = QPushButton(self.frame_main)
        self.generate_files.setObjectName(u"generate_files")

        self.verticalLayout.addWidget(self.generate_files)


        self.horizontalLayout.addWidget(self.frame_main)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Renombrado Archivos NP", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Directorio:", None))
        self.input_directory.setPlaceholderText("")
#if QT_CONFIG(tooltip)
        self.search_directory_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Iniciar b\u00fasqueda", None))
#endif // QT_CONFIG(tooltip)
        self.search_directory_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Etiqueta Origen", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Etiqueta Destino", None))
        self.generate_files.setText(QCoreApplication.translate("MainWindow", u"Generar", None))
    # retranslateUi

