# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from neopixel import *
import sys
import time

import pymysql
import pymysql.cursors
from kivy.app import App
from kivy.cache import Cache
from kivy.config import Config
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput

reload(sys)
sys.setdefaultencoding('utf-8')
LabelBase.register(name="NotoSans",
                   fn_regular="NotoSans-hinted/NotoSansUI-Regular.ttf",
                   fn_bold="NotoSans-hinted/NotoSansUI-Bold.ttf",
                   fn_italic="NotoSans-hinted/NotoSansUI-Italic.ttf",
                   fn_bolditalic="NotoSans-hinted/NotoSansUI-BoldItalic.ttf")
Config.set('graphics', 'default_font',
           '[‘Roboto’, ‘data/fonts/uming.ttc’, ‘data/fonts/uming.ttc’, ‘data/fonts/uming.ttc’, ‘data/fonts/uming.ttc’]')

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

'''
In order to not have to access the SD card which can be slow, here we make sure everything stays in the cache increasing performance. (Hopefully)
'''
Cache.register('kv.image', limit=None, timeout=None)

# Window.fullscreen = 'auto'
LED_COUNT = 198
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 5
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0


LED_STRIP = ws.WS2811_STRIP_GRB
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
strip.begin()


def colorWipe(strip, color, wait_ms=0):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        # time.sleep(wait_ms/1000.0)


def getVGrade(fontGrade):
    switcher = {
        "5+": "V2",
        "6a": "V3",
        "6a+": "V3+",
        "6B": "V4",
        "6b": "V4",
        "6B+": "V4+",
        "6b+": "V4+",
        "6C": "V5",
        "6c": "V5",
        "6C+": "V5+",
        "6c+": "V5+",
        "7A": "V6",
        "7a": "V6",
        "7A+": "V7",
        "7a+": "V7",
        "7B": "V8",
        "7b": "V8",
        "7B+": "V8+",
        "7b+": "V8+",
        "7C": "V9",
        "7c": "V9",
        "7C+": "V10",
        "7c+": "V10",
        "8A": "V11",
        "8a": "V11",
        "8A+": "V12",
        "8a+": "V12",
        "8B": "V13",
        "8b": "V13",
        "8B+": "V14",
        "8b+": "V14",
        "8C": "V15",
        "8c": "V15"
    }
    return switcher.get(fontGrade, None)


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
    # print(index)
    return switcher.get(index, None)


class DbCon:
    def __init__(self):
        self.filteredCommandStr = ""
        self.orderCommandStr = ""
        self.db = pymysql.connect(host="localhost", user="root", passwd="root", db="climbingholdsape")
        self.c = self.db.cursor()

    def get_rows(self):
        self.c.execute("(SELECT * FROM routes ORDER BY DateInserted DESC LIMIT 0,10)")
        return self.c.fetchall()

    def get_rows_filtered(self, v4, v4plus, v5, v5plus, v6, v7, v8, v8plus, v9, v10, v11, v12, v13, v14, star3, star2,
                          star1,
                          star0, popular, newest, benchmark, search):
        global filteredCommandStr, orderCommandStr, addedCommandStr, filterBox, pageIndex
        filteredCommandStr = ""
        orderCommandStr = ""
        addedCommandStr = ""
        if v4:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"6B\"' "
        if v4plus:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"6B+\"' "
        if v5:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("

            filteredCommandStr += "Grade = '\"6C\"'"
        if v5plus:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"6C+\"'"
        if v6:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"7A\"'"
        if v7:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"7A+\"'"
        if v8:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"7B\"'"
        if v8plus:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"V8+\"'"
        if v9:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"7C\"'"
        if v10:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"7C+\"'"
        if v11:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"8A\"'"
        if v12:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"8A+\"'"
        if v13:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"8B\"'"
        if v14:
            if filteredCommandStr != "":
                filteredCommandStr += " OR "
            else:
                filteredCommandStr += " WHERE ("
            filteredCommandStr += "Grade = '\"8B+\"'"
        if v4plus or v5 or v5plus or v6 or v7 or v8 or v8plus or v9 or v10 or v11 or v12 or v13 or v14:
            filteredCommandStr += ") "
            if star0 or star1 or star2 or star3:
                filteredCommandStr += "AND ("
        else:
            filteredCommandStr += " WHERE ("
        if star0:
            filteredCommandStr += "UserRating = 0"
        if star1:
            if star0:
                filteredCommandStr += " OR "
            filteredCommandStr += "UserRating = 1"
        if star2:
            if star0 or star1:
                filteredCommandStr += " OR "
            filteredCommandStr += "UserRating = 2"
        if star3:
            if star0 or star1 or star2:
                filteredCommandStr += " OR "
            filteredCommandStr += "UserRating = 3"
        if star0 or star1 or star2 or star3:
            filteredCommandStr += ")"
        if benchmark:
            filteredCommandStr += " AND (isBenchmark = 1)"
        if popular and newest:
            orderCommandStr = " ORDER BY DateInserted ASC "
            addedCommandStr = " ORDER BY Repeats DESC"
        elif popular:
            orderCommandStr = " ORDER BY Repeats DESC "
            addedCommandStr = ""
        elif newest:
            orderCommandStr = " ORDER BY DateInserted ASC "
            addedCommandStr = ""
        elif not popular and not newest:
            orderCommandStr = " ORDER BY DateInserted DESC "
            addedCommandStr = ""
        elif popular and not newest:
            addedCommandStr = " ORDER BY Repeats DESC"
        else:
            filterBox[20] = False
        print(
        "(SELECT * FROM routes" + filteredCommandStr + " AND (Method = \'Feet follow hands\' OR Method = \'Footless + kickboard\')" + " AND (HoldSetupDesc = 'MoonBoard Masters 2017') AND (ConfigurationDesc) REGEXP '40'" + " AND concat(SetterNickName, '', routes.Name, '', Grade, '', UserRating, '', Repeats, '') REGEXP '%s'" % search + " AND CONCAT_WS(StartHold1Desc, StartHold2Desc, IntermediateHold1Desc, IntermediateHold2Desc, IntermediateHold3Desc, IntermediateHold4Desc, IntermediateHold5Desc, IntermediateHold6Desc, IntermediateHold7Desc, IntermediateHold8Desc, IntermediateHold9Desc, IntermediateHold10Desc, IntermediateHold11Desc, IntermediateHold12Desc, IntermediateHold13Desc, FinishHold1Desc, FinishHold2Desc) NOT REGEXP 'B5|E5|G5|J5|C6|I6|A7|D7|H7|K7|C9|E9|G9|I9|A10|K10|C11|I11|B12|E12|G12|J12|D13|H13|B15|E15|G15|J15|D16|H16|C18,I18'" + "" + orderCommandStr + "LIMIT " + str(
            pageIndex * 10) + ",10)" + addedCommandStr)
        self.c.execute(
            "(SELECT * FROM routes" + filteredCommandStr + " AND (Method = \'Feet follow hands\' OR Method = \'Footless + kickboard\')" + " AND (HoldSetupDesc = 'MoonBoard Masters 2017') AND (ConfigurationDesc) REGEXP '40'" + " AND concat(SetterNickName, '', routes.Name, '', Grade, '', UserRating, '', Repeats, '') REGEXP '%s'" % search + " AND CONCAT_WS(StartHold1Desc, StartHold2Desc, IntermediateHold1Desc, IntermediateHold2Desc, IntermediateHold3Desc, IntermediateHold4Desc, IntermediateHold5Desc, IntermediateHold6Desc, IntermediateHold7Desc, IntermediateHold8Desc, IntermediateHold9Desc, IntermediateHold10Desc, IntermediateHold11Desc, IntermediateHold12Desc, IntermediateHold13Desc, FinishHold1Desc, FinishHold2Desc) NOT REGEXP 'B5|E5|G5|J5|C6|I6|A7|D7|H7|K7|C9|E9|G9|I9|A10|K10|C11|I11|B12|E12|G12|J12|D13|H13|B15|E15|G15|J15|D16|H16|C18,I18'" + "" + orderCommandStr + "LIMIT " + str(
                pageIndex * 10) + ",10)" + addedCommandStr)
        return self.c.fetchall()

    def get_rows_searched(self, search=""):
        global filteredCommandStr, pageIndex
        if filteredCommandStr == "":
            self.c.execute(
                    "SELECT * FROM routes WHERE (Grade = '\"6B\"' OR Grade = '\"6B+\"'  OR Grade = '\"6C\"' OR Grade = '\"6C+\"' OR Grade = '\"7A\"' OR Grade = '\"7A+\"' OR Grade = '\"7B\"' OR Grade = '\"V8+\"' OR Grade = '\"7C\"' OR Grade = '\"7C+\"' OR Grade = '\"8A\"' OR Grade = '\"8A+\"' OR Grade = '\"8B\"' OR Grade = '\"8B+\"') AND (UserRating = 0 OR UserRating = 1 OR UserRating = 2 OR UserRating = 3)" + " AND (Method = \'Feet follow hands\' OR Method = \'Footless + kickboard\')" + " AND (HoldSetupDesc = 'MoonBoard Masters 2017') AND (ConfigurationDesc) REGEXP '40'" + " AND concat(SetterNickName, '', routes.Name, '', Grade, '', UserRating, '', Repeats, '') REGEXP '%s' AND CONCAT_WS(StartHold1Desc, StartHold2Desc, IntermediateHold1Desc, IntermediateHold2Desc, IntermediateHold3Desc, IntermediateHold4Desc, IntermediateHold5Desc, IntermediateHold6Desc, IntermediateHold7Desc, IntermediateHold8Desc, IntermediateHold9Desc, IntermediateHold10Desc, IntermediateHold11Desc, IntermediateHold12Desc, IntermediateHold13Desc, FinishHold1Desc, FinishHold2Desc) NOT REGEXP 'B5|E5|G5|J5|C6|I6|A7|D7|H7|K7|C9|E9|G9|I9|A10|K10|C11|I11|B12|E12|G12|J12|D13|H13|B15|E15|G15|J15|D16|H16|C18,I18' ORDER BY DateInserted ASC LIMIT " % search + str(
                    pageIndex * 10) + ",10")
        else:
            self.c.execute(
                "SELECT * FROM routes" + filteredCommandStr + " AND (Method = \'Feet follow hands\' OR Method = \'Footless + kickboard\')" + " AND (HoldSetupDesc = 'MoonBoard Masters 2017') AND (ConfigurationDesc) REGEXP '40'" + " AND concat(SetterNickName, '', routes.Name, '',  Grade, '', UserRating, '', Repeats, '') REGEXP '%s' AND CONCAT_WS(StartHold1Desc, StartHold2Desc, IntermediateHold1Desc, IntermediateHold2Desc, IntermediateHold3Desc, IntermediateHold4Desc, IntermediateHold5Desc, IntermediateHold6Desc, IntermediateHold7Desc, IntermediateHold8Desc, IntermediateHold9Desc, IntermediateHold10Desc, IntermediateHold11Desc, IntermediateHold12Desc, IntermediateHold13Desc, FinishHold1Desc, FinishHold2Desc) NOT REGEXP 'B5|E5|G5|J5|C6|I6|A7|D7|H7|K7|C9|E9|G9|I9|A10|K10|C11|I11|B12|E12|G12|J12|D13|H13|B15|E15|G15|J15|D16|H16|C18,I18' ORDER BY DateInserted ASC LIMIT 0,10" % search)
        return self.c.fetchall()


class SearchButton(Button):
    def on_press(self):
        return 0  # print("TODO mySQL search")


class Problem(Button):
    route = [None] * 34
    global LED_ROUTE_IMAGES
    routeName = ""
    setterName = ""
    gradeUK = ""
    Grade = ""
    UserRating = 0
    # moves = 0
    repeats = 0
    font_name = 'DejaVuSans.ttf'

    def on_press(self):
        # colorWipe(strip, Color(0, 0, 0))
        start = time.time()
        self.coordLED = [None] * 34
        '''
            # Example Array setup:   [SH1, SH2, SH3, SH4,IH1,.....IH196,FH1,FH2]   SH1-4  is a combination of 2 hands and 2 feet, Intermediate max is with only 1 hand hold to start and 1 finish 
            # hold max making a remaining 196 Intermediate holds potentially if the wall is filled We need designated locations for these combinations
            '''
        self.colorLED = [0] * 198
        # start holds
        print(self.route)
        self.coordLED[0] = moonToLED(self.route[1])
        self.coordLED[1] = moonToLED(self.route[3])
        self.coordLED[2] = None  # only because of moonboard only having 2 start holds
        self.coordLED[3] = None  # only because of moonboard only having 2 start holds
        # finish Holds
        self.coordLED[31] = moonToLED(self.route[31])
        self.coordLED[33] = moonToLED(self.route[33])

        temp = 5  # starting index in route that intermediate holds belong to
        temp2 = 4
        while self.route[temp] != '':
            self.coordLED[temp2] = moonToLED(self.route[temp])
            temp2 += 1
            temp += 2
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
            elif index > 3 and index < 31:
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
        self.tmp = 0  # running index for 228 images
        self.TEMP = 197  # running index for 197 LEDs
        self.REVERSE = True
        for i in range(19):
            for j in range(12):
                # print("i=&s", i)
                # print("j=&s", j)
                if self.tmp < 13:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 24:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 36:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 48:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 60:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 72:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 84:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 96:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 108:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 120:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 132:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 144:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 156:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 168:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 180:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 192:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 204:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                elif self.tmp == 216:
                    imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                    LED_ROUTE_IMAGES[self.tmp].source = imageStr
                else:
                    # since LED's go in zig zags, we need to adjust mirror numbers.
                    if self.colorLED[picIndexLookUp(self.TEMP)] == 0:
                        imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                        LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    elif self.colorLED[picIndexLookUp(self.TEMP)] == 1:
                        imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-green-square.png")
                        LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    elif self.colorLED[picIndexLookUp(self.TEMP)] == 2:
                        imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-blue-square.png")
                        LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    elif self.colorLED[picIndexLookUp(self.TEMP)] == 3:
                        imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-red-square.png")
                        LED_ROUTE_IMAGES[self.tmp].source = imageStr
                    else:
                        print("WE HAVE A PROBLEM")
                    self.TEMP -= 1
                    # adjust Row and Column
                self.tmp += 1
        end = time.time()
        print(end - start)


class FilterBox(CheckBox):
    def __init__(self, **kwargs):
        super(FilterBox, self).__init__(**kwargs)



class moonBoardProblemImage(GridLayout):
    def __init__(self, **kwargs):
        super(moonBoardProblemImage, self).__init__(**kwargs)
        self.orientation = "horizontal"
        self.cols = 12
        self.padding = 0
        self.spacing = 0


class moonBoardImage(Image):
    def update(self):
        self.source = "images/" + MoonLayout + "moon-1-1-blue-square.png"
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
        self.source = "images/" + MoonLayout + "moon-1-1-blue-square.png"
        self.reload()

    def on_press(self):
        imageStrTemp = self.regularImage
        coordinates = imageStrTemp.split('-', 1)[1]
        ycoordinate = coordinates.split('-', 1)[0]
        xcoordinate = coordinates.split('-', 1)[1].split('.', 1)[0]
        imageStrTemp = imageStrTemp.split('.', 1)[0]
        letterCoordinate = numberToLetter(xcoordinate)
        ycoordinateAdjusted = flipRow(ycoordinate)
        if not ycoordinate == str(0) and not xcoordinate == str(0):
            self.index += 1
            if self.index == 6:
                self.index = 0
            if self.index == 0:
                self.background_normal = self.regularImage
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                strip.setPixelColorRGB(LEDNum, 0, 0, 0)
            if self.index == 1:
                self.background_normal = imageStrTemp + "-blue-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                strip.setPixelColorRGB(LEDNum, 0, 0, 255)
            if self.index == 2:
                self.background_normal = imageStrTemp + "-red-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                strip.setPixelColorRGB(LEDNum, 0, 255, 0)
            if self.index == 3:
                self.background_normal = imageStrTemp + "-green-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                strip.setPixelColorRGB(LEDNum, 255, 0, 0)
            if self.index == 4:
                self.background_normal = imageStrTemp + "-yellow-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                strip.setPixelColorRGB(LEDNum, 255, 255, 0)
            if self.index == 5:
                self.background_normal = imageStrTemp + "-white-square.png"
                LEDNum = moonToLED(letterCoordinate + ycoordinateAdjusted)
                strip.setPixelColorRGB(LEDNum, 255, 255, 255)
        strip.show()

    pass


class MoonboardAppLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MoonboardAppLayout, self).__init__(**kwargs)
        self.cols = 2
        self.rows = 2
        self.db = DbCon()
        global Routes, problemButton, filterBox, FilterLabel, filteredCommandStr, orderCommandStr, pageIndex, MoonLayout
        MoonLayout = "2017/"
        filteredCommandStr = ""
        orderCommandStr = "ORDER BY RAND() "
        pageIndex = 0
        Routes = self.db.get_rows()
        # print(Routes)
        problemButton = [None] * len(Routes)
        filterBox = [None] * 21
        FilterLabel = [None] * 20
        filterBox[20] = False
        self.moonImages = [None] * 240
        self.problemList = GridLayout(cols=1, size_hint_y=None)
        self.problemList.bind(minimum_height=self.problemList.setter('height'))
        toggleText = ["6B+/V4+", "6C/V5", "6C+/V5+", "7A/V6", "7A+/V7", "7B/V8", "7B+/V8+", "7C/V9", "7C+/V10",
                      "8A/V11", "8A+/V12", "8B/V13", "8B+/V14", "3 UserRating",
                      "2 UserRating", "1 Star", "0 UserRating", "Popular", "Newest", "Benchmarks"]
        for i in range(len(Routes)):
            # for i in range(10):
            problemButton[i] = Problem(
                text=(Routes[i][1] + '\n' + "Set By: " + Routes[i][10].encode('utf-8')) + '\n' + "Grade: " + Routes[i][
                    2] + " UserRating: " + str(Routes[i][19]) + '\n' + '     ' + "Repeats: " + str(Routes[i][20]),
                size_hint_y=None)
            # print(Routes[i][34:68])
            problemButton[i].route = Routes[i][34:68]
            problemButton[i].routeName = Routes[i][1]
            problemButton[i].setterName = str(Routes[i][10])
            # problemButton[i].gradeUK = str(Routes[i][2])
            problemButton[i].Grade = str(Routes[i][2])
            problemButton[i].UserRating = Routes[i][19]
            # problemButton[i].moves = Routes[i][5]
            problemButton[i].repeats = Routes[i][20]
            self.problemList.add_widget(problemButton[i])
        self.moonImageGroup = moonBoardProblemImage()
        self.temp = 0
        for i in range(19):
            for j in range(12):
                self.imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
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
        # self.random_button = Button(text="Random", on_press=self.randomPressed)
        self.prev_page_button = Button(text="<", on_press=self.pageDecrease)
        self.customize = Button(text="Create Your Own!", on_press=self.custom_screen)
        self.return_home = Button(text="Return Home", on_press=self.home_screen)
        # self.nextPage = SearchButton(text="search", on_press=self.search)
        self.searchGrid = GridLayout(cols=1)
        self.navigateGrid = GridLayout(rows=2, orientation="vertical", size_hint_y=None)
        self.filterGroup = GridLayout(cols=4)
        start = time.time()
        self.add_widget(self.navigateGrid)
        self.add_widget(self.customizeBox)
        self.moonboardProblemsScroll.add_widget(self.problemList)
        self.add_widget(self.moonboardProblemsScroll)
        self.add_widget(self.searchGrid)
        for i in range(len(toggleText)):

            if toggleText[i] == "Popular":
                # print("FALSE CHECKBOX")
                filterBox[i] = FilterBox(on_press=self.filter, active=False)
            elif toggleText[i] == "Newest":
                # print("FALSE CHECKBOX")
                filterBox[i] = FilterBox(on_press=self.filter, active=True)
            elif toggleText[i] == "Benchmarks":
                filterBox[i] = FilterBox(on_press=self.filter, active=False)
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
        # self.navigation_field.add_widget(self.random_button)
        self.navigation_field.add_widget(self.next_page_button)
        self.navigateGrid.add_widget(self.search_field)
        self.navigateGrid.add_widget(self.navigation_field)
        self.customizeBox.add_widget(self.customize)


    def pageIncrease(self, pageNum):  # TODO account for something like remaining 99 if there isn't an even search
        global Routes, pageIndex, filterBox
        # print(pageIndex)
        # print(len(Routes))
        filterBox[20] = False
        if (len(Routes) > 9):
            pageIndex += 1
        else:
            pageIndex += 0
        self.filter()

    def pageDecrease(self, pageNum):  # TODO account for something like remaining 99 if there isn't an even search
        global Routes, pageIndex, filterBox
        # print(pageIndex)
        # print(len(Routes))

        filterBox[20] = False
        if (pageIndex > 0):
            pageIndex -= 1
        else:
            pageIndex += 0
        self.filter()

    def creationScreen(self, *args):
        return 0

    def filter_table(self, search=""):
        global Routes, filterBox, pageIndex
        Routes = self.db.get_rows_filtered(True, filterBox[0].active, filterBox[1].active, filterBox[2].active,
                                           filterBox[3].active, filterBox[4].active, filterBox[5].active,
                                           filterBox[6].active, filterBox[7].active, filterBox[8].active,
                                           filterBox[9].active, filterBox[10].active, filterBox[11].active,
                                           filterBox[12].active, filterBox[13].active, filterBox[14].active,
                                           filterBox[15].active, filterBox[16].active, filterBox[17].active,
                                           filterBox[18].active, filterBox[19].active, search)
        for index in range(len(Routes)):
            problemButton[index] = Problem(
                text=(Routes[index][1] + '\n' + "Set By: " + Routes[index][10].encode('utf-8')) + '\n' + "Grade: " +
                     Routes[index][
                         2] + " UserRating: " + str(Routes[index][19]) + '\n' + '     ' + "Repeats: " + str(
                    Routes[index][20]),
                size_hint_y=None)
            problemButton[index].route = Routes[index][34:68]
            problemButton[index].routeName = Routes[index][1]
            problemButton[index].setterName = str(Routes[index][10])
            problemButton[index].Grade = str(Routes[index][2])
            problemButton[index].UserRating = Routes[index][19]
            problemButton[index].repeats = Routes[index][20]
            self.problemList.add_widget(problemButton[index])

    def update_table(self, search=""):
        global Routes
        Routes = self.db.get_rows_searched(search)
        for index in range(len(Routes)):
            problemButton[index] = Problem(
                text=(Routes[index][1] + '\n' + "Set By: " + Routes[index][10].encode('utf-8')) + '\n' + "Grade: " +
                     Routes[index][
                         2] + " UserRating: " + str(Routes[index][19]) + '\n' + '     ' + "Repeats: " + str(
                    Routes[index][20]),
                size_hint_y=None)
            problemButton[index].route = Routes[index][34:68]
            problemButton[index].routeName = Routes[index][1]
            problemButton[index].setterName = str(Routes[index][10])
            problemButton[index].Grade = str(Routes[index][2])
            problemButton[index].UserRating = Routes[index][19]
            # problemButton[i].moves = Routes[i][5]
            problemButton[index].repeats = Routes[index][20]
            self.problemList.add_widget(problemButton[index])

    def clear_table(self):
        self.problemList.clear_widgets()

    def custom_screen(self, custom):
        # colorWipe(strip, Color(0, 0, 0))
        start = time.time()
        self.clear_widgets()

        self.cols = 1
        self.return_home.size_hint_y = None
        self.moonImageGroup = moonBoardProblemImage()
        self.temp = 0
        for i in range(19):
            for j in range(12):
                self.imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                global LED_ROUTE_IMAGES
                LED_ROUTE_IMAGES[self.temp] = moonBoardButton(background_normal=self.imageStr,
                                                              background_down=self.imageStr, size_hint_y=1,
                                                              size_hint_x=1,
                                                              allow_stretch=False, keep_ratio=True, border=(0, 0, 0, 0))
                # self.moonImagesArray[temp]
                self.temp += 1
        for i in range(228):
            self.moonImageGroup.add_widget(LED_ROUTE_IMAGES[i])

        self.add_widget(self.moonImageGroup)
        self.add_widget(self.return_home)
        end = time.time()
        print(end - start)
        # dataApp.build()

    def home_screen(self, home):
        self.clear_widgets()
        self.__init__()


    def search(self, *args):
        global pageIndex
        pageIndex = 0
        self.clear_table()
        if "\'" in self.search_input.text:
            temp = self.search_input.text
            temp = temp.replace("'", "+[^.apostrophe.]+")
            try:
                self.update_table(temp)
            except:
                pass
        elif "\\" in self.search_input.text:
            temp = self.search_input.text
            temp = temp.replace("\\", "+[^.solidus.]+")
            try:
                self.update_table(temp)
            except:
                pass
        elif self.search_input.text == '':
            temp = self.search_input.text
            temp = temp.replace("", ".*.*")
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
            temp = temp.replace("'", "+[^.apostrophe.]+")
            print(temp)
            try:
                self.filter_table(temp)
            except:
                pass
        elif "\\" in self.search_input.text:
            temp = self.search_input.text
            temp = temp.replace("\\", "+[[.solidus.]]+")
            try:
                self.filter_table(temp)
            except:
                pass
        elif self.search_input.text == '':
            temp = self.search_input.text
            temp = temp.replace("", ".*.*")
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
        MoonLayout = "2017/"
        for i in range(19):
            for j in range(12):
                imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                tempimage = moonBoardImage(source=imageStr)
                imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-white-square.png")
                tempimage = moonBoardImage(source=imageStr)
                imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-yellow-square.png")
                tempimage = moonBoardImage(source=imageStr)
                imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-green-square.png")
                tempimage = moonBoardImage(source=imageStr)
                imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-red-square.png")
                tempimage = moonBoardImage(source=imageStr)
                imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-blue-square.png")
                tempimage = moonBoardImage(source=imageStr)
        self.title = "MOONBOARD"
        parent = BoxLayout(size=(Window.width, Window.height))
        self.gridsDisplay = MoonboardAppLayout()
        parent.add_widget(self.gridsDisplay)
        return parent


dataApp = DatabaseApp()
dataApp.run()
