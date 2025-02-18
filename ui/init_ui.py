# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'init.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Init(object):
    def setupUi(self, Init):
        if not Init.objectName():
            Init.setObjectName(u"Init")
        Init.resize(420, 555)
        self.verticalLayout_3 = QVBoxLayout(Init)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.logo = QLabel(Init)
        self.logo.setObjectName(u"logo")
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.logo)

        self.name = QLabel(Init)
        self.name.setObjectName(u"name")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Fira Code"])
        font.setPointSize(24)
        font.setBold(True)
        self.name.setFont(font)
        self.name.setFrameShadow(QFrame.Plain)
        self.name.setTextFormat(Qt.RichText)
        self.name.setScaledContents(True)
        self.name.setAlignment(Qt.AlignCenter)
        self.name.setWordWrap(True)

        self.verticalLayout.addWidget(self.name)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.progressBar = QProgressBar(Init)
        self.progressBar.setObjectName(u"progressBar")
        font1 = QFont()
        font1.setFamilies([u"Droid Sans [1ASC]"])
        self.progressBar.setFont(font1)
        self.progressBar.setValue(24)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.progressStats = QLabel(Init)
        self.progressStats.setObjectName(u"progressStats")
        font2 = QFont()
        font2.setFamilies([u"Source Code Pro Medium"])
        font2.setPointSize(10)
        self.progressStats.setFont(font2)
        self.progressStats.setLayoutDirection(Qt.LeftToRight)
        self.progressStats.setTextFormat(Qt.AutoText)
        self.progressStats.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.verticalLayout_2.addWidget(self.progressStats)

        self.expLabel = QLabel(Init)
        self.expLabel.setObjectName(u"expLabel")
        self.expLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.expLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verLabel = QLabel(Init)
        self.verLabel.setObjectName(u"verLabel")
        font3 = QFont()
        font3.setFamilies([u"URW Gothic"])
        font3.setItalic(True)
        self.verLabel.setFont(font3)
        self.verLabel.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.verLabel)

        self.authLabel = QLabel(Init)
        self.authLabel.setObjectName(u"authLabel")
        self.authLabel.setFont(font3)
        self.authLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout.addWidget(self.authLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.retranslateUi(Init)

        QMetaObject.connectSlotsByName(Init)
    # setupUi

    def retranslateUi(self, Init):
        Init.setWindowTitle(QCoreApplication.translate("Init", u"Sight", None))
        self.logo.setText(QCoreApplication.translate("Init", u"LOGO", None))
        self.name.setText(QCoreApplication.translate("Init", u"Sight", None))
        self.progressStats.setText(QCoreApplication.translate("Init", u"Progress : STATUS", None))
        self.expLabel.setText("")
        self.verLabel.setText(QCoreApplication.translate("Init", u"Version :  Beta", None))
        self.authLabel.setText(QCoreApplication.translate("Init", u"Author : Rishabh Garg", None))
    # retranslateUi

