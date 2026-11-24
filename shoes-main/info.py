from PySide6.QtWidgets import QWidget,QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QIcon
from sqlalchemy.orm import Session
from PySide6.QtCore import Qt, Signal
from datetime import date, timedelta
from models import create, engine,Tovars,Size,TovarItems


class Info(QWidget):
    add = Signal(Tovars,Size,int,float)
    def __init__(self, parent=None):
        super().__init__(parent)
        #загружаем UI
        loader = QUiLoader()
        self.ui = loader.load("info.ui", self)
        #заголовок окна
        self.setWindowTitle('Карточка товара')
        #логотип фирмы загружаем
        self.setWindowIcon(QIcon('Чудо Обувь.ico'))

        self.ui.pushButton.clicked.connect(self.close)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.ui.pushButton_3.clicked.connect(self.add_tovar)

    #добавление товара в заказ
    def add_tovar(self):
        #получаем выбранный размер
        size=self.ui.comboBox.currentData()
        #получим кол-во
        amount=self.ui.spinBox.value()
        #нельзя заказать ноль штук или менее
        if amount<=0:
            QMessageBox.critical(self,'Ошибка','Без количества нельзя заказать!')
            return
        #нельзя заказать больше кол-ва чем на складе
        with Session(engine) as db:
            #получим товар со склада
            tovar_item = db.query(TovarItems).filter(TovarItems.tovar_id==self.tovar.id, TovarItems.size_id==size.id).first()
            if amount > int(tovar_item.amount):
                QMessageBox.critical(self,'Ошибка',f'Количество не может быть больше, чем {tovar_item.amount}.\nВот столько есть на складе!')
                return
        self.add.emit(self.tovar,size,amount,self.tovar.price)
        self.close()


    def show_info(self,tovar,user):
        #запомним товар
        self.tovar = tovar
        #если не авторизован - заказать товар нельзя
        if user is None:
            self.ui.comboBox.setEnabled(False)
            self.ui.spinBox.setEnabled(False)
            self.ui.pushButton_3.setEnabled(False)
        else:
            self.ui.comboBox.setEnabled(True)
            self.ui.spinBox.setEnabled(True)
            self.ui.pushButton_3.setEnabled(True)
        self.ui.lbl_name.setText(tovar.name)
        self.ui.lbl_desc.setText(tovar.description)
        self.ui.lbl_category.setText(tovar.category.name)
        #размерный ряд
        sizes = [x.size.name for x in tovar.items]
        self.ui.lbl_size.setText(', '.join(sizes))
        #доступные для заказа размеры

        available_sizes = [x.size for x in tovar.items if int(x.amount) > 0]
        self.ui.comboBox.clear()
        for s in available_sizes:
            self.ui.comboBox.addItem(s.name, s)

        self.ui.lbl_man.setText(tovar.manufacture.name)
        self.ui.lbl_sostav.setText(tovar.content)
        #скидка
        current_date=date.today()
        first_day_current = current_date.replace(day=1)
        last_day_prev = first_day_current - timedelta(days=1)
        first_day_prev = last_day_prev.replace(day=1)
        has_in_prev_month = False
        for item in tovar.order_items:
            if first_day_prev <= item.orders.date <= last_day_prev:
                has_in_prev_month = True
                print(item.order.date)
                break
        if has_in_prev_month is True:
            self.ui.lbl_price.setText(f'{tovar.price} руб)')
        else:
            self.ui.lbl_price.setText(f'{tovar.price*0.75} руб (скидка!) ')
        #вывод фото
        if tovar.image_path != '':
            self.ui.lbl_image.setPixmap(QPixmap(tovar.image_path))
        else:
            self.ui.lbl_image.setPixmap(QPixmap('picture.png'))

        #покажем окно "модально"
        self.setWindowFlag(Qt.Window)
        self.setWindowModality(Qt.ApplicationModal)
        self.show()

        #total_count = sum(int(item.amount) for item in tovars.items)
       # self.ui.lbl_count.setText(str(total_count))








