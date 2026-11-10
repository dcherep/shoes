from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox, QWidget
from sqlalchemy.orm import Session
from PySide6.QtGui import QIcon, QPixmap
from models import *


class Login(QWidget):
    def __init__(self, main_window,parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui = loader.load("login.ui", self)
        self.main_window = main_window
        self.setWindowTitle('Авторизация')
        self.setWindowIcon(QIcon('Чудо Обувь.ico'))
        self.ui.label_3.setPixmap(QPixmap('Чудо Обувь.ico'))
        self.ui.pushButton.clicked.connect(self.check_login)
        self.ui.pushButton_2.clicked.connect(self.close)

    def check_login(self):
        l=self.ui.lineEdit.text()
        #p=self.ui.lineEdit_2.text()

        with Session(engine) as db:
            user= db.query(User).filter(User.login == l).first()
            if user is None:
                msg = QMessageBox(self)
                msg.setText('Неверный логин ')
                msg.exec()
            else:
                self.main_window.user = user
                self.main_window.load()
                self.main_window.show()
                self.close()


