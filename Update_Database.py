# encoding: utf-8
# decoding: utf-8
from bs4 import BeautifulSoup
import MySQLdb
import requests
import urllib
import time
import re
#from neopixel import *
from urllib.parse import quote
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
# LED_COUNT                = 196 
# LED_PIN                  = 18
# LED_FREQ_HZ              = 800000
# LED_DMA                  = 5
# LED_BRIGHTNESS           = 255
# LED_INVERT               = False
# LED_CHANNEL              = 0
# LED_STRIP                = ws.WS2811_STRIP_GRB

#define the color grid
# strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL, LED_STRIP)
# strip.begin()
pageProblems = requests.get("http://www.moonboard.com/problems")
#.decode('utf-8','ignore')
soupProblems = BeautifulSoup(pageProblems.content, 'html.parser')

problems = soupProblems.find(class_='ProblemList')
#print(problems.prettify(encoding='utf-8'))
def colorWipe(strip, color, wait_ms=50):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

problemsArray = problems.find_all('a')
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


for classes in problemsArray:
	entry = [0] * 210
	coordLED = [None] * 198
	'''
	# Example Array setup:   [SH1, SH2, SH3, SH4,IH1,.....IH196,FH1,FH2]   SH1-4  is a combination of 2 hands and 2 feet, Intermediate max is with only 1 hand hold to start and 1 finish 
	# hold max making a remaining 196 Intermediate holds potentially if the wall is filled We need designated locations for these combinations
	'''
	colorLED = [0] * 198   
	title = classes.get('title')
	if "?" in title:
	 	title = classes.get('rel')
	 	#link = title.string
	# url = urllib.parse.urlsplit(title)
	# url = list(url)
	# url[2] = urllib.parse.quote(url[2])
	# url = urllib.parse.urlunsplit(url)
	else:
		link = title.replace(" ", "-")
		link = urllib.parse.urlsplit(link)
		link = list(link)
		link[2] = urllib.parse.quote(link[2])
		link = urllib.parse.urlunsplit(link)
		link = link.replace("%21", "!")
		link = link.replace("%27", "")
		link = link.replace("%E2%80%99", "")
		link = link.replace("%28", "(")
		link = link.replace("%29", ")")
		link = link.replace("%C3%97", "x")
		link = link.replace("'", "")
		link = link.replace("â€™", "")
		link = link.replace("%2A", "*")
		link = link.replace("%3D", "=")
		link = link.replace("%40", "@")
		link = link.replace("%E2%80%A6", "...")
		link = link.replace("%26", "&")
		print("---------------Problem Name---------------")
		entry[0] = link
		print(link)
		pageProblem  = requests.get("http://www.moonboard.com/problems/"+link)

		#print(page.content)

		soup = BeautifulSoup(pageProblem.content, 'html.parser')

		#print(soup.prettify(encoding='utf-8'))
		
		problemName = soup.find(class_='post-title')
		#print(problemName.string)

		print("---------------Problem Summary---------------")

		problemSummary = soup.find_all(class_='summary')
		for ids in problemSummary:
			#print(ids.getText().find("Set by : "))
			string = ids.getText()
			stringarray = re.split(r'\t+', string)
			indexAnother = 0
			for elements in stringarray:
				print("-------------------")
				if len(elements) > 2:
					#getTitle
					if indexAnother == 0:
						title = elements[1:len(elements)-1]
						#print("title: %s"  % title)
					#getSetter
					if indexAnother == 1:
						author = elements[9:len(elements)]
						print("author: %s" % author)
					#getGrade
					if indexAnother == 2:
						grade = elements[8:len(elements)]
						print("grade: %s" % grade)
					#getStars
					if indexAnother == 3:
						if elements[13:14] == ' ':
							stars = 0
						else:
							stars = int(elements[13:14])
						repeats = 0
						print("Stars: %d" % stars)
					#if indexAnother == 5:
					# #getRepeats
					# 	repeats = elements
					indexAnother+=1
					print("-------------------")
			#print(ids.getText()+'\n')

		print("---------------Start Holds----------------")
		startHold1 = soup.find_all(id="SH1")
		startHold2 = soup.find_all(id="SH2")

		finishHold1 = soup.find_all(id="FH1")
		finishHold2 = soup.find_all(id="FH2")

		for ids in startHold1:
			#print(ids.prettify(encoding='utf-8'))
			if ids.string != None:
				entry[1] = ids.string
				print(ids.string)
		for ids in startHold2:
			#print(ids.prettify(encoding='utf-8'))
			if ids.string != None:
				entry[2] = ids.string
				print(ids.string)
		holdNum = 0
		moves = True
		numMoves = 0
		print("---------------Intermediate Holds---------")
		while moves == True:
			holdNum+=1
			temp = soup.find(id="IH"+str(holdNum))
			if temp:
				if temp.string != None:
					entry[2+holdNum] = temp.string
					numMoves+=1
					print(temp.string)
			else:
				moves = False
		print("---------------Finish Holds---------------")
		for ids in finishHold1:
			#print(ids.prettify(encoding='utf-8'))
			if ids.string != None:
				entry[208] = ids.string
				numMoves+=1
				print(ids.string)
		for ids in finishHold2:
			#print(ids.prettify(encoding='utf-8'))
			if ids.string != None:
				entry[209] = ids.string
				numMoves+=1
				print(ids.string)
	db = MySQLdb.connect(host="ClimbingHoldsApe.db.8216949.hostedresource.com",    # your host, usually localhost
                     user="ClimbingHoldsApe",         # your username
                     passwd="Comply9879!",  # your password
                     db="ClimbingHoldsApe")        # name of the data base
	db.set_character_set('utf8')
	cur = db.cursor()
	cur.execute("""
        INSERT INTO Moonboard 
            (
            Name, 
            Author, 
            Grade, 
            Stars, 
            Moves,
            Repeats, 
            StartHold1, 
            Starthold2,
            IntermediateHold1,
			IntermediateHold2,
			IntermediateHold3,	
			IntermediateHold4,	
			IntermediateHold5,	
			IntermediateHold6,	
			IntermediateHold7,	
			IntermediateHold8,	
			IntermediateHold9,	
			IntermediateHold10,	
			IntermediateHold11,	
			IntermediateHold12,	
			IntermediateHold13,	
			IntermediateHold14,	
			IntermediateHold15,	
			IntermediateHold16,	
			IntermediateHold17,	
			IntermediateHold18,	
			IntermediateHold19,	
			IntermediateHold20,	
			IntermediateHold21,	
			IntermediateHold22,	
			IntermediateHold23,	
			IntermediateHold24,	
			IntermediateHold25,	
			IntermediateHold26,	
			IntermediateHold27,	
			IntermediateHold28,	
			IntermediateHold29,	
			IntermediateHold30,	
			IntermediateHold31,	
			IntermediateHold32,	
			IntermediateHold33,	
			IntermediateHold34,	
			IntermediateHold35,	
			IntermediateHold36,	
			IntermediateHold37,	
			IntermediateHold38,	
			IntermediateHold39,	
			IntermediateHold40,	
			IntermediateHold41,	
			IntermediateHold42,	
			IntermediateHold43,	
			IntermediateHold44,	
			IntermediateHold45,	
			IntermediateHold46,	
			IntermediateHold47,	
			IntermediateHold48,	
			IntermediateHold49,	
			IntermediateHold50,	
			IntermediateHold51,	
			IntermediateHold52,	
			IntermediateHold53,	
			IntermediateHold54,	
			IntermediateHold55,	
			IntermediateHold56,	
			IntermediateHold57,	
			IntermediateHold58,	
			IntermediateHold59,	
			IntermediateHold60,	
			IntermediateHold61,	
			IntermediateHold62,	
			IntermediateHold63,	
			IntermediateHold64,	
			IntermediateHold65,	
			IntermediateHold66,	
			IntermediateHold67,	
			IntermediateHold68,	
			IntermediateHold69,	
			IntermediateHold70,	
			IntermediateHold71,	
			IntermediateHold72,	
			IntermediateHold73,
			IntermediateHold74,	
			IntermediateHold75,	
			IntermediateHold76,	
			IntermediateHold77,	
			IntermediateHold78,	
			IntermediateHold79,	
			IntermediateHold80,	
			IntermediateHold81,	
			IntermediateHold82,
			IntermediateHold83,	
			IntermediateHold84,	
			IntermediateHold85,	
			IntermediateHold86,
			IntermediateHold87,	
			IntermediateHold88,	
			IntermediateHold89,	
			IntermediateHold90,	
			IntermediateHold91,	
			IntermediateHold92,	
			IntermediateHold93,	
			IntermediateHold94,	
			IntermediateHold95,
			IntermediateHold96,	
			IntermediateHold97,	
			IntermediateHold98,	
			IntermediateHold99,
			IntermediateHold100,	
            IntermediateHold101,
			IntermediateHold102,
			IntermediateHold103,	
			IntermediateHold104,	
			IntermediateHold105,	
			IntermediateHold106,	
			IntermediateHold107,	
			IntermediateHold108,	
			IntermediateHold109,	
			IntermediateHold110,	
			IntermediateHold111,	
			IntermediateHold112,	
			IntermediateHold113,	
			IntermediateHold114,	
			IntermediateHold115,	
			IntermediateHold116,	
			IntermediateHold117,	
			IntermediateHold118,	
			IntermediateHold119,	
			IntermediateHold120,	
			IntermediateHold121,	
			IntermediateHold122,	
			IntermediateHold123,	
			IntermediateHold124,	
			IntermediateHold125,	
			IntermediateHold126,	
			IntermediateHold127,	
			IntermediateHold128,	
			IntermediateHold129,	
			IntermediateHold130,	
			IntermediateHold131,	
			IntermediateHold132,	
			IntermediateHold133,	
			IntermediateHold134,	
			IntermediateHold135,	
			IntermediateHold136,	
			IntermediateHold137,	
			IntermediateHold138,	
			IntermediateHold139,	
			IntermediateHold140,	
			IntermediateHold141,	
			IntermediateHold142,	
			IntermediateHold143,	
			IntermediateHold144,	
			IntermediateHold145,	
			IntermediateHold146,	
			IntermediateHold147,	
			IntermediateHold148,	
			IntermediateHold149,	
			IntermediateHold150,	
			IntermediateHold151,	
			IntermediateHold152,	
			IntermediateHold153,	
			IntermediateHold154,	
			IntermediateHold155,	
			IntermediateHold156,	
			IntermediateHold157,	
			IntermediateHold158,	
			IntermediateHold159,	
			IntermediateHold160,	
			IntermediateHold161,	
			IntermediateHold162,	
			IntermediateHold163,	
			IntermediateHold164,	
			IntermediateHold165,	
			IntermediateHold166,	
			IntermediateHold167,	
			IntermediateHold168,	
			IntermediateHold169,	
			IntermediateHold170,	
			IntermediateHold171,	
			IntermediateHold172,	
			IntermediateHold173,
			IntermediateHold174,	
			IntermediateHold175,	
			IntermediateHold176,	
			IntermediateHold177,	
			IntermediateHold178,	
			IntermediateHold179,	
			IntermediateHold180,	
			IntermediateHold181,	
			IntermediateHold182,
			IntermediateHold183,	
			IntermediateHold184,	
			IntermediateHold185,	
			IntermediateHold186,
			IntermediateHold187,	
			IntermediateHold188,	
			IntermediateHold189,	
			IntermediateHold190,	
			IntermediateHold191,	
			IntermediateHold192,	
			IntermediateHold193,	
			IntermediateHold194,	
			IntermediateHold195,
			IntermediateHold196,	
			IntermediateHold197,	
			IntermediateHold198,	
			IntermediateHold199,
			IntermediateHold200,		
			FinishHold1,	
			FinishHold2
			)
        VALUES 
            (
			title, author, grade, stars, numMoves, repeats, entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7], entry[8], entry[9], entry[10],
            entry[11], entry[12], entry[13], entry[14], entry[15], entry[16], entry[17], entry[18], entry[19], entry[20], entry[21], entry[22], 
            entry[23], entry[24], entry[25], entry[26], entry[27], entry[28], entry[29], entry[30], entry[31], entry[32], entry[33], entry[34], 
            entry[35], entry[36], entry[37], entry[38], entry[39], entry[40], entry[41], entry[42], entry[43], entry[44], entry[45], entry[46], 
            entry[47], entry[48], entry[49], entry[50], entry[51], entry[52], entry[53], entry[54], entry[55], entry[56], entry[57], entry[58], 
            entry[59], entry[60], entry[61], entry[62], entry[63], entry[64], entry[65], entry[66], entry[67], entry[68], entry[69], entry[70], 
            entry[71], entry[72], entry[73], entry[74], entry[75], entry[76], entry[77], entry[78], entry[79], entry[80], entry[81], entry[82], 
            entry[83], entry[84], entry[85], entry[86], entry[87], entry[88], entry[89], entry[90], entry[91], entry[92], entry[93], entry[94], 
            entry[95], entry[96], entry[97], entry[98], entry[99], entry[100], entry[101], entry[102], entry[103], entry[104], entry[105], entry[106], 
            entry[107], entry[108], entry[109], entry[110], entry[111], entry[112], entry[113], entry[114], entry[115], entry[116], entry[117], 
            entry[118], entry[119], entry[120], entry[121], entry[122], entry[123], entry[124], entry[125], entry[126], entry[127], entry[128], 
            entry[129], entry[130], entry[131], entry[132], entry[133], entry[134], entry[135], entry[136], entry[137], entry[138], entry[139], 
            entry[140], entry[141], entry[142], entry[143], entry[144], entry[145], entry[146], entry[147], entry[148], entry[149], entry[150], 
            entry[151], entry[152], entry[153], entry[154], entry[155], entry[156], entry[157], entry[158], entry[159], entry[160], entry[161], 
            entry[162], entry[163], entry[164], entry[165], entry[166], entry[167], entry[168], entry[169], entry[170], entry[171], entry[172], 
            entry[173], entry[174], entry[175], entry[176], entry[177], entry[178], entry[179], entry[180], entry[181], entry[182], entry[183], 
            entry[184], entry[185], entry[186], entry[187], entry[188], entry[189], entry[190], entry[191], entry[192], entry[193], entry[194], 
            entry[195], entry[196], entry[197], entry[198], entry[199], entry[200], entry[201], entry[202], entry[203], entry[204], entry[205], 
            entry[206], entry[207], entry[208], entry[209]
            ) 
        ON DUPLICATE KEY UPDATE 
      		#no need to update the name, author, moves, or climbing holds JUST repeats and star rating
            Stars  = VALUES(stars), 
            Repeats   = VALUES(repeats) ;
                   """
    )
	#start holds
	coordLED[0] = moonToLED(entry[4])
	coordLED[1] = moonToLED(entry[5])
	coordLED[2] = None #only because of moonboard only having 2 start holds
	coordLED[3] = None #only because of moonboard only having 2 start holds


	#finish Holds
	coordLED[196] = moonToLED(entry[28])
	coordLED[197] = moonToLED(entry[29])
	temp = 6
	temp2 = 4
	#print(*entry)
	#intermediate holds
	while entry[temp] != None:
		coordLED[temp-2] = moonToLED(entry[temp])
		temp+=1
		#print(temp)

	#print(*entry)
	#print(*coordLED)

	'''
	# Color Choice:
	# 0. Off
	# 1. Blue - Start Hold
	# 2. Red - Intermediate Hold
	# 3. Green - Finish Hold
	'''
	# index = 0
	# while index < len(coordLED):
	# 	if index < 4:
	# 		#start Holds
	# 		if coordLED[index] != None :
	# 			colorLED[coordLED[index]] = 1
	# 			strip.setPixelColorRGB(coordLED[index],0,255,0)
	# 	elif index > 3 and index < 196:
	# 		if coordLED[index] != None :
	# 			colorLED[coordLED[index]] = 2
	# 			strip.setPixelColorRGB(coordLED[index],255,0,0)
	# 		# else:
	# 		# 	#colorLED[coordLED[index]] = 0
	# 	else:
	# 		if coordLED[index] != None :
	# 			colorLED[coordLED[index]] = 3
	# 			strip.setPixelColorRGB(coordLED[index],0,0,255)
	# 		# else:
	# 		# 	#colorLED[coordLED[index]] = 0
	# 	index+=1
	# index = 0
	# while index < len(colorLED):
	# 	if colorLED[index] == None:
	# 		colorLED[index] = 0
	# 		strip.setPixelColorRGB(index, 0,0,0)
	# 	index+=1
	# print(*colorLED)
	# strip.show()
	# time.sleep(1)
	# colorWipe(strip, Color(0,0,0))			
# name = divs.find("name")
# for names in name:
# 	print(names.prettify(encoding='utf-8'))




'''
	Individual Problem lists

'''

# pageProblem  = requests.get("http://www.moonboard.com/problems/problem-5")

# #print(page.content)

# soup = BeautifulSoup(pageProblem.content, 'html.parser')

# #print(soup.prettify(encoding='utf-8'))
# print("---------------Problem Name---------------")

# problemName = soup.find(class_='post-title')
# print(problemName.string)

# print("---------------Problem Summary---------------")

# problemSummary = soup.find_all(class_='summary')
# for ids in problemSummary:
# 	print(ids.getText())

# print("---------------Start Holds----------------")
# startHold1 = soup.find_all(id="SH1")
# startHold2 = soup.find_all(id="SH2")

# finishHold1 = soup.find_all(id="FH1")
# finishHold2 = soup.find_all(id="FH2")

# for ids in startHold1:
# 	#print(ids.prettify(encoding='utf-8'))
# 	if ids.string != None:
# 		print(ids.string)
# for ids in startHold2:
# 	#print(ids.prettify(encoding='utf-8'))
# 	if ids.string != None:
# 		print(ids.string)
# holdNum = 0
# moves = True
# print("---------------Intermediate Holds---------")
# while moves == True:
# 	holdNum+=1
# 	temp = soup.find(id="IH"+str(holdNum))
# 	if temp:
# 		if temp.string != None:
# 			print(temp.string)
# 	else:
# 		moves = False
# print("---------------Finish Holds----------------")
# for ids in finishHold1:
# 	#print(ids.prettify(encoding='utf-8'))
# 	if ids.string != None:
# 		print(ids.string)
# for ids in finishHold2:
# 	#print(ids.prettify(encoding='utf-8'))
# 	if ids.string != None:
# 		print(ids.string)

# # name = divs.find("name")
# # for names in name:
# # 	print(names.prettify(encoding='utf-8'))
