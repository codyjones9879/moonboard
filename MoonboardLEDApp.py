# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import kivy
#from neopixel import *
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.checkbox import CheckBox
from kivy.config import Config
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

'''
Coordinate Key: This is for color value

            A1=0     A2=21----A3=22    A4=43----A5=44    A6=65----A7=66    A8=87----A9=88    A10=109----A11=110    A12=131----A13=132    A14=153----A15=154    A16=175----A17=176    A18=197
             |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |
            B1=1     B2=20    B3=23    B4=42    B5=45    B6=64    B7=67    B8=86    B9=89    B10=108    B11=111    B12=130    B13=133    B14=152    B15=155    B16=174    B17=177    B18=196
             |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |
            C1=2     C2=19    C3=24    C4=41    C5=46    C6=63    C7=68    C8=85    C9=90    C10=107    C11=112    C12=129    C13=134    C14=151    C15=156    C16=173    C17=178    C18=195
             |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |
            D1=3     D2=18    D3=25    D4=40    D5=47    D6=62    D7=69    D8=84    D9=91    D10=106    D11=113    D12=128    D13=135    D14=150    D15=157    D16=172    D17=179    D18=194
B			 |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |           T
O			E1=4     E2=17    E3=26    E4=39    E5=48    E6=61    E7=70    E8=83    E9=92    E10=105    E11=114    E12=127    E13=136    E14=149    E15=158    E16=171    E17=180    E18=193        O
T			 |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |           P
T			F1=5     F2=16    F3=27    F4=38    F5=49    F6=60    F7=71    F8=82    F9=93    F10=104    F11=115    F12=126    F13=137    F14=148    F15=159    F16=170    F17=181    F18=192
O			 |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |
M			G1=6     G2=15    G3=28    G4=37    G5=50    G6=59    G7=72    G8=81    G9=94    G10=103    G11=116    G12=125    G13=138    G14=147    G15=160    G16=169    G17=182    G18=191
             |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |
            H1=7     H2=14    H3=29    H4=36    H5=51    H6=58    H7=73    H8=80    H9=95    H10=102    H11=117    H12=124    H13=139    H14=146    H15=161    H16=168    H17=183    H18=190
             |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |
            I1=8     I2=13    I3=30    I4=35    I5=52    I6=57    I7=74    I8=79    I9=96    I10=101    I11=118    I12=123    I13=140    I14=145    I15=162    I16=167    I17=184    I18=189
             |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |
            J1=9     J2=12    J3=31    J4=34    J5=53    J6=56    J7=75    J8=78    J9=97    J10=100    J11=119    J12=122    J13=141    J14=144    J15=163    J16=166    J17=185    J18=188
             |         |        |        |        |        |        |        |        |         |          |          |          |          |          |          |          |          |
            K1=10----K2=11    K3=32----K4=33    K5=54----K6=55    K7=76----K8=77    K9=98----K10=99     K11=120----K12=121    K13=142----K14=143    K15=164----K16=165    K17=186----K18=187


'''
'''
Globals
'''
count = 0
#Window.fullscreen = 'auto'
LED_COUNT                = 196
LED_PIN                  = 18
LED_FREQ_HZ              = 800000
LED_DMA                  = 5
LED_BRIGHTNESS           = 255
LED_INVERT               = False
LED_CHANNEL              = 0
#LED_STRIP                = ws.WS2811_STRIP_GRB
#strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
#strip.begin()


def colorWipe(strip, color, wait_ms=50):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        # time.sleep(wait_ms/1000.0)


def moonToLED(coord):
    switcher = {
        "A1": 0,
        "B1": 1,
        "C1": 2,
        "D1": 3,
        "E1": 4,
        "F1": 5,
        "G1": 6,
        "H1": 7,
        "I1": 8,
        "J1": 9,
        "K1": 10,
        "K2": 11,
        "J2": 12,
        "I2": 13,
        "H2": 14,
        "G2": 15,
        "F2": 16,
        "E2": 17,
        "D2": 18,
        "C2": 19,
        "B2": 20,
        "A2": 21,
        "A3": 22,
        "B3": 23,
        "C3": 24,
        "D3": 25,
        "E3": 26,
        "F3": 27,
        "G3": 28,
        "H3": 29,
        "I3": 30,
        "J3": 31,
        "K3": 32,
        "K4": 33,
        "J4": 34,
        "I4": 35,
        "H4": 36,
        "G4": 37,
        "F4": 38,
        "E4": 39,
        "D4": 40,
        "C4": 41,
        "B4": 42,
        "A4": 43,
        "A5": 44,
        "B5": 45,
        "C5": 46,
        "D5": 47,
        "E5": 48,
        "F5": 49,
        "G5": 50,
        "H5": 51,
        "I5": 52,
        "J5": 53,
        "K5": 54,
        "K6": 55,
        "J6": 56,
        "I6": 57,
        "H6": 58,
        "G6": 59,
        "F6": 60,
        "E6": 61,
        "D6": 62,
        "C6": 63,
        "B6": 64,
        "A6": 65,
        "A7": 66,
        "B7": 67,
        "C7": 68,
        "D7": 69,
        "E7": 70,
        "F7": 71,
        "G7": 72,
        "H7": 73,
        "I7": 74,
        "J7": 75,
        "K7": 76,
        "K8": 77,
        "J8": 78,
        "I8": 79,
        "H8": 80,
        "G8": 81,
        "F8": 82,
        "E8": 83,
        "D8": 84,
        "C8": 85,
        "B8": 86,
        "A8": 87,
        "A9": 88,
        "B9": 89,
        "C9": 90,
        "D9": 91,
        "E9": 92,
        "F9": 93,
        "G9": 94,
        "H9": 95,
        "I9": 96,
        "J9": 97,
        "K9": 98,
        "K10": 99,
        "J10": 100,
        "I10": 101,
        "H10": 102,
        "G10": 103,
        "F10": 104,
        "E10": 105,
        "D10": 106,
        "C10": 107,
        "B10": 108,
        "A10": 109,
        "A11": 110,
        "B11": 111,
        "C11": 112,
        "D11": 113,
        "E11": 114,
        "F11": 115,
        "G11": 116,
        "H11": 117,
        "I11": 118,
        "J11": 119,
        "K11": 120,
        "K12": 121,
        "J12": 122,
        "I12": 123,
        "H12": 124,
        "G12": 125,
        "F12": 126,
        "E12": 127,
        "D12": 128,
        "C12": 129,
        "B12": 130,
        "A12": 131,
        "A13": 132,
        "B13": 133,
        "C13": 134,
        "D13": 135,
        "E13": 136,
        "F13": 137,
        "G13": 138,
        "H13": 139,
        "I13": 140,
        "J13": 141,
        "K13": 142,
        "K14": 143,
        "J14": 144,
        "I14": 145,
        "H14": 146,
        "G14": 147,
        "F14": 148,
        "E14": 149,
        "D14": 150,
        "C14": 151,
        "B14": 152,
        "A14": 153,
        "A15": 154,
        "B15": 155,
        "C15": 156,
        "D15": 157,
        "E15": 158,
        "F15": 159,
        "G15": 160,
        "H15": 161,
        "I15": 162,
        "J15": 163,
        "K15": 164,
        "K16": 165,
        "J16": 166,
        "I16": 167,
        "H16": 168,
        "G16": 169,
        "F16": 170,
        "E16": 171,
        "D16": 172,
        "C16": 173,
        "B16": 174,
        "A16": 175,
        "A17": 176,
        "B17": 177,
        "C17": 178,
        "D17": 179,
        "E17": 180,
        "F17": 181,
        "G17": 182,
        "H17": 183,
        "I17": 184,
        "J17": 185,
        "K17": 186,
        "K18": 187,
        "J18": 188,
        "I18": 189,
        "H18": 190,
        "G18": 191,
        "F18": 192,
        "E18": 193,
        "D18": 194,
        "C18": 195,
        "B18": 196,
        "A18": 197,
    }
    return switcher.get(coord, None)

class DbCon:
    def __init__(self):
        self.db = pymysql.connect(host="localhost",user="root",passwd="root",db="climbingholdsape")
        self.c = self.db.cursor()

    def get_rows(self):
        self.c.execute("SELECT * FROM Moonboard")
        return self.c.fetchall()

class Problem(Button):
    route = [None] * 205
    routeName = ""
    setterName = ""
    gradeUK = ""
    gradeUS = ""
    stars = 0
    moves = 0
    repeats = 0
    def on_press(self):
        #colorWipe(strip, Color(0, 0, 0))
        self.coordLED = [None] * 198
        '''
            # Example Array setup:   [SH1, SH2, SH3, SH4,IH1,.....IH196,FH1,FH2]   SH1-4  is a combination of 2 hands and 2 feet, Intermediate max is with only 1 hand hold to start and 1 finish 
            # hold max making a remaining 196 Intermediate holds potentially if the wall is filled We need designated locations for these combinations
            '''
        self.colorLED = [0] * 198
        # start holds
        self.coordLED[0] = moonToLED(self.route[0])
        self.coordLED[1] = moonToLED(self.route[1])
        self.coordLED[2] = None  # only because of moonboard only having 2 start holds
        self.coordLED[3] = None  # only because of moonboard only having 2 start holds
        # finish Holds
        self.coordLED[196] = moonToLED(self.route[202])
        self.coordLED[197] = moonToLED(self.route[203])
        temp = 2 #starting index in route that intermediate holds belong to
        temp2 = 4
        while self.route[temp] != '0':
            self.coordLED[temp2] = moonToLED(self.route[temp])
            temp2+=1
            temp+=1
        '''
        	# Color Choice:
        	# 0. Off
        	# 1. Blue - Start Hold
        	# 2. Red - Intermediate Hold
        	# 3. Green - Finish Hold
        	'''
        index = 0
        while index < len(self.coordLED):
            if index < 4:
                # start Holds
                if self.coordLED[index] != None:
                    self.colorLED[self.coordLED[index]] = 1
                    #strip.setPixelColorRGB(coordLED[index], 0, 255, 0)
            elif index > 3 and index < 196:
                if self.coordLED[index] != None:
                    self.colorLED[self.coordLED[index]] = 2
                    #strip.setPixelColorRGB(coordLED[index], 255, 0, 0)
                    # else:
                    # 	#colorLED[coordLED[index]] = 0
            else:
                if self.coordLED[index] != None:
                    self.colorLED[self.coordLED[index]] = 3
                    #strip.setPixelColorRGB(coordLED[index], 0, 0, 255)
                    # else:
                    # 	#colorLED[coordLED[index]] = 0
            index += 1
        index = 0
        while index < len(self.colorLED):
            if self.colorLED[index] == None:
                self.colorLED[index] = 0
                #strip.setPixelColorRGB(index, 0, 0, 0)
            index += 1
        #strip.show()
        print(self.routeName)
        print(self.setterName)
        print(self.gradeUK)
        print(self.gradeUS)
        print(self.stars)
        print(self.moves)
        print(self.repeats)
        print(*self.route)
        print(*self.coordLED)
        print(*self.colorLED)

        
class MoonboardAppLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MoonboardAppLayout, self).__init__(**kwargs)
        self.cols = 1
        self.rows = 3
        self.db = DbCon()
        self.Routes = self.db.get_rows()
        problemButton = [None] * len(self.Routes)
        self.problemList = GridLayout(cols=1, size_hint_y=None)
        self.problemList.bind(minimum_height=self.problemList.setter('height'))
        for i in range(len(self.Routes)):
            problemButton[i] = Problem(text=str(self.Routes[i][0]+'\n'+self.Routes[i][1])+'\n'+"Font Grade: "+self.Routes[i][2], size_hint_y=None)
            problemButton[i].route = self.Routes[i][7:211]
            problemButton[i].routeName = str(self.Routes[i][0])
            problemButton[i].setterName = str(self.Routes[i][1])
            problemButton[i].gradeUK = str(self.Routes[i][2])
            problemButton[i].gradeUS = str(self.Routes[i][3])
            problemButton[i].stars = self.Routes[i][4]
            problemButton[i].moves = self.Routes[i][5]
            problemButton[i].repeats = self.Routes[i][6]
            self.problemList.add_widget(problemButton[i])
        self.moonboardProblemsScroll = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        self.filters = CheckBox()
        self.filtered = CheckBox()
        self.moonboardProblemsScroll.add_widget(self.problemList)
        self.add_widget(self.moonboardProblemsScroll)
        self.add_widget(self.filters)
        self.add_widget(self.filtered)


class DatabaseApp(App):

    def build(self):
        parent = BoxLayout(size=(Window.width, Window.height))
        self.gridsDisplay = MoonboardAppLayout()
        parent.add_widget(self.gridsDisplay)
        return parent

dataApp = DatabaseApp()
dataApp.run()