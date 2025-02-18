# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QApplication, QGraphicsView, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStatusBar, QToolButton, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(744, 539)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ImgLable = QLabel(self.centralwidget)
        self.ImgLable.setObjectName(u"ImgLable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ImgLable.sizePolicy().hasHeightForWidth())
        self.ImgLable.setSizePolicy(sizePolicy)
        self.ImgLable.setAlignment(Qt.AlignCenter)
        self.ImgLable.setMargin(2)
        self.ImgLable.setIndent(-1)

        self.horizontalLayout.addWidget(self.ImgLable)

        self.CamLable = QLabel(self.centralwidget)
        self.CamLable.setObjectName(u"CamLable")
        self.CamLable.setAlignment(Qt.AlignCenter)
        self.CamLable.setMargin(2)

        self.horizontalLayout.addWidget(self.CamLable)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.ImgView = QGraphicsView(self.centralwidget)
        self.ImgView.setObjectName(u"ImgView")

        self.horizontalLayout_2.addWidget(self.ImgView)

        self.CamView = QGraphicsView(self.centralwidget)
        self.CamView.setObjectName(u"CamView")

        self.horizontalLayout_2.addWidget(self.CamView)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Settings = QToolButton(self.centralwidget)
        self.Settings.setObjectName(u"Settings")

        self.horizontalLayout_4.addWidget(self.Settings)

        self.Label = QLabel(self.centralwidget)
        self.Label.setObjectName(u"Label")
        self.Label.setAlignment(Qt.AlignCenter)
        self.Label.setMargin(10)

        self.horizontalLayout_4.addWidget(self.Label)

        self.More = QToolButton(self.centralwidget)
        self.More.setObjectName(u"More")

        self.horizontalLayout_4.addWidget(self.More)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.LoadBtn = QPushButton(self.centralwidget)
        self.LoadBtn.setObjectName(u"LoadBtn")

        self.horizontalLayout_5.addWidget(self.LoadBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer)

        self.GuideBtn = QPushButton(self.centralwidget)
        self.GuideBtn.setObjectName(u"GuideBtn")

        self.horizontalLayout_5.addWidget(self.GuideBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Sight", None))
        self.ImgLable.setText(QCoreApplication.translate("MainWindow", u"IMG View", None))
        self.CamLable.setText(QCoreApplication.translate("MainWindow", u"CAM View", None))
        self.Settings.setText("")
        self.Label.setText(QCoreApplication.translate("MainWindow", u"Image Classified as : ", None))
        self.More.setText("")
        self.LoadBtn.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.GuideBtn.setText(QCoreApplication.translate("MainWindow", u"Architecture Guide", None))
    # retranslateUi

