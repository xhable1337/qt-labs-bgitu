from math import sqrt
from sys import argv

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase

import design



class MiniCalcApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        """Метод инициализации интерфейса."""
        super().__init__()
        QFontDatabase.addApplicationFont('fonts/circe.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-bold.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-extrabold.ttf')
        self.setupUi(self)
        # Привязка клавиши к функции расчёта
        self.pushButton.clicked.connect(self.count)

    def __get_fields_values(self):
        """Возвращает значение, введённое в поле.
        Если ничего не введено, возвращает и устанавливает 
        в поле значение плейсхолдера."""
        values = (self.number_1.text(), self.number_2.text())

        if values == ('', ''):
            placeholder_1 = self.number_1.placeholderText()
            self.number_1.setText(placeholder_1)

            placeholder_2 = self.number_2.placeholderText()
            self.number_2.setText(placeholder_2)

            return map(int, (placeholder_1, placeholder_2))
        else:
            return map(int, values)

    def count(self):
        """Выполняет расчёт выражения, введённого в поле."""

        # Получение и валидация введённых значений
        x, y = self.__get_fields_values()
        print(x, y, sep=' | ')

        addition = x + y
        subtraction = x - y
        multiplication = x * y

        try: 
            division = x / y
        except ZeroDivisionError: 
            division = 'Error'

        print(addition, subtraction, multiplication, division, sep=" :: ")

        self.addition.display(addition)
        self.subtraction.display(subtraction)
        self.multiplication.display(multiplication)
        self.division.display(division)


def main():
    app = QApplication(argv) 
    window = MiniCalcApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()