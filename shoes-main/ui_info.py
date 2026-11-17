# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
        Form.resize(874, 604)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_image = QLabel(Form)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setMaximumSize(QSize(120, 120))
        self.lbl_image.setScaledContents(True)

        self.gridLayout.addWidget(self.lbl_image, 11, 0, 1, 5)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 9, 0, 1, 1)

        self.lbl_count = QLabel(Form)
        self.lbl_count.setObjectName(u"lbl_count")
        self.lbl_count.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_count, 9, 1, 1, 1)

        self.lbl_size = QLabel(Form)
        self.lbl_size.setObjectName(u"lbl_size")
        self.lbl_size.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_size, 7, 1, 1, 1)

        self.lbl_desc = QLabel(Form)
        self.lbl_desc.setObjectName(u"lbl_desc")
        self.lbl_desc.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_desc, 6, 1, 1, 1)

        self.lbl_sostav = QLabel(Form)
        self.lbl_sostav.setObjectName(u"lbl_sostav")
        self.lbl_sostav.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_sostav, 5, 1, 1, 1)

        self.lbl_price = QLabel(Form)
        self.lbl_price.setObjectName(u"lbl_price")
        self.lbl_price.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.lbl_price.setFont(font1)

        self.gridLayout.addWidget(self.lbl_price, 4, 1, 1, 1)

        self.lbl_category = QLabel(Form)
        self.lbl_category.setObjectName(u"lbl_category")

        self.gridLayout.addWidget(self.lbl_category, 3, 1, 1, 1)

        self.lbl_man = QLabel(Form)
        self.lbl_man.setObjectName(u"lbl_man")

        self.gridLayout.addWidget(self.lbl_man, 2, 1, 1, 1)

        self.lbl_name = QLabel(Form)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 1, 1, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lbl_image.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u0430\u0432:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u044b\u0439 \u0440\u044f\u0434", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u0440\u0430\u0437\u043c\u0435\u0440\u044b", None))
        self.lbl_count.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_size.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_desc.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_sostav.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_price.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_category.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_man.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

