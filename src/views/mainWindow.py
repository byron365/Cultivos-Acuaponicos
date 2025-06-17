# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeZVLOLv.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QMainWindow, QSizePolicy,
    QVBoxLayout, QWidget)
from src.resources import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 481)
        MainWindow.setStyleSheet(u"")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setStyleSheet(u"#centralWidget{\n"
"	background-image:url(:/Img/bg.png);\n"
"}")
        self.horizontalLayout_4 = QHBoxLayout(self.centralWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.centralCtn = QVBoxLayout()
        self.centralCtn.setObjectName(u"centralCtn")

        self.horizontalLayout_4.addLayout(self.centralCtn)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cultivos Acuicolas", None))
    # retranslateUi

