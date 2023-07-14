import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLineEdit, QPushButton, QVBoxLayout
from functools import partial

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Calculator')
        self.setFixedSize(400, 500)
        self.generalLayout = QVBoxLayout()
        self.widget = QWidget(self)
        self.setCentralWidget(self.widget)
        self.widget.setLayout(self.generalLayout)
        self.Display()
        self.Buttons()
    def Display(self):
        self.display = QLineEdit()
        self.display.setFixedSize(370,80)
        self.display.setReadOnly(True)
        self.generalLayout.addWidget(self.display)
    def Buttons(self):
        self.buttons = {}
        buttonsLayout = QGridLayout()
        buttons = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '*': (0, 3),
                   '4': (1, 0), '5': (1, 1),'6': (1, 2), '/': (1, 3),
                   '1': (2, 0), '2': (2, 1), '3': (2, 2), '+': (2, 3),
                   '0': (3, 0), '=': (3, 1), 'C': (3,2), '-': (3, 3)}
        for buttontext, position in buttons.items():
            self.buttons[buttontext] = QPushButton(buttontext)
            self.buttons[buttontext].setFixedSize(100,50)
            buttonsLayout.addWidget(self.buttons[buttontext], position[0], position[1])
        self.generalLayout.addLayout(buttonsLayout)
    def setDisplayText(self, text):
        self.display.setText(text)
        self.display.setFocus()
    def displayText(self):
        return self.display.text()
    def clearDisplay(self):
        self.setDisplayText('')

class Functions:
    def __init__(self, calculation, app):
        self._evaluate = calculation
        self._app = app
        self.connection()
    def calcRes(self):
        result = self._evaluate(expr=self._app.displayText())
        self._app.setDisplayText(result)
    def Expr(self, sub_exp):
        if self._app.displayText() == alert:
            self._app.clearDisplay()
        expr = self._app.displayText() + sub_exp
        self._app.setDisplayText(expr)
    def connection(self):
        for buttontext, btn in self._app.buttons.items():
            if buttontext not in {'=', 'C'}:
                btn.clicked.connect(partial(self.Expr, buttontext))
        self._app.buttons['='].clicked.connect(self.calcRes)
        self._app.display.returnPressed.connect(self.calcRes)
        self._app.buttons['C'].clicked.connect(self._app.clearDisplay)

alert = 'Cannot divide by zero'
def calc(expr):
    try:
        result = str(eval(expr, {}, {}))
    except ZeroDivisionError:
        result = alert
    return result

pycalc = QApplication(sys.argv)
app = Calculator()
app.show()
calculation = calc
Functions(calculation=calculation, app=app)
sys.exit(pycalc.exec_())


