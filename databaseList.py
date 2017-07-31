# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.text import LabelBase
import pymysql
import pymysql.cursors
from kivy.core.window import Window

LabelBase.register(name="NotoSans",
                   fn_regular="NotoSans-hinted/NotoSansUI-Regular.ttf",
                   fn_bold="NotoSans-hinted/NotoSansUI-Bold.ttf",
                   fn_italic="NotoSans-hinted/NotoSansUI-Italic.ttf",
                   fn_bolditalic="NotoSans-hinted/NotoSansUI-BoldItalic.ttf")
count = 0
class DbCon:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",user="root",passwd="root",db="climbingholdsape")
        self.c = self.db.cursor()

    def get_rows(self):
        self.c.execute("SELECT * FROM Moonboard")
        return self.c.fetchall()

class MyButton(Button):
    def on_press(self):
        print(self.text)

class DisplayGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(DisplayGridLayout, self).__init__(**kwargs)

        self.db = DbCon()
        self.Routes = self.db.get_rows()
        btn = [None] * len(self.Routes)
        self.grid = GridLayout(cols=1, size_hint_y=None)
        self.grid.bind(minimum_height=self.grid.setter('height'))
        for i in range(len(self.Routes)):
            btn[i] = MyButton(text=str(self.Routes[i][0]+'\n'+self.Routes[i][1])+'\n'+"Font Grade: "+self.Routes[i][2], size_hint_y=None)
            self.grid.add_widget(btn[i])
        self.scrolling = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.scrolling.add_widget(self.grid)
        self.add_widget(self.scrolling)










class DatabaseApp(App):

    def build(self):
        return DisplayGridLayout()

dataApp = DatabaseApp()
dataApp.run()