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
problemsArrayEdited = []
link = ""
problemInfo = [0] * 205

HTMLCODE1 = """<!DOCTYPE html>\n<html lang="en-gb" prefix="og: http://ogp.me/ns#">\n <head>\n  <meta charset="utf-8"/>\n  <meta content="width=device-width, initial-scale=1, minimum-scale=1, maximum-scale=1" name="viewport"/>\n  <meta content="yes" name="apple-mobile-web-app-capable"/>\n  <meta content="black" name="apple-mobile-web-app-status-bar-style"/>\n  <title>\n   MoonBoard - DYNAMIC FINISH 5+ set by elder\n  </title>\n  <meta content="MoonBoard - DYNAMIC FINISH 5+ set by elder" name="description"/>\n  <link href="https://www.moonboard.com" rel="canonical"/>\n  <meta content="article" property="og:type"/>\n  <meta content="MoonBoard - DYNAMIC FINISH 5+ set by elder" property="og:title"/>\n  <meta content="MoonBoard - DYNAMIC FINISH 5+ set by elder" property="og:description"/>\n  <meta content="http://www.moonboard.com/Problems/View/319710/dynamic-finish" property="og:url"/>\n  <meta content="MoonBoard - Train hard, climb harder!" property="og:site_name"/>\n  <meta content="https://www.moonboard.com/Content/images/Home/schoolroom_tab.jpg" property="og:image"/>\n  <meta content="https://www.facebook.com/MoonClimbing/" property="article:publisher"/>\n  <meta content="summary" name="twitter:card"/>\n  <meta content="Welcome to training on the MoonBoard, climb on the same problems as other climbers from around the world." name="twitter:description"/>\n  <meta content="MoonBoard - DYNAMIC FINISH 5+ set by elder" name="twitter:title"/>\n  <meta content="@moonclimbing" name="twitter:site"/>\n  <link href="/Content/css?v=QkCv3Ink8UhO4MvvMbDj7c6n4a_MCzLO5nvR6ScCoME1" rel="stylesheet"/>\n  <link href="/Content/kendocss?v=McTNyEYACNI8AT8W05Ck_xrqJNpWsLaPJyswFdHht2U1" rel="stylesheet"/>\n  <link href="https://fonts.googleapis.com/css?family=Allerta+Stencil|Open+Sans" rel="stylesheet"/>\n  <link href="/Content/mb-home.min.css" rel="stylesheet">\n   <script src="/bundles/jquery?v=lp1DmbzZOS69_gd1TSKRrjSgn0R95B8ZUZN-5qo5FQI1">\n   </script>\n   <script src="/bundles/jqueryval?v=WhRmI8vUVF186UwYB1zRP7-DwJzqpKlt0JksOBJvolw1">\n   </script>\n   <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js">\n   </script>\n   <script src="/Scripts/helpers.min.js">\n   </script>\n   <script src="https://kendo.cdn.telerik.com/2017.2.504/js/kendo.all.min.js">\n   </script>\n   <script src="https://kendo.cdn.telerik.com/2017.2.504/js/kendo.aspnetmvc.min.js">\n   </script>\n   <script src="/Scripts/helpers.min.js">\n   </script>\n   <script src="/Scripts/pixi.min.js">\n   </script>\n   <script src="/Scripts/wbx-MoonBoard.min.js">\n   </script>\n   <script src="//s7.addthis.com/js/300/addthis_widget.js#pubid=ra-594017332469389d&amp;async=1&amp;domready=1" type="text/javascript">\n   </script>\n   <link href="favicon.ico" rel="shortcut icon"/>\n   <style type="text/css">\n    .video-wrap {\r\n            width: 100%;\r\n            max-width: 100%;\r\n        }\r\n\r\n        iframe {\r\n            width: 100%;\r\n        }\r\n\r\n        .btnMbFloatMnuComment{\r\n            display: none;\r\n        }\n   </style>\n  </link>\n </head>\n <body>\n  <div class="relative">\n   <div class="container mb-header">\n    <div class="row">\n     <div class="col-sm-12 col-md-5 pl-0 pr-0">\n      <div class="mb-brand ">\n       <a href="/">\n        <img alt="Moon, 100% Climbing" class="logo-des" src="/Content/images/logos/moonboard.gif"/>\n       </a>\n      </div>\n     </div>\n     <div class="col-sm-12 col-md-7">\n      <div class="appStoreWrapper">\n       <span class="bold text-uppercase strap">\n        Download the free MoonBoard app\n       </span>\n       <ul class="appStore">\n        <li>\n         <a href="https://itunes.apple.com/gb/app/moon-climbing-moonboard/id1090934862?mt=8" target="_blank">\n          <img alt="AppStore" src="/Content/images/apple.jpg" title="Apple app store"/>\n         </a>\n        </li>\n        <li>\n         <a href="https://play.google.com/store/apps/details?id=com.moonclimbing.moonboard&amp;hl=en_GB">\n          <img alt="Google play Store" src="/Content/images/android.jpg" title="Google play store"/>\n         </a>\n        </li>\n       </ul>\n      </div>\n      <div class="account-profile">\n       <ul class="nav navbar-nav navbar-right">\n        <li>\n         <a href="/Account/Register" id="registerLink">\n          Register\n         </a>\n        </li>\n        <li>\n         <a href="/Account/Login" id="loginLink">\n          Log in\n         </a>\n        </li>\n       </ul>\n      </div>\n     </div>\n    </div>\n   </div>\n   <div class="navbar navbar-expand-md">\n    <div class="container">\n     <div class="navbar-header">\n      <button class="navbar-toggle" data-target=".navbar-collapse" data-toggle="collapse" type="button">\n       <span class="icon-bar">\n       </span>\n       <span class="icon-bar">\n       </span>\n       <span class="icon-bar">\n       </span>\n      </button>\n     </div>\n     <div class="navbar-collapse collapse">\n      <ul class="nav navbar-nav">\n       <li>\n        <a href="/what-is-the-moonboard" id="lnkwhat">\n         What is the MoonBoard\n        </a>\n       </li>\n       <li>\n        <a href="/how-to-build-your-moonboard" id="lnkbuild">\n         Build a MoonBoard\n        </a>\n       </li>\n       <li>\n        <a href="https://www.moonclimbing.com" target="_blank">\n         Buy MoonBoard Holds\n        </a>\n       </li>\n       <li>\n        <a href="/Video/moonboard-how-to-videos" id="lnkhowto">\n         How to use the App\n        </a>\n       </li>\n       <li>\n        <a href="/Faq" id="lnkfaq">\n         FAQ\n        </a>\n       </li>\n       <li id="lilogin">\n        <a href="/Account/Login">\n         Login\n        </a>\n       </li>\n       <li id="liregister">\n        <a href="/Account/Register">\n         Register\n        </a>\n       </li>\n      </ul>\n     </div>\n    </div>\n   </div>\n  </div>\n  <div class="container body-content pl-0 pr-0">\n   <div class="inner-container">\n    <div class="row fullheight relative">\n     <div class="col-md-6 fullheight moon-slide-menu white-tab">\n      <div class="moonTabstrip">\n       <button class="closeButton">\n        <img alt="Close information" aria-label="Close information" src="/Content/images/Buttons/close.png">\n        </img>\n       </button>\n      </div>\n      <div class="problem addthis">\n       <span class="field-validation-valid" data-valmsg-for="Problem-Not-Found" data-valmsg-replace="true">\n       </span>\n       <div class="problem-inner view">\n        <h3>\n         DYNAMIC FINISH\n        </h3>\n        <p>\n         elder\n        </p>\n        <p>\n         Be the first to repeat this problem\n        </p>\n        <p>\n         5+\n        </p>\n        <p>\n         Feet follow hands\n        </p>\n        <ul>\n         <li>\n          <img src="/Content/images/starempty.png">\n          </img>\n         </li>\n         <li>\n          <img src="/Content/images/starempty.png"/>\n         </li>\n         <li>\n          <img src="/Content/images/starempty.png"/>\n         </li>\n        </ul>\n        <div addthis:description="MoonBoard - DYNAMIC FINISH 5+ set by elder" addthis:media="https://moonboard.ems-x.com/Content/images/Home/schoolroom_tab.jpg" addthis:title="DYNAMIC FINISH 5+ set by elder" addthis:url="http://www.moonboard.com/Problems/View/319710/dynamic-finish" class="addthis_inline_share_toolbox">\n        </div>\n       </div>\n      </div>\n      <div class="k-tabstrip-wrapper">\n       <div class="k-widget k-tabstrip k-header" id="tabViewProblem">\n        <ul class="k-reset k-tabstrip-items">\n         <li class="k-item k-state-default k-state-active">\n          <a class="k-link" href="#tabViewProblem-1">\n           Repeats\n          </a>\n         </li>\n         <li class="k-item k-state-default">\n          <a class="k-link" href="#tabViewProblem-2">\n           Videos\n          </a>\n         </li>\n        </ul>\n        <div class="k-content k-state-active" id="tabViewProblem-1" style="display:block">\n         <div class="k-widget k-grid" id="grdRepeats">\n          <div class="k-grid-header">\n           <div class="k-grid-header-wrap">\n            <table>\n             <colgroup>\n              <col/>\n             </colgroup>\n             <thead class="k-grid-header">\n              <tr>\n               <th class="k-header" data-index="0" scope="col">\n                <div class="grid-header" id="hdrRepeatsTotal">\n                 Repeats\n                </div>\n               </th>\n              </tr>\n             </thead>\n            </table>\n           </div>\n          </div>\n          <div class="k-grid-content" style="height:200px">\n           <table>\n            <colgroup>\n             <col/>\n            </colgroup>\n            <tbody>\n             <tr class="k-no-data">\n              <td colspan="1">\n              </td>\n             </tr>\n            </tbody>\n           </table>\n          </div>\n          <div class="k-pager-wrap k-grid-pager">\n           <ul class="k-pager-numbers k-reset">\n            <li>\n             <span class="k-state-selected" data-page="1">\n              1\n             </span>\n            </li>\n           </ul>\n          </div>\n         </div>\n         <script>\n          kendo.syncReady(function(){jQuery("#grdRepeats").kendoGrid({"columns":[{"template":" "}],"pageable":{"autoBind":false,"info":false,"previousNext":false,"buttonCount":5},"sortable":true,"scrollable":{"height":"200px"},"noRecords":{"template":"\\u003cdiv class=\\"no-records\\"\\u003e\\u003cbr/\\u003e\\u003cspan\\u003eThis problem is unrepeated\\u003c/span\\u003e\\u003c/div\\u003e"},"messages":{"noRecords":"No records available."},"autoBind":false,"dataSource":{"type":(function(){if(kendo.data.transports[\'aspnetmvc-ajax\']){return \'aspnetmvc-ajax\';} else{throw new Error(\'The kendo.aspnetmvc.min.js script is not included.\');}})(),"transport":{"read":{"url":"/Problems/GetRepeats"},"prefix":""},"pageSize":15,"page":1,"total":0,"serverPaging":true,"serverSorting":true,"serverFiltering":true,"serverGrouping":true,"serverAggregates":true,"filter":[],"schema":{"data":"Data","total":"Total","errors":"Errors","model":{"fields":{"Id":{"type":"number"},"Problem":{"type":"object"},"Attempts":{"type":"number"},"Grade":{"type":"string"},"NumberOfTries":{"type":"string"},"Rating":{"type":"number","defaultValue":null},"DateClimbed":{"type":"date"},"DateClimbedAsString":{"type":"string"},"DateInserted":{"type":"date","defaultValue":null},"Comment":{"type":"string"},"IsSuggestedBenchmark":{"type":"boolean"},"User":{"type":"object"}}}}},"rowTemplate":"\\u003ctr data-uid=\\u0027#: Id #\\u0027\\u003e\\r\\n\\r\\n\\u003ctd\\u003e\\r\\n\\r\\n\\u003cdiv class=\\u0027repeats\\u0027\\u003e\\r\\n\\r\\n           \\u003cdiv class=\\u0027icon\\u0027\\u003e\\r\\n\\r\\n\\r\\n\\r\\n\\u003cdiv class=\\u0027profile\\u0027 style=\\u0027background-image:url(#:User.ProfileImageUrl#)\\u0027\\u003e\\u003c/div\\u003e\\r\\n\\r\\n\\u003c/div\\u003e\\r\\n\\r\\n\\r\\n\\r\\n\\r\\n\\u003cdiv class=\\u0027repeat\\u0027\\u003e\\r\\n\\r\\n    \\u003ch3\\u003e\\u003ca href=\\u0027/Account/Profile/#:User.Id#\\u0027\\u003e#:User.Nickname#\\u003c/a\\u003e\\u003c/h3\\u003e\\r\\n\\r\\n\\r\\n\\r\\n\\u003cp\\u003e\\r\\n\\r\\n #:NumberOfTries #\\r\\n\\r\\n\\u003c/p\\u003e\\r\\n\\r\\n\\r\\n\\r\\n\\r\\n\\u003cp\\u003e\\r\\n\\r\\nGrade: #:Grade #\\r\\n\\r\\n\\u003c/p\\u003e\\r\\n\\r\\n\\u003cp\\u003e\\r\\n\\r\\nClimbed: #:DateClimbedAsString#\\r\\n\\r\\n\\u003c/p\\u003e\\r\\n\\u003cp\\u003e\\r\\n\\r\\n\\r\\n   #if(Comment != null){#\\r\\n#:Comment#\\r\\n\\r\\n            #}#\\r\\n\\r\\n\\r\\n\\r\\n\\u003c/p\\u003e\\r\\n\\u003c/div\\u003e\\u003c/div\\u003e\\r\\n\\r\\n\\u003c/td\\u003e\\u003c/tr\\u003e"});});\n         </script>\n        </div>\n        <div class="k-content" id="tabViewProblem-2">\n         <div class="video-wrap">\n          <div class="no-video">\n           <br/>\n           <a href="/Video/Edit">\n            Add a video\n           </a>\n          </div>\n         </div>\n        </div>\n       </div>\n      </div>\n      <script>\n       kendo.syncReady(function(){jQuery("#tabViewProblem").kendoTabStrip({"animation":false});});\n      </script>\n     </div>\n     <div class="col-md-6 fullheight moon-slide-menu-butt">\n      <div id="moonboard">\n       <div id="mb-loader">\n       </div>\n      </div>\n      <script type="text/javascript">\n       $(function ($) {\r\n\r\n\r\n        moonBoardObj.init(true, false);\r\n\r\n\r\n    });\r\n\r\n\r\n\r\n\r\n\r\n\r\n    var $lastProblemTr;\r\n\r\n    function problemSelected(logbook) {\r\n\r\n        \r\n        var $problemTr = $(event.target).closest("tr");\r\n\r\n\r\n        var $grid = $("#" + $problemTr.closest(".k-grid").attr("id")).data("kendoGrid");\r\n\r\n\r\n        var model = $grid.dataItem($problemTr);\r\n\r\n        moonBoardObj.renderProblem(logbook ? model.Problem : model);\r\n\r\n        $problemTr.addClass(\'selected\');\r\n\r\n        if ($lastProblemTr) {\r\n\r\n            $lastProblemTr.removeClass(\'selected\');\r\n        }\r\n\r\n        $lastProblemTr = $problemTr;\r\n\r\n    }\n      </script>\n      <div id="mb-sidemenu">\n       <button id="btnMbFloatMnu">\n        <img alt="Show problems" src="/Content/images/Buttons/information.png"/>\n       </button>\n       <button id="btnMbFloatMnuComment">\n        <img alt="Show comments" src="/Content/images/Buttons/comment.png"/>\n       </button>\n      </div>\n      <script>\n       $("#btnMbFloatMnu").on("click", function () {\r\n\r\n\r\n\r\n        toggleSlideMenu();\r\n\r\n\r\n    });\r\n\r\n\r\n\r\n    $("#btnMbFloatMnuComment").on("click", function () {\r\n\r\n\r\n        if (currentProblem) {\r\n\r\n            var $win = $("#commentsWrapper");\r\n\r\n            if ($win.isInvisible()) {\r\n                $win.visible();\r\n            }\r\n            else {\r\n                $win.invisible();\r\n            }\r\n        }\r\n    });\r\n\r\n\r\n\r\n\r\n    function toggleSlideMenu() {\r\n\r\n\r\n        $(\'body\').toggleClass(\'moon-slide-menu-open\');\r\n    }\n      </script>\n     </div>\n    </div>\n   </div>\n   <script type="text/javascript">\n    var problem = JSON.parse(\'{"Method":"Feet follow hands","Name":"DYNAMIC FINISH","Grade":"5+","UserGrade":null,"MoonBoardConfiguration":{"Id":2,"Description":"25\xb0 MoonBoard","LowGrade":null,"HighGrade":null},"MoonBoardConfigurationId":0,"Setter":{"Id":"352585bb-32e6-44e9-82c9-5e515c8f79c6","Nickname":"elder","Firstname":"david","Lastname":"elder","City":"glasgow","Country":"SCOTLAND","ProfileImageUrl":"/Content/Account/Images/default-profile.png?636622683545554976","CanShareData":false},"FirstAscender":false,"Rating":0,"UserRating":0,"Repeats":0,"Attempts":0,"Holdsetup":{"Id":15,"Description":"MoonBoard Masters 2017","Setby":null,"DateInserted":null,"DateUpdated":null,"DateDeleted":null,"IsLocked":false,"Holdsets":null,"MoonBoardConfigurations":null,"HoldLayoutId":0,"AllowClimbMethods":true},"IsBenchmark":false,"Moves":[{"Id":1737402,"Description":"G2","IsStart":true,"IsEnd":false},{"Id":1737403,"Description":"A3","IsStart":true,"IsEnd":false},{"Id":1737404,"Description":"B9","IsStart":false,"IsEnd":false},{"Id":1737405,"Description":"D11","IsStart":false,"IsEnd":false},{"Id":1737406,"Description":"H14","IsStart":false,"IsEnd":false},{"Id":1737408,"Description":"J18","IsStart":false,"IsEnd":true}],"Holdsets":null,"Locations":[{"Id":0,"Holdset":null,"Description":"A3","X":95,"Y":838,"Color":"0x00FF00","Rotation":0,"Type":1,"HoldNumber":null,"Direction":0,"DirectionString":"N"},{"Id":0,"Holdset":null,"Description":"B9","X":145,"Y":536,"Color":"0x0000FF","Rotation":0,"Type":2,"HoldNumber":null,"Direction":0,"DirectionString":"N"},{"Id":0,"Holdset":null,"Description":"D11","X":245,"Y":436,"Color":"0x0000FF","Rotation":0,"Type":2,"HoldNumber":null,"Direction":0,"DirectionString":"N"},{"Id":0,"Holdset":null,"Description":"G2","X":395,"Y":888,"Color":"0x00FF00","Rotation":0,"Type":1,"HoldNumber":null,"Direction":0,"DirectionString":"N"},{"Id":0,"Holdset":null,"Description":"H14","X":445,"Y":286,"Color":"0x0000FF","Rotation":0,"Type":2,"HoldNumber":null,"Direction":0,"DirectionString":"N"},{"Id":0,"Holdset":null,"Description":"J18","X":545,"Y":86,"Color":"0xFF0000","Rotation":0,"Type":3,"HoldNumber":null,"Direction":0,"DirectionString":"N"},{"Id":0,"Holdset":null,"Description":"J16","X":545,"Y":186,"Color":"0x0000FF","Rotation":0,"Type":2,"HoldNumber":null,"Direction":0,"DirectionString":"N"}],"RepeatText":"Be the first to repeat this problem","NumberOfTries":null,"NameForUrl":"dynamic-finish","Id":319710,"ApiId":0,"DateInserted":"\\/Date(1526562861860)\\/","DateUpdated":null,"DateDeleted":null,"DateTimeString":"17 May 2018 14:14"}\');\r\n\r\n    window.onresize = function (event) {\r\n\r\n\r\n        sizeContent();\r\n    };\r\n\r\n\r\n\r\n\r\n    function sizeContent() {\r\n        var MARGIN = 50;\r\n        var headerHeight = $(".header").outerHeight(true);\r\n        var $bodyContent = $(".body-content");\r\n\r\n\r\n        var offset = (document.body.clientHeight - $bodyContent.offset().top - $("footer").outerHeight());\r\n\r\n            $bodyContent.innerHeight(offset);\r\n\r\n\r\n            var $grdRepeats = $("#grdRepeats");\r\n\r\n    \r\n            var headerHeight = $("#hdrRepeatsTotal").outerHeight(true);\r\n\r\n            var $tabViewProblem = $("#tabViewProblem");\r\n\r\n            var tabHeight = $tabViewProblem.find(".k-tabstrip-items").outerHeight(true);\r\n\r\n            var $content = $tabViewProblem.find(".k-content");\r\n\r\n\r\n\r\n            $content.height($bodyContent.innerHeight() - ($("div.k-tabstrip-wrapper").offset().top - tabHeight - headerHeight));\r\n\r\n            $grdRepeats.data("kendoGrid").resize();\r\n\r\n\r\n        if (moonBoardObj) {\r\n            moonBoardObj.resize();\r\n        }\r\n\r\n\r\n\r\n    }\r\n\r\n            function getHoldsetConfig(Id)\r\n        {\r\n\r\n             ajax("/Problems/GetHoldsets/" + Id, "GET", null, function (data) {\r\n\r\n            moonBoardObj.clearHolds();\r\n\r\n            moonBoardObj.clear();\r\n\r\n            moonBoardObj.loadHoldsets(data);\r\n\r\n\r\n\r\n            moonBoardObj.renderProblem(problem);\r\n\r\n\r\n        })\r\n    }\r\n\r\n\r\n\r\n    $(function ($) {\r\n\r\n\r\nsizeContent();\r\n\r\n        moonBoardObj.problemRendered = function (model) {\r\n\r\n            var $grdRepeats = $("#grdRepeats").data("kendoGrid");\r\n\r\n            $grdRepeats.dataSource.filter({ field: "Id", operator: "eq", value: problem.Id });\r\n\r\n        }\r\n\r\n\r\n\r\n        if (problem) {\r\n\r\n\r\n            getHoldsetConfig(problem.Holdsetup.Id);\r\n\r\n\r\n\r\n        }\r\n\r\n\r\n        $(".moonTabstrip .closeButton").on("click", function () {\r\n\r\n            toggleSlideMenu();\r\n\r\n        });\r\n\r\n\r\n\r\n\r\n    });\r\n\r\n\r\n\r\n            var addthis_share = {\r\n        url: \'http://www.moonboard.com/Problems/View/319710/dynamic-finish\',\r\n        title: \'DYNAMIC FINISH 5+ set by elder\',\r\n        description: \'MoonBoard - DYNAMIC FINISH 5+ set by elder\',\r\n        media: \'https://www.moonboard.com/Content/images/Home/schoolroom_tab.jpg\'\r\n\r\n            }\n   </script>\n   <footer>\n    <div class="row">\n     <div class="col-xs-12 col-md-6">\n      <span class="f-caption">\n       \xc2\xa9 2018, Moon Climbing. All Rights Reserved.\n      </span>\n     </div>\n     <div class="col-xs-12 col-md-6">\n      <div aria-label="Social media links" class="social" role="region">\n       <ul>\n        <li>\n         <span class="f-caption">\n          Follow Moon Climbing on\n         </span>\n        </li>\n        <li>\n         <a href="https://www.facebook.com/moonclimbing/" target="_blank">\n          <img alt="Moon Climbing - Facebook" border="0" height="42" src="/Content/images/logos/facebook.png" title="Moon Climbing - Facebook" width="42"/>\n         </a>\n        </li>\n        <li>\n         <a href="https://www.twitter.com/moonclimbing/" target="_blank">\n          <img alt="Moon Climbing - Twitter" border="0" height="42" src="/Content/images/logos/twitter.png" title="Moon Climbing - Twitter" width="42"/>\n         </a>\n        </li>\n        <li>\n         <a href="https://www.instagram.com/moonclimbing/?utm_source=MoonBoard" target="_blank">\n          <img alt="Moon Climbing - Instagram" border="0" height="44" src="/Content/images/logos/instagram.png" title="Moon Climbing - Instagram" width="44"/>\n         </a>\n        </li>\n       </ul>\n      </div>\n     </div>\n    </div>\n   </footer>\n  </div>\n  <!-- Global site tag (gtag.js) - Google Analytics -->\n  <script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-73435918-1">\n  </script>\n  <script>\n   window.dataLayer = window.dataLayer || [];\r\n        function gtag() { dataLayer.push(arguments); }\r\n        gtag(\'js\', new Date());\r\n\r\n        gtag(\'config\', \'UA-73435918-1\');\r\n\r\n\r\n        $(document).click(function (event) {\r\n            $(\'.navbar-collapse\').collapse(\'hide\');\r\n        });\n  </script>\n </body>\n</html>"""

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
    # return (problemInfo[0], problemInfo[1], problemInfo[2], problemInfo[3], problemInfo[4], problemInfo[5],
    #         problemInfo[6], problemInfo[7], problemInfo[8], problemInfo[9], problemInfo[10], problemInfo[11],
    #         problemInfo[12], problemInfo[13], problemInfo[14], problemInfo[15], problemInfo[16], problemInfo[17],
    #         problemInfo[18], problemInfo[19], problemInfo[20], problemInfo[21], problemInfo[22], problemInfo[23],
    #         problemInfo[24], problemInfo[25], problemInfo[26], problemInfo[27], problemInfo[28], problemInfo[29],
    #         problemInfo[30], problemInfo[31], problemInfo[32], problemInfo[33], problemInfo[34], problemInfo[35],
    #         problemInfo[36], problemInfo[37], problemInfo[38], problemInfo[39], problemInfo[40], problemInfo[41],
    #         problemInfo[42], problemInfo[43], problemInfo[44], problemInfo[45], problemInfo[46], problemInfo[47],
    #         problemInfo[48], problemInfo[49], problemInfo[50], problemInfo[51], problemInfo[52], problemInfo[53],
    #         problemInfo[54], problemInfo[55], problemInfo[56], problemInfo[57], problemInfo[58], problemInfo[59],
    #         problemInfo[60], problemInfo[61], problemInfo[62], problemInfo[63], problemInfo[64], problemInfo[65],
    #         problemInfo[66], problemInfo[67], problemInfo[68], problemInfo[69], problemInfo[70], problemInfo[71],
    #         problemInfo[72], problemInfo[73], problemInfo[74], problemInfo[75], problemInfo[76], problemInfo[77],
    #         problemInfo[78], problemInfo[79], problemInfo[80], problemInfo[81], problemInfo[82], problemInfo[83],
    #         problemInfo[84], problemInfo[85], problemInfo[86], problemInfo[87], problemInfo[88], problemInfo[89],
    #         problemInfo[90], problemInfo[91], problemInfo[92], problemInfo[93], problemInfo[94], problemInfo[95],
    #         problemInfo[96], problemInfo[97], problemInfo[98], problemInfo[99], problemInfo[100], problemInfo[101],
    #         problemInfo[102], problemInfo[103], problemInfo[104], problemInfo[105], problemInfo[106], problemInfo[107],
    #         problemInfo[108], problemInfo[109], problemInfo[110], problemInfo[111], problemInfo[112], problemInfo[113],
    #         problemInfo[114])
    # return args
    return (problemInfo[0], problemInfo[1], problemInfo[2], problemInfo[3], problemInfo[4], problemInfo[5], problemInfo[6], problemInfo[7], problemInfo[8], problemInfo[9], problemInfo[10], problemInfo[11], problemInfo[12], problemInfo[13], problemInfo[14], problemInfo[15], problemInfo[16], problemInfo[17], problemInfo[18],problemInfo[19], problemInfo[20], problemInfo[21], problemInfo[22], problemInfo[23], problemInfo[24], problemInfo[25], problemInfo[26], problemInfo[27], problemInfo[28], problemInfo[29],problemInfo[30], problemInfo[31], problemInfo[32], problemInfo[33], problemInfo[34], problemInfo[35], problemInfo[36], problemInfo[37], problemInfo[38], problemInfo[39],problemInfo[40], problemInfo[41], problemInfo[42], problemInfo[43], problemInfo[44], problemInfo[45], problemInfo[46], problemInfo[47], problemInfo[48], problemInfo[49],problemInfo[50], problemInfo[51], problemInfo[52], problemInfo[53], problemInfo[54], problemInfo[55], problemInfo[56], problemInfo[57], problemInfo[58], problemInfo[59],problemInfo[60], problemInfo[61], problemInfo[62], problemInfo[63], problemInfo[64], problemInfo[65], problemInfo[66], problemInfo[67], problemInfo[68], problemInfo[69], problemInfo[70], problemInfo[71], problemInfo[72], problemInfo[73], problemInfo[74], problemInfo[75], problemInfo[76], problemInfo[77])


def getQuery():
    query = "SELECT * FROM routelinks"

    return query

def getqueryproblem():
    
    #         "ON DUPLICATE KEY UPDATE DateUpdated = IF(Rating != VALUES(Rating) OR " \
    #         "(Repeats != VALUES(Repeats)), VALUES(DateUpdated), DateUpdated)," \
    #         "Rating  = IF(Rating != VALUES(Rating), VALUES(Rating), Rating)," \
    #         "Repeats = IF(Repeats != VALUES(Repeats), VALUES(Repeats), Repeats)"
    query = "INSERT INTO routes (Method, Name, Grade, UserGrade, ConfigurationID, ConfigurationDesc, ConfigurationLowGrade, ConfigurationHighGrade,MoonConfigID,SetterID,SetterNickName,SetterFirstName,SetterLastName,SetterCity,SetterCountry,SetterProfileImageUrl,SetterCanShareData,FirstAscender,Rating,UserRating,Repeats,Attempts,HoldSetupID,HoldSetupDesc,HoldSetupSetBy,HoldSetupDateInserted,HoldSetupDateUpdated,HoldSetupDateDeleted,HoldSetupIsLocked,HoldSetupHoldSets,HoldSetupMoonboardConfig,HoldSetupHoldLayoutID,HoldSetupAllowClimbMethods,IsBenchmark,StartHold1ID, StartHold1Desc,StartHold2ID,StartHold2Desc,IntermediateHold1ID,IntermediateHold1Desc,IntermediateHold2ID,IntermediateHold2Desc,IntermediateHold3ID,IntermediateHold3Desc,IntermediateHold4ID,IntermediateHold4Desc,IntermediateHold5ID,IntermediateHold5Desc,IntermediateHold6ID,IntermediateHold6Desc,IntermediateHold7ID,IntermediateHold7Desc,IntermediateHold8ID,IntermediateHold8Desc,IntermediateHold9ID,IntermediateHold9Desc,IntermediateHold10ID,IntermediateHold10Desc,IntermediateHold11ID,IntermediateHold11Desc,IntermediateHold12ID,IntermediateHold12Desc,IntermediateHold13ID,IntermediateHold13Desc,FinishHold1ID,FinishHold1Desc,FinishHold2ID,FinishHold2Desc,Holdsets,RepeatText,NumberOfTries,NameForUrl,Id,ApiID,DateInserted,DateUpdated,DateDeleted,DateTimeString) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"


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

def isStartHold(array):
    pass

def isIntermediateHold(array):
    pass

def isFinishHold(array):
    pass


def numMoves(array):
    pass


def numRepeats(array):
    pass

def indexLoadCheck(indexNum):
    switcher = {
        0: True,
        1: True,
        2: False,
        3: "V3+",
        4: "V3",
        5: "V3+",
        6: "V3",
        7: "V3+",
        8: "V3",
        9: "V3+",
        10: "V3",
        11: "V3+",
        12: "V3",
        13: "V3+",
        14: "V3",
        15: "V3+",
        16: "V3",
        17: "V3+",
        18: "V3",
        19: "V3+",
        20: "V3",
        21: "V3+",
        22: "V3",
        23: "V3+",
        24: "V3",
        25: "V3+",
        26: "V3",
        27: "V3+",
        28: "V3",
        29: "V3+",
        30: "V3",
        31: "V3+",
        32: "V3",
        33: "V3+",
        34: "V3",
        35: "V3+",
        36: "V3",
        37: "V3+",
        38: "V3",
        39: "V3+",
        40: "V3",
        41: "V3+",
        42: "V3",
        43: "V3+",
        44: "V3",
        45: "V3+",
        46: "V3",
        47: "V3+",
        48: "V3",
        49: "V3+",
        50: "V3",
        51: "V3+",
        52: "V3",
        53: "V3+",
        54: "V3",
        55: "V3+",
        56: "V3",
        57: "V3+",
        58: "V3",
        59: "V3+",
        60: "V3",
        61: "V3+",
        62: "V3",
        63: "V3+",
        64: "V3",
        65: "V3+",
        66: "V3",
        67: "V3+",
        68: "V3",
        69: "V3+",
        70: "V3",
        71: "V3+",
        72: "V3",
        73: "V3+",
        74: "V3",
        75: "V3+",
        76: "V3",
        77: "V3+",
        78: "V3",
        79: "V3+",
        80: "V3",
        81: "V3+",
        82: "V3",
        83: "V3+",
        84: "V3",
        85: "V3+",
        86: "V3",
        87: "V3+",
        88: "V3",
        89: "V3+",
        90: "V3",
        91: "V3+",
        92: "V3",
        93: "V3+",
        94: "V3",
        95: "V3+",
        96: "V3",
        97: "V3+",
        98: "V3",
        99: "V3+",
        100: "V3",
        101: "V3+",
        102: "V3",
        103: "V3+",
        104: False,
        105: False,
        106: False,
        107: False,
        108: False,
        109: False,
        110: False,
        111: False,
        112: False,
        113: False,
        114: False,
        115: False,
        116: False,
        117: False,
        118: False,
        119: False,
        120: False,
        121: False,
        122: False,
        123: False,
        124: False,
        125: False,
        126: False,
        127: False,
        128: False,
        129: False,
        130: False,
        131: False,
        132: False,
        133: False,
        134: False,
        135: False,
        136: False,
        137: False,
        138: True,
        139: True,
        140: True,
        141: True,
        142: True,
        143: True,
        144: True,
        145: False,

    }
    return switcher.get(indexNum, None)
# Allow the beautiful soup library to read the contents of the HTML
###################################


def loadMainPage():
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0'}


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
        problemNumber += 1
        problemInfoArray = [None] *80
        print(str(links))
        # string = zip(*links)
        print("https://www.moonboard.com" + links[0])
        #pageProblem = requests.get("https://www.moonboard.com" + links[0], headers=headers)
        #print(pageProblem.status_code)
            #pageProblem = requests.get("http://www.moonboard.com/problems/View/" + problemNum + "/" + link)
        #logger.info('pageContent = %s' % pageProblem.content)
        #soup = BeautifulSoup(pageProblem.content, 'html.parser')
        soupproblem = BeautifulSoup(HTMLCODE1, 'html.parser')
        #logger.debug(soupproblem.prettify(encoding='utf-8'))
        problemDetail = soupproblem.find_all("script", type="text/javascript")
        #problemDetail = soup.find_all("script", type="text/javascript")
        print(problemDetail)
        MoonLayout2016 = False
        Location = False
        HoldsArray = [None] * 200
        holdsIndex = 0
        holdType = [None] * 200
        for ids in problemDetail:
            string = ids.getText()
            if ("var problem = ") in ids.getText():
                problemInfo = string.strip().split('\n', 1)[0]
                detailsArray = problemInfo.split(',')
                infoIndex = 0
                arrayIndex = 0
                endHoldsIndex = 200
                for item in detailsArray:
                    if ("var problem = ") in item:
                        item = item[27:]
                    itemInfo = item.split(':')
                    print(itemInfo[1])

                    if (infoIndex != 2):
                        itemInfo[0] = itemInfo[0].replace("[", "")
                        itemInfo[0] = itemInfo[0].replace("]", "")
                        itemInfo[0] = itemInfo[0].replace("\"", "")
                        itemInfo[0] = itemInfo[0].replace("{", "")
                        itemInfo[0] = itemInfo[0].replace("}", "")
                        itemInfo[1] = itemInfo[1].replace("\"", "")
                        itemInfo[1] = itemInfo[1].replace("{", "")
                        itemInfo[1] = itemInfo[1].replace("}", "")
                        itemInfo[1] = itemInfo[1].replace("[", "")
                        itemInfo[1] = itemInfo[1].replace("]", "")
                        print(itemInfo[0])
                        print(itemInfo[1])
                        if infoIndex == 142:
                            itemInfo[1] = itemInfo[1].replace("\\", "")
                            itemInfo[1] = itemInfo[1].replace("/", "")
                            itemInfo[1] = itemInfo[1].replace("Date(", "")
                            itemInfo[1] = itemInfo[1].replace(")", "")
                    if infoIndex == 4:
                        ##2016 Layout
                        if itemInfo[1] == u'null':
                            MoonLayout2016 = True
                            arrayIndex += 4
                            infoIndex += 1
                            print("NULLIFY")
                        else:
                            #2017Layout
                            MoonLayout2016 = False
                            problemInfoArray[arrayIndex] = itemInfo[2] ##is 2017 Layout this will have 3 arguments
                            arrayIndex += 1
                            infoIndex += 1
                    elif (not MoonLayout2016) and (infoIndex > 4):
                        #2017 logic
                        if (infoIndex == 9) or (infoIndex == 22):
                            ##Setter ID has 3 arguments
                            problemInfoArray[arrayIndex] = itemInfo[2]  ##is 2017 Layout this will have 3 arguments
                            arrayIndex += 1
                            infoIndex += 1
                        elif (infoIndex == 16) or (infoIndex == 17) or (infoIndex == 28) or (infoIndex == 32) or (infoIndex == 33):
                            ##Boolean I'll try to pass true or false
                            if itemInfo[1] == u'null':
                                print("NULLIFY")
                                arrayIndex += 1
                                infoIndex += 1
                            else:
                                if itemInfo[1] == u'false':
                                    problemInfoArray[arrayIndex] = 0
                                else:
                                    problemInfoArray[arrayIndex] = 1
                                arrayIndex += 1
                                infoIndex += 1
                        elif infoIndex == 17:
                            ##Boolean I'll try to pass true or false
                            if itemInfo[1] == u'null':
                                print("NULLIFY")
                                arrayIndex += 1
                                infoIndex += 1
                            else:
                                if itemInfo[1] == u'false':
                                    problemInfoArray[arrayIndex] = 0
                                else:
                                    problemInfoArray[arrayIndex] = 1
                                arrayIndex += 1
                                infoIndex += 1
                        elif (itemInfo[0] == u'Locations') or (Location == True):
                            if itemInfo[0] != u'RepeatText':
                                Location = True
                                infoIndex += 1
                            else:
                                if itemInfo[1] == u'null':
                                    print("NULLIFY")
                                    Location = False
                                    arrayIndex += 1
                                    infoIndex += 1
                                else:
                                    Location = False
                                    problemInfoArray[arrayIndex] = itemInfo[1]
                                    arrayIndex += 1
                                    infoIndex += 1
                        ##Logic for StartHolds
                        elif infoIndex == 34:
                            HoldsArray[holdsIndex] = itemInfo[2] #
                            holdsIndex += 1
                            infoIndex += 1
                        elif (infoIndex > 34) and (itemInfo[0] != u'Holdsets') and (infoIndex < endHoldsIndex):
                            # the rest of the hold information
                            HoldsArray[holdsIndex] = itemInfo[1]
                            holdsIndex += 1
                            infoIndex += 1
                        elif (itemInfo[0] == u'Holdsets') and (infoIndex > 33):
                            i = 0
                            k = 0

                            StartHolds = [None] * 8
                            FinishHolds = [None] * 8
                            Intermediate = [None] * 200
                            numStartHolds = 0
                            numFinishHolds = 0
                            HoldsArray = filter(None, HoldsArray)
                            while i < len(HoldsArray):
                                endHoldsIndex = len(HoldsArray)
                                j = 0
                                holdType = [None] * 4
                                while j < 4:
                                    holdType[j] = HoldsArray[i]
                                    j += 1
                                    i += 1
                                if holdType[2] == u'true':
                                    #isaStartHold

                                    numStartHolds += 1
                                    if numStartHolds == 2:
                                        #problemInfoArray.insert(37,holdType)
                                        problemInfoArray[36] = holdType[0]
                                        problemInfoArray[37] = holdType[1]
                                    else:
                                        problemInfoArray[34] = holdType[0]
                                        problemInfoArray[35] = holdType[1]

                                elif holdType[3] == u'true':
                                    numFinishHolds += 1
                                    if numFinishHolds == 2:
                                        problemInfoArray[66] = holdType[0]
                                        problemInfoArray[67] = holdType[1]
                                    else:
                                        problemInfoArray[64] = holdType[0]
                                        problemInfoArray[65] = holdType[1]
                                else:
                                    problemInfoArray[38+k] = holdType[0]
                                    problemInfoArray[39+k] = holdType[1]
                                    k += 2













                            arrayIndex = 68
                            problemInfoArray[arrayIndex] = itemInfo[1]
                            arrayIndex += 1
                        else:
                            if itemInfo[1] == u'null':
                                print("NULLIFY")
                                arrayIndex += 1
                                infoIndex += 1
                            else:
                                problemInfoArray[arrayIndex] = itemInfo[1]
                                arrayIndex += 1
                                infoIndex += 1


                    elif (MoonLayout2016) and (infoIndex > 4):
                        #2016 logic
                        if infoIndex == 6:
                            problemInfoArray[arrayIndex] = itemInfo[2]  ##is 2017 Layout this will have 3 arguments
                            arrayIndex += 1
                            infoIndex += 1


                        else:
                            if itemInfo[1] == u'null':
                                print("NULLIFY")
                                arrayIndex += 1
                                infoIndex += 1
                            else:
                                problemInfoArray[arrayIndex] = itemInfo[1]
                                arrayIndex += 1
                                infoIndex += 1




                    else:
                        if itemInfo[1] == u'null':
                            print("NULLIFY")
                            arrayIndex += 1
                            infoIndex += 1
                        else:
                            problemInfoArray[arrayIndex] = itemInfo[1]
                            arrayIndex += 1
                            infoIndex += 1


                    print(infoIndex)
                    print(arrayIndex)

                    #print(itemInfo)
                    #infoIndex+=1
                    #print(itemInfo[1])
                #print(problemInfoArray)
                #print(infoIndex)


        #print(problemInfoArray)
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

