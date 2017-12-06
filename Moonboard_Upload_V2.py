
from __future__ import unicode_literals
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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





#problemList = driver.find_element_by_class_name("problem")
#print problemList

#<div class="k-grid-content" style="height: 752.563px;"><table role="grid"><colgroup></colgroup><tbody role="rowgroup"><tr data-uid="308025" onclick="problemSelected();" class="selected"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308025/hyul-001" target="_blank">HYUL 001</a></h3><p>            ki won Nam        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308024" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308024/chundercut" target="_blank">CHUNDERCUT</a></h3><p>            Remus Knowles        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7B        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308023" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308023/kreuzung" target="_blank">KREUZUNG</a></h3><p>            Danny Maldener        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308022" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308022/judgement-rains" target="_blank">JUDGEMENT RAINS</a></h3><p>            Gus Carter        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308021" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308021/second-place-1st-lou-ser" target="_blank">SECOND PLACE, 1ST LOU-SER</a></h3><p>            Gus Carter        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7C+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308020" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308020/right-left-up-down" target="_blank">RIGHT, LEFT, UP, DOWN</a></h3><p>            Tim Teylan        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308019" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308019/dyno-fit" target="_blank">DYNO FIT</a></h3><p>            Chuchi Climber        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308018" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308018/crossword" target="_blank">CROSSWORD</a></h3><p>            Jon Pål Hamre        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308017" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308017/habibi-direkt" target="_blank">HABIBI DIREKT</a></h3><p>            Daniel Pliegl        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7A+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308016" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308016/test-a1" target="_blank">TEST A1</a></h3><p>            iTTE Climbing        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7A        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308015" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308015/ror" target="_blank">ROR</a></h3><p>            abi        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308014" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308014/oh-rock-beautiful" target="_blank">OH ROCK BEAUTIFUL</a></h3><p>            abi        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308013" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308013/fun-stuff" target="_blank">FUN STUFF</a></h3><p>            Tauty        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308012" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308012/daipanman" target="_blank">DAIPANMAN</a></h3><p>            DAI NUMATA        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308011" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308011/たい" target="_blank">たい</a></h3><p>            DAI NUMATA        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr></tbody></table></div>