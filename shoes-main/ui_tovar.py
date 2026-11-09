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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(783, 338)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.lbl_image = QLabel(self.groupBox)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setGeometry(QRect(30, 150, 49, 16))
        self.lbl_image.setScaledContents(True)

        self.horizontalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)

        self.lbl_name = QLabel(self.groupBox_2)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 0, 1, 1, 1)

        self.lbl_category = QLabel(self.groupBox_2)
        self.lbl_category.setObjectName(u"lbl_category")

        self.gridLayout.addWidget(self.lbl_category, 1, 1, 1, 1)

        self.lbl_count = QLabel(self.groupBox_2)
        self.lbl_count.setObjectName(u"lbl_count")

        self.gridLayout.addWidget(self.lbl_count, 2, 1, 1, 1)

        self.lbl_sostav = QLabel(self.groupBox_2)
        self.lbl_sostav.setObjectName(u"lbl_sostav")

        self.gridLayout.addWidget(self.lbl_sostav, 3, 1, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.lbl_price = QLabel(self.groupBox_3)
        self.lbl_price.setObjectName(u"lbl_price")
        self.lbl_price.setGeometry(QRect(40, 150, 49, 16))

        self.horizontalLayout.addWidget(self.groupBox_3)

        self.horizontalLayout.setStretch(0, 2)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle("")
        self.lbl_image.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_2.setTitle("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u0430\u0432", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e | \u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.lbl_name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_category.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_count.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_sostav.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox_3.setTitle("")
        self.lbl_price.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

