from PySide6.QtWidgets import QWidget
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QPixmap

class Tovar(QWidget):
    def __init__(self, tovars, main_window, parent=None):
        super().__init__(parent)
        loader = QUiLoader()
        self.ui = loader.load("tovar.ui", self)
        self.main_window = main_window
        self.tovars = tovars

        self.ui.lbl_name.setText(f'{tovars.manufacturer.name} | {tovars.name}')
        self.ui.lbl_category.setText(tovars.cat.name)
        total_count = sum(item.count for item in tovars.items)
        self.ui.lbl_count.setText(str(total_count))
        self.ui.lbl_sostav.setText(tovars.content)
        self.ui.lbl_price.setText(f'{tovars.price} руб')

        if tovars.image_path != '':
            self.ui.lbl_image.setPixmap(QPixmap('/ ' + tovars.image_path))
        else:
            self.ui.lbl_image.setPixmap(QPixmap('picture.png'))


