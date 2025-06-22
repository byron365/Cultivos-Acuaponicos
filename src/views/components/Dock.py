# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DockwHrwGc.ui'
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
from PySide6.QtWidgets import (QApplication, QDockWidget, QFrame, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
from src.resources import resources_rc

class Ui_DockWidget(object):
    def setupUi(self, DockWidget):
        if not DockWidget.objectName():
            DockWidget.setObjectName(u"DockWidget")
        DockWidget.resize(400, 480)
        DockWidget.setMinimumSize(QSize(400, 480))
        DockWidget.setMaximumSize(QSize(1000, 1000))
        DockWidget.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea|Qt.DockWidgetArea.RightDockWidgetArea)
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.dockWidgetContents.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.DockCtn = QVBoxLayout()
        self.DockCtn.setObjectName(u"DockCtn")
        self.widget = QWidget(self.dockWidgetContents)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setStyleSheet(u"QPushButton{\n"
"	border-radius:10px;\n"
"	background-color: #2980b9;\n"
"	color:white;\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.prevDateBtn = QPushButton(self.widget)
        self.prevDateBtn.setObjectName(u"prevDateBtn")
        self.prevDateBtn.setMinimumSize(QSize(0, 50))
        self.prevDateBtn.setMaximumSize(QSize(50, 50))
        self.prevDateBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icon/aL.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.prevDateBtn.setIcon(icon)
        self.prevDateBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.prevDateBtn)

        self.dateLB = QLabel(self.widget)
        self.dateLB.setObjectName(u"dateLB")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.dateLB.setFont(font)
        self.dateLB.setFrameShape(QFrame.Shape.NoFrame)
        self.dateLB.setFrameShadow(QFrame.Shadow.Plain)
        self.dateLB.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dateLB.setWordWrap(True)

        self.horizontalLayout.addWidget(self.dateLB)

        self.nextDateBtn = QPushButton(self.widget)
        self.nextDateBtn.setObjectName(u"nextDateBtn")
        self.nextDateBtn.setMinimumSize(QSize(0, 50))
        self.nextDateBtn.setMaximumSize(QSize(50, 50))
        self.nextDateBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icon/aR.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.nextDateBtn.setIcon(icon1)
        self.nextDateBtn.setIconSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.nextDateBtn)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.DockCtn.addWidget(self.widget)

        self.scrollArea = QScrollArea(self.dockWidgetContents)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 378, 376))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.scrollItems = QVBoxLayout()
        self.scrollItems.setObjectName(u"scrollItems")

        self.verticalLayout_3.addLayout(self.scrollItems)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.DockCtn.addWidget(self.scrollArea)


        self.verticalLayout_2.addLayout(self.DockCtn)

        DockWidget.setWidget(self.dockWidgetContents)

        self.retranslateUi(DockWidget)

        QMetaObject.connectSlotsByName(DockWidget)
    # setupUi

    def retranslateUi(self, DockWidget):
        DockWidget.setWindowTitle(QCoreApplication.translate("DockWidget", u"DockWidget", None))
        self.prevDateBtn.setText("")
        self.dateLB.setText(QCoreApplication.translate("DockWidget", u"20/05/2025", None))
        self.nextDateBtn.setText("")
    # retranslateUi

