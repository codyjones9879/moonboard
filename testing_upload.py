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


driver = webdriver.Chrome('D:/chromedriver.exe')
# load the page
driver.get("http://web.archive.org/web/20170314150132/www.moonboard.com/problems")


#username = driver.find_element_by_id("username")
# username = driver.find_element_by_name("Login.Username")
# password = driver.find_element_by_name("Login.Password")
#
# username.send_keys("theapedoctor")
# password.send_keys("comply9879")


# get the submit button
# bt_submit = driver.find_element_by_css_selector("[type=submit]")

# wait for the user to click the submit button (check every 1s with a 1000s timeout)
# WebDriverWait(driver, timeout=9000, poll_frequency=1) \
#   .until(EC.staleness_of(bt_submit))

#print "submitted"
#html = driver.page_source
soupProblems = BeautifulSoup(driver.page_source, 'html.parser')
problems = soupProblems.find(class_='ProblemList')
print(soupProblems)
print(problems.prettify(encoding='utf-8'))

# problemsButton = driver.find_element_by_id("lProblems")
# problemsButton.click()
# viewProblem = driver.find_element_by_id("m-viewproblem").click()

#problemList = driver.find_element_by_class_name("problem")
#print problemList