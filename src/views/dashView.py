# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashboardbamXtC.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_FormDash(object):
    def setupUi(self, FormDash):
        if not FormDash.objectName():
            FormDash.setObjectName(u"FormDash")
        FormDash.resize(640, 480)
        FormDash.setMaximumSize(QSize(16777215, 16777215))
        FormDash.setStyleSheet(u"#FormDash{\n"
"	border-radius:10px;\n"
"	background-color: red;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(FormDash)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(FormDash)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setMinimumSize(QSize(600, 500))
        self.scrollArea.setMaximumSize(QSize(680, 1000))
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.ctn = QWidget()
        self.ctn.setObjectName(u"ctn")
        self.ctn.setGeometry(QRect(0, 0, 638, 498))
        self.ctn.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.ctn)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.centralCtn = QVBoxLayout()
        self.centralCtn.setObjectName(u"centralCtn")

        self.verticalLayout_3.addLayout(self.centralCtn)

        self.scrollArea.setWidget(self.ctn)

        self.verticalLayout.addWidget(self.scrollArea, 0, Qt.AlignmentFlag.AlignTop)


        self.retranslateUi(FormDash)

        QMetaObject.connectSlotsByName(FormDash)
    # setupUi

    def retranslateUi(self, FormDash):
        FormDash.setWindowTitle(QCoreApplication.translate("FormDash", u"Dashboard ", None))
    # retranslateUi

