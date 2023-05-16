from PyQt6 import QtWidgets
import clipboard
from gui import Ui_MainWindow
import gen


class window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(window, self).__init__(parent)
        self.setupUi(self)

        self.passGenButton.clicked.connect(self.gen_pass)
        self.copy.clicked.connect(self.copy_text)

        # self.pass_input = QtWidgets.QLineEdit('pass_input')
        self.pass_input.textChanged.connect(self.text_changed)

        self.label_4.setText('sss')
        self.label_3.setHidden(True)
        self.label_4.setHidden(True)

    def gen_pass(self):
        print('clicked!!')
        length = self.length.text()
        param = (self.sw_lowercase.isChecked(), self.sw_uppercase.isChecked(), self.sw_digits.isChecked(),
                 self.sw_punctuation.isChecked(), self.sw_spaces.isChecked())
        if length == '':
            length = 20
            self.length.setText('20')
        if not any(param):
            self.sw_lowercase.setChecked(True)
            self.sw_uppercase.setChecked(True)
            self.sw_digits.setChecked(True)
            param = (self.sw_lowercase.isChecked(), self.sw_uppercase.isChecked(), self.sw_digits.isChecked(),
                     self.sw_punctuation.isChecked(), self.sw_spaces.isChecked())
        dict_param = []
        for i, item in enumerate(param):
            if item:
                dict_param.append(i)
        print(f'{dict_param= }')
        password = gen.pass_gen(int(length), *dict_param)
        print(f'{password= }')
        self.pass_input.setText(password)

    def text_changed(self):
        easterEggs = {'qwertyuiop1': 'есть что-либо надёжнее?',
                      'pupa': 'lupa', 'ping': 'pong', 'fl0ppa': 'pelmeni'
                      }
        s = self.pass_input.text()
        if s == '':
            self.label_3.setHidden(True)
            self.label_4.setHidden(True)
        else:
            self.label_3.setHidden(False)
            self.label_4.setHidden(False)
            get_s = easterEggs.get(s)
            print(get_s)
            if get_s != None:
                self.label_4.setText(get_s)
            else:
                score = gen.pass_check(s)
                print(f'{score= }')
                if score < 5:
                    self.label_4.setText('пароль слабый')
                elif score < 7:
                    self.label_4.setText('пароль нормальный')
                else:
                    self.label_4.setText('пароль сильный')

    def copy_text(self):
        text = self.pass_input.text()
        print(text)
        clipboard.copy(text)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    w = window()
    w.show()

    sys.exit(app.exec())
