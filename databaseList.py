# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kivy.app import App
import pymysql
import pymysql.cursors

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp

class DbCon:

    def __init__(self):
        self.db = pymysql.connect(host="localhost",user="root",passwd="root",db="climbingholdsape")
        self.c = self.db.cursor()

    def get_rows(self):
        self.c.execute("SELECT * FROM Moonboard")
        return self.c.fetchall()


class Table(BoxLayout):

    def __init__(self,**kwargs):
        super(Table,self).__init__(**kwargs)

        self.orientation = "vertical"

        self.search_field = BoxLayout(orientation="horizontal")

        self.search_input = TextInput(text='search',multiline=False)
        self.search_button = Button(text="search",on_press=self.search)

        self.search_field.add_widget(self.search_input)
        self.search_field.add_widget(self.search_button)

        self.add_widget(self.search_field)

        self.db = DbCon()
        self.Routes = self.db.get_rows()

        self.grid = GridLayout(cols=1, size_hint_y=None)

        for i in range(50):
            btn = Button(text=str(self.Routes[i][0]+'\n'+self.Routes[i][1])+'\n'+"Font Grade: "+self.Routes[i][2], size_hint_y=None)
            self.grid.add_widget(btn)
        self.scrolling = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.scrolling.add_widget(self.grid)
        self.add_widget(self.scrolling)






    def update_table(self,search=""):
        for index,row in enumerate(self.db.get_rows(search)):
            self.rows[index][0].text = row[0]
            self.rows[index][1].text = str(row[1])
            self.rows[index][2].text = str(row[2])

    def clear_table(self):
        for index in range(3):
            self.rows[index][0].text = ""
            self.rows[index][1].text = ""
            self.rows[index][2].text = ""

    def search(self, *args):
        self.clear_table()
        self.update_table(self.search_input.text)


class MyApp(App):
    def build(self):
        return Table()


MyApp().run()