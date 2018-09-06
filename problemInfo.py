# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# encoding: utf-8
# decoding: utf-8
from bs4 import BeautifulSoup
import pymysql
import pymysql.cursors
import requests
import re
import logging

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
problemsArrayEdited = []
link = ""
probleminfo = [0] * 205


###################################

def connectdb():
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


def getargsproblem(probleminfo):
    return (
        probleminfo[0], probleminfo[1].encode("utf-8"), probleminfo[2], probleminfo[3], probleminfo[4], probleminfo[5],
        probleminfo[6], probleminfo[7], probleminfo[8], probleminfo[9], probleminfo[10], probleminfo[11], 
        probleminfo[12], probleminfo[13], probleminfo[14], probleminfo[15], probleminfo[16], probleminfo[17], 
        probleminfo[18], probleminfo[19], probleminfo[20], probleminfo[21], probleminfo[22], probleminfo[23], 
        probleminfo[24], probleminfo[25], probleminfo[26], probleminfo[27], probleminfo[28], probleminfo[29], 
        probleminfo[30], probleminfo[31], probleminfo[32], probleminfo[33], probleminfo[34], probleminfo[35], 
        probleminfo[36], probleminfo[37], probleminfo[38], probleminfo[39], probleminfo[40], probleminfo[41], 
        probleminfo[42], probleminfo[43], probleminfo[44], probleminfo[45], probleminfo[46], probleminfo[47], 
        probleminfo[48], probleminfo[49], probleminfo[50], probleminfo[51], probleminfo[52], probleminfo[53], 
        probleminfo[54], probleminfo[55], probleminfo[56], probleminfo[57], probleminfo[58], probleminfo[59], 
        probleminfo[60], probleminfo[61], probleminfo[62], probleminfo[63], probleminfo[64], probleminfo[65], 
        probleminfo[66], probleminfo[67], probleminfo[68], probleminfo[69], probleminfo[70], probleminfo[71], 
        probleminfo[72], probleminfo[73], probleminfo[74], probleminfo[75], probleminfo[76], probleminfo[77]
    )


def getquery():
    query = "SELECT * FROM routelinks"
    return query


def getqueryproblem():
    #         "ON DUPLICATE KEY UPDATE DateUpdated = IF(Rating != VALUES(Rating) OR " \
    #         "(Repeats != VALUES(Repeats)), VALUES(DateUpdated), DateUpdated)," \
    #         "Rating  = IF(Rating != VALUES(Rating), VALUES(Rating), Rating)," \
    #         "Repeats = IF(Repeats != VALUES(Repeats), VALUES(Repeats), Repeats)"
    query = "INSERT INTO routes (Method, Name, Grade, UserGrade, ConfigurationID, ConfigurationDesc, " \
            "ConfigurationLowGrade, ConfigurationHighGrade,MoonConfigID,SetterID,SetterNickName,SetterFirstName," \
            "SetterLastName,SetterCity,SetterCountry,SetterProfileImageUrl,SetterCanShareData,FirstAscender,Rating," \
            "UserRating,Repeats,Attempts,HoldSetupID,HoldSetupDesc,HoldSetupSetBy,HoldSetupDateInserted," \
            "HoldSetupDateUpdated,HoldSetupDateDeleted,HoldSetupIsLocked,HoldSetupHoldSets,HoldSetupMoonboardConfig," \
            "HoldSetupHoldLayoutID,HoldSetupAllowClimbMethods,IsBenchmark,StartHold1ID, StartHold1Desc,StartHold2ID," \
            "StartHold2Desc,IntermediateHold1ID,IntermediateHold1Desc,IntermediateHold2ID,IntermediateHold2Desc," \
            "IntermediateHold3ID,IntermediateHold3Desc,IntermediateHold4ID,IntermediateHold4Desc,IntermediateHold5ID," \
            "IntermediateHold5Desc,IntermediateHold6ID,IntermediateHold6Desc,IntermediateHold7ID," \
            "IntermediateHold7Desc,IntermediateHold8ID,IntermediateHold8Desc,IntermediateHold9ID," \
            "IntermediateHold9Desc,IntermediateHold10ID,IntermediateHold10Desc,IntermediateHold11ID," \
            "IntermediateHold11Desc,IntermediateHold12ID,IntermediateHold12Desc,IntermediateHold13ID," \
            "IntermediateHold13Desc,FinishHold1ID,FinishHold1Desc,FinishHold2ID,FinishHold2Desc,Holdsets,RepeatText," \
            "NumberOfTries,NameForUrl,Id,ApiID,DateInserted,DateUpdated,DateDeleted,DateTimeString) VALUES (%s, %s, " \
            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    return query


def removeproblem(linkname):
    query = "DELETE FROM routelinks WHERE link=" + "\"" + linkname + "\""
    return query


def submitdb(db, query):
    cur = db.cursor()
    cur.execute(query)
    return cur


def submitdbproblem(db, query, args):
    cur = db.cursor()
    cur.execute(query, args)
    return cur


####################################################################
# Allow the beautiful soup library to read the contents of the HTML
####################################################################

def routeexists(urlname):
    query = "SELECT * FROM routes WHERE Id=" + urlname + " LIMIT 1"
    return query


def uploading():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}
    db = connectdb()
    query = getquery()
    linkcollection = submitdb(db, query)
    problemnumber = 0
    for links in linkcollection.fetchall():
        problemnumber += 1
        name = links[0].split('/')
        probleminfoarray = [None] * 80
        problemexistsquery = routeexists(name[3])
        routecontained = submitdb(db, problemexistsquery)
        #logger.info(links[0])
        if routecontained.fetchall():
            pass
        else:
            result = None
            while result is None:
                try:
                    pageproblem = requests.get("https://www.moonboard.com" + links[0], headers=headers)
                    #logger.info("Found Page")
                    result = True
                except:
                    pass
            soup = BeautifulSoup(pageproblem.content, 'html.parser')
            checkexist = soup.find_all('span', {'class': 'field-validation-error'})
            badlinktext = soup.select('h1')
            checkbadlink = False
            if len(badlinktext) > 0 or (name[3] == u'309230') or (name[3] == u'308089'):
                checkbadlink = True
            problemdetail = soup.find_all("script", type="text/javascript")
            moonlayout2016 = False
            location = False
            holdsarray = [None] * 200
            holdsindex = 0
            logger.info(links[0])
            if checkexist:
                logger.info("Problem Doesn't Exist Removing from Database....")
                logger.info("Removing Route:" + str(problemnumber))
                # MySQL command to remove Links[0]
                query = removeproblem(links[0])
                submitdb(db, query)
            elif checkbadlink:
                logger.info("Problem Exists But Doesn't Have a Webpage....Skipping but keeping in DataBase.")
                logger.info("Skipping Route:" + str(problemnumber))
            else:
                for ids in problemdetail:
                    string = ids.getText()
                    if "var problem = " in ids.getText():
                        probleminfo = string.strip().split('\n', 1)[0]
                        probleminfo = probleminfo.replace('},{', '\",\"')
                        detailsarray = re.split(',(?=")', probleminfo)
                        if detailsarray[2] == u'"':
                            detailsarray.pop(2)
                        infoindex = 0
                        arrayindex = 0
                        endholdsindex = 200
                        for item in detailsarray:
                            if item == u'"':
                                detailsarray.pop(arrayindex)
                            else:
                                if "var problem = " in item:
                                    item = item[27:]
                                iteminfo = item.split(':')
                                if infoindex != 2:
                                    iteminfo[0] = iteminfo[0].replace("[", "")
                                    iteminfo[0] = iteminfo[0].replace("]", "")
                                    iteminfo[0] = iteminfo[0].replace("\"", "")
                                    iteminfo[0] = iteminfo[0].replace("{", "")
                                    iteminfo[0] = iteminfo[0].replace("}", "")
                                    iteminfo[1] = iteminfo[1].replace("\"", "")
                                    iteminfo[1] = iteminfo[1].replace("{", "")
                                    iteminfo[1] = iteminfo[1].replace("}", "")
                                    iteminfo[1] = iteminfo[1].replace("[", "")
                                    iteminfo[1] = iteminfo[1].replace("]", "")
                                    if infoindex == 142:
                                        iteminfo[1] = iteminfo[1].replace("\\", "")
                                        iteminfo[1] = iteminfo[1].replace("/", "")
                                        iteminfo[1] = iteminfo[1].replace("Date(", "")
                                        iteminfo[1] = iteminfo[1].replace(")", "")
                                if infoindex == 4:
                                    # 2016 Layout
                                    if iteminfo[1] == u'null':
                                        moonlayout2016 = True
                                        arrayindex += 4
                                        infoindex += 1
                                    else:
                                        # 2017Layout
                                        moonlayout2016 = False
                                        # is 2017 Layout this will have 3 arguments
                                        probleminfoarray[arrayindex] = iteminfo[2]
                                        arrayindex += 1
                                        infoindex += 1
                                elif (not moonlayout2016) and (infoindex > 4):
                                    # 2017 logic
                                    if (infoindex == 9) or (infoindex == 22):
                                        # Setter ID has 3 arguments
                                        # ##is 2017 Layout this will have 3 arguments
                                        probleminfoarray[arrayindex] = iteminfo[2]
                                        arrayindex += 1
                                        infoindex += 1
                                    elif (infoindex == 16) or (infoindex == 17) or (infoindex == 28) or (
                                                infoindex == 32) or (infoindex == 33):
                                        # Boolean I'll try to pass true or false
                                        if iteminfo[1] == u'null':
                                            # print("NULLIFY")
                                            arrayindex += 1
                                            infoindex += 1
                                        else:
                                            if iteminfo[1] == u'false':
                                                probleminfoarray[arrayindex] = 0
                                            else:
                                                probleminfoarray[arrayindex] = 1
                                            arrayindex += 1
                                            infoindex += 1
                                    elif infoindex == 17:
                                        # Boolean I'll try to pass true or false
                                        if iteminfo[1] == u'null':
                                            arrayindex += 1
                                            infoindex += 1
                                        else:
                                            if iteminfo[1] == u'false':
                                                probleminfoarray[arrayindex] = 0
                                            else:
                                                probleminfoarray[arrayindex] = 1
                                            arrayindex += 1
                                            infoindex += 1
                                    elif iteminfo[0] == u'Locations' or location:
                                        if iteminfo[0] != u'RepeatText':
                                            location = True
                                            infoindex += 1
                                        else:
                                            if iteminfo[1] == u'null':
                                                location = False
                                                arrayindex += 1
                                                infoindex += 1
                                            else:
                                                location = False
                                                probleminfoarray[arrayindex] = iteminfo[1]
                                                arrayindex += 1
                                                infoindex += 1
                                    # Logic for StartHolds
                                    elif infoindex == 36:
                                        holdsarray[holdsindex] = iteminfo[2]  #
                                        holdsindex += 1
                                        infoindex += 1
                                    elif (infoindex > 35) and (iteminfo[0] != u'Holdsets') and (
                                                infoindex < endholdsindex):
                                        # the rest of the hold information
                                        holdsarray[holdsindex] = iteminfo[1]
                                        holdsindex += 1
                                        infoindex += 1
                                    elif (iteminfo[0] == u'Holdsets') and (infoindex > 35):
                                        i = 0
                                        k = 0
                                        numstartholds = 0
                                        numfinishholds = 0
                                        holdsarray = filter(None, holdsarray)
                                        while i < len(holdsarray):
                                            endholdsindex = len(holdsarray)
                                            j = 0
                                            holdtype = [None] * 4
                                            while j < 4:
                                                holdtype[j] = holdsarray[i]
                                                j += 1
                                                i += 1
                                            if holdtype[2] == u'true':
                                                # isaStartHold
                                                numstartholds += 1
                                                if numstartholds == 2:
                                                    probleminfoarray[36] = holdtype[0]
                                                    probleminfoarray[37] = holdtype[1]
                                                else:
                                                    probleminfoarray[34] = holdtype[0]
                                                    probleminfoarray[35] = holdtype[1]

                                            elif holdtype[3] == u'true':
                                                numfinishholds += 1
                                                if numfinishholds == 2:
                                                    probleminfoarray[66] = holdtype[0]
                                                    probleminfoarray[67] = holdtype[1]
                                                else:
                                                    probleminfoarray[64] = holdtype[0]
                                                    probleminfoarray[65] = holdtype[1]
                                            else:
                                                probleminfoarray[38 + k] = holdtype[0]
                                                probleminfoarray[39 + k] = holdtype[1]
                                                k += 2
                                        arrayindex = 68
                                        probleminfoarray[arrayindex] = iteminfo[1]
                                        arrayindex += 1
                                    else:
                                        if iteminfo[1] == u'null':
                                            arrayindex += 1
                                            infoindex += 1
                                        else:
                                            probleminfoarray[arrayindex] = iteminfo[1]
                                            arrayindex += 1
                                            infoindex += 1
                                elif moonlayout2016 and infoindex > 4:
                                    # 2016 logic
                                    if (infoindex == 6) or (infoindex == 19):
                                        probleminfoarray[arrayindex] = iteminfo[2]
                                        # is 2017 Layout this will have 3 arguments
                                        arrayindex += 1
                                        infoindex += 1
                                    elif (infoindex == 13) or (infoindex == 14) or (infoindex == 25) or (
                                                infoindex == 29) or (infoindex == 30):
                                        # Boolean I'll try to pass true or false
                                        if iteminfo[1] == u'null':
                                            arrayindex += 1
                                            infoindex += 1
                                        else:
                                            if iteminfo[1] == u'false':
                                                probleminfoarray[arrayindex] = 0
                                            else:
                                                probleminfoarray[arrayindex] = 1
                                            arrayindex += 1
                                            infoindex += 1
                                    elif iteminfo[0] == u'Locations' or location:
                                        if iteminfo[0] != u'RepeatText':
                                            location = True
                                            infoindex += 1
                                        else:
                                            if iteminfo[1] == u'null':
                                                location = False
                                                arrayindex += 1
                                                infoindex += 1
                                            else:
                                                location = False
                                                probleminfoarray[arrayindex] = iteminfo[1]
                                                arrayindex += 1
                                                infoindex += 1
                                    elif infoindex == 33:
                                        holdsarray[holdsindex] = iteminfo[2]  #
                                        holdsindex += 1
                                        infoindex += 1
                                    elif (infoindex > 32) and (iteminfo[0] != u'Holdsets') and (
                                                infoindex < endholdsindex):
                                        # the rest of the hold information
                                        holdsarray[holdsindex] = iteminfo[1]
                                        holdsindex += 1
                                        infoindex += 1
                                    elif (iteminfo[0] == u'Holdsets') and (infoindex > 32):
                                        i = 0
                                        k = 0
                                        numstartholds = 0
                                        numfinishholds = 0
                                        holdsarray = filter(None, holdsarray)
                                        while i < len(holdsarray):
                                            endholdsindex = len(holdsarray)
                                            j = 0
                                            holdtype = [None] * 4
                                            while j < 4:
                                                holdtype[j] = holdsarray[i]
                                                j += 1
                                                i += 1
                                            if holdtype[2] == u'true':
                                                # isaStartHold
                                                numstartholds += 1
                                                if numstartholds == 2:
                                                    probleminfoarray[36] = holdtype[0]
                                                    probleminfoarray[37] = holdtype[1]
                                                else:
                                                    probleminfoarray[34] = holdtype[0]
                                                    probleminfoarray[35] = holdtype[1]

                                            elif holdtype[3] == u'true':
                                                numfinishholds += 1
                                                if numfinishholds == 2:
                                                    probleminfoarray[66] = holdtype[0]
                                                    probleminfoarray[67] = holdtype[1]
                                                else:
                                                    probleminfoarray[64] = holdtype[0]
                                                    probleminfoarray[65] = holdtype[1]
                                            else:
                                                probleminfoarray[38 + k] = holdtype[0]
                                                probleminfoarray[39 + k] = holdtype[1]
                                                k += 2
                                        arrayindex = 68
                                        probleminfoarray[arrayindex] = iteminfo[1]
                                        arrayindex += 1
                                    else:
                                        if iteminfo[1] == u'null':
                                            arrayindex += 1
                                            infoindex += 1
                                        else:
                                            probleminfoarray[arrayindex] = iteminfo[1]
                                            arrayindex += 1
                                            infoindex += 1
                                else:
                                    if iteminfo[1] == u'null':
                                        arrayindex += 1
                                        infoindex += 1
                                    else:
                                        probleminfoarray[arrayindex] = iteminfo[1]
                                        arrayindex += 1
                                        infoindex += 1

                args = getargsproblem(probleminfoarray)
                query = getqueryproblem()
                submitdbproblem(db, query, args)
                logger.info("Adding Route:" + str(problemnumber))


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
    uploading()
