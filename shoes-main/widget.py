import sys
from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem
from ui_form import Ui_Widget
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize
from sqlalchemy.orm import Session
from models import create, engine, Tovars
from tovar import Tovar

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

