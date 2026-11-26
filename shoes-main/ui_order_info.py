# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'order_info.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHeaderView, QLabel, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(736, 419)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.tableView = QTableView(Form)
        self.tableView.setObjectName(u"tableView")

        self.gridLayout.addWidget(self.tableView, 4, 0, 2, 5)

        self.comboBox = QComboBox(Form)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 2, 4, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 5)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.dateEdit = QDateEdit(Form)
        self.dateEdit.setObjectName(u"dateEdit")

        self.gridLayout.addWidget(self.dateEdit, 1, 4, 1, 1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 6, 0, 1, 5)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 7, 0, 1, 2)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 7, 2, 1, 3)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 2, 1, 3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u0422\u043e\u0432\u0430\u0440\u044b", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u041f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u044c", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

