# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# encoding: utf-8
# decoding: utf-8
from bs4 import BeautifulSoup
# import MySQLdb
import pymysql
import pymysql.cursors
import requests
import urllib
import time
import re
import logging
import os
import sys

###################################
# Logging levels Setup
logger = logging.getLogger('Loading HTTP Page APP')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
###################################

###################################
# GLOBALS
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
    db = pymysql.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="root",  # your password
                         db="climbingholdsape",
                         charset='utf8mb4',
                         autocommit=True)  # name of the data base
    return db


def getArgs(problemInfo):
    return None
    # return args

def getargsproblem(problemInfo):
    return (problemInfo[0], problemInfo[1], problemInfo[2], problemInfo[3], problemInfo[4], problemInfo[5],
            problemInfo[6], problemInfo[7], problemInfo[8], problemInfo[9], problemInfo[10], problemInfo[11],
            problemInfo[12], problemInfo[13], problemInfo[14], problemInfo[15], problemInfo[16], problemInfo[17],
            problemInfo[18], problemInfo[19], problemInfo[20], problemInfo[21], problemInfo[22], problemInfo[23],
            problemInfo[24], problemInfo[25], problemInfo[26], problemInfo[27], problemInfo[28], problemInfo[29],
            problemInfo[30], problemInfo[31], problemInfo[32], problemInfo[33], problemInfo[34], problemInfo[35],
            problemInfo[36], problemInfo[37], problemInfo[38], problemInfo[39], problemInfo[40], problemInfo[41],
            problemInfo[42], problemInfo[43], problemInfo[44], problemInfo[45], problemInfo[46], problemInfo[47],
            problemInfo[48], problemInfo[49], problemInfo[50], problemInfo[51], problemInfo[52], problemInfo[53],
            problemInfo[54], problemInfo[55], problemInfo[56], problemInfo[57], problemInfo[58], problemInfo[59],
            problemInfo[60], problemInfo[61], problemInfo[62], problemInfo[63], problemInfo[64], problemInfo[65],
            problemInfo[66], problemInfo[67], problemInfo[68], problemInfo[69], problemInfo[70], problemInfo[71],
            problemInfo[72], problemInfo[73], problemInfo[74], problemInfo[75], problemInfo[76], problemInfo[77],
            problemInfo[78], problemInfo[79], problemInfo[80], problemInfo[81], problemInfo[82], problemInfo[83],
            problemInfo[84], problemInfo[85], problemInfo[86], problemInfo[87], problemInfo[88], problemInfo[89],
            problemInfo[90], problemInfo[91], problemInfo[92], problemInfo[93], problemInfo[94], problemInfo[95],
            problemInfo[96], problemInfo[97], problemInfo[98], problemInfo[99], problemInfo[100], problemInfo[101],
            problemInfo[102], problemInfo[103], problemInfo[104], problemInfo[105], problemInfo[106], problemInfo[107],
            problemInfo[108], problemInfo[109], problemInfo[110], problemInfo[111], problemInfo[112], problemInfo[113],
            problemInfo[114])
    # return args


def getQuery():
    query = "SELECT * FROM routelinks"

    return query

def getqueryproblem():
    query = "INSERT INTO routes (Method, Name, GradeUS, GradeUK, UserGradeUS, UserGradeUK, MoonBoardConfiguration, " \
            "MoonBoardConfigurationId, SetterId, SetterNickName, FirstName, LastName, City, Country, ProfileImageUrl, "\
            "FirstAscender, Rating, UserRating, Repeats, Attempts, HoldsetupId, HoldsetupDescription, IsBenchmark, "\
            "StartHold1, Starthold2, IntermediateHold1,IntermediateHold2,IntermediateHold3,   IntermediateHold4,  " \
            "IntermediateHold5, IntermediateHold6,  IntermediateHold7,  IntermediateHold8,  IntermediateHold9,  " \
            "IntermediateHold10, IntermediateHold11, IntermediateHold12, IntermediateHold13, IntermediateHold14, " \
            "IntermediateHold15, IntermediateHold16, IntermediateHold17, IntermediateHold18, IntermediateHold19, " \
            "IntermediateHold20, FinishHold1, FinishHold2, NumberOfTries, NameForUrl, Id, ApiId, DateUpdated, " \
            "DateDeleted, DateAdded) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s," \
            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP(), CURRENT_TIMESTAMP()) " \
            "ON DUPLICATE KEY UPDATE DateUpdated = IF(Rating != VALUES(Rating) OR " \
            "(Repeats != VALUES(Repeats)), VALUES(DateUpdated), DateUpdated)," \
            "Rating  = IF(Rating != VALUES(Rating), VALUES(Rating), Rating)," \
            "Repeats = IF(Repeats != VALUES(Repeats), VALUES(Repeats), Repeats)"

    return query


def submitDB(db, query):
    cur = db.cursor()
    cur.execute(query)
    return cur

def submitDBproblem(db, query, args):
    cur = db.cursor()
    cur.execute(query, args)
    return cur

def getVGrade(fontGrade):
    switcher = {
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

    ###################################


# Allow the beautiful soup library to read the contents of the HTML
###################################


def loadMainPage():
    problemInfoArray = [0] * 144
    db = connectDB()
    query = getQuery()
    args = getArgs(None)
    linkCollection = submitDB(db, query)
    #print(linkCollection.fetchone())
    # logger.info(pageProblems.content)
    #soupProblems = BeautifulSoup(pageProblems.content, 'html.parser')
    # logger.info(soupProblems)
    # problems = soupProblems.find(class_='ProblemList')
    # logger.debug(problems.prettify(encoding='utf-8'))
    # problemsArray = problems.find_all('a')
    problemNumber = 0
    for links in linkCollection.fetchall():
        problemNumber+=1
        # print(str(links))
        # string = zip(*links)
        print(links[0])
        pageProblem = requests.get("http://www.moonboard.com" + links[0])
            #pageProblem = requests.get("http://www.moonboard.com/problems/View/" + problemNum + "/" + link)
        logger.info('pageContent = %s' % pageProblem.content)
        soup = BeautifulSoup(pageProblem.content, 'html.parser')
        logger.debug(soup.prettify(encoding='utf-8'))
        problemDetail = soup.find_all("script", type="text/javascript")
        for ids in problemDetail:
            string = ids.getText()
            if ("var problem = ") in ids.getText():
                problemInfo = string.strip().split('\n', 1)[0]
                detailsArray = problemInfo.split(',')
                infoIndex = 0
                arrayIndex = 0
                for item in detailsArray:
                    if ("var problem = ") in item:
                        item = item[27:]
                    itemInfo = item.split(':')
                    itemInfo[0] = itemInfo[0].replace("\"", "")
                    itemInfo[0] = itemInfo[0].replace("{", "")
                    itemInfo[0] = itemInfo[0].replace("}", "")
                    itemInfo[1] = itemInfo[1].replace("\"", "")
                    itemInfo[1] = itemInfo[1].replace("{", "")
                    itemInfo[1] = itemInfo[1].replace("}", "")

                    if infoIndex == 2:
                        problemInfoArray[arrayIndex] = getVGrade(itemInfo[1])
                        problemInfoArray[arrayIndex+1] = itemInfo[1]
                        print(problemInfoArray)
                        arrayIndex += 2
                        infoIndex+=2

                    elif infoIndex == 4:
                        problemInfoArray[arrayIndex] = getVGrade(itemInfo[1])
                        problemInfoArray[arrayIndex+1] = itemInfo[1]
                        print(problemInfoArray)
                        arrayIndex+=2
                        infoIndex += 2
                    elif infoIndex == 8:
                        problemInfoArray[arrayIndex] = itemInfo[2]
                        arrayIndex+=1
                        infoIndex+=1
                        print(problemInfoArray)
                    elif infoIndex == 20:
                        problemInfoArray[arrayIndex] = itemInfo[2]
                        arrayIndex+=1
                        infoIndex+=1
                        print(problemInfoArray)
                    elif (infoIndex >= 22 and infoIndex <= 30) or (infoIndex == 31):
                        #problemInfoArray[infoIndex] = itemInfo[2]
                        infoIndex+=1
                        print(problemInfoArray)
                    elif (infoIndex == 35):
                        #problemInfoArray[infoIndex] = itemInfo[2]
                        infoIndex+=1
                        print(problemInfoArray)
                    else:
                        problemInfoArray[arrayIndex] = str(itemInfo[1])
                        infoIndex+=1
                        arrayIndex+=1
                        print(problemInfoArray)
                    print(infoIndex)

                    print(itemInfo)
                    #infoIndex+=1
                    # print(itemInfo[1])
                print(problemInfoArray)
                print(infoIndex)
        args = getargsproblem(problemInfoArray)
        query = getqueryproblem()
        submitDBproblem(db, query, args)
        logger.info("Updating and Added Route:" + str(problemNumber))

if __name__ == '__main__':
    ###################################
    # GLOBALS
    # problemsArray = []
    link = ""
    ###################################
    logger.debug('debug message')
    logger.info('info message')
    logger.warn('warn message')
    logger.error('error message')
    logger.critical('critical message')
    problemsArray = loadMainPage()

