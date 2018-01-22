# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import kivy
# from neopixel import *
import sys
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
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

reload(sys)
sys.setdefaultencoding('utf-8')
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
global LED_ROUTE_IMAGES, problemButton, Routes, filterBox, FilterLabel, filteredCommandStr, orderCommandStr, addedCommandStr, pageIndex
LED_ROUTE_IMAGES = [None] * 228


# Window.fullscreen = 'auto'
LED_COUNT = 198
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0


# LED_STRIP                = ws.WS2811_STRIP_GRB
# strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# strip.begin()


def colorWipe(strip, color, wait_ms=0):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        # time.sleep(wait_ms/1000.0)

def numberToLetter(coord):
    switcher = {

        "1": "A",
        "2": "B",
        "3": "C",
        "4": "D",
        "5": "E",
        "6": "F",
        "7": "G",
        "8": "H",
        "9": "I",
        "10": "J",
        "11": "K",
    }
    return switcher.get(coord, None)

def flipRow(coord):
    switcher = {

        "18": "1",
        "17": "2",
        "16": "3",
        "15": "4",
        "14": "5",
        "13": "6",
        "12": "7",
        "11": "8",
        "10": "9",
        "9": "10",
        "8": "11",
        "7": "12",
        "6": "13",
        "5": "14",
        "4": "15",
        "3": "16",
        "2": "17",
        "1": "18",
    }
    return switcher.get(coord, None)

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


def picIndexLookUp(index):
    switcher = {
        # REVERSE
        0: 10,
        1: 9,
        2: 8,
        3: 7,
        4: 6,
        5: 5,
        6: 4,
        7: 3,
        8: 2,
        9: 1,
        10: 0,
        # NORMAL
        11: 11,
        12: 12,
        13: 13,
        14: 14,
        15: 15,
        16: 16,
        17: 17,
        18: 18,
        19: 19,
        20: 20,
        21: 21,
        # REVERSE
        22: 32,
        23: 31,
        24: 30,
        25: 29,
        26: 28,
        27: 27,
        28: 26,
        29: 25,
        30: 24,
        31: 23,
        32: 22,
        # NORMAL
        33: 33,
        34: 34,
        35: 35,
        36: 36,
        37: 37,
        38: 38,
        39: 39,
        40: 40,
        41: 41,
        42: 42,
        43: 43,
        # REVERSE
        44: 54,
        45: 53,
        46: 52,
        47: 51,
        48: 50,
        49: 49,
        50: 48,
        51: 47,
        52: 46,
        53: 45,
        54: 44,
        # NORMAL
        55: 55,
        56: 56,
        57: 57,
        58: 58,
        59: 59,
        60: 60,
        61: 61,
        62: 62,
        63: 63,
        64: 64,
        65: 65,
        # REVERSE
        66: 76,
        67: 75,
        68: 74,
        69: 73,
        70: 72,
        71: 71,
        72: 70,
        73: 69,
        74: 68,
        75: 67,
        76: 66,
        # NORMAL
        77: 77,
        78: 78,
        79: 79,
        80: 80,
        81: 81,
        82: 82,
        83: 83,
        84: 84,
        85: 85,
        86: 86,
        87: 87,
        # REVERSE
        88: 98,
        89: 97,
        90: 96,
        91: 95,
        92: 94,
        93: 93,
        94: 92,
        95: 91,
        96: 90,
        97: 89,
        98: 88,
        # NORMAL
        99: 99,
        100: 100,
        101: 101,
        102: 102,
        103: 103,
        104: 104,
        105: 105,
        106: 106,
        107: 107,
        108: 108,
        109: 109,
        # REVERSE
        110: 120,
        111: 119,
        112: 118,
        113: 117,
        114: 116,
        115: 115,
        116: 114,
        117: 113,
        118: 112,
        119: 111,
        120: 110,
        # NORMAL
        121: 121,
        122: 122,
        123: 123,
        124: 124,
        125: 125,
        126: 126,
        127: 127,
        128: 128,
        129: 129,
        130: 130,
        131: 131,
        # REVERSE
        132: 142,
        133: 141,
        134: 140,
        135: 139,
        136: 138,
        137: 137,
        138: 136,
        139: 135,
        140: 134,
        141: 133,
        142: 132,
        # NORMAL
        143: 143,
        144: 144,
        145: 145,
        146: 146,
        147: 147,
        148: 148,
        149: 149,
        150: 150,
        151: 151,
        152: 152,
        153: 153,
        # REVERSE
        154: 164,
        155: 163,
        156: 162,
        157: 161,
        158: 160,
        159: 159,
        160: 158,
        161: 157,
        162: 156,
        163: 155,
        164: 154,
        # NORMAL
        165: 165,
        166: 166,
        167: 167,
        168: 168,
        169: 169,
        170: 170,
        171: 171,
        172: 172,
        173: 173,
        174: 174,
        175: 175,
        # REVERSE
        176: 186,
        177: 185,
        178: 184,
        179: 183,
        180: 182,
        181: 181,
        182: 180,
        183: 179,
        184: 178,
        185: 177,
        186: 176,
        # NORMAL
        187: 187,
        188: 188,
        189: 189,
        190: 190,
        191: 191,
        192: 192,
        193: 193,
        194: 194,
        195: 195,
        196: 196,
        197: 197,
    }
    #print(index)
    return switcher.get(index, None)


class DbCon:
    def __init__(self):
        self.filteredCommandStr = ""
        self.orderCommandStr = ""
        self.db = pymysql.connect(host="localhost", user="root", passwd="root", db="climbingholdsape")
        self.c = self.db.cursor()

    def get_rows(self):
        self.c.execute("(SELECT * FROM Moonboard ORDER BY DateAdded ASC LIMIT 0,10)")
        return self.c.fetchall()

    def get_rows_filtered(self, v4plus, v5, v5plus, v6, v7, v8, v8plus, v9, v10, v11, v12, v13, v14, star3, star2, star1,
                          star0, popular, newest, random, search):
        global filteredCommandStr, orderCommandStr, addedCommandStr, filterBox, pageIndex
        filteredCommandStr = ""
        orderCommandStr = ""
        addedCommandStr = ""
        #print(popular)
        if v4plus:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V4+' "
        if v5:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("

            filteredCommandStr += "GradeUS = 'V5'"
        if v5plus:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V5+'"
        if v6:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V6'"
        if v7:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V7'"
        if v8:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V8'"
        if v8plus:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V8+'"
        if v9:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V9'"
        if v10:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V10'"
        if v11:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V11'"
        if v12:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V12'"
        if v13:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V13'"
        if v14:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "GradeUS = 'V14'"
        if v4plus or v5 or v5plus or v6 or v7 or v8 or v8plus or v9 or v10 or v11 or v12 or v13 or v14:
            filteredCommandStr += ") "
            if star0 or star1 or star2 or star3:
                filteredCommandStr += "AND ("
        else:
            filteredCommandStr += " WHERE ("
        if star0:
            filteredCommandStr += "Stars = 0"
        if star1:
            if star0:
                filteredCommandStr += " OR "
            filteredCommandStr += "Stars = 1"
        if star2:
            if star0 or star1:
                filteredCommandStr += " OR "
            filteredCommandStr += "Stars = 2"
        if star3:
            if star0 or star1 or star2:
                filteredCommandStr += " OR "
            filteredCommandStr += "Stars = 3"
        if star0 or star1 or star2 or star3:
            filteredCommandStr += ")"
        if filteredCommandStr == " WHERE (":
            filteredCommandStr += "Stars = 4)"
        #print(filteredCommandStr)
        if popular and newest:
            # print("popular: " + str(popular) + "NEWEST: " + str(newest) + " Random: " + str(random))
            orderCommandStr = " ORDER BY DateAdded ASC "
            addedCommandStr = " ORDER BY Repeats DESC"
        elif popular:
            # print("popular: " + str(popular) + "NEWEST: " + str(newest) + " Random: " + str(random))
            orderCommandStr = " ORDER BY Repeats DESC "
            addedCommandStr = ""
        elif newest:
            # print("popular: " + str(popular) + "NEWEST: " + str(newest) + " Random: " + str(random))
            orderCommandStr = " ORDER BY DateAdded ASC "
            addedCommandStr = ""
        elif not popular and not newest:
            # print("popular: " + str(popular) + "NEWEST: " + str(newest) + " Random: " + str(random))
            orderCommandStr = " ORDER BY DateAdded DESC "
            addedCommandStr = ""
        elif popular and not newest:
            # orderCommandStr = " ORDER BY DateAdded DESC "
            addedCommandStr = " ORDER BY Repeats DESC"
        if random:
            # print("popular: " + str(popular) + "NEWEST: " + str(newest) + " Random: " + str(random))
            addedCommandStr = " ORDER BY RAND() "
        else:
            filterBox[19] = False
            addCommandStr = ""
        #print(orderCommandStr)

        #execute = "SELECT * FROM Moonboard" + filteredCommandStr + " AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '')"  "REGEXP '.*%s.*'" + orderCommandStr + "LIMIT 0,100" % search
        #print(execute)
        #print("(SELECT * FROM Moonboard" + filteredCommandStr + " AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '') REGEXP '%s'" % search + "" + orderCommandStr + "LIMIT "  + str(pageIndex*10) + ",10)" + addedCommandStr)
        self.c.execute("(SELECT * FROM Moonboard" + filteredCommandStr + " AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '') REGEXP '%s'" % search + "" + orderCommandStr + "LIMIT " + str(pageIndex*10) + ",10)" + addedCommandStr)
        return self.c.fetchall()

    def get_rows_searched(self, search=""):
        # self.c.execute("SELECT * FROM Moonboard WHERE Author REGEXP '.*%s.*' LIMIT 30" % search)
        #print("SELECT * from moonboard" + filteredCommandStr + " AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '') REGEXP '.*%s.*'" % search)
        global filteredCommandStr, pageIndex
        if filteredCommandStr == "":
            #print(filteredCommandStr)
            pageNum = str(pageIndex * 10)
            #print(pageNum)
            #print("SELECT * from moonboard WHERE (GradeUS = 'V4+'  OR GradeUS = 'V5' OR GradeUS = 'V5+' OR GradeUS = 'V6' OR GradeUS = 'V7' OR GradeUS = 'V8' OR GradeUS = 'V8+' OR GradeUS = 'V9' OR GradeUS = 'V10' OR GradeUS = 'V11' OR GradeUS = 'V12' OR GradeUS = 'V13' OR GradeUS = 'V14') AND (Stars = 0 OR Stars = 1 OR Stars = 2 OR Stars = 3) AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '') REGEXP '%s' ORDER BY DateAdded ASC LIMIT " % search + str(pageIndex*10) + ",10" )
            self.c.execute(
                #"SELECT * from moonboard WHERE (GradeUS = 'V4+'  OR GradeUS = 'V5' OR GradeUS = 'V5+' OR GradeUS = 'V6' OR GradeUS = 'V7' OR GradeUS = 'V8' OR GradeUS = 'V8+' OR GradeUS = 'V9' OR GradeUS = 'V10' OR GradeUS = 'V11' OR GradeUS = 'V12' OR GradeUS = 'V13' OR GradeUS = 'V14') AND (Stars = 0 OR Stars = 1 OR Stars = 2 OR Stars = 3) AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '') REGEXP '.*%s.*' ORDER BY DateAdded ASC LIMIT 100" % search)
                #"SELECT * from moonboard WHERE (GradeUS = 'V4+'  OR GradeUS = 'V5' OR GradeUS = 'V5+' OR GradeUS = 'V6' OR GradeUS = 'V7' OR GradeUS = 'V8' OR GradeUS = 'V8+' OR GradeUS = 'V9' OR GradeUS = 'V10' OR GradeUS = 'V11' OR GradeUS = 'V12' OR GradeUS = 'V13' OR GradeUS = 'V14') AND (Stars = 0 OR Stars = 1 OR Stars = 2 OR Stars = 3) AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '') REGEXP '.*%s.*' ORDER BY DateAdded ASC LIMIT 100" % search

                "SELECT * from moonboard WHERE (GradeUS = 'V4+'  OR GradeUS = 'V5' OR GradeUS = 'V5+' OR GradeUS = 'V6' OR GradeUS = 'V7' OR GradeUS = 'V8' OR GradeUS = 'V8+' OR GradeUS = 'V9' OR GradeUS = 'V10' OR GradeUS = 'V11' OR GradeUS = 'V12' OR GradeUS = 'V13' OR GradeUS = 'V14') AND (Stars = 0 OR Stars = 1 OR Stars = 2 OR Stars = 3) AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '') REGEXP '%s' ORDER BY DateAdded ASC LIMIT " % search + str(pageIndex*10) + ",10" )

        else:
            #print("Filtered Command:"+filteredCommandStr)
            #print(                "SELECT * from moonboard" + filteredCommandStr + " AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '') REGEXP '%s' ORDER BY DateAdded ASC LIMIT 0,10" % search)
            self.c.execute(
                "SELECT * from moonboard" + filteredCommandStr + " AND concat(Author, '', moonboard.Name, '',  GradeUK, '', GradeUS, '', Moves, '', Stars, '', Repeats, '') REGEXP '%s' ORDER BY DateAdded ASC LIMIT 0,10" % search)
        return self.c.fetchall()

class SearchButton(Button):
    def on_press(self):
        return 0  # print("TODO mySQL search")


class Problem(Button):
    route = [None] * 205
    global LED_ROUTE_IMAGES
    routeName = ""
    setterName = ""
    gradeUK = ""
    gradeUS = ""
    stars = 0
    moves = 0
    repeats = 0

    def on_press(self):
        colorWipe(strip, Color(0, 0, 0))
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

        temp = 2  # starting index in route that intermediate holds belong to
        temp2 = 4
        while self.route[temp] != '0':
            self.coordLED[temp2] = moonToLED(self.route[temp])
            #print(self.coordLED[temp2])
            temp2 += 1
            temp += 1
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
                    strip.setPixelColorRGB(self.coordLED[index], 255, 0, 0)
            elif index > 3 and index < 196:
                if self.coordLED[index] != None:
                    self.colorLED[self.coordLED[index]] = 2
                    strip.setPixelColorRGB(self.coordLED[index], 0, 0, 255)
                    # else:
                    # 	#colorLED[coordLED[index]] = 0
            else:
                if self.coordLED[index] != None:
                    self.colorLED[self.coordLED[index]] = 3
                    strip.setPixelColorRGB(self.coordLED[index], 0, 255, 0)
                    # else:
                    # 	#colorLED[coordLED[index]] = 0
            index += 1
        index = 0
        while index < len(self.colorLED):
            if self.colorLED[index] == None:
                self.colorLED[index] = 0
                strip.setPixelColorRGB(index, 0, 0, 0)
            index += 1
        strip.show()

        # picturesAdjusted(LED_ROUTE_IMAGES)

        self.tmp = 0  # running index for 228 images
        self.TEMP = 197  # running index for 197 LEDs
        self.REVERSE = True
        for i in range(19):
            for j in range(12):
                #print("i=&s", i)
                #print("j=&s", j)
                if self.tmp < 13:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 24:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 36:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 48:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 60:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 72:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 84:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 96:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 108:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 120:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 132:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 144:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 156:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 168:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 180:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 192:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 204:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                elif self.tmp == 216:
                    imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    LED_ROUTE_IMAGES[self.tmp].reload()
                else:
                    # imageIndex = picIndexLookUp(self.tmp)
                    # since LED's go in zig zags, we need to adjust mirror numbers.
                    if self.colorLED[picIndexLookUp(self.TEMP)] == 0:
                        #print("NO COLOR")
                        imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                        LED_ROUTE_IMAGES[self.tmp].source = imageStr
                        LED_ROUTE_IMAGES[self.tmp].reload()
                    elif self.colorLED[picIndexLookUp(self.TEMP)] == 1:
                        #print("i=&s", i)
                        #print("j=&s", j)
                        #print("BLUE")
                        imageStr = str("images/moon-" + str(i) + "-" + str(j) + "-green-square.png")
                        LED_ROUTE_IMAGES[self.tmp].source = imageStr
                        LED_ROUTE_IMAGES[self.tmp].reload()
                    elif self.colorLED[picIndexLookUp(self.TEMP)] == 2:
                        imageStr = str("images/moon-" + str(i) + "-" + str(j) + "-blue-square.png")
                        LED_ROUTE_IMAGES[self.tmp].source = imageStr
                        LED_ROUTE_IMAGES[self.tmp].reload()
                        #print("RED")
                    elif self.colorLED[picIndexLookUp(self.TEMP)] == 3:
                        imageStr = str("images/moon-" + str(i) + "-" + str(j) + "-red-square.png")
                        LED_ROUTE_IMAGES[self.tmp].source = imageStr
                        LED_ROUTE_IMAGES[self.tmp].reload()
                        #print("GREEN")
                    else:
                        print("WE HAVE A PROBLEM")

                    #print(self.tmp)
                    #print(self.TEMP)
                    self.TEMP -= 1
                    # adjust Row and Column

                # self.moonImagesArray[temp]
                self.tmp += 1
                # print(self.tmp)
                # print(self.TEMP)

        # global LED_ROUTE_IMAGES = colorLED[]
        #print(self.routeName)
        #print(self.setterName)
        #print(self.gradeUK)
        #print(self.gradeUS)
        #print(self.stars)
        #print(self.moves)
        #print(self.repeats)
        #print(self.route)
        #print(self.coordLED)
        #print(self.colorLED)


class FilterBox(CheckBox):
    def __init__(self, **kwargs):
        super(FilterBox, self).__init__(**kwargs)
        #self.active = True

    #text = ""


class moonBoardProblemImage(GridLayout):
    def __init__(self, **kwargs):
        super(moonBoardProblemImage, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.cols = 12
        self.padding = 0
        self.spacing = 0


class moonBoardImage(Image):
    def update(self):
        self.source = "images/moon-1-1-blue-square.png"
        print("Call to Update")
        self.reload()

    pass

class moonBoardButton(Button):
    route = [None] * 205
    global LED_ROUTE_IMAGES
    def __init__(self, **kwargs):
        super(moonBoardButton, self).__init__(**kwargs)
        self.index = 0
        self.regularImage = self.background_normal

    def update(self):
        self.source = "images/moon-1-1-blue-square.png"
        #print("Call to Update")
        self.reload()

    def on_press(self):
        # self.coordLED = [None] * 198
        # self.colorLED = [0] * 198

        #print(self.index)
        #print(self.background_normal)

        imageStrTemp = self.regularImage
        coordinates = imageStrTemp.split('-',1)[1]
        ycoordinate = coordinates.split('-', 1)[0]
        #ycoordinateAdjusted = picIndexLookUp(int(ycoordinate))
        xcoordinate = coordinates.split('-', 1)[1].split('.', 1)[0]
        #print(coordinates)
        #print(xcoordinate)
        #print(ycoordinate)
        imageStrTemp = imageStrTemp.split('.',1)[0]
        letterCoordinate = numberToLetter(xcoordinate)
        ycoordinateAdjusted = flipRow(ycoordinate)
        #print(letterCoordinate + ycoordinateAdjusted)
        if not ycoordinate == str(0) and not xcoordinate == str(0):

            self.index+=1
            if self.index == 6:
                self.index = 0
            if self.index == 0:
                self.background_normal = self.regularImage
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                # strip.setPixelColorRGB(LEDNum, 0, 0, 0)
                print(self.index)
            if self.index == 1:
                self.background_normal = imageStrTemp + "-blue-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                # strip.setPixelColorRGB(LEDNum, 0, 0, 255)
                print(LEDNum)
            if self.index == 2:
                self.background_normal = imageStrTemp + "-red-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                # strip.setPixelColorRGB(LEDNum, 255, 0, 0)
            if self.index == 3:
                self.background_normal = imageStrTemp + "-green-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                # strip.setPixelColorRGB(LEDNum, 0, 255, 0)
            if self.index == 4:
                self.background_normal = imageStrTemp + "-yellow-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                #strip.setPixelColorRGB(LEDNum, 255, 255, 0)
            if self.index == 5:
                self.background_normal = imageStrTemp + "-white-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                #strip.setPixelColorRGB(LEDNum, 255, 255, 255)
            #print(self.background_normal)
         #strip.show()


    pass


class MoonboardAppLayout(GridLayout):


    def __init__(self, **kwargs):
        super(MoonboardAppLayout, self).__init__(**kwargs)
        # self.moonImagesArray = [None] * 228
        self.cols = 2
        self.rows = 2
        self.db = DbCon()
        global Routes, problemButton, filterBox, FilterLabel, filteredCommandStr, orderCommandStr, pageIndex
        #filteredCommandStr = " WHERE (GradeUS = 'V4+' OR GradeUS = 'V5' OR GradeUS = 'V5+' OR GradeUS = 'V6' OR GradeUS = 'V7' OR GradeUS = 'V8' OR GradeUS = 'V8+' OR GradeUS = 'V9' OR GradeUS = 'V10' OR GradeUS = 'V11' OR GradeUS = 'V12' OR GradeUS = 'V13' OR GradeUS = 'V14') AND (Stars = 0 OR Stars = 1 OR Stars = 2 OR Stars = 3) ORDER BY DateAdded ASC LIMIT 0,100"
        filteredCommandStr = ""
        orderCommandStr = "ORDER BY RAND() "
        pageIndex = 0
        Routes = self.db.get_rows()
        problemButton = [None] * len(Routes)
        filterBox = [None] * 20
        FilterLabel = [None] * 19
        filterBox[19] = False
        self.moonImages = [None] * 240
        self.problemList = GridLayout(cols=1, size_hint_y=None)
        self.problemList.bind(minimum_height=self.problemList.setter('height'))
        toggleText = ["6B+/V4+", "6C/V5", "6C+/V5+", "7A/V6", "7A+/V7", "7B/V8", "7B+/V8+", "7C/V9", "7C+/V10", "8A/V11", "8A+/V12", "8B/V13", "8B+/V14", "3 Stars",
                      "2 Stars", "1 Star", "0 Stars", "Popular", "Newest"]
        for i in range(len(Routes)):
        #for i in range(10):
            problemButton[i] = Problem(
                text=str(Routes[i][0] + '\n' + "Set By: " + Routes[i][1]) + '\n' + "Grade: " + Routes[i][2] + '/' +
                     Routes[i][3] + " Stars: " + str(Routes[i][4]) + '\n' + "Moves: " + str(Routes[i][5]) + '     ' + "Repeats: " + str(Routes[i][6]),
                size_hint_y=None)
            problemButton[i].route = Routes[i][7:211]
            problemButton[i].routeName = str(Routes[i][0])
            problemButton[i].setterName = str(Routes[i][1])
            problemButton[i].gradeUK = str(Routes[i][2])
            problemButton[i].gradeUS = str(Routes[i][3])
            problemButton[i].stars = Routes[i][4]
            problemButton[i].moves = Routes[i][5]
            problemButton[i].repeats = Routes[i][6]
            self.problemList.add_widget(problemButton[i])
        self.moonImageGroup = moonBoardProblemImage()
        self.temp = 0
        for i in range(19):
            for j in range(12):
                self.imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                global LED_ROUTE_IMAGES
                LED_ROUTE_IMAGES[self.temp] = moonBoardImage(source=self.imageStr, size_hint_y=1, size_hint_x=1,
                                                             allow_stretch=True, keep_ratio=False)
                # self.moonImagesArray[temp]
                self.temp += 1
        for i in range(228):
            self.moonImageGroup.add_widget(LED_ROUTE_IMAGES[i])

        self.moonboardProblemsScroll = ScrollView()
        self.search_field = BoxLayout()
        self.navigation_field = BoxLayout()
        self.customizeBox = GridLayout(cols=1, size_hint_y=None)
        self.search_input = TextInput(text="", multiline=False)
        self.search_button = SearchButton(text="search", on_press=self.search)
        self.next_page_button = Button(text=">", on_press=self.pageIncrease)
        self.random_button = Button(text="Random", on_press=self.randomPressed)
        self.prev_page_button = Button(text="<", on_press=self.pageDecrease)
        self.customize = Button(text="Create Your Own!", on_press=self.custom_screen)
        self.return_home = Button(text="Return Home", on_press=self.home_screen)
        #self.nextPage = SearchButton(text="search", on_press=self.search)
        self.searchGrid = GridLayout(cols=1)
        self.navigateGrid = GridLayout(rows=2, orientation="vertical", size_hint_y=None)
        self.filterGroup = GridLayout(cols=4)

        self.add_widget(self.navigateGrid)
        self.add_widget(self.customizeBox)
        self.moonboardProblemsScroll.add_widget(self.problemList)
        self.add_widget(self.moonboardProblemsScroll)
        self.add_widget(self.searchGrid)


        for i in range(len(toggleText)):

            if toggleText[i] == "Popular":
                #print("FALSE CHECKBOX")
                filterBox[i] = FilterBox(on_press=self.filter, active=False)
            elif toggleText[i] == "Newest":
                #print("FALSE CHECKBOX")
                filterBox[i] = FilterBox(on_press=self.filter, active=True)
            else:
                filterBox[i] = FilterBox(on_press=self.filter, active=True)
            # print(filterBox[i])
            # lastFilterBox[i] = filterBox[i]
            FilterLabel[i] = Label()
            FilterLabel[i].text = toggleText[i]
            self.filterGroup.add_widget(filterBox[i])
            self.filterGroup.add_widget(FilterLabel[i])
        self.searchGrid.add_widget(self.filterGroup)
        self.searchGrid.add_widget(self.moonImageGroup)
        self.search_field.add_widget(self.search_input)
        self.search_field.add_widget(self.search_button)
        self.navigation_field.add_widget(self.prev_page_button)
        self.navigation_field.add_widget(self.random_button)
        self.navigation_field.add_widget(self.next_page_button)
        self.navigateGrid.add_widget(self.search_field)
        self.navigateGrid.add_widget(self.navigation_field)
        self.customizeBox.add_widget(self.customize)


        #self.add_widget(self.nextPage)


        # self.moonImagesArray[13].source = "images/moon-1-1-blue-square.png"
        # self.moonImagesArray[14].source = "images/moon-1-1-blue-square.png"
        # self.moonImagesArray.reload()



    def randomPressed(self, random):

        global filterBox, pageIndex
        if filterBox[19] == False:
            filterBox[19] = True
        pageIndex = 0

        self.filter()


    def pageIncrease(self, pageNum):  #TODO account for something like remaining 99 if there isn't an even search
        global Routes, pageIndex, filterBox
        #print(pageIndex)
        #print(len(Routes))
        filterBox[19] = False
        if (len(Routes) > 9):
            pageIndex+=1
        else:
            pageIndex+=0
        self.filter()


    def pageDecrease(self, pageNum):  #TODO account for something like remaining 99 if there isn't an even search
        global Routes, pageIndex, filterBox
        #print(pageIndex)
        #print(len(Routes))

        filterBox[19] = False
        if (pageIndex > 0):
            pageIndex-=1
        else:
            pageIndex+=0
        self.filter()

    def creationScreen(self, *args):
        return 0

    def filter_table(self, search=""):
        global Routes, filterBox, pageIndex
        # if filterBox[17].active or filterBox[18].active:
        #     filterBox[19] = False
        if filterBox[19]:
            filterBox[17].active = False
            filterBox[18].active = False

        #Routes = self.db.get_rows_filtered(filterBox[0].active, filterBox[1].active, filterBox[2].active, filterBox[3].active, filterBox[4].active, filterBox[5].active, filterBox[6].active, filterBox[7].active, filterBox[8].active, filterBox[9].active, filterBox[10].active, filterBox[11].active, filterBox[12].active, filterBox[13].active, filterBox[14].active, filterBox[15].active, filterBox[16].active, filterBox[17].active, filterBox[18].active, filterBox[19].active, search)
        Routes = self.db.get_rows_filtered(filterBox[0].active, filterBox[1].active, filterBox[2].active,
                                           filterBox[3].active, filterBox[4].active, filterBox[5].active,
                                           filterBox[6].active, filterBox[7].active, filterBox[8].active,
                                           filterBox[9].active, filterBox[10].active, filterBox[11].active,
                                           filterBox[12].active, filterBox[13].active, filterBox[14].active,
                                           filterBox[15].active, filterBox[16].active, filterBox[17].active,
                                           filterBox[18].active, filterBox[19], search)
        for index in range(len(Routes)):
            #print(Routes[index])
            #print(len(Routes[index]))
            problemButton[index] = Problem(
                text=str(Routes[index][0] + '\n' + "Set By: " + Routes[index][1]) + '\n' + "Grade: " + Routes[index][2] + '/' +
                     Routes[index][3] + " Stars: " + str(Routes[index][4]) + '\n' + "Moves: " + str(Routes[index][5]) + '     ' + "Repeats: " + str(Routes[index][6]),
                size_hint_y=None)
            problemButton[index].route = Routes[index][7:211]
            problemButton[index].routeName = str(Routes[index][0])
            problemButton[index].setterName = str(Routes[index][1])
            problemButton[index].gradeUK = str(Routes[index][2])
            problemButton[index].gradeUS = str(Routes[index][3])
            problemButton[index].stars = Routes[index][4]
            problemButton[index].moves = Routes[index][5]
            problemButton[index].repeats = Routes[index][6]
            self.problemList.add_widget(problemButton[index])


    def update_table(self, search=""):
        global Routes
        Routes = self.db.get_rows_searched(search)
        #print(Routes)
        for index in range(len(Routes)):
            problemButton[index] = Problem(
                text=str(Routes[index][0].decode('utf-8') + '\n' + "Set By: " + Routes[index][1]) + '\n' + "Grade: " + Routes[index][2] + '/' +
                     Routes[index][3] + " Stars: " + str(Routes[index][4]) + '\n' + "Moves: " + str(Routes[index][5]) + '     ' + "Repeats: " + str(Routes[index][6]),
                size_hint_y=None)
            problemButton[index].route = Routes[index][7:211]
            problemButton[index].routeName = str(Routes[index][0])
            problemButton[index].setterName = str(Routes[index][1])
            problemButton[index].gradeUK = str(Routes[index][2])
            problemButton[index].gradeUS = str(Routes[index][3])
            problemButton[index].stars = Routes[index][4]
            problemButton[index].moves = Routes[index][5]
            problemButton[index].repeats = Routes[index][6]
            self.problemList.add_widget(problemButton[index])

    def clear_table(self):
        self.problemList.clear_widgets()

    def custom_screen(self, custom):
        #colorWipe(strip, Color(0, 0, 0))
        self.clear_widgets()
        self.cols = 1
        self.return_home.size_hint_y = None
        self.moonImageGroup = moonBoardProblemImage()
        self.temp = 0
        for i in range(19):
            for j in range(12):
                self.imageStr = str("images/moon-" + str(i) + "-" + str(j) + ".png")
                global LED_ROUTE_IMAGES
                LED_ROUTE_IMAGES[self.temp] = moonBoardButton(background_normal=self.imageStr, background_down=self.imageStr, size_hint_y=1, size_hint_x=1,
                                                             allow_stretch=False, keep_ratio=True, border=(0,0,0,0))
                # self.moonImagesArray[temp]
                self.temp += 1
        for i in range(228):
            self.moonImageGroup.add_widget(LED_ROUTE_IMAGES[i])

        self.add_widget(self.moonImageGroup)
        self.add_widget(self.return_home)
        #dataApp.build()

    def home_screen(self, home):
        self.clear_widgets()
        self.__init__()

    # def change_button_image(self, random):
    #     print(self.imageStr)




    def search(self, *args):
        global pageIndex
        pageIndex = 0
        self.clear_table()
        if "\'" in self.search_input.text:
            temp = self.search_input.text
            temp = temp.replace("'","+[^.apostrophe.]+")
            #print(temp)
            try:
                self.update_table(temp)
            except:
                pass
        elif "\\" in self.search_input.text:
                temp = self.search_input.text
                temp = temp.replace("\\", "+[^.solidus.]+")
                #print(temp)
                try:
                    self.update_table(temp)
                except:
                    pass
        elif self.search_input.text == '':
            temp = self.search_input.text
            temp = temp.replace("",".*.*")
            #print(temp)
            try:
                self.filter_table(temp)
            except:
                pass
        else:
            try:
                self.update_table(self.search_input.text)
            except:
                pass

    def filter(self, *args):
        self.clear_table()
        if "\'" in self.search_input.text:
            temp = self.search_input.text
            temp = temp.replace("'","+[^.apostrophe.]+")
            #print(temp)
            try:
                self.filter_table(temp)
            except:
                pass
        elif "\\" in self.search_input.text:
                temp = self.search_input.text
                temp = temp.replace("\\", "+[[.solidus.]]+")
                #print(temp)
                try:
                    self.filter_table(temp)
                except:
                    pass
        elif self.search_input.text == '':
            temp = self.search_input.text
            temp = temp.replace("",".*.*")
            #print(temp)
            try:
                self.filter_table(temp)
            except:
                pass
        else:
            try:
                self.filter_table(self.search_input.text)
            except:
                pass


class DatabaseApp(App):
    def build(self):
        self.title = "MOONBOARD"
        parent = BoxLayout(size=(Window.width, Window.height))
        self.gridsDisplay = MoonboardAppLayout()
        parent.add_widget(self.gridsDisplay)
        return parent


dataApp = DatabaseApp()
dataApp.run()
