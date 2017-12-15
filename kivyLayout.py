# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import kivy
# from neopixel import *
import sys
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.scatterlayout import ScatterLayout
from kivy.uix.checkbox import CheckBox
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.properties import BooleanProperty, StringProperty, ListProperty
from kivy.uix.behaviors import ToggleButtonBehavior
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.button import Button
from kivy.core.text import LabelBase
import pymysql
import pymysql.cursors
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_string('''
<ScreenManagement>:
	ScreenOne:
	ScreenTwo:


<ScreenOne>:
	name: 'Home'
	id: 'home'
	BoxLayout:
		GridLayout:
		    id: "MoonboardLayout"
		    cols: 2
		    rows: 2
		    GridLayout:
		        cols:1
		        size_hint_y: None
		        


<ScreenTwo>:
	name: 'Second'
	BoxLayout:
		orientation: 'vertical'
		


''')


class ScreenManagement(ScreenManager):
	pass

class ScreenOne(Screen):
	pass

class ScreenTwo(Screen):
	pass





class MyApp(App):

	def build(self):
		return ScreenManagement()

if __name__ == '__main__':
	MyApp().run()