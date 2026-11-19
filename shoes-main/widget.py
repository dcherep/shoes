import sys
from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem,QMessageBox
from ui_form import Ui_Widget
from PySide6.QtGui import QIcon,QPixmap,QStandardItemModel, QStandardItem
from PySide6.QtCore import QSize
from sqlalchemy.orm import Session
from models import create, engine, Tovars, TovarItems,OrdersItems,Category,Orders,User
from tovar import Tovar
from login import Login
from info import Info
from datetime import date, timedelta

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.login_window=None
        self.info_window=None
        self.user=None
        self.setWindowIcon(QIcon('Чудо Обувь.ico'))
        self.setWindowTitle('Обувной магазин')
        #создаем таблицы если их еще нет
        create()

        #загружаем товары
        self.load_tovars()

        #создаем модель  и привязываем ее к QListView
        self.model = QStandardItemModel()
        self.ui.listView.setModel(self.model)

        #соединяем сигналы со слотами
        self.ui.pushButton.clicked.connect(self.show_login)
        self.ui.comboBox.currentIndexChanged.connect(self.load_tovars)
        self.ui.radioButton.toggled.connect(self.load_tovars)
        self.ui.radioButton_2.toggled.connect(self.load_tovars)
        self.ui.radioButton_3.toggled.connect(self.load_tovars)
        self.ui.radioButton_4.toggled.connect(self.load_tovars)
        self.ui.radioButton_5.toggled.connect(self.load_tovars)
        self.ui.lineEdit.textChanged.connect(self.load_tovars)
        self.ui.listWidget.itemClicked.connect(self.show_info)
        self.ui.pushButton_2.clicked.connect(self.create_order)

        #скрываем виджет бокс для неавторизованных
        self.ui.comboBox.hide()
        self.ui.groupBox_2.hide()
        self.ui.lineEdit.hide()
        #self.ui.listWidget.itemClicked.hide()

    #создание заказа
    def create_order(self):
        with Session(engine) as db:
            #создадим новый заказ
            new_order = Orders(date=date.today(),user_id=self.user.id)
            db.add(new_order)
            db.flush()#отправляет INSERT в БД, но ещё не фиксирует транзакцию
            #id нового заказа теперь доступен вот так: new_order.id

            #перебираем позиции в заказе
            for row in range(self.model.rowCount()):
                item=self.model.item(row)#берем QStandardItem напрямую по номеру строки
                #товар
                tovar=item.data()['tovar']
                #размер
                size=item.data()['size']
                #количество
                amount=item.data()['amount']
                #цена
                price=item.data()['price']
                #добавляем товары к заказу (в таблицу order_items)
                orders_items=OrdersItems(order_id=new_order.id,tovar_id=tovar.id,size_id=size.id,amount=amount,price=price)
                db.add(orders_items)

            db.commit()
        #выведем сообщение об успехе
        QMessageBox.information(self,'Успех','Заказ успешно оформлен!')
        #уберем товары из заказа
        self.model.clear()

    def show_info(self,item):
        #если окно ещё не создано - создаём его
        if self.info_window is None:
            self.info_window = Info()
            self.info_window.add.connect(self.add_tovar)

        tovar = self.ui.listWidget.itemWidget(item)
        if tovar:
            self.info_window.show_info(tovar.tovars)


    def add_tovar(self, t, s, a,p):
        item = QStandardItem(t.name)
        item.setData({"tovar": t, "size":s,"amount": a,"price": p})#сохраняем словарь
        self.model.appendRow(item)

    #покажем окно авторизации
    def show_login(self):
        #если окно ещё не создано - создаём его
        if self.login_window is None:
            self.login_window=Login()
            self.login_window.success.connect(self.login_success)
        #покажем окно
        self.login_window.show()
        #разлогиним текущего пользователя
        self.user=None
        self.ui.label.setText('Не авторизован')
        self.ui.pushButton.setText('Войти')

        self.ui.comboBox.hide()
        self.ui.groupBox_2.hide()
        self.ui.lineEdit.hide()
        #self.ui.listWidget.itemClicked.hide()

    #авторизация прошла
    def login_success(self,user):
        self.user=user
        self.ui.label.setText(f'{self.user.surname} {self.user.name} {self.user.patr}')
        self.ui.pushButton.setText('Выйти')
        #показываем виджет бокс
        self.ui.comboBox.show()

        self.ui.groupBox_2.show()
        self.ui.lineEdit.show()
        #self.ui.listWidget.itemClicked.show()

    #загружаем список товаров
    def load_tovars(self):
        #очистка списка
        self.ui.listWidget.clear()
        #получаем список товаров
        with Session(engine) as db:
            tovary = db.query(Tovars).all()
            #фильтрация
            current_cat = self.ui.comboBox.currentText()
            if current_cat != "Все категории" and current_cat != "":
                tovary = [t for t in tovary if t.category and t.category.name == current_cat]

            # total_count = sum(t.items.amount)
            #сортировка
            if self.ui.radioButton_2.isChecked():
                tovary = sorted(tovary, key=lambda t: t.price)
            elif self.ui.radioButton_3.isChecked():
                tovary = sorted(tovary, key=lambda t: t.price, reverse=True)
            elif self.ui.radioButton_4.isChecked():
                tovary = sorted(tovary, key=lambda t: total_count)
            elif self.ui.radioButton_5.isChecked():
                tovary = sorted(tovary, key=lambda t: total_count, reverse=True)

            #поиск
            search = self.ui.lineEdit.text().strip().lower()
            if len(search)>0:
                tovary = [t for t in tovary if t.name.lower().find(search) != -1 or t.description.lower().find(search) != -1]

            for t in tovary:
                tovars=Tovar(t,self)
                #создаем стандартный контейнер-строку для списка
                item= QListWidgetItem(self.ui.listWidget)
                item.setSizeHint(QSize(0,200))
                self.ui.listWidget.setItemWidget(item, tovars)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())

