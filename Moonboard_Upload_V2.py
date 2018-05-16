
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
# -*- coding: utf-8 -*-

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
import os
import sys

###################################
#Logging levels Setup
logger = logging.getLogger('Loading HTTP Page APP')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)
###################################

###################################
#GLOBALS
problemsLinkArray = []
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
                         db="climbingholdsape",
                         charset='utf8mb4',
                         autocommit=True)        # name of the data base
    return db

def getQuery():
    query = "INSERT INTO `climbingholdsape`.`routelinks` (`link`) VALUES (%s)"

    return query


def submitDB(db, query, args):
    cur = db.cursor()
    cur.execute(query, args)


db = connectDB()

driver = webdriver.Chrome('D:\Python27\selenium\webdriver\chromedriver.exe')
# load the page
driver.get("https://moonboard.com/Account/Login")


#username = driver.find_element_by_id("username")
username = driver.find_element_by_name("Login.Username")
password = driver.find_element_by_name("Login.Password")

username.send_keys("theapedoctor")
password.send_keys("comply9879")


# get the submit button
bt_submit = driver.find_element_by_css_selector("[type=submit]")

# wait for the user to click the submit button (check every 1s with a 1000s timeout)
WebDriverWait(driver, timeout=9000, poll_frequency=1) \
  .until(EC.staleness_of(bt_submit))

#print "submitted"

problemsButton = driver.find_element_by_id("lProblems")
problemsButton.click()
viewProblem = driver.find_element_by_id("m-viewproblem").click()
time.sleep(2)




try:
    soupProblems = BeautifulSoup(driver.page_source, 'html.parser')
    #problems = soupProblems.find_all("a", href=True)
    print(soupProblems)
    # for divs in soupProblems.find_all("div", class_="problem"):
    #     for a in divs.find_all("a", href=True):
    #         print("Found the URL:", a['href'])
    index = 2
    moreProblems = True
    query = getQuery()
    while moreProblems:
      soupProblems = BeautifulSoup(driver.page_source, 'html.parser')
      pageClick = driver.find_element_by_css_selector('[data-page="%d"]' % index)
      print(pageClick)
      pageClick.click()
      time.sleep(5)
      for divs in soupProblems.find_all("div", class_="problem"):
        for a in divs.find_all("a", href=True):
          if a is None:
            moreProblems = False
          else:
            query = getQuery()

            link = a['href']
            submitDB(db, query, link)
            problemsLinkArray.append(a['href'])
            #linkIndex+=1
            print("Found the URL:", a['href'])
        #print(pages)
      #print(problemsLinkArray)
      index+=1
except:
    print("Done1")





viewProblems2016 = Select(driver.find_element_by_id('Holdsetup'))
viewProblems2016.select_by_visible_text('MoonBoard 2016')
time.sleep(2)

try:
    soupProblems = BeautifulSoup(driver.page_source, 'html.parser')
    # problems = soupProblems.find_all("a", href=True)
    print(soupProblems)
    # for divs in soupProblems.find_all("div", class_="problem"):
    #     for a in divs.find_all("a", href=True):
    #         print("Found the URL:", a['href'])
    index = 2
    moreProblems = True
    query = getQuery()
    while moreProblems:
        soupProblems = BeautifulSoup(driver.page_source, 'html.parser')
        pageClick = driver.find_element_by_css_selector('[data-page="%d"]' % index)
        print(pageClick)
        pageClick.click()
        time.sleep(5)
        for divs in soupProblems.find_all("div", class_="problem"):
            for a in divs.find_all("a", href=True):
                if a is None:
                    moreProblems = False
                else:
                    query = getQuery()

                    link = a['href']
                    submitDB(db, query, link)
                    problemsLinkArray.append(a['href'])
                    # linkIndex+=1
                    print("Found the URL:", a['href'])
                    # print(pages)
        # print(problemsLinkArray)
        index += 1
except:
    print("Done2")


