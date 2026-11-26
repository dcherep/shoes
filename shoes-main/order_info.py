from PySide6.QtWidgets import QWidget,QMessageBox,QHeaderView,QTableView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QIcon,QStandardItemModel, QStandardItem
from sqlalchemy.orm import Session
from PySide6.QtCore import Qt, Signal
from models import create, engine,Tovars,Size,TovarItems,Orders,OrdersItems,User

class OrderInfo(QWidget):
    add = Signal(Orders,Size,int,float)
    def __init__(self, parent=None):
        super().__init__(parent)
        #загружаем UI
        loader = QUiLoader()
        self.ui = loader.load("order_info.ui", self)
        #заголовок окна
        self.setWindowTitle('Заказ')
        #логотип фирмы загружаем
        self.setWindowIcon(QIcon('Чудо Обувь.ico'))
        self.load_users()

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["Товар","Размер","Количество","Цена"])
        self.ui.tableView.setModel(self.model)


        self.ui.tableView.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)


        self.ui.pushButton.clicked.connect(self.close)
        #self.ui.pushButton_2.clicked.connect(self.)
        #self.ui.pushButton_3.clicked.connect(self.edit_order)

    #def edit_order(self,order):
    def load_orders_item(self, order):
        self.model.clear()
        with Session(engine) as db:
            print(order.id)
            orders_items = db.query(OrdersItems).filter(OrdersItems.order_id == order.id).all()

            for o_i in orders_items:
                #создаем ячейки таблицы
                #id=QStandardItem(str(o_i.id))
                #id.setData(o_i, 256)

                tovar = QStandardItem(str(o_i.tovar))
                size=QStandardItem(str(o_i.size))
                amount=QStandardItem(o_i.amount)
                price=QStandardItem(f"{float(o_i.price)}")
                self.model.appendRow([tovar,size,amount,price])



    #загрузка списка пользователя
    def load_users(self):
        self.ui.comboBox.clear()
        with Session(engine) as db:
            users = db.query(User).all()
            for u in users:
                self.ui.comboBox.addItem(str(u),u)


    def show_window(self, order):
        #выводим данные заказа
        self.ui.label.setText(f'Заказ № {order.id}')
        self.ui.dateEdit.setDate(order.date)
        #выбрать пользователя
        for i in range(self.ui.comboBox.count()):
            item_user=self.ui.comboBox.itemData(i)
            if item_user and item_user.id == order.user.id:
                self.ui.comboBox.setCurrentIndex(i)
                break

        self.load_orders_item(order)
        #покажем окно "модально"
        self.setWindowFlag(Qt.Window)
        self.setWindowModality(Qt.ApplicationModal)
        self.show()