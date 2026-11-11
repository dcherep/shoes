import sys
from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem
from ui_form import Ui_Widget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from sqlalchemy.orm import Session
from models import create, engine, Tovars, TovarItems,OrdersItems,Category
from tovar import Tovar
from login import Login

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.login_window=None
        self.user=None
        self.setWindowIcon(QIcon('Чудо Обувь.ico'))
        self.setWindowTitle('Обувной магазин')
        create()

        with Session(engine) as db:
            for cat in db.query(Category).all():
                self.ui.comboBox.addItem(cat.name)

        self.load_tovars()

        self.ui.pushButton.clicked.connect(self.show_login)
        self.ui.comboBox.currentIndexChanged.connect(self.load_tovars)
        self.ui.radioButton.toggled.connect(self.load_tovars)
        self.ui.radioButton_2.toggled.connect(self.load_tovars)
        self.ui.radioButton_3.toggled.connect(self.load_tovars)
        self.ui.radioButton_4.toggled.connect(self.load_tovars)
        self.ui.radioButton_5.toggled.connect(self.load_tovars)
        self.ui.lineEdit.textChanged.connect(self.load_tovars)

                
        self.ui.comboBox.hide()
        self.ui.groupBox_2.hide()
        self.ui.groupBox.hide()



    def show_login(self):
        if self.login_window is None:
            self.login_window=Login()
            self.login_window.success.connect(self.login_success)
        self.login_window.show()
        self.user=None
        self.ui.label.setText('Не авторизован')

        self.ui.comboBox.hide()
        self.ui.groupBox_2.hide()
        self.ui.groupBox.hide()

    def login_success(self,user):
        self.user=user
        self.ui.label.setText(f'{self.user.surname} {self.user.name} {self.user.patr}')
        self.ui.pushButton.setText('Выйти')
                
        self.ui.comboBox.show()
        self.ui.groupBox_2.show()
        self.ui.groupBox.show()

    def load_tovars(self):
        self.ui.listWidget.clear()

        with Session(engine) as db:
            tovary = db.query(Tovars).all()

            current_cat = self.ui.comboBox.currentText()
            if current_cat != "Все категории" and current_cat != "":
                tovary = [t for t in tovary if t.category and t.category.name == current_cat]

            def get_total_count(t):
                return sum(int(item.amount) for item in t.items) if t.items else 0

            if self.ui.radioButton_2.isChecked():
                tovary = sorted(tovary, key=lambda t: t.price)
            elif self.ui.radioButton_3.isChecked():
                tovary = sorted(tovary, key=lambda t: t.price, reverse=True)
            elif self.ui.radioButton_4.isChecked():
                tovary = sorted(tovary, key=lambda t: get_total_count(t))
            elif self.ui.radioButton_5.isChecked():
                tovary = sorted(tovary, key=lambda t: get_total_count(t), reverse=True)


            search = self.ui.lineEdit.text().strip().lower()
            if len(search)>0:
                tovary = [t for t in tovary if t.name.lower().find(search) != -1 or t.description.lower().find(search) != -1]

            for t in tovary:
                tovars=Tovar(t,self)
                item= QListWidgetItem(self.ui.listWidget)
                item.setSizeHint(QSize(0,200))
                self.ui.listWidget.setItemWidget(item, tovars)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

