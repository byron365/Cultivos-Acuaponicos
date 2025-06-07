# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataViewkYNcCV.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_dataView(object):
    def setupUi(self, Main):
        if not Main.objectName():
            Main.setObjectName(u"Main")
        Main.resize(550, 425)
        Main.setMaximumSize(QSize(600, 450))
        Main.setStyleSheet(u"QWidget{\n"
"	border-radius: 10px;\n"
"	padding: 5px;\n"
"	color: \"white\";\n"
"}\n"
"#graphCtn{\n"
"	background-color: #f39c12;\n"
"}\n"
"#widget{\n"
"	background-color: #3498db;\n"
"}\n"
"#widget_2{\n"
"	background-color: #2ecc71;\n"
"}\n"
"\n"
"#widget_3{\n"
"	background-color: #1abc9c;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(Main)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphCtn = QWidget(Main)
        self.graphCtn.setObjectName(u"graphCtn")
        self.verticalLayout_3 = QVBoxLayout(self.graphCtn)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.Title = QLabel(self.graphCtn)
        self.Title.setObjectName(u"Title")
        self.Title.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setPointSize(22)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.Title)

        self.graphView = QWidget(self.graphCtn)
        self.graphView.setObjectName(u"graphView")
        self.graphView.setMaximumSize(QSize(16777215, 200))

        self.verticalLayout_3.addWidget(self.graphView)

        self.horizontalWidget_2 = QWidget(self.graphCtn)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_7 = QWidget(self.horizontalWidget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_5 = QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.maxLb = QLabel(self.widget_7)
        self.maxLb.setObjectName(u"maxLb")
        font2 = QFont()
        font2.setPointSize(13)
        font2.setBold(True)
        self.maxLb.setFont(font2)
        self.maxLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.maxLb)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.horizontalWidget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.promLb = QLabel(self.widget_6)
        self.promLb.setObjectName(u"promLb")
        self.promLb.setFont(font2)
        self.promLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.promLb)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.horizontalWidget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.minLb = QLabel(self.widget_5)
        self.minLb.setObjectName(u"minLb")
        self.minLb.setFont(font2)
        self.minLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.minLb)


        self.horizontalLayout_3.addWidget(self.widget_5)


        self.verticalLayout_3.addWidget(self.horizontalWidget_2)


        self.verticalLayout.addWidget(self.graphCtn)

        self.horizontalWidget = QWidget(Main)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMaximumSize(QSize(600, 100))
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget_2 = QWidget(self.horizontalWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_7 = QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.widget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.medLb = QLabel(self.widget_2)
        self.medLb.setObjectName(u"medLb")
        self.medLb.setFont(font2)
        self.medLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.medLb)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.horizontalWidget)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9)

        self.modLb = QLabel(self.widget_3)
        self.modLb.setObjectName(u"modLb")
        self.modLb.setFont(font2)
        self.modLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.modLb)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget = QWidget(self.horizontalWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_11)

        self.varLb = QLabel(self.widget)
        self.varLb.setObjectName(u"varLb")
        self.varLb.setFont(font2)
        self.varLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.varLb)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout.addWidget(self.horizontalWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Main)

        QMetaObject.connectSlotsByName(Main)
    # setupUi

    def retranslateUi(self, Main):
        Main.setWindowTitle(QCoreApplication.translate("Main", u"Form", None))
        self.Title.setText(QCoreApplication.translate("Main", u"TITLE", None))
        self.label.setText(QCoreApplication.translate("Main", u"MAX", None))
        self.maxLb.setText(QCoreApplication.translate("Main", u"100", None))
        self.label_4.setText(QCoreApplication.translate("Main", u"PROM", None))
        self.promLb.setText(QCoreApplication.translate("Main", u"50", None))
        self.label_5.setText(QCoreApplication.translate("Main", u"MIN", None))
        self.minLb.setText(QCoreApplication.translate("Main", u"0", None))
        self.label_7.setText(QCoreApplication.translate("Main", u"MEDIANA", None))
        self.medLb.setText(QCoreApplication.translate("Main", u"100", None))
        self.label_9.setText(QCoreApplication.translate("Main", u"MODA", None))
        self.modLb.setText(QCoreApplication.translate("Main", u"100", None))
        self.label_11.setText(QCoreApplication.translate("Main", u"VARIANZA", None))
        self.varLb.setText(QCoreApplication.translate("Main", u"100", None))
    # retranslateUi

