import kivy
kivy.require("1.9.0")

from kivy.app import App
from kivy.uix.gridlayout import GridLayout

import random
class CalcGridLayout(GridLayout):
    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(random.randint(1,5))
            except Exception:
                self.display.text = "ERROR"

class CalculatorApp(App):

    def build(self):
        return CalcGridLayout()

calcApp = CalculatorApp()
calcApp.run()