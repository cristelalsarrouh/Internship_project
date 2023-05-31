from model import Model

from PyQt5.QtWidgets import QApplication


class Controller:

    def __init__(self):

        from view import Ui_MainWindow

        self.model = Model()

        self.view = Ui_MainWindow(self)

        self.view.show()

    def read_file(self, filename):

        if filename:

            print('The file exists')

            return self.model.read_file(filename)

        else:

            print("Please select a file that exists")


if __name__ == "__main__":
    app = QApplication([])

    controller = Controller()

    app.exec_()



