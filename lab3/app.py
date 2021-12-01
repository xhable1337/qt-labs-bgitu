from math import sqrt
from sys import argv

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QFontDatabase

import design



class CheckBoxesApp(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        """Метод инициализации интерфейса."""
        super().__init__()
        QFontDatabase.addApplicationFont('fonts/circe.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-bold.ttf')
        QFontDatabase.addApplicationFont('fonts/circe-extrabold.ttf')
        self.setupUi(self)

        self.field_1.setVisible(False)
        self.field_2.setVisible(False)
        self.field_3.setVisible(False)
        # Привязка клавиши к функции расчёта
        self.checkBox_1.stateChanged.connect(lambda state: self.field_1.setVisible(state))
        self.checkBox_2.stateChanged.connect(lambda state: self.field_2.setVisible(state))
        self.checkBox_3.stateChanged.connect(lambda state: self.field_3.setVisible(state))


def main():
    app = QApplication(argv) 
    window = CheckBoxesApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()