# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowCtnsDVXgu.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
from src.resources import resources_rc

class Ui_mainCtn(object):
    def setupUi(self, mainCtn):
        if not mainCtn.objectName():
            mainCtn.setObjectName(u"mainCtn")
        mainCtn.resize(640, 480)
        mainCtn.setStyleSheet(u"#widget{\n"
"	background-color: rgba(0,0,0,0.5);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"#widget{\n"
"	\n"
"	\n"
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
"}")
        self.verticalLayout_2 = QVBoxLayout(mainCtn)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget = QWidget(mainCtn)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"margin:20px;")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(380, 86))
        self.label.setMaximumSize(QSize(16777215, 86))
        font = QFont()
        font.setFamilies([u"MS UI Gothic"])
        font.setPointSize(23)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(Qt.ContextMenuPolicy.PreventContextMenu)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"")
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(False)
        font1 = QFont()
        font1.setPointSize(12)
        self.label_2.setFont(font1)
        self.label_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setFrameShape(QFrame.Shape.NoFrame)
        self.label_2.setFrameShadow(QFrame.Shadow.Plain)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2.setWordWrap(True)

        self.verticalLayout.addWidget(self.label_2)

        self.createBtn = QPushButton(self.widget)
        self.createBtn.setObjectName(u"createBtn")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.createBtn.setFont(font2)
        self.createBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.createBtn.setAutoFillBackground(False)
        self.createBtn.setStyleSheet(u"background-color: rgba(46, 204, 113,1.0);\n"
"padding:10px;\n"
"color:\"white\";")
        icon = QIcon()
        icon.addFile(u":/icon/file-circle-plus-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.createBtn.setIcon(icon)
        self.createBtn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.createBtn)

        self.RecentBtn = QPushButton(self.widget)
        self.RecentBtn.setObjectName(u"RecentBtn")
        self.RecentBtn.setFont(font2)
        self.RecentBtn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.RecentBtn.setAutoFillBackground(False)
        self.RecentBtn.setStyleSheet(u"background-color: rgba(52, 152, 219,1.0);\n"
"padding:10px;\n"
"color:\"white\";")
        icon1 = QIcon()
        icon1.addFile(u":/icon/chart-simple-solid.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.RecentBtn.setIcon(icon1)
        self.RecentBtn.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.RecentBtn)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.widget)


        self.retranslateUi(mainCtn)

        QMetaObject.connectSlotsByName(mainCtn)
    # setupUi

    def retranslateUi(self, mainCtn):
        mainCtn.setWindowTitle(QCoreApplication.translate("mainCtn", u"Form", None))
        self.label.setText(QCoreApplication.translate("mainCtn", u"CULTIVOS ACUAPN\u00d3ICOS", None))
        self.label_2.setText(QCoreApplication.translate("mainCtn", u"<html><head/><body><p align=\"center\">Impulsa el futuro de la acuicultura con tecnolog\u00eda que cuida, controla y transforma tu cultivo desde el primer d\u00eda.</p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.createBtn.setToolTip(QCoreApplication.translate("mainCtn", u"<html><head/><body><p align=\"justify\">Abre una nueva ventana en donde se indicar\u00e1n los archivos .csv con los datos para analizar.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.createBtn.setWhatsThis(QCoreApplication.translate("mainCtn", u"<html><head/><body><p>Crear un nuevo proyecto (Dashboard).</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.createBtn.setText(QCoreApplication.translate("mainCtn", u"  CREAR NUEVO PROYECTO", None))
#if QT_CONFIG(tooltip)
        self.RecentBtn.setToolTip(QCoreApplication.translate("mainCtn", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.RecentBtn.setWhatsThis(QCoreApplication.translate("mainCtn", u"<html><head/><body><p>Abrir un proyecto (Dashboard) existente.</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.RecentBtn.setText(QCoreApplication.translate("mainCtn", u"  PROYECTO RECIENTE", None))
    # retranslateUi

