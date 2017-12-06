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


def getQuery():
    query = "SELECT * FROM routelinks"

    return query


def submitDB(db, query):
    cur = db.cursor()
    cur.execute(query)
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
    # problemNumber = 0
    for links in linkCollection.fetchall():
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
                print(detailsArray[1])



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

