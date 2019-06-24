# -*- coding: utf-8 -*-

from neopixel import *
import time
from kivy.app import App
from kivy.cache import Cache
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image


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
global LED_ROUTE_IMAGES
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
        global MoonLayout
        MoonLayout = "2017/"
        self.moonImageGroup = moonBoardProblemImage()
        self.temp = 0
        for i in range(19):
            for j in range(12):
                self.imageStr = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + ".png")
                if i != 0 and j != 0:

                    self.imageStr1 = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-white-square.png")
                    self.imageStr2 = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-yellow-square.png")
                    self.imageStr3 = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-blue-square.png")
                    self.imageStr4 = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-red-square.png")
                    self.imageStr5 = str("images/" + MoonLayout + "moon-" + str(i) + "-" + str(j) + "-green-square.png")
                    temp = moonBoardImage(source=self.imageStr1, size_hint_y=1, size_hint_x=1,
                                      allow_stretch=True, keep_ratio=False)
                    temp = moonBoardImage(source=self.imageStr2, size_hint_y=1, size_hint_x=1,
                                      allow_stretch=True, keep_ratio=False)
                    temp = moonBoardImage(source=self.imageStr3, size_hint_y=1, size_hint_x=1,
                                      allow_stretch=True, keep_ratio=False)
                    temp = moonBoardImage(source=self.imageStr4, size_hint_y=1, size_hint_x=1,
                                      allow_stretch=True, keep_ratio=False)
                    temp = moonBoardImage(source=self.imageStr5, size_hint_y=1, size_hint_x=1,
                                      allow_stretch=True, keep_ratio=False)
                global LED_ROUTE_IMAGES
                LED_ROUTE_IMAGES[self.temp] = moonBoardImage(source=self.imageStr, size_hint_y=1, size_hint_x=1,
                                                             allow_stretch=True, keep_ratio=False)
                self.temp += 1
        for i in range(228):
            self.moonImageGroup.add_widget(LED_ROUTE_IMAGES[i])

        self.return_home = Button(text="Clear", on_press=self.home_screen)

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







    def creationScreen(self, *args):
        return 0



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







class DatabaseApp(App):
    def build(self):
        self.title = "MOONBOARD"
        parent = BoxLayout(size=(Window.width, Window.height))
        self.gridsDisplay = MoonboardAppLayout()
        parent.add_widget(self.gridsDisplay)

        return parent


dataApp = DatabaseApp()
dataApp.run()
