from PySide6.QtWidgets import QWidget,QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap,QIcon
from PySide6.QtCore import Qt
from datetime import date, timedelta


class Info(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("info.ui", self)
        self.setWindowTitle('Карточка товара')
        self.setWindowIcon(QIcon('Чудо Обувь.ico'))

    def show_info(self,tovar):
        self.ui.lbl_name.setText(tovar.name)
        self.ui.lbl_desc.setText(tovar.description)
        self.ui.lbl_category.setText(tovar.category.name)
        sizes = [x.size.name for x in tovar.items]
        self.ui.lbl_size.setText(', '.join(sizes))
        total_count = sum(int(item.amount) for item in tovar.items)
        self.ui.lbl_count.setText(str(total_count))
        self.ui.lbl_man.setText(tovar.manufacture.name)
        self.ui.lbl_sostav.setText(tovar.content)
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

        if tovar.image_path != '':
            self.ui.lbl_image.setPixmap(QPixmap(tovar.image_path))
        else:
            self.ui.lbl_image.setPixmap(QPixmap('picture.png'))

        self.setWindowFlag(Qt.Window)
        self.setWindowModality(Qt.ApplicationModal)
        self.show()

        #total_count = sum(int(item.amount) for item in tovars.items)
       # self.ui.lbl_count.setText(str(total_count))








