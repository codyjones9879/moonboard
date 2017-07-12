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
        self.db = pymysql.connect(host="ClimbingHoldsApe.db.8216949.hostedresource.com",user="ClimbingHoldsApe",passwd="Comply9879!",db="ClimbingHoldsApe")
        self.c = self.db.cursor()

    def get_rows(self,search = ""):
        self.c.execute("SELECT * FROM Moonboard WHERE Author REGEXP '.*%s.*'limit 50" % search)
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

        self.add_widget(Label(text="Routes"))

        self.table = GridLayout(cols=3,rows=51)
        self.table.add_widget(Label(text="Problem"))
        self.table.add_widget(Label(text="Setter"))
        self.table.add_widget(Label(text="Grade"))

        self.rows = [[Label(text="Problem"),Label(text="Setter"),Label(text="Grade")] for x in range(50)]

        for Problem,Setter,Grade in self.rows:
            self.table.add_widget(Problem)
            self.table.add_widget(Setter)
            self.table.add_widget(Grade)

        self.add_widget(self.table)


        self.db = DbCon()
        self.update_table()


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