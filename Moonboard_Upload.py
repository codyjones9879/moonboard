# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# encoding: utf-8
# decoding: utf-8
from bs4 import BeautifulSoup
#import MySQLdb
import pymysql
import pymysql.cursors
import requests
import urllib
import time
import re
import logging
import sys
###################################
#Logging levels Setup
logger = logging.getLogger('Loading HTTP Page APP')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
###################################

###################################
#GLOBALS
problemsArray = []
link = ""
problemInfo = [0] * 205
###################################

def connectDB():
    # db = pymysql.connect(host="ClimbingHoldsApe.db.8216949.hostedresource.com",    # your host, usually localhost
    #                      user="ClimbingHoldsApe",         # your username
    #                      passwd="Comply9879!",  # your password
    #                      db="ClimbingHoldsApe",
    #                      charset='utf8mb4',
    #                      autocommit=True)        # name of the data base 
    db = pymysql.connect(host="localhost",    # your host, usually localhost
                         user="root",         # your username
                         passwd="root",  # your password
                         db="ClimbingHoldsApe",
                         charset='utf8mb4',
                         autocommit=True)        # name of the data base 
    return db





def getArgs(problemInfo):
    return (problemInfo[0], problemInfo[1], problemInfo[2],
            problemInfo[3], problemInfo[4], problemInfo[5],
            problemInfo[6], problemInfo[7], problemInfo[8],
            problemInfo[9], problemInfo[10], problemInfo[11],
            problemInfo[12], problemInfo[13], problemInfo[14],
            problemInfo[15], problemInfo[16], problemInfo[17],
            problemInfo[18], problemInfo[19], problemInfo[20], problemInfo[21], problemInfo[22], problemInfo[23], problemInfo[24], problemInfo[25], problemInfo[26], problemInfo[27], problemInfo[28], problemInfo[29], problemInfo[30], problemInfo[31], problemInfo[32], problemInfo[33], problemInfo[34], problemInfo[35], problemInfo[36], problemInfo[37], problemInfo[38], problemInfo[39], problemInfo[40], problemInfo[41], problemInfo[42], problemInfo[43], problemInfo[44], problemInfo[45], problemInfo[46], problemInfo[47], problemInfo[48], problemInfo[49], problemInfo[50], problemInfo[51], problemInfo[52], problemInfo[53], problemInfo[54], problemInfo[55], problemInfo[56], problemInfo[57], problemInfo[58], problemInfo[59], problemInfo[60], problemInfo[61], problemInfo[62], problemInfo[63], problemInfo[64], problemInfo[65], problemInfo[66], problemInfo[67], problemInfo[68], problemInfo[69], problemInfo[70], problemInfo[71], problemInfo[72], problemInfo[73], problemInfo[74], problemInfo[75], problemInfo[76], problemInfo[77], problemInfo[78], problemInfo[79], problemInfo[80], problemInfo[81], problemInfo[82], problemInfo[83], problemInfo[84], problemInfo[85], problemInfo[86], problemInfo[87], problemInfo[88], problemInfo[89], problemInfo[90], problemInfo[91], problemInfo[92], problemInfo[93], problemInfo[94], problemInfo[95], problemInfo[96], problemInfo[97], problemInfo[98], problemInfo[99], problemInfo[100], problemInfo[101], problemInfo[102], problemInfo[103], problemInfo[104], problemInfo[105], problemInfo[106], problemInfo[107], problemInfo[108], problemInfo[109], problemInfo[110], problemInfo[111], problemInfo[112], problemInfo[113], problemInfo[114], problemInfo[115], problemInfo[116], problemInfo[117], problemInfo[118], problemInfo[119], problemInfo[120], problemInfo[121], problemInfo[122], problemInfo[123], problemInfo[124], problemInfo[125], problemInfo[126], problemInfo[127], problemInfo[128], problemInfo[129], problemInfo[130], problemInfo[131], problemInfo[132], problemInfo[133], problemInfo[134], problemInfo[135], problemInfo[136], problemInfo[137], problemInfo[138], problemInfo[139], problemInfo[140], problemInfo[141], problemInfo[142], problemInfo[143], problemInfo[144], problemInfo[145], problemInfo[146], problemInfo[147], problemInfo[148], problemInfo[149], problemInfo[150], problemInfo[151], problemInfo[152], problemInfo[153], problemInfo[154], problemInfo[155], problemInfo[156], problemInfo[157], problemInfo[158], problemInfo[159], problemInfo[160], problemInfo[161], problemInfo[162], problemInfo[163], problemInfo[164], problemInfo[165], problemInfo[166], problemInfo[167], problemInfo[168], problemInfo[169], problemInfo[170], problemInfo[171], problemInfo[172], problemInfo[173], problemInfo[174], problemInfo[175], problemInfo[176], problemInfo[177], problemInfo[178], problemInfo[179], problemInfo[180], problemInfo[181], problemInfo[182], problemInfo[183], problemInfo[184], problemInfo[185], problemInfo[186], problemInfo[187], problemInfo[188], problemInfo[189], problemInfo[190], problemInfo[191], problemInfo[192], problemInfo[193], problemInfo[194], problemInfo[195], problemInfo[196], problemInfo[197], problemInfo[198], problemInfo[199], problemInfo[200], problemInfo[201], problemInfo[202], problemInfo[203], problemInfo[204], problemInfo[205], problemInfo[206], problemInfo[207], problemInfo[208], problemInfo[209])
    # return args    


def getQuery():
    query = "INSERT INTO Moonboard (Name, Author, Grade, Stars, Moves, Repeats, StartHold1, Starthold2,IntermediateHold1,IntermediateHold2,IntermediateHold3,   IntermediateHold4,  IntermediateHold5,  IntermediateHold6,  IntermediateHold7,  IntermediateHold8,  IntermediateHold9,  IntermediateHold10, IntermediateHold11, IntermediateHold12, IntermediateHold13, IntermediateHold14, IntermediateHold15, IntermediateHold16, IntermediateHold17, IntermediateHold18, IntermediateHold19, IntermediateHold20, IntermediateHold21, IntermediateHold22, IntermediateHold23, IntermediateHold24, IntermediateHold25, IntermediateHold26, IntermediateHold27, IntermediateHold28, IntermediateHold29, IntermediateHold30, IntermediateHold31, IntermediateHold32, IntermediateHold33, IntermediateHold34, IntermediateHold35, IntermediateHold36, IntermediateHold37, IntermediateHold38, IntermediateHold39, IntermediateHold40, IntermediateHold41, IntermediateHold42, IntermediateHold43, IntermediateHold44, IntermediateHold45, IntermediateHold46, IntermediateHold47, IntermediateHold48, IntermediateHold49, IntermediateHold50, IntermediateHold51, IntermediateHold52, IntermediateHold53, IntermediateHold54, IntermediateHold55, IntermediateHold56, IntermediateHold57, IntermediateHold58, IntermediateHold59, IntermediateHold60, IntermediateHold61, IntermediateHold62, IntermediateHold63, IntermediateHold64, IntermediateHold65, IntermediateHold66, IntermediateHold67, IntermediateHold68, IntermediateHold69, IntermediateHold70, IntermediateHold71, IntermediateHold72, IntermediateHold73,IntermediateHold74,  IntermediateHold75, IntermediateHold76, IntermediateHold77, IntermediateHold78, IntermediateHold79, IntermediateHold80, IntermediateHold81, IntermediateHold82,IntermediateHold83,  IntermediateHold84, IntermediateHold85, IntermediateHold86,IntermediateHold87,  IntermediateHold88, IntermediateHold89, IntermediateHold90, IntermediateHold91, IntermediateHold92, IntermediateHold93, IntermediateHold94, IntermediateHold95,IntermediateHold96,  IntermediateHold97, IntermediateHold98, IntermediateHold99,IntermediateHold100, IntermediateHold101,IntermediateHold102,IntermediateHold103,    IntermediateHold104,    IntermediateHold105,    IntermediateHold106,    IntermediateHold107,    IntermediateHold108,    IntermediateHold109,    IntermediateHold110,    IntermediateHold111,    IntermediateHold112,    IntermediateHold113,    IntermediateHold114,    IntermediateHold115,    IntermediateHold116,    IntermediateHold117,    IntermediateHold118,    IntermediateHold119,    IntermediateHold120,    IntermediateHold121,    IntermediateHold122,    IntermediateHold123,    IntermediateHold124,    IntermediateHold125,    IntermediateHold126,    IntermediateHold127,    IntermediateHold128,    IntermediateHold129,    IntermediateHold130,    IntermediateHold131,    IntermediateHold132,    IntermediateHold133,    IntermediateHold134,    IntermediateHold135,    IntermediateHold136,    IntermediateHold137,    IntermediateHold138,    IntermediateHold139,    IntermediateHold140,    IntermediateHold141,    IntermediateHold142,    IntermediateHold143,    IntermediateHold144,    IntermediateHold145,    IntermediateHold146,    IntermediateHold147,    IntermediateHold148,    IntermediateHold149,    IntermediateHold150,    IntermediateHold151,    IntermediateHold152,    IntermediateHold153,    IntermediateHold154,    IntermediateHold155,    IntermediateHold156,    IntermediateHold157,    IntermediateHold158,    IntermediateHold159,    IntermediateHold160,    IntermediateHold161,    IntermediateHold162,    IntermediateHold163,    IntermediateHold164,    IntermediateHold165,    IntermediateHold166,    IntermediateHold167,    IntermediateHold168,    IntermediateHold169,    IntermediateHold170,    IntermediateHold171,    IntermediateHold172,    IntermediateHold173,IntermediateHold174,    IntermediateHold175,    IntermediateHold176,    IntermediateHold177,    IntermediateHold178,    IntermediateHold179,    IntermediateHold180,    IntermediateHold181,    IntermediateHold182,IntermediateHold183,    IntermediateHold184,    IntermediateHold185,    IntermediateHold186,IntermediateHold187,    IntermediateHold188,    IntermediateHold189,    IntermediateHold190,    IntermediateHold191,    IntermediateHold192,    IntermediateHold193,    IntermediateHold194,    IntermediateHold195,IntermediateHold196,    IntermediateHold197,    IntermediateHold198,    IntermediateHold199,IntermediateHold200,        FinishHold1,    FinishHold2) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE Stars  = VALUES(Stars), Repeats   = VALUES(Repeats)"    
    return query

def submitDB(db, query, args):
    cur = db.cursor()
    cur.execute(query, args)

###################################
#Allow the beautiful soup library to read the contents of the HTML
###################################


def loadMainPage():
    pageProblems = requests.get("http://www.moonboard.com/problems")
    soupProblems = BeautifulSoup(pageProblems.content, 'html.parser')
    problems = soupProblems.find(class_='ProblemList')
    logger.debug(problems.prettify(encoding='utf-8'))
    problemsArray = problems.find_all('a')
    for classes in problemsArray:
        problemInfo = [0] * 210
        title = classes.get('title')
        problemInfo[0] = title
        if "%A3" in title:
            title = classes.get('rel')
            title = title.replace("[", "")
            title = title.replace("]", "")
            link = title
        elif "%2C" in title:
            title = classes.get('rel')
            title = title.replace("[", "")
            title = title.replace("]", "")
            link = title
        elif "%C2%BF" in title:
            title = classes.get('rel')
            title = title.replace("[", "")
            title = title.replace("]", "")
            link = title
        elif "=/-" in title:
            title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        elif "¿" in title:
            title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        elif "¿?¿" in title:
            title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        elif ":))" in title:
            title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        elif title == "Far from the Madding Crowd":
            link = "problem-1"
        elif title == "Wuthering Heights":
            link = "problem-2"
        elif title == "Hard Times":
            link = "problem-4"
        elif "Vurt" in title:
            link = "problem-8"
        elif title == "Mark and Lard":
            link = "mark-lard"
        elif "???" in title:
            # title = "207982"
            title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        elif "??" in title:
            # title = "206103"
            title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        elif "?" in title:
            # title = "204447"
            title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        elif title == "$$":
            # title = "204447"
            title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        elif title == "Warm up number two":
            title = "warm-up-number-2"
            #title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        elif title == "frigging fingers":
            title = "fucking-fingers"
            #title = classes.get('rel')
            # title = title.replace("[", "")
            # title = title.replace("]", "")
            link = title
        else:
            link = title.replace("ø", "o")
            link = title.replace(" ", "-")
            link = urllib.parse.urlsplit(link)
            link = list(link)
            link[2] = urllib.parse.quote(link[2])
            link = urllib.parse.urlunsplit(link)
            link = link.replace("?", "")
            link = link.replace("¿", "")
            link = link.replace("'", "")
            link = link.replace("â€™", "")
            link = link.replace("%20", "-")
            link = link.replace("%21", "!")
            link = link.replace("%24", "")
            link = link.replace("%26", "&")
            link = link.replace("%27", "")
            link = link.replace("%28", "(")
            link = link.replace("%29", ")")
            link = link.replace("%2A", "*")
            link = link.replace("%2B", "+")
            link = link.replace("%2C", "")
            link = link.replace("%3A", ":")
            link = link.replace("%3B", ";")
            link = link.replace("%3D", "=")
            link = link.replace("%40", "@")
            link = link.replace("%5C", "\\")
            link = link.replace("%5E", "")
            link = link.replace(".", "-")
            link = link.replace("/", "")
            link = link.replace("#", "")
            link = link.replace("%23", "")
            link = link.replace("%C2%A1", "")
            link = link.replace("%C2%B0", "")
            link = link.replace("%C2%BF", "")
            link = link.replace("%C3%80", "A")
            link = link.replace("%C3%85", "A")
            link = link.replace("%C3%89", "E")
            link = link.replace("%C3%90", "D")
            link = link.replace("%C3%96", "O")
            link = link.replace("%C3%97", "x")
            link = link.replace("%C3%9F", "S")
            link = link.replace("%C3%A0", "a")
            link = link.replace("%C3%A1", "a")
            link = link.replace("%C3%A2", "a")
            link = link.replace("%C3%A3", "a")
            link = link.replace("%C3%A4", "a")
            link = link.replace("%C3%A5", "a")
            link = link.replace("%C3%A6", "a")
            link = link.replace("%C3%A7", "c")
            link = link.replace("%C3%A8", "e")
            link = link.replace("%C3%A9", "e")
            link = link.replace("%C3%AC", "i")
            link = link.replace("%C3%AE", "i")
            link = link.replace("%C3%B0", "d")
            link = link.replace("%C3%B1", "n")
            link = link.replace("%C3%B2", "o")
            link = link.replace("%C3%B3", "o")
            link = link.replace("%C3%B6", "o")
            link = link.replace("%C3%B8", "o")
            link = link.replace("%C3%BA", "u")
            link = link.replace("%C3%BC", "u")
            link = link.replace("%C4%97", "e")
            link = link.replace("%C5%82", "l")
            link = link.replace("%C5%9B", "s")
            link = link.replace("%D1%80", "p")
            link = link.replace("%DO%90", "A")
            link = link.replace("%DO%92", "B")
            link = link.replace("%DO%BF", "n")
            link = link.replace("%E2%80%93", "")
            link = link.replace("%E2%80%98", "")
            link = link.replace("%E2%80%99", "")
            link = link.replace("%E2%80%9C", "")
            link = link.replace("%E2%80%9D", "")
            link = link.replace("%E2%80%A6", "...")
            link = link.replace("%E2%80%B3", "")
            link = link.replace("\u201d", "")
            logger.info('Link for Loading Page: %s' % link)
            # problemInfo[0] = link
            if problemInfo[0] == "":
                logger.debug('Blank Link Name')
            elif problemInfo[0] == " ":
                logger.debug('Blank Link Name')
            elif problemInfo[0] == "\t":
                logger.debug('Blank Link Name')
            else:
                pageProblem = requests.get("http://www.moonboard.com/problems/"+link)
                logger.debug('pageContent = %s' % pageProblem.content)
                soup = BeautifulSoup(pageProblem.content, 'html.parser')
                # problemName = soup.find(class_='post-title')
                # logger.debug('problemName = %s' % problemName.string)
                problemSummary = soup.find_all(class_='summary')
                for ids in problemSummary:
                    string = ids.getText()
                    stringarray = re.split(r'\t+', string)
                    problemInfoIndex = 0
                    for elements in stringarray:
                        logger.debug('-----------------')
                        if len(elements) > 2:
                            #TITLE
                            if problemInfoIndex == 0:
                                # problemInfo[0] = elements[1:len(elements)-1]
                                logger.debug('Problem Name = %s' % problemInfo[0])
                            if problemInfoIndex == 1:
                                problemInfo[1] = elements[9:len(elements)]
                                logger.debug('Setter = %s' % problemInfo[1])
                            if problemInfoIndex == 2:
                                problemInfo[2] = elements[8:len(elements)]
                                logger.debug('Grade = %s' % problemInfo[2])
                            if problemInfoIndex == 8:
                                if elements[4:6] == "Be":
                                    problemInfo[5] = 0
                                    #logger.info('Repeat: %s' % problemInfo[5])
                                else:
                                    if elements[5] == ' ':
                                        problemInfo[5] = elements[4]
                                    elif elements[6] == ' ':
                                        problemInfo[5] = elements[4:5]
                                    elif elements[7] == ' ':
                                        problemInfo[5] = elements[4:7]
                                    elif elements[8] == ' ':
                                        problemInfo[5] = elements[4:8]
                                logger.debug('Repeat: %s' % problemInfo[5])
                            problemInfoIndex+=1
                            logger.debug('---------------')
                # if problemInfoIndex == 3:
                #     if elements[14:15] == ' ':
                #         problemInfo[3] = 0
                #         logger.info('Stars = %s' % elements[0:15])
                #     else:
                #         problemInfo[3] = elements[14:15]
                #         logger.info('Stars = %s' % elements[0:15])
                
                # logger.info('Stars = %s' % problemInfo[3])
                startHold1 = soup.find_all(id="SH1")
                startHold2 = soup.find_all(id="SH2")
                finishHold1 = soup.find_all(id="FH1")
                finishHold2 = soup.find_all(id="FH2")
                for ids in startHold1:
                    if ids.string != None:
                        problemInfo[6] = ids.string
                        logger.debug('Start Hold 1: %s' % problemInfo[6])
                for ids in startHold2:
                    if ids.string != None:
                        problemInfo[7] = ids.string
                        logger.debug('Start Hold 2: %s' % problemInfo[7])
                holdNum = 0
                moves = True
                numMoves = 0
                while moves == True:
                    holdNum+=1
                    temp = soup.find(id="IH"+str(holdNum))
                    if temp:
                        if temp.string != None:
                            problemInfo[7+holdNum] = temp.string
                            numMoves+=1
                            logger.debug('Intermediate Hold: %s' % problemInfo[7+holdNum])
                    else:
                        moves = False
                for ids in finishHold1:
                    #print(ids.prettify(encoding='utf-8'))
                    if ids.string != None:
                        problemInfo[208] = ids.string
                        numMoves+=1
                        logger.debug('Finish Hold 1: %s' % problemInfo[208])
                for ids in finishHold2:
                    #print(ids.prettify(encoding='utf-8'))
                    if ids.string != None:
                        problemInfo[209] = ids.string
                        numMoves+=1
                        logger.debug('Finish Hold 2: %s' % problemInfo[209])
                problemInfo[4] = numMoves
                images = soup.find_all("img")
                imageIndex = 0
                for ids in images:
                    if imageIndex == 0:
                        logger.debug("Images: %s" % ids)
                        
                        if "3stars-small.png" in str(ids):
                            problemInfo[3] = "3"
                        elif "2stars-small.png" in str(ids):
                            problemInfo[3] = "2"
                        elif "1stars-small.png" in str(ids):
                            problemInfo[3] = "1"
                        else:
                            problemInfo[3] = "0"
                    imageIndex+=1
                logger.debug("Stars: %s" % problemInfo[3])
                db = connectDB()
                args = getArgs(problemInfo)
                query = getQuery()
                submitDB(db, query, args)
                     




if __name__ == '__main__':
    ###################################
    #GLOBALS
    #problemsArray = []
    link = ""
    ###################################
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
    problemsArray = loadMainPage()
    