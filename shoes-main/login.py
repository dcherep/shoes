from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox, QWidget
from PySide6.QtCore import Signal
from sqlalchemy.orm import Session
from PySide6.QtGui import QIcon, QPixmap
from models import User,engine


class Login(QWidget):
    success=Signal(User)
    def __init__(self, parent=None):
        super().__init__(parent)
        loader=QUiLoader()
        self.ui = loader.load("login.ui", self)
        self.setWindowTitle('Авторизация')
        self.setWindowIcon(QIcon('Чудо Обувь.ico'))
        self.ui.label_3.setPixmap(QPixmap('Чудо Обувь.ico'))
        self.ui.pushButton.clicked.connect(self.check_login)
        self.ui.pushButton_2.clicked.connect(self.close)

    def check_login(self):
        l=self.ui.lineEdit.text().strip()
        if l == '':
            msg=QMessageBox(self)
            msg.setText("Введите логин")
            msg.setIcon(QMessageBox.Critical)
            msg.exec()
            return

        try:
            with Session(engine) as db:
                user= db.query(User).filter(User.login == l).first()
                if user == None:
                    msg = QMessageBox(self)
                    msg.setText('Неверный логин ')
                    msg.setIcon(QMessageBox.Critical)
                    msg.exec()
                else:
                    self.success.emit(user)
                    self.close()
        except Exception as e:
            msg=QMessageBox(self)
            msg.setText(f'Ошибка: {e} ')
            msg.setIcon(QMessageBox.Critical)
            msg.exec()



