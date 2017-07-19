# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.scatter import Scatter
from kivy.uix.floatlayout import FloatLayout

class TutorialApp(App):
    def build(self):
        f = FloatLayout()
        s = Scatter()
        l = Label(text="Malibus"+u'2710'+"-Most-Var", font_size=15, font_name=Noto)
        f.add_widget(s)
        s.add_widget(l)
        return f
if __name__ == "__main__":
    TutorialApp().run()