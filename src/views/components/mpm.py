# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MpmCIuRxI.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Mmp(object):
    def setupUi(self, Mmp):
        if not Mmp.objectName():
            Mmp.setObjectName(u"Mmp")
        Mmp.resize(750, 171)
        font = QFont()
        font.setPointSize(16)
        Mmp.setFont(font)
        Mmp.setStyleSheet(u"QLabel{\n"
"	color:\"white\";\n"
"}\n"
"QWidget{\n"
"	border-radius: 10px;\n"
"	margin-top: 5px;\n"
"	margin-bottom: 5px;\n"
"}\n"
"#Mmp{\n"
"	background-color: \"white\";\n"
"	margin-right: 10px;\n"
"}\n"
"#Max{\n"
"	background-color: \"#1abc9c\";\n"
"	margin-right: 10px;\n"
"	margin-left: 10px;\n"
"}\n"
"#Min{\n"
"	background-color: \"#2ecc71\";\n"
"}\n"
"#Prom{\n"
"	background-color: \"#3498db\";\n"
"	margin-right: 10px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Mmp)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(Mmp)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.MaxCtn = QVBoxLayout()
        self.MaxCtn.setObjectName(u"MaxCtn")
        self.Max = QWidget(self.horizontalWidget)
        self.Max.setObjectName(u"Max")
        self.verticalLayout = QVBoxLayout(self.Max)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.maxTLb = QLabel(self.Max)
        self.maxTLb.setObjectName(u"maxTLb")
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.maxTLb.setFont(font1)
        self.maxTLb.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.maxTLb.setStyleSheet(u"")
        self.maxTLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.maxTLb)

        self.maxVLB = QLabel(self.Max)
        self.maxVLB.setObjectName(u"maxVLB")
        font2 = QFont()
        font2.setPointSize(48)
        font2.setBold(True)
        self.maxVLB.setFont(font2)
        self.maxVLB.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.maxVLB)


        self.MaxCtn.addWidget(self.Max)


        self.horizontalLayout_2.addLayout(self.MaxCtn)

        self.PromCtn = QVBoxLayout()
        self.PromCtn.setObjectName(u"PromCtn")
        self.Prom = QWidget(self.horizontalWidget)
        self.Prom.setObjectName(u"Prom")
        self.verticalLayout_2 = QVBoxLayout(self.Prom)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.promTLb = QLabel(self.Prom)
        self.promTLb.setObjectName(u"promTLb")
        self.promTLb.setFont(font1)
        self.promTLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.promTLb)

        self.promVLB = QLabel(self.Prom)
        self.promVLB.setObjectName(u"promVLB")
        self.promVLB.setFont(font2)
        self.promVLB.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.promVLB)


        self.PromCtn.addWidget(self.Prom)


        self.horizontalLayout_2.addLayout(self.PromCtn)

        self.MinCtn = QVBoxLayout()
        self.MinCtn.setObjectName(u"MinCtn")
        self.Min = QWidget(self.horizontalWidget)
        self.Min.setObjectName(u"Min")
        self.verticalLayout_3 = QVBoxLayout(self.Min)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.minTLb = QLabel(self.Min)
        self.minTLb.setObjectName(u"minTLb")
        self.minTLb.setFont(font1)
        self.minTLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.minTLb)

        self.minVLB = QLabel(self.Min)
        self.minVLB.setObjectName(u"minVLB")
        self.minVLB.setFont(font2)
        self.minVLB.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.minVLB)


        self.MinCtn.addWidget(self.Min)


        self.horizontalLayout_2.addLayout(self.MinCtn)


        self.horizontalLayout.addWidget(self.horizontalWidget)


        self.retranslateUi(Mmp)

        QMetaObject.connectSlotsByName(Mmp)
    # setupUi

    def retranslateUi(self, Mmp):
        Mmp.setWindowTitle(QCoreApplication.translate("Mmp", u"Frame", None))
        self.maxTLb.setText(QCoreApplication.translate("Mmp", u"MAX", None))
        self.maxVLB.setText(QCoreApplication.translate("Mmp", u"100", None))
        self.promTLb.setText(QCoreApplication.translate("Mmp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">PROMEDIO</span></p></body></html>", None))
        self.promVLB.setText(QCoreApplication.translate("Mmp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700; color:#ffffff;\">50</span></p></body></html>", None))
        self.minTLb.setText(QCoreApplication.translate("Mmp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700; color:#ffffff;\">MIN</span></p></body></html>", None))
        self.minVLB.setText(QCoreApplication.translate("Mmp", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:700; color:#ffffff;\">0</span></p></body></html>", None))
    # retranslateUi

