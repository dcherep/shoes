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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLabel,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(777, 603)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 12, 0, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 13, 0, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_6.setFont(font)

        self.gridLayout.addWidget(self.label_6, 10, 0, 1, 1)

        self.lbl_image = QLabel(Form)
        self.lbl_image.setObjectName(u"lbl_image")
        self.lbl_image.setMaximumSize(QSize(120, 120))
        self.lbl_image.setScaledContents(True)

        self.gridLayout.addWidget(self.lbl_image, 9, 0, 1, 1)

        self.lbl_name = QLabel(Form)
        self.lbl_name.setObjectName(u"lbl_name")

        self.gridLayout.addWidget(self.lbl_name, 1, 2, 1, 1)

        self.lbl_man = QLabel(Form)
        self.lbl_man.setObjectName(u"lbl_man")

        self.gridLayout.addWidget(self.lbl_man, 2, 2, 1, 1)

        self.lbl_category = QLabel(Form)
        self.lbl_category.setObjectName(u"lbl_category")

        self.gridLayout.addWidget(self.lbl_category, 3, 2, 1, 1)

        self.lbl_price = QLabel(Form)
        self.lbl_price.setObjectName(u"lbl_price")
        self.lbl_price.setMinimumSize(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        self.lbl_price.setFont(font1)

        self.gridLayout.addWidget(self.lbl_price, 4, 2, 1, 1)

        self.lbl_sostav = QLabel(Form)
        self.lbl_sostav.setObjectName(u"lbl_sostav")
        self.lbl_sostav.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_sostav, 5, 2, 1, 1)

        self.lbl_desc = QLabel(Form)
        self.lbl_desc.setObjectName(u"lbl_desc")
        self.lbl_desc.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_desc, 6, 2, 1, 1)

        self.lbl_size = QLabel(Form)
        self.lbl_size.setObjectName(u"lbl_size")
        self.lbl_size.setWordWrap(True)

        self.gridLayout.addWidget(self.lbl_size, 7, 2, 1, 1)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 10, 1, 1, 2)

        self.spinBox = QSpinBox(Form)
        self.spinBox.setObjectName(u"spinBox")

        self.gridLayout.addWidget(self.spinBox, 12, 1, 1, 2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 13, 1, 1, 2)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 2)

        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font)

        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 2)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 4, 0, 1, 2)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 2)

        self.label_9 = QLabel(Form)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 2)

        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u041e\u0442\u043c\u0435\u043d\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0441\u0442\u0443\u043f\u043d\u044b\u0435 \u0440\u0430\u0437\u043c\u0435\u0440\u044b", None))
        self.lbl_image.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_name.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_man.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_category.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_price.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_sostav.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_desc.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.lbl_size.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0417\u0430\u043a\u0430\u0437\u0430\u0442\u044c", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0441\u0442\u0432\u043e", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u0426\u0435\u043d\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0441\u0442\u0430\u0432:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u0420\u0430\u0437\u043c\u0435\u0440\u043d\u044b\u0439 \u0440\u044f\u0434", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

