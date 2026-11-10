import sys
from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem
from ui_form import Ui_Widget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from sqlalchemy.orm import Session
from models import create, engine, Tovars
from tovar import Tovar
from login import Login

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.user =None
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon('Чудо Обувь.ico'))
        self.setWindowTitle('Обувной магазин')
        create()

        self.load_tovars()

    def load_tovars(self):
        self.ui.listWidget.clear()

        with Session(engine) as db:
            tovary = db.query(Tovars).all()
            for t in tovary:
                tovars=Tovar(t,self)
                item= QListWidgetItem(self.ui.listWidget)
                item.setSizeHint(QSize(0,125))
                self.ui.listWidget.setItemWidget(item, tovars)



    def load(self):
        self.ui.label.setText(f'{self.user.surname} {self.user.name} {self.user.patr}')
        self.load_tovars()

    def logout(self):
        self.user=None
        login_window.show()
        self.hide()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    login_window =Login(widget)
    login_window.show()
    sys.exit(app.exec())

