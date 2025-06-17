# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataViewBZMciS.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from src.resources import resources_rc

class Ui_DataView(object):
    def setupUi(self, DataView):
        if not DataView.objectName():
            DataView.setObjectName(u"DataView")
        DataView.resize(550, 500)
        DataView.setMinimumSize(QSize(0, 500))
        DataView.setMaximumSize(QSize(600, 500))
        DataView.setStyleSheet(u"#Main{\n"
"	background-color: rgba(0,0,0,0);\n"
"}\n"
"QWidget, #graphView{\n"
"	border-radius: 10px;\n"
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
"}\n"
"QPushButton{\n"
"	background-color: #e67e22;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(DataView)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.allCtn = QWidget(DataView)
        self.allCtn.setObjectName(u"allCtn")
        self.verticalLayout = QVBoxLayout(self.allCtn)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.graphCtn = QWidget(self.allCtn)
        self.graphCtn.setObjectName(u"graphCtn")
        self.verticalLayout_3 = QVBoxLayout(self.graphCtn)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalWidget = QWidget(self.graphCtn)
        self.horizontalWidget.setObjectName(u"horizontalWidget")
        self.horizontalWidget.setMinimumSize(QSize(0, 40))
        self.horizontalWidget.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.minDateBtn = QPushButton(self.horizontalWidget)
        self.minDateBtn.setObjectName(u"minDateBtn")
        self.minDateBtn.setMaximumSize(QSize(50, 50))
        self.minDateBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icon/aL.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.minDateBtn.setIcon(icon)
        self.minDateBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.minDateBtn)

        self.Title = QLabel(self.horizontalWidget)
        self.Title.setObjectName(u"Title")
        self.Title.setMinimumSize(QSize(100, 0))
        self.Title.setMaximumSize(QSize(300, 35))
        font = QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.Title.setFont(font)
        self.Title.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.Title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_2.addWidget(self.Title)

        self.maxDateBtn = QPushButton(self.horizontalWidget)
        self.maxDateBtn.setObjectName(u"maxDateBtn")
        self.maxDateBtn.setMaximumSize(QSize(50, 50))
        self.maxDateBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icon/aR.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.maxDateBtn.setIcon(icon1)
        self.maxDateBtn.setIconSize(QSize(22, 22))

        self.horizontalLayout_2.addWidget(self.maxDateBtn)


        self.verticalLayout_3.addWidget(self.horizontalWidget)

        self.graphView = QVBoxLayout()
        self.graphView.setSpacing(0)
        self.graphView.setObjectName(u"graphView")

        self.verticalLayout_3.addLayout(self.graphView)

        self.horizontalWidget_2 = QWidget(self.graphCtn)
        self.horizontalWidget_2.setObjectName(u"horizontalWidget_2")
        self.horizontalWidget_2.setMaximumSize(QSize(16777215, 65))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.horizontalWidget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_5 = QVBoxLayout(self.widget_7)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.widget_7)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label)

        self.maxLb = QLabel(self.widget_7)
        self.maxLb.setObjectName(u"maxLb")
        self.maxLb.setMaximumSize(QSize(16777215, 30))
        self.maxLb.setFont(font1)
        self.maxLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.maxLb)


        self.horizontalLayout_3.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.horizontalWidget_2)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_4 = QVBoxLayout(self.widget_6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget_6)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 30))
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_4)

        self.promLb = QLabel(self.widget_6)
        self.promLb.setObjectName(u"promLb")
        self.promLb.setMaximumSize(QSize(16777215, 30))
        self.promLb.setFont(font1)
        self.promLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.promLb)


        self.horizontalLayout_3.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.horizontalWidget_2)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.widget_5)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_5)

        self.minLb = QLabel(self.widget_5)
        self.minLb.setObjectName(u"minLb")
        self.minLb.setMaximumSize(QSize(16777215, 30))
        self.minLb.setFont(font1)
        self.minLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.minLb)


        self.horizontalLayout_3.addWidget(self.widget_5)


        self.verticalLayout_3.addWidget(self.horizontalWidget_2)


        self.verticalLayout.addWidget(self.graphCtn)

        self.horizontalWidget1 = QWidget(self.allCtn)
        self.horizontalWidget1.setObjectName(u"horizontalWidget1")
        self.horizontalWidget1.setMaximumSize(QSize(600, 75))
        self.horizontalLayout = QHBoxLayout(self.horizontalWidget1)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 10, 0, 0)
        self.widget_2 = QWidget(self.horizontalWidget1)
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
        self.medLb.setFont(font1)
        self.medLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.medLb)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.horizontalWidget1)
        self.widget_3.setObjectName(u"widget_3")
        self.verticalLayout_8 = QVBoxLayout(self.widget_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_9)

        self.modLb = QLabel(self.widget_3)
        self.modLb.setObjectName(u"modLb")
        self.modLb.setFont(font1)
        self.modLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_8.addWidget(self.modLb)


        self.horizontalLayout.addWidget(self.widget_3)

        self.widget = QWidget(self.horizontalWidget1)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_9 = QVBoxLayout(self.widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font2)
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_11)

        self.varLb = QLabel(self.widget)
        self.varLb.setObjectName(u"varLb")
        self.varLb.setFont(font1)
        self.varLb.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.varLb)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout.addWidget(self.horizontalWidget1)


        self.verticalLayout_2.addWidget(self.allCtn)


        self.retranslateUi(DataView)

        QMetaObject.connectSlotsByName(DataView)
    # setupUi

    def retranslateUi(self, DataView):
        DataView.setWindowTitle(QCoreApplication.translate("DataView", u"Form", None))
        self.minDateBtn.setText("")
        self.Title.setText(QCoreApplication.translate("DataView", u"TITLE", None))
        self.maxDateBtn.setText("")
        self.label.setText(QCoreApplication.translate("DataView", u"MAX", None))
        self.maxLb.setText(QCoreApplication.translate("DataView", u"100", None))
        self.label_4.setText(QCoreApplication.translate("DataView", u"PROM", None))
        self.promLb.setText(QCoreApplication.translate("DataView", u"50", None))
        self.label_5.setText(QCoreApplication.translate("DataView", u"MIN", None))
        self.minLb.setText(QCoreApplication.translate("DataView", u"0", None))
        self.label_7.setText(QCoreApplication.translate("DataView", u"MEDIANA", None))
        self.medLb.setText(QCoreApplication.translate("DataView", u"100", None))
        self.label_9.setText(QCoreApplication.translate("DataView", u"MODA", None))
        self.modLb.setText(QCoreApplication.translate("DataView", u"100", None))
        self.label_11.setText(QCoreApplication.translate("DataView", u"VARIANZA", None))
        self.varLb.setText(QCoreApplication.translate("DataView", u"100", None))
    # retranslateUi

