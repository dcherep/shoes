from PySide6.QtWidgets import QWidget,QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QIcon,QStandardItemModel, QStandardItem
from sqlalchemy.orm import Session
from PySide6.QtCore import Qt, Signal
from datetime import date, timedelta
from models import create, engine,Tovars,Size,TovarItems,Orders,OrdersItems


class Zakaz(QWidget):
    #add = Signal(Tovars,Size,int,float)
    def __init__(self, parent=None):
        super().__init__(parent)
        #загружаем UI
        loader = QUiLoader()
        self.ui = loader.load("zakaz.ui", self)
        #заголовок окна
        self.setWindowTitle('Заказы товаров')
        #логотип фирмы загружаем
        self.setWindowIcon(QIcon('Чудо Обувь.ico'))

        #создаем модель  и привязываем ее к QTableView
        self.model = QStandardItemModel()
        self.ui.tableView.setModel(self.model)

        self.ui.pushButton.clicked.connect(self.close)

    def show_order(self,order):
        self.order = order
        orders_items=OrdersItems(order_id=new_order.id,tovar_id=tovar.id,size_id=size.id,amount=amount,price=price)


