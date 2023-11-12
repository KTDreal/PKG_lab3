# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QPushButton, QSizePolicy,
    QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(1200, 800)
        self.label = QLabel(Widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(290, 50, 171, 211))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label_sharp = QLabel(Widget)
        self.label_sharp.setObjectName(u"label_sharp")
        self.label_sharp.setGeometry(QRect(630, 40, 171, 211))
        sizePolicy.setHeightForWidth(self.label_sharp.sizePolicy().hasHeightForWidth())
        self.label_sharp.setSizePolicy(sizePolicy)
        self.label_adopted = QLabel(Widget)
        self.label_adopted.setObjectName(u"label_adopted")
        self.label_adopted.setGeometry(QRect(950, 50, 171, 211))
        sizePolicy.setHeightForWidth(self.label_adopted.sizePolicy().hasHeightForWidth())
        self.label_adopted.setSizePolicy(sizePolicy)
        self.label_global = QLabel(Widget)
        self.label_global.setObjectName(u"label_global")
        self.label_global.setGeometry(QRect(290, 350, 171, 211))
        sizePolicy.setHeightForWidth(self.label_global.sizePolicy().hasHeightForWidth())
        self.label_global.setSizePolicy(sizePolicy)
        self.label_otsu = QLabel(Widget)
        self.label_otsu.setObjectName(u"label_otsu")
        self.label_otsu.setGeometry(QRect(610, 350, 171, 211))
        sizePolicy.setHeightForWidth(self.label_otsu.sizePolicy().hasHeightForWidth())
        self.label_otsu.setSizePolicy(sizePolicy)
        self.left = QPushButton(Widget)
        self.left.setObjectName(u"left")
        self.left.setGeometry(QRect(370, 690, 80, 31))
        font = QFont()
        font.setPointSize(12)
        self.left.setFont(font)
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(470, 690, 261, 31))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.pushButton_2.setFont(font1)
        self.right = QPushButton(Widget)
        self.right.setObjectName(u"right")
        self.right.setGeometry(QRect(750, 690, 80, 31))
        self.right.setFont(font)
        self.label_image = QLabel(Widget)
        self.label_image.setObjectName(u"label_image")
        self.label_image.setGeometry(QRect(160, 80, 881, 591))
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(370, 740, 461, 31))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(90, 20, 1031, 51))
        font3 = QFont()
        font3.setPointSize(18)
        self.label_3.setFont(font3)

        self.retranslateUi(Widget)
        self.left.clicked.connect(Widget.leftClicked)
        self.right.clicked.connect(Widget.rightClicked)
        self.pushButton_2.clicked.connect(Widget.chooseImg)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label.setText("")
        self.label_sharp.setText("")
        self.label_adopted.setText("")
        self.label_global.setText("")
        self.label_otsu.setText("")
        self.left.setText(QCoreApplication.translate("Widget", u"<<", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Choose image...", None))
        self.right.setText(QCoreApplication.translate("Widget", u">>", None))
        self.label_image.setText(QCoreApplication.translate("Widget", u"Image", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"Original Image", None))
        self.label_3.setText(QCoreApplication.translate("Widget", u"blurredBuilding.png", None))
    # retranslateUi

