# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'nuevoProyectoWgmRtf.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from src.resources import resources_rc

class Ui_newProyectView(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(750, 600)
        Form.setStyleSheet(u"#centralwidget,#widget{\n"
"	background-image: url(:/Img/fondo_oscuro.png);\n"
"}\n"
"\n"
"#widget{\n"
"	background-color: rgba(0,0,0,0.5);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#label, #label_2, #label_3,#label_4,#label_5,#label_6{\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit, QComboBox, QPushButton{\n"
"	padding: 5px;\n"
"}\n"
"\n"
"\n"
"#dsBtn:diseabled{\n"
"	opacity:0.5;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayoutWidget = QWidget(self.widget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 70, 711, 448))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout.addWidget(self.label_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.nameLE = QLineEdit(self.verticalLayoutWidget)
        self.nameLE.setObjectName(u"nameLE")
        font = QFont()
        font.setPointSize(13)
        self.nameLE.setFont(font)
        self.nameLE.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)

        self.horizontalLayout_4.addWidget(self.nameLE)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label_6.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_6)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_13 = QLabel(self.verticalLayoutWidget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_12.addWidget(self.label_13)

        self.LeTa = QLineEdit(self.verticalLayoutWidget)
        self.LeTa.setObjectName(u"LeTa")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(False)
        self.LeTa.setFont(font2)
        self.LeTa.setStyleSheet(u"")

        self.horizontalLayout_12.addWidget(self.LeTa)

        self.fTaBtn = QPushButton(self.verticalLayoutWidget)
        self.fTaBtn.setObjectName(u"fTaBtn")
        self.fTaBtn.setMinimumSize(QSize(45, 30))
        font3 = QFont()
        font3.setPointSize(13)
        font3.setBold(True)
        self.fTaBtn.setFont(font3)
        self.fTaBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fTaBtn.setAutoFillBackground(False)
        self.fTaBtn.setStyleSheet(u"background-color:rgb(255, 170, 0);")
        icon = QIcon()
        icon.addFile(u":/icon/folder-plus-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.fTaBtn.setIcon(icon)
        self.fTaBtn.setFlat(False)

        self.horizontalLayout_12.addWidget(self.fTaBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_12 = QLabel(self.verticalLayoutWidget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.LeTe = QLineEdit(self.verticalLayoutWidget)
        self.LeTe.setObjectName(u"LeTe")
        self.LeTe.setFont(font2)
        self.LeTe.setStyleSheet(u"")

        self.horizontalLayout_11.addWidget(self.LeTe)

        self.fTeBtn = QPushButton(self.verticalLayoutWidget)
        self.fTeBtn.setObjectName(u"fTeBtn")
        self.fTeBtn.setMinimumSize(QSize(45, 30))
        self.fTeBtn.setFont(font3)
        self.fTeBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fTeBtn.setAutoFillBackground(False)
        self.fTeBtn.setStyleSheet(u"background-color:rgb(255, 170, 0);")
        self.fTeBtn.setIcon(icon)
        self.fTeBtn.setFlat(False)

        self.horizontalLayout_11.addWidget(self.fTeBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_11 = QLabel(self.verticalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.horizontalSpacer = QSpacerItem(70, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer)

        self.LePh = QLineEdit(self.verticalLayoutWidget)
        self.LePh.setObjectName(u"LePh")
        self.LePh.setFont(font2)
        self.LePh.setStyleSheet(u"")

        self.horizontalLayout_10.addWidget(self.LePh)

        self.fPhBtn = QPushButton(self.verticalLayoutWidget)
        self.fPhBtn.setObjectName(u"fPhBtn")
        self.fPhBtn.setMinimumSize(QSize(45, 30))
        self.fPhBtn.setFont(font3)
        self.fPhBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fPhBtn.setAutoFillBackground(False)
        self.fPhBtn.setStyleSheet(u"background-color:rgb(255, 170, 0);")
        self.fPhBtn.setIcon(icon)
        self.fPhBtn.setFlat(False)

        self.horizontalLayout_10.addWidget(self.fPhBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_7 = QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.horizontalSpacer_2 = QSpacerItem(55, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.LePpm = QLineEdit(self.verticalLayoutWidget)
        self.LePpm.setObjectName(u"LePpm")
        self.LePpm.setFont(font2)
        self.LePpm.setStyleSheet(u"")

        self.horizontalLayout_5.addWidget(self.LePpm)

        self.fPpmBtn = QPushButton(self.verticalLayoutWidget)
        self.fPpmBtn.setObjectName(u"fPpmBtn")
        self.fPpmBtn.setMinimumSize(QSize(45, 30))
        self.fPpmBtn.setFont(font3)
        self.fPpmBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fPpmBtn.setAutoFillBackground(False)
        self.fPpmBtn.setStyleSheet(u"background-color:rgb(255, 170, 0);")
        self.fPpmBtn.setIcon(icon)
        self.fPpmBtn.setFlat(False)

        self.horizontalLayout_5.addWidget(self.fPpmBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_8 = QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.LeHum = QLineEdit(self.verticalLayoutWidget)
        self.LeHum.setObjectName(u"LeHum")
        self.LeHum.setFont(font2)
        self.LeHum.setStyleSheet(u"")

        self.horizontalLayout_6.addWidget(self.LeHum)

        self.fHumBtn = QPushButton(self.verticalLayoutWidget)
        self.fHumBtn.setObjectName(u"fHumBtn")
        self.fHumBtn.setMinimumSize(QSize(45, 30))
        self.fHumBtn.setFont(font3)
        self.fHumBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fHumBtn.setAutoFillBackground(False)
        self.fHumBtn.setStyleSheet(u"background-color:rgb(255, 170, 0);")
        self.fHumBtn.setIcon(icon)
        self.fHumBtn.setFlat(False)

        self.horizontalLayout_6.addWidget(self.fHumBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_9 = QLabel(self.verticalLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.horizontalSpacer_4 = QSpacerItem(15, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.LeLuz = QLineEdit(self.verticalLayoutWidget)
        self.LeLuz.setObjectName(u"LeLuz")
        self.LeLuz.setFont(font2)
        self.LeLuz.setStyleSheet(u"")

        self.horizontalLayout_8.addWidget(self.LeLuz)

        self.fLuzBtn = QPushButton(self.verticalLayoutWidget)
        self.fLuzBtn.setObjectName(u"fLuzBtn")
        self.fLuzBtn.setMinimumSize(QSize(45, 30))
        self.fLuzBtn.setFont(font3)
        self.fLuzBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.fLuzBtn.setAutoFillBackground(False)
        self.fLuzBtn.setStyleSheet(u"background-color:rgb(255, 170, 0);")
        self.fLuzBtn.setIcon(icon)
        self.fLuzBtn.setFlat(False)

        self.horizontalLayout_8.addWidget(self.fLuzBtn)


        self.verticalLayout_3.addLayout(self.horizontalLayout_8)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayoutWidget_3 = QWidget(self.widget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(10, 20, 711, 34))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget_3)
        self.label.setObjectName(u"label")
        font4 = QFont()
        font4.setFamilies([u"MS Gothic"])
        font4.setPointSize(24)
        self.label.setFont(font4)

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayoutWidget_3 = QWidget(self.widget)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(10, 530, 711, 46))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_5 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.createDashBtn = QPushButton(self.horizontalLayoutWidget_3)
        self.createDashBtn.setObjectName(u"createDashBtn")
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.createDashBtn.setFont(font5)
        self.createDashBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.createDashBtn.setStyleSheet(u"color: \"white\";\n"
"padding:10px;\n"
"background-color: rgba(46, 204, 113,1.0);")
        icon1 = QIcon()
        icon1.addFile(u":/icon/chart-simple-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.createDashBtn.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.createDashBtn)

        self.horizontalSpacer_6 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Nuevo Proyecto", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Nombre del Proyecto</span></p></body></html>", None))
        self.nameLE.setPlaceholderText(QCoreApplication.translate("Form", u"Ej: Cultivo de Ostras", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Ruta de los archivos .csv</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">Temperatura </span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">Ambiente</span></p></body></html>", None))
        self.LeTa.setText("")
        self.LeTa.setPlaceholderText(QCoreApplication.translate("Form", u"Ej: C:\\Mis arcivos\\TemperaturaAmbiente.csv", None))
        self.fTaBtn.setText("")
        self.label_12.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">Temperatura </span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">Estanque</span></p></body></html>", None))
        self.LeTe.setText("")
        self.LeTe.setPlaceholderText(QCoreApplication.translate("Form", u"Ej: C:\\Mis arcivos\\TemperaturaEstanque.csv", None))
        self.fTeBtn.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">Ph</span></p></body></html>", None))
        self.LePh.setText("")
        self.LePh.setPlaceholderText(QCoreApplication.translate("Form", u"Ej: C:\\Mis arcivos\\Ph.csv", None))
        self.fPhBtn.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">PPM</span></p></body></html>", None))
        self.LePpm.setText("")
        self.LePpm.setPlaceholderText(QCoreApplication.translate("Form", u"Ej: C:\\Mis arcivos\\Ppm.csv", None))
        self.fPpmBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">Humedad</span></p></body></html>", None))
        self.LeHum.setText("")
        self.LeHum.setPlaceholderText(QCoreApplication.translate("Form", u"Ej: C:\\Mis arcivos\\Humedad.csv", None))
        self.fHumBtn.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">Luz </span></p><p align=\"center\"><span style=\" font-size:11pt; font-weight:700; color:#ffffff;\">Ambiental</span></p></body></html>", None))
        self.LeLuz.setText("")
        self.LeLuz.setPlaceholderText(QCoreApplication.translate("Form", u"Ej: C:\\Mis arcivos\\Luz.csv", None))
        self.fLuzBtn.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">NUEVO PROYECTO </span></p></body></html>", None))
        self.createDashBtn.setText(QCoreApplication.translate("Form", u" CREAR PROYECTO", None))
    # retranslateUi

