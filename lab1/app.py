from math import sqrt
from sys import argv

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase

import design



class EvalApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        """Метод инициализации интерфейса."""
        super().__init__()
        QFontDatabase.addApplicationFont('fonts/circe.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-bold.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-extrabold.ttf')
        self.setupUi(self)
        # Привязка клавиши к функции расчёта
        self.pushButton.clicked.connect(self.count)

    def __get_field_value(self):
        """Возвращает значение, введённое в поле.
        Если ничего не введено, возвращает и устанавливает 
        в поле значение плейсхолдера."""
        value = self.lineEdit.text()

        if value == '':
            placeholder = self.lineEdit.placeholderText()
            self.lineEdit.setText(placeholder)
            return placeholder
        else:
            return value

    def count(self):
        """Выполняет расчёт выражения, введённого в поле."""

        # Получение введённого значения
        value = self.__get_field_value()

        # Установка результата выражения в поле
        self.lineEdit_2.setText(str(eval(value)))


def main():
    app = QApplication(argv) 
    window = EvalApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()