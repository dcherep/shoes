from PySide6.QtWidgets import QWidget,QMessageBox,QHeaderView,QTableView
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QIcon,QStandardItemModel, QStandardItem
from sqlalchemy.orm import Session
from PySide6.QtCore import Qt, Signal
from datetime import date, timedelta
from models import create, engine,Tovars,Size,TovarItems,Orders,OrdersItems
from order_info import OrderInfo


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
        self.order_window = None

        #создаем модель  и привязываем ее к QTableView
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID","Дата","ФИО клиента"])
        self.ui.tableView.setModel(self.model)
        #настройка внешнего вида и выделения
        self.ui.tableView.setSelectionBehavior(QTableView.SelectionBehavior.SelectRows)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.ui.tableView.clicked.connect(self.order_clicked)

        self.load_orders()
        self.ui.pushButton.clicked.connect(self.close)
        #self.ui.pushButton_2.clicked.connect(self.)

    def order_clicked(self, index):
        #переходим к ячейке первого столбца (индекс 0) в выбранной строке,
        #так как именно в ячейку id мы положили объект order
        first_col_index=index.siblingAtColumn(0)
        #извлекаем объект Order по роли UserRole
        order = first_col_index.data(256)
        if order is not None:
            #если окно ещё не создано - создаём его
            if self.order_window is None:
                self.order_window = OrderInfo()
            self.order_window.show_window(order)

    #загрузим список заказов из базы
    def load_orders(self):
        with Session(engine) as db:
            orders = db.query(Orders).all()
            for o in orders:
                #создаем ячейки таблицы
                id=QStandardItem(str(o.id))
                #сохраняем сам объект Order в первую ячейку (удобно при клике)
                id.setData(o, 256)
                date = QStandardItem(o.date.strftime("%d.%m.%Y"))
                user=QStandardItem(str(o.user))
                self.model.appendRow([id,date,user])