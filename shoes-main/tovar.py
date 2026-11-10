from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap
from datetime import date, timedelta

class Tovar(QWidget):
    def __init__(self, tovars, main_window, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("tovar.ui", self)
        self.main_window = main_window
        self.tovars = tovars

        self.ui.lbl_name.setText(f'{tovars.manufacture.name} | {tovars.name}')
        self.ui.lbl_category.setText(tovars.category.name)
        total_count = sum(int(item.amount) for item in tovars.items)
        self.ui.lbl_count.setText(str(total_count))
        self.ui.lbl_sostav.setText(tovars.content)
        current_date=date.today()
        first_day_current = current_date.replace(day=1)
        last_day_prev = first_day_current - timedelta(days=1)
        first_day_prev = last_day_prev.replace(day=1)
        has_in_prev_month = False
        for item in tovars.order_items:
            if first_day_prev <= item.orders.date <= last_day_prev:
                has_in_prev_month = True
                print(item.order.date)
                break
        if has_in_prev_month is True:
            self.ui.lbl_price.setText(f'{tovars.price} руб)')
        else:
            self.ui.lbl_price.setText(f'{tovars.price*0.75} руб (скидка!) ')

        if tovars.image_path != '':
            self.ui.lbl_image.setPixmap(QPixmap(' ' + tovars.image_path))
        else:
            self.ui.lbl_image.setPixmap(QPixmap('picture.png'))

        if total_count <= 3:
            self.ui.setStyleSheet('background-color:#70B2AF;')







