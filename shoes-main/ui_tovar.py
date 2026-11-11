# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tovar.ui'
##
## Created by: Qt User Interface Compiler version 6.12.0
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
        Form.resize(800, 180)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_image = QLabel(Form)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setMinimumSize(QSize(100, 100))
        self.lbl_image.setMaximumSize(QSize(100, 100))
        self.lbl_image.setScaledContents(True)

        self.gridLayout.addWidget(self.lbl_image, 0, 0, 4, 1)

        self.lbl_name = QLabel(Form)
        self.lbl_name.setObjectName(u"lbl_name")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_name.setFont(font)
        self.lbl_name.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_name, 0, 1, 1, 2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.lbl_category = QLabel(Form)
        self.lbl_category.setObjectName(u"lbl_category")

        self.gridLayout.addWidget(self.lbl_category, 1, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)

        self.lbl_count = QLabel(Form)
        self.lbl_count.setObjectName(u"lbl_count")

        self.gridLayout.addWidget(self.lbl_count, 2, 2, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 1, 1, 1)

        self.lbl_sostav = QLabel(Form)
        self.lbl_sostav.setObjectName(u"lbl_sostav")
        self.lbl_sostav.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_sostav, 3, 2, 1, 1)

        self.lbl_price = QLabel(Form)
        self.lbl_price.setObjectName(u"lbl_price")
        self.lbl_price.setMinimumSize(QSize(120, 0))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.lbl_price.setFont(font1)
        self.lbl_price.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.addWidget(self.lbl_price, 0, 3, 4, 1, Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTop)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 3)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        self.lbl_name.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e | \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.lbl_category.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e:", None))
        self.lbl_count.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u0430\u0432:", None))
        self.lbl_sostav.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_price.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        pass
    # retranslateUi

