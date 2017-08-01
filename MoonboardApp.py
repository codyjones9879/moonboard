# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kivy.app import App
import pymysql
import pymysql.cursors
from time import time
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.properties import NumericProperty, StringProperty, BooleanProperty,\
    ListProperty
Builder.load_file('database.kv')

class DbCon:

    def __init__(self):
        self.db = pymysql.connect(host="ClimbingHoldsApe.db.8216949.hostedresource.com",user="ClimbingHoldsApe",passwd="Comply9879!",db="ClimbingHoldsApe")
        self.c = self.db.cursor()

    def get_rows(self,search = ""):
        self.c.execute("SELECT * FROM Moonboard")
        return self.c.fetchall()



# layout = GridLayout(cols=2, rows=2, spacing=10, size_hint_y=None)
# layout.bind(minimum_height=layout.setter('height'))
# #orientation = "vertical"

#     # self.search_field = BoxLayout(orientation="horizontal")

#     # self.search_input = TextInput(text='search',multiline=False)
#     # self.search_button = Button(text="search",on_press=self.search)

#     # self.search_field.add_widget(self.search_input)
#     # self.search_field.add_widget(self.search_button)

#     # self.add_widget(self.search_field)

# layout.add_widget(Label(text="Hyperbolic Time Chamber"))
# layout.add_widget(Label(text="Place Holder for a search Window"))
# layout.add_widget(Label(text="Place Holder for the Moonboard Image"))
# problemLayout = BoxLayout()
# root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
# for i in range(100):
#     btn = Button(text=str(i), size_hint_y=None, height=40)
#     problemLayout.add_widget(btn)
# root.add_widget(problemLayout)
# layout.add_widget()

    # self.table = GridLayout(cols=3,rows=51)
    # self.table.add_widget(Label(text="Problem"))
    # self.table.add_widget(Label(text="Setter"))
    # self.table.add_widget(Label(text="Grade"))

    # self.rows = [[Label(text="Problem"),Label(text="Setter"),Label(text="Grade")] for x in range(50)]

    # for Problem,Setter,Grade in self.rows:
    #     self.table.add_widget(Problem)
    #     self.table.add_widget(Setter)
    #     self.table.add_widget(Grade)

    # self.add_widget(self.table)


    # self.db = DbCon()
    # self.update_table()


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


class Table(GridLayout):
    pass


class MyMoonboardApp(App):
    time = NumericProperty(0)
    def build(self):
        self.title = "The Hyperbolic Time Chamber Training"
        Clock.schedule_interval(self._update_clock, 1 / 60.)

        return Table()

    def _update_clock(self, dt):
        self.time = time()
if __name__ == '__main__':
    MyMoonboardApp().run()
