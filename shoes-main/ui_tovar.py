# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tovar.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(599, 104)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setFamilies([u"Calibri"])
        font.setBold(True)
        font.setItalic(True)
        self.label_3.setFont(font)

        self.gridLayout_2.addWidget(self.label_3, 2, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout_2.addWidget(self.label_4, 3, 1, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout_2.addWidget(self.label_5, 4, 1, 1, 1)

        self.lbl_name = QLabel(Form)
        self.lbl_name.setObjectName(u"lbl_name")
        font1 = QFont()
        font1.setFamilies([u"Calibri"])
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setItalic(True)
        self.lbl_name.setFont(font1)

        self.gridLayout_2.addWidget(self.lbl_name, 1, 1, 1, 3, Qt.AlignmentFlag.AlignHCenter)

        self.lbl_image = QLabel(Form)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setMaximumSize(QSize(100, 100))
        self.lbl_image.setScaledContents(True)

        self.gridLayout_2.addWidget(self.lbl_image, 2, 0, 3, 1)

        self.lbl_price = QLabel(Form)
        self.lbl_price.setObjectName(u"lbl_price")

        self.gridLayout_2.addWidget(self.lbl_price, 2, 4, 3, 1)

        self.lbl_count = QLabel(Form)
        self.lbl_count.setObjectName(u"lbl_count")
        self.lbl_count.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lbl_count, 3, 2, 1, 2)

        self.lbl_category = QLabel(Form)
        self.lbl_category.setObjectName(u"lbl_category")
        self.lbl_category.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lbl_category, 2, 2, 1, 2)

        self.lbl_sostav = QLabel(Form)
        self.lbl_sostav.setObjectName(u"lbl_sostav")
        self.lbl_sostav.setWordWrap(True)

        self.gridLayout_2.addWidget(self.lbl_sostav, 4, 2, 1, 2)

        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 3)
        self.gridLayout_2.setColumnStretch(4, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u0430\u0432", None))
        self.lbl_name.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e  |  \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.lbl_image.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_price.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_count.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_category.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_sostav.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

