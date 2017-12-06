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

HTMLCODE1 = """<!DOCTYPE html>
<html class="k-webkit k-webkit62"><head>

    <title>MoonBoard Dashboard</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="robots" content="noindex, nofollow">

    <link href="/Content/kendocss?v=McTNyEYACNI8AT8W05Ck_xrqJNpWsLaPJyswFdHht2U1" rel="stylesheet">


    

    <link href="/Content/slider/nouislider.min.css" rel="stylesheet">
    <link href="/Content/slider/moonslider.min.css" rel="stylesheet">




    <link href="/Content/dashcss?v=C98r-pUZayslCWiyF1wGRwk_m404vtYS6e-kcdQwOjY1" rel="stylesheet">



    
    <script type="text/javascript" async="" src="https://www.google-analytics.com/analytics.js"></script><script src="/bundles/jquery?v=lp1DmbzZOS69_gd1TSKRrjSgn0R95B8ZUZN-5qo5FQI1"></script>

    <script src="/bundles/jqueryval?v=WhRmI8vUVF186UwYB1zRP7-DwJzqpKlt0JksOBJvolw1"></script>

    <script src="/bundles/dashscripts?v=RNMinrrCqXRwosfJueierzz0zsOSzN_Dp4J97BJZs681"></script>



    



    

    <script src="/Scripts/pixi.min.js"></script>
    <script src="/Scripts/wbx-MoonBoard.min.js"></script>
    <script src="/Scripts/hammer.min.js"></script>
    <script src="/Content/slider/nouislider.min.js"></script>

    <script type="text/javascript">


        function getSetupId()
        {
            return $("#Holdsetup").val();
        }



        function tbHandler(e) {



            if (e.id == "tbtnComments" && currentProblem) {

                var $win = $("#commentsWrapper");

                if ($win.isInvisible())
                {
                    $win.visible();
                }
                else
                {
                    $win.invisible();
                }
            } else if (e.id == "tbtnProblems") {

                toggleSlideMenu();
            }


        }

    </script>

    
</head>
<body>


    <div class="container-fluid fullheight">
      
        <div class="row row-offcanvas row-offcanvas-left fullheight">
       

 


            <div id="nav-section" class="col-xs-12 column fullheight">
     
                <div class="navbar-default">
                    <button id="toggle-button" type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                        <span class="icon-bar"></span>
                    </button>
                </div>

                <a href="/">
                    <img id="dash-logo" class="center-block" src="/Content/images/logos/moonclimbing-64x.png">
                </a>

                <div class="collapse navbar-collapse" id="sidebar-nav" role="navigation">
                    <ul class="nav"><li class="visible-xs-block   menu-account-profile">

    <div class="account-profile">

        <form method="post" action="/Account/LogOff" id="logoutForm">

            <input name="__RequestVerificationToken" type="hidden" value="-ENJELusTxd8iZ_kBChIjnOLIJUXp5YkcLJ2nyGRiq0_9djHlYwyksDTtCsOIyih1zVX-Ys-I83pO9Jd3fQaCrKrOlQWwVHffplGmmMJjImkud44Z53koAp_vM69hTPS1y_GEhIr84zWykNFkeQ0xw2">




            <div class="profile">
                <div class="profile-pic" style="background-image:url('/Content/Account/Images/default-profile.png?636481710069217897');"></div>
                <div class="detail">

                    <h1><a href="/Dashboard/Index" title="Go to dashboard">Cody Jones</a></h1>
                    <h2><a href="javascript:document.getElementById('logoutForm').submit()" title="Sign out of the MoonBoard dashboard">Sign out</a></h2>

                </div>
            </div>


        </form>


</div>



</li>
                        <li id="m-home"><a href="/Dashboard/Index"><span class="icon icon-chart-column"></span>Home</a></li>

                        <li id="m-problems" class="active">

                            <a href="#" id="lProblems" data-toggle="collapse" data-target="#probsSubMenu" aria-expanded="true"><span class="icon icon-faves"></span>Problems</a>

                            <ul class="nav" id="probsSubMenu" role="menu" aria-labelledby="lProblems" aria-expanded="true">

                                <li id="m-viewproblem" class="active"><a href="/Problems/Index"><span class="icon icon-faves"></span>View</a>

                                </li><li id="m-addproblem"><a href="/Problems/Create"><span class="icon icon-faves"></span>Add</a></li>

                            </ul>

                        </li>


     

                        <li id="m-logbook">
                            <a href="#" id="llogbook" data-toggle="collapse" data-target="#logbookSubMenu" aria-expanded="false"><span class="icon icon-faves"></span>Logbook</a>




                            <ul class="nav collapse" id="logbookSubMenu" role="menu" aria-labelledby="llogbook">


                                <li id="m-viewlogbook"><a href="/Logbook/Index"><span class="icon icon-faves"></span>View</a>

                                </li><li id="m-addlogbookentry"><a href="/Logbook/Edit"><span class="icon icon-faves"></span>Add entry</a></li>




                            </ul>



                        </li>

                        <li id="m-hold-setups">

                            <a href="#" id="lHoldsetups" data-toggle="collapse" data-target="#setupsSubMenu" aria-expanded="false"><span class="icon icon-faves"></span>Hold Setups</a>

                            <ul class="nav collapse" id="setupsSubMenu" role="menu" aria-labelledby="lHoldsetups">

                                <li id="m-viewholdsetups"><a href="/HoldSetups/Index"><span class="icon icon-faves"></span>View</a></li>



                            </ul>

                        </li>
                        <li id="m-users">
                        
                        
                        <a href="/Account/Index"><span class="icon icon-faves"></span>Users</a>
                        
                        
                        
                        
                        </li>
                        <li id="m-moonboards">
                            <a href="#" id="lMoonBoards" data-toggle="collapse" data-target="#mbSubMenu" aria-expanded="false"><span class="icon icon-faves"></span>MoonBoards</a>

                            <ul class="nav collapse" id="mbSubMenu" role="menu" aria-labelledby="lMoonBoards">

                                <li id="m-worldmap"><a href="/MoonBoard/Overview"><span class="icon icon-faves"></span>World Map</a>

                                </li><li id="m-addmoonboard"><a href="/MoonBoard/Edit"><span class="icon icon-faves"></span>Add</a></li>

                            </ul>
                        </li>

                        <li id="m-videos">
                            <a href="#" id="lVideos" data-toggle="collapse" data-target="#vidSubMenu" aria-expanded="false"><span class="icon icon-faves"></span>Videos</a>

                            <ul class="nav collapse" id="vidSubMenu" role="menu" aria-labelledby="lVideos">

                                <li id="m-viewvideos"><a href="/Video/Index"><span class="icon icon-faves"></span>View</a>

                                </li><li id="m-addvideo"><a href="/Video/Edit"><span class="icon icon-faves"></span>Add</a>

</li></ul>
                        </li>





                        <li id="m-activeusers">


                            <a href="/Account/ActiveUsers"><span class="icon icon-faves"></span>Active Users</a>




                        </li>

                    </ul>



                    <div id="rights">
                        <p>© 2017 Moon Climbing. All Rights Reserved.</p>
                    </div>
                </div>




         

            </div>



  
       
             

            <div id="main-section" class="col-xs-12 column" style="height: 2263px;">
        
          

                <div class="row">

                    <div class="col-md-12">

                        


    <div data-role="toolbar" id="tbProblems" class="k-toolbar k-widget k-toolbar-resizable" data-uid="1f99acea-5081-4296-8975-36821efe550d" tabindex="0"><div tabindex="0" class="k-overflow-anchor k-button" style="visibility: hidden; width: 1px;"><span class="k-icon k-i-arrow-60-down"></span></div><a href="" tabindex="0" class="k-button k-button-icontext" id="tbtnComments" data-uid="178b64a8-16b5-479b-b580-697992c46355" data-overflow="auto" style="visibility: visible;"><span class="k-icon k-i-comment"></span>Comments/Repeats</a></div><script>
	kendo.syncReady(function(){jQuery("#tbProblems").kendoToolBar({"items":[{"click":tbHandler,"icon":"comment","id":"tbtnComments","text":"Comments/Repeats","type":"button","showIcon":"both"}]});});
</script>



                    </div>
                </div>


                <div class="body-content" style="height: 2247px;">
                    














<div class="row fullheight relative">


    <div class="moon-slide-menu col-md-6 fullheight pr-0">


        <!--Tab strip buttons-->

        <div class="row fullheight moon-menu">



            <div class="col-md-12 pl-0 pr-0">

                <div class="moonTabstrip">
                    <ul class="tab-buttons">
                        <li class="active">

                            <button data-id="Problems" class="tabButton selected">Problems</button>
                        </li>
                        <li>
                            <button data-id="Filters" class="tabButton">Filters/Sort</button>

                        </li>




                    </ul>

                    <button class="closeButton">
                        <img src="/Content/images/Buttons/close.png" aria-label="Close filters">
                    </button>

                </div>

            </div>

            <div class="w-100"></div><div class="col-xs-12 col-sm-12 col-md-6 fullheight moon-menu-item moon-tab active" data-id="Problems" id="tabProblems" style="height: 2198px;">




                <div class="row search-wrap">
    <div class="col-md-12 pr-0 pl-0">


        <h1 id="totalProblems">15722 PROBLEMs</h1>
        

        <div class="row search row-no-padding margin-wrapper">
            <div class="col-xs-10 col-sm-10 col-md-10">
                <input id="TxtProblemName" maxlength="25" min="1" type="text" placeholder="Search problems..." class="clearable">
            </div>
            <div class="col-xs-2 col-sm-2 col-md-2">
                <button id="btnProblemSearch" class="moon-roundbutton">
                    <img src="/Content/images/Buttons/searchproblem.png" aria-label="Search problem" alt="Search problem">
                </button>
            </div>
        </div>


    </div>


</div>





<div class="k-widget k-grid k-display-block" id="grdProblems" data-role="grid" style="height: 2130.56px;"><div class="k-grid-header" style="padding-right: 8px;"><div class="k-grid-header-wrap k-auto-scrollable"><table role="grid"><colgroup></colgroup><thead role="rowgroup"><tr role="row"><th class="k-header" data-index="0" scope="col" style="display:none"><span class="k-link">&nbsp;</span></th></tr></thead></table></div></div><div class="k-grid-content" style="height: 2095.56px;"><table role="grid"><colgroup></colgroup><tbody role="rowgroup"><tr data-uid="308026" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308026/brother-louie" target="_blank">BROTHER LOUIE</a></h3><p>            Jan.dooo        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308025" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308025/hyul-001" target="_blank">HYUL 001</a></h3><p>            ki won Nam        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308024" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308024/chundercut" target="_blank">CHUNDERCUT</a></h3><p>            Remus Knowles        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7B        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308023" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308023/kreuzung" target="_blank">KREUZUNG</a></h3><p>            Danny Maldener        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308022" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308022/judgement-rains" target="_blank">JUDGEMENT RAINS</a></h3><p>            Gus Carter        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308021" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308021/second-place-1st-lou-ser" target="_blank">SECOND PLACE, 1ST LOU-SER</a></h3><p>            Gus Carter        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7C+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308020" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308020/right-left-up-down" target="_blank">RIGHT, LEFT, UP, DOWN</a></h3><p>            Tim Teylan        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308019" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308019/dyno-fit" target="_blank">DYNO FIT</a></h3><p>            Chuchi Climber        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308018" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308018/crossword" target="_blank">CROSSWORD</a></h3><p>            Jon Pål Hamre        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308017" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308017/habibi-direkt" target="_blank">HABIBI DIREKT</a></h3><p>            Daniel Pliegl        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7A+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308016" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308016/test-a1" target="_blank">TEST A1</a></h3><p>            iTTE Climbing        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7A        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308015" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308015/ror" target="_blank">ROR</a></h3><p>            abi        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308014" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308014/oh-rock-beautiful" target="_blank">OH ROCK BEAUTIFUL</a></h3><p>            abi        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308013" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308013/fun-stuff" target="_blank">FUN STUFF</a></h3><p>            Tauty        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308011" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308011/たい" target="_blank">たい</a></h3><p>            DAI NUMATA        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr></tbody></table></div><div class="k-pager-wrap k-grid-pager k-widget k-floatwrap" data-role="pager"><ul class="k-pager-numbers k-reset"><li class="k-current-page"><span class="k-link k-pager-nav">1</span></li><li><span class="k-state-selected">1</span></li><li><a tabindex="-1" href="#" class="k-link" data-page="2">2</a></li><li><a tabindex="-1" href="#" class="k-link" data-page="3">3</a></li><li><a tabindex="-1" href="#" class="k-link" data-page="4" title="More pages">...</a></li></ul></div></div><script>
	kendo.syncReady(function(){jQuery("#grdProblems").kendoGrid({"dataBound":grdProblemsLoaded,"columns":[{"hidden":true,"template":" "}],"pageable":{"info":false,"previousNext":false,"buttonCount":3},"scrollable":{"height":"200px"},"noRecords":{"template":"\u003cdiv class=\"no-records\"\u003e\u003cbr/\u003e\u003cspan\u003eNo problems for these settings\u003c/span\u003e\u003c/div\u003e"},"messages":{"noRecords":"No records available."},"dataSource":{"type":(function(){if(kendo.data.transports['aspnetmvc-ajax']){return 'aspnetmvc-ajax';} else{throw new Error('The kendo.aspnetmvc.min.js script is not included.');}})(),"transport":{"read":{"url":"/Problems/GetProblems"},"prefix":""},"pageSize":15,"page":1,"total":0,"serverPaging":true,"serverSorting":true,"serverFiltering":true,"serverGrouping":true,"serverAggregates":true,"filter":[],"schema":{"data":"Data","total":"Total","errors":"Errors","model":{"fields":{"Method":{"type":"string"},"Name":{"type":"string"},"Grade":{"type":"string"},"UserGrade":{"type":"string"},"MoonBoardConfiguration":{"type":"object"},"MoonBoardConfigurationId":{"type":"number"},"Setter":{"type":"object"},"FirstAscender":{"type":"boolean"},"Rating":{"type":"number"},"UserRating":{"type":"number"},"Repeats":{"type":"number"},"Attempts":{"type":"number"},"Holdsetup":{"type":"object"},"IsBenchmark":{"type":"boolean"},"Moves":{"type":"object"},"Holdsets":{"type":"object"},"Locations":{"type":"object"},"RepeatText":{"editable":false,"type":"string"},"NumberOfTries":{"type":"string"},"NameForUrl":{"editable":false,"type":"string"},"Id":{"type":"number"},"ApiId":{"type":"number"},"DateInserted":{"type":"date","defaultValue":null},"DateUpdated":{"type":"date","defaultValue":null},"DateDeleted":{"type":"date","defaultValue":null},"DateTimeString":{"editable":false,"type":"string"}}}}},"rowTemplate":"\u003ctr data-uid=\u0027#: Id #\u0027 onclick=\u0027problemSelected();\u0027\u003e\u003ctd\u003e\u003cdiv class=\u0027problem\u0027\u003e   #if(IsBenchmark){#           \u003cdiv class=\u0027benchmark\u0027\u003e\u003cimg src=\u0027/Content/images/Problems/benchmark.png\u0027 /\u003e\u003c/div\u003e     #}#   #if(FirstAscender || NumberOfTries != null){#           \u003cdiv class=\u0027firstascender\u0027\u003e\u003cimg src=\u0027/Content/images/Problems/flash.png\u0027 /\u003e\u003c/div\u003e            #}#\u003cdiv class=\u0027problem-inner\u0027\u003e        \u003ch3\u003e\u003ca href=\u0027/Problems/View/#:Id#/#:NameForUrl#\u0027 target=\u0027_blank\u0027\u003e#:Name#\u003c/a\u003e\u003c/h3\u003e\u003cp\u003e            #:Setter.Nickname#        \u003c/p\u003e        \u003cp\u003e            #:RepeatText#           \u003c/p\u003e        \u003cp\u003e            #if(UserGrade == null){##:Grade##}else{##:Grade# (User grade #:UserGrade#)#}#        \u003c/p\u003e\u003cp\u003e#: Method#\u003c/p\u003e\u003cul\u003e#switch(UserRating) {case 3:#\u003cli\u003e    \u003cimg src=\u0027/Content/images/star.png\u0027 /\u003e\u003c/li\u003e\u003cli\u003e\u003cimg src=\u0027/Content/images/star.png\u0027 /\u003e\u003c/li\u003e\u003cli\u003e\u003cimg src=\u0027/Content/images/star.png\u0027 /\u003e\u003c/li\u003e#break;##case 2:#\u003cli\u003e    \u003cimg src=\u0027/Content/images/star.png\u0027 /\u003e\u003c/li\u003e\u003cli\u003e\u003cimg src=\u0027/Content/images/star.png\u0027 /\u003e\u003c/li\u003e\u003cli\u003e\u003cimg src=\u0027/Content/images/starempty.png\u0027 /\u003e\u003c/li\u003e#break;##case 1:#\u003cli\u003e    \u003cimg src=\u0027/Content/images/star.png\u0027 /\u003e\u003c/li\u003e\u003cli\u003e\u003cimg src=\u0027/Content/images/starempty.png\u0027 /\u003e\u003c/li\u003e\u003cli\u003e\u003cimg src=\u0027/Content/images/starempty.png\u0027 /\u003e\u003c/li\u003e#break;##default:#\u003cli\u003e    \u003cimg src=\u0027/Content/images/starempty.png\u0027 /\u003e\u003c/li\u003e\u003cli\u003e\u003cimg src=\u0027/Content/images/starempty.png\u0027 /\u003e\u003c/li\u003e\u003cli\u003e\u003cimg src=\u0027/Content/images/starempty.png\u0027 /\u003e\u003c/li\u003e#break;##}#\u003c/ul\u003e   #if(NumberOfTries != null){#\u003cp class=\u0027bold\u0027\u003e#: NumberOfTries#            #if(Attempts \u003e 0){#(#:Attempts#)#}#\u003c/p\u003e#}#\u003cp class=\u0027bold\u0027\u003e  #if(MoonBoardConfiguration != null){##:MoonBoardConfiguration.Description# #}#\u003c/p\u003e\u003c/div\u003e\u003cdiv class=\u0027add\u0027\u003e\u003cbutton class=\u0027moon-roundbutton\u0027\u003e\u003cimg src=\u0027/Content/images/Buttons/add.png\u0027 /\u003e\u003c/button\u003e\u003cspan\u003eAdd\u003c/span\u003e       \u003c/div\u003e\u003c/div\u003e\u003c/td\u003e\u003c/tr\u003e"});});
</script>




            </div>

            <div class="col-xs-12 col-sm-12 col-md-6 moon-menu-item moon-tab filter-wrap" data-id="Filters" id="tabFilters" style="height: 2198px;">


                <div class="row section-header">

                    <div class="col-md-12">
                        <h3>
                            Hold Setup
                        </h3>

                    </div>

                </div>




                <select id="Holdsetup" name="Holdsetup"><option selected="selected" value="1">MoonBoard 2016</option>
</select>



                    <ul class="holdsetups margin-wrapper mb-hidden" data-id="1" style="display: block;">





                            <li class="full">
                                <button type="button" class="btnHoldset selected" data-id="3" data-key="original school holds">Original School Holds</button>
                            </li>
                            <li class="full">
                                <button type="button" class="btnHoldset selected" data-id="4" data-key="hold set a">Hold Set A</button>
                            </li>
                            <li class="full">
                                <button type="button" class="btnHoldset selected" data-id="5" data-key="hold set b">Hold Set B</button>
                            </li>


                    </ul>







                <!--#endregion-->
                <!--#region Filters-->



                <div class="row search-wrap">
    <div class="col-md-12 pr-0 pl-0">


        <h1 id="totalSetters">SET BY: (4176 setters)</h1>


        <div class="row search row-no-padding margin-wrapper">
            <div class="col-xs-10 col-sm-10 col-md-10">
                <input id="TxtSetterName" maxlength="25" min="1" type="text" placeholder="Search setters..." class="clearable">
            </div>
            <div class="col-xs-2 col-sm-2 col-md-2">
                <button id="btnSetterSearch" class="moon-roundbutton">
                    <img src="/Content/images/Buttons/searchproblem.png" aria-label="Search setters" alt="Search setters">
                </button>
            </div>
        </div>

       


    </div>


</div>



<div class="k-widget k-grid k-display-block" id="grdSetters" style="height:200px" data-role="grid"><div class="k-grid-header" style="padding-right: 9px;"><div class="k-grid-header-wrap k-auto-scrollable"><table role="grid"><colgroup></colgroup><thead role="rowgroup"><tr role="row"><th class="k-header" data-index="0" scope="col" style="display:none"><span class="k-link">&nbsp;</span></th></tr></thead></table></div></div><div class="k-grid-content" style="height: 200px; width: auto; overflow: hidden; padding-right: 9px;" data-role="virtualscrollable"><div class="k-virtual-scrollable-wrap"><table role="grid"><colgroup></colgroup><tbody role="rowgroup"><tr data-uid="0629B4D4-48B0-4EFC-BA71-EB40D1BEC7E9" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083096637)"></div>

</div>

<div class="setter">

    <h3>0988614220 0988614220</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr><tr data-uid="9af9d0de-3e9f-4cb1-b538-0e8d706d0183" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083096637)"></div>

</div>

<div class="setter">

    <h3>47aleks</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr><tr data-uid="b9a763ce-5882-403d-aaa6-de3642365e4c" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083106648)"></div>

</div>

<div class="setter">

    <h3>9 degrees</h3><p>
            14 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="880F6A0E-70C9-4BB2-BE2D-00B725B83856" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083116656)"></div>

</div>

<div class="setter">

    <h3>A.j.Renshaw</h3><p>
            18 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="97600922-ed4f-44c9-9a25-6aa9d9a9c1b5" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083126664)"></div>

</div>

<div class="setter">

    <h3>Aaaaaaa123h</h3><p>
            6 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="a0acaaa9-e959-4f02-a151-79c1a71180c5" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083126664)"></div>

</div>

<div class="setter">

    <h3>Aaron</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr><tr data-uid="78EB323B-3FE7-429B-93AE-8163674CE7BF" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083126664)"></div>

</div>

<div class="setter">

    <h3>aaron anderson</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr><tr data-uid="29B14F27-33A0-4E2B-A3DC-3E3E9D9FF9F2" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083126664)"></div>

</div>

<div class="setter">

    <h3>Aaron Brouwers</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr><tr data-uid="E661A9F4-78E5-46B5-91DD-B023A580563F" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083136679)"></div>

</div>

<div class="setter">

    <h3>Aaron Chan</h3><p>
            4 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="1DE2EA41-E89B-4C38-9057-0D27691B9B54" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083136679)"></div>

</div>

<div class="setter">

    <h3>Aaron Evans</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr><tr data-uid="509E836A-CB2E-49CD-8228-7C471B64470A" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083136679)"></div>

</div>

<div class="setter">

    <h3>Aaron Henriquez</h3><p>
            5 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="78B9737B-1185-47D7-8513-68284732E47E" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083136679)"></div>

</div>

<div class="setter">

    <h3>Aaron Livingston</h3><p>
            2 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="0C8CA198-FFEF-42DA-817A-6BC4C7247B89" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083136679)"></div>

</div>

<div class="setter">

    <h3>aaron merlino</h3><p>
            2 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="CD5064C8-5FA9-4888-87B2-580455942592" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083156694)"></div>

</div>

<div class="setter">

    <h3>Aaron teo</h3><p>
            41 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="bc57d970-e4dd-4e11-89e4-c136edf9f89f" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083166706)"></div>

</div>

<div class="setter">

    <h3>Aaron Young</h3><p>
            3 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="87c9bc3f-a88b-44d7-a4c1-eafe7b0ec389" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083166706)"></div>

</div>

<div class="setter">

    <h3>AAT</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr><tr data-uid="1C1CF459-12C8-42E4-BA21-792EEE763933" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083166706)"></div>

</div>

<div class="setter">

    <h3>Abbe Guff</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr><tr data-uid="CC245B6D-96FC-4AF7-A6E5-A445A7A014A9" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083166706)"></div>

</div>

<div class="setter">

    <h3>Abbie Robinson</h3><p>
            2 problems
        </p>


</div>

</div>

</td></tr><tr data-uid="8d297b88-29bb-4e08-9bf7-e628e6ca4be4" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083166706)"></div>

</div>

<div class="setter">

    <h3>Abby</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr><tr data-uid="68EE3C2C-3144-4A9A-B4DD-842CC0B52DDE" onclick="filterBySetter();">

<td>

<div class="setters">

         <div class="icon">



<div class="profile" style="background-image:url(/Content/Account/Images/default-profile.png?636481710083166706)"></div>

</div>

<div class="setter">

    <h3>Abby Wilson</h3><p>
            1 problem
        </p>


</div>

</div>

</td></tr></tbody></table></div><div class="k-scrollbar k-scrollbar-vertical" style="width: 9px;"><div style="width:1px;height:250000px"></div><div style="width:1px;height:191403.2px"></div></div></div></div><script>
	kendo.syncReady(function(){jQuery("#grdSetters").kendoGrid({"dataBound":grdSettersLoaded,"columns":[{"hidden":true,"template":" "}],"sortable":true,"scrollable":{"virtual":true,"height":"200px"},"messages":{"noRecords":"No records available."},"dataSource":{"type":(function(){if(kendo.data.transports['aspnetmvc-ajax']){return 'aspnetmvc-ajax';} else{throw new Error('The kendo.aspnetmvc.min.js script is not included.');}})(),"transport":{"read":{"url":"/Problems/GetSetters"},"prefix":""},"pageSize":20,"page":1,"total":0,"serverPaging":true,"serverSorting":true,"serverFiltering":true,"serverGrouping":true,"serverAggregates":true,"filter":[],"schema":{"data":"Data","total":"Total","errors":"Errors","model":{"fields":{"Id":{"type":"string"},"ProfileImageUrl":{"type":"string"},"SetBy":{"type":"string"},"ProblemCount":{"type":"number"}}}}},"rowTemplate":"\u003ctr data-uid=\u0027#: Id #\u0027 onclick=\u0027filterBySetter();\u0027\u003e\r\n\r\n\u003ctd\u003e\r\n\r\n\u003cdiv class=\u0027setters\u0027\u003e\r\n\r\n         \u003cdiv class=\u0027icon\u0027\u003e\r\n\r\n\r\n\r\n\u003cdiv class=\u0027profile\u0027 style=\u0027background-image:url(#:ProfileImageUrl#)\u0027\u003e\u003c/div\u003e\r\n\r\n\u003c/div\u003e\r\n\r\n\u003cdiv class=\u0027setter\u0027\u003e\r\n\r\n    \u003ch3\u003e#:SetBy#\u003c/h3\u003e\u003cp\u003e\r\n            #: toDisplayText(\u0027problem\u0027, ProblemCount)#\r\n        \u003c/p\u003e\r\n\r\n\r\n\u003c/div\u003e\r\n\r\n\u003c/div\u003e\r\n\r\n\u003c/td\u003e\u003c/tr\u003e"});});
</script>



                <div class="slider-wrapper margin-wrapper">
                    <div id="slider" class="noUi-target noUi-ltr noUi-horizontal"><div class="noUi-base"><div class="noUi-origin" style="left: 0%;"><div class="noUi-handle noUi-handle-lower" data-handle="0" tabindex="0" role="slider" aria-orientation="horizontal" aria-valuemin="0.0" aria-valuemax="100.0" aria-valuenow="0.0" aria-valuetext="0.00" style="z-index: 5;"></div></div><div class="noUi-connect" style="left: 0%; right: 0%;"></div><div class="noUi-origin" style="left: 100%;"><div class="noUi-handle noUi-handle-upper" data-handle="1" tabindex="0" role="slider" aria-orientation="horizontal" aria-valuemin="0.0" aria-valuemax="100.0" aria-valuenow="100.0" aria-valuetext="16.00" style="z-index: 4;"></div></div></div><div class="noUi-pips noUi-pips-horizontal"><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 0%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 0%;">5+</div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 6.25%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 6.25%;"> </div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 12.5%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 12.5%;">6A+</div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 18.75%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 18.75%;"> </div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 25%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 25%;">6B+</div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 31.25%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 31.25%;"> </div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 37.5%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 37.5%;">6C+</div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 43.75%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 43.75%;"> </div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 50%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 50%;">7A+</div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 56.25%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 56.25%;"> </div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 62.5%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 62.5%;">7B+</div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 68.75%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 68.75%;"> </div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 75%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 75%;">7C+</div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 81.25%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 81.25%;"> </div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 87.5%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 87.5%;">8A+</div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 93.75%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 93.75%;"> </div><div class="noUi-marker noUi-marker-horizontal noUi-marker-large" style="left: 100%;"></div><div class="noUi-value noUi-value-horizontal noUi-value-large" style="left: 100%;">8B+</div></div></div>
                </div>


                <div class="row section-header">

                    <div class="col-md-12">
                        <h3>
                            Filters
                        </h3>

                    </div>

                </div>



                <ul class="filters margin-wrapper">

                    <li>
                        <button class="filter" data-field="Myascents">My ascents</button>
                    </li>


                    <li>

                        <button class="filter" data-field="Setbyme">Set by me</button>
                    </li>
                    <li>

                        <button class="filter" data-field="Benchmarks">Benchmarks</button>

                    </li>
                    <li>

                        <button class="filter" data-field="None">Clear filters</button>
                    </li>

                </ul>

                <div class="row section-header">

                    <div class="col-md-12">
                        <h3>
                            Sort
                        </h3>

                    </div>

                </div>

                <ul class="sort margin-wrapper">

                    <li>
                        <button class="sortBtn selected" data-field="New" data-dir="desc">New</button>
                    </li>


                    <li>

                        <button class="sortBtn" data-field="GradeAsc" data-dir="asc">Easy</button>
                    </li>
                    <li>

                        <button class="sortBtn" data-field="GradeDesc" data-dir="desc">Hard</button>

                    </li>
                    <li>

                        <button class="sortBtn" data-field="Rating" data-dir="desc">Rating</button>
                    </li>
                    <li>

                        <button class="sortBtn" data-field="RepeatsDesc" data-dir="desc">Most Repeats</button>

                    </li>
                    <li>

                        <button class="sortBtn" data-field="RepeatsAsc" data-dir="asc">Least Repeated</button>
                    </li>
                </ul>



            </div>






        </div>
    </div>



    <div class="moon-slide-menu-butt fullheight col-md-6 pr-0 pl-0">



        <div class="fullheight relative">
            <div id="commentsWrapper" style="height: 2247px;">

                



<div class="k-widget k-grid k-display-block" id="grdRepeats" data-role="grid" style=""><div class="k-grid-header" style="padding-right: 8px;"><div class="k-grid-header-wrap k-auto-scrollable"><table role="grid"><colgroup><col></colgroup><thead role="rowgroup"><tr role="row"><th class="k-header" data-index="0" scope="col">

<div id="hdrRepeatsTotal" class="grid-header">Repeats</div>
</th></tr></thead></table></div></div><div class="k-grid-content" style="height: 2160.3px;"><table role="grid"><colgroup><col></colgroup><tbody role="rowgroup"><tr class="k-no-data"><td colspan="1"></td></tr></tbody></table><div class="k-grid-content-expander" style="width: 735px;"></div></div><div class="k-pager-wrap k-grid-pager k-widget k-floatwrap" data-role="pager"><ul class="k-pager-numbers k-reset"><li><span class="k-state-selected" data-page="1">1</span></li></ul></div></div><script>
	kendo.syncReady(function(){jQuery("#grdRepeats").kendoGrid({"dataBound":grdRepeatsBound,"columns":[{"template":" "}],"pageable":{"autoBind":false,"info":false,"previousNext":false,"buttonCount":5},"sortable":true,"scrollable":{"height":"200px"},"noRecords":{"template":"\u003cdiv class=\"no-records\"\u003e\u003cbr/\u003e\u003cspan\u003eThis problem is unrepeated\u003c/span\u003e\u003c/div\u003e"},"messages":{"noRecords":"No records available."},"autoBind":false,"dataSource":{"type":(function(){if(kendo.data.transports['aspnetmvc-ajax']){return 'aspnetmvc-ajax';} else{throw new Error('The kendo.aspnetmvc.min.js script is not included.');}})(),"transport":{"read":{"url":"/Problems/GetRepeats"},"prefix":""},"pageSize":15,"page":1,"total":0,"serverPaging":true,"serverSorting":true,"serverFiltering":true,"serverGrouping":true,"serverAggregates":true,"filter":[],"schema":{"data":"Data","total":"Total","errors":"Errors","model":{"fields":{"Id":{"type":"number"},"Problem":{"type":"object"},"Attempts":{"type":"number"},"Grade":{"type":"string"},"NumberOfTries":{"type":"string"},"Rating":{"type":"number","defaultValue":null},"DateClimbed":{"type":"date"},"DateClimbedAsString":{"type":"string"},"DateInserted":{"type":"date","defaultValue":null},"Comment":{"type":"string"},"IsSuggestedBenchmark":{"type":"boolean"},"User":{"type":"object"}}}}},"rowTemplate":"\u003ctr data-uid=\u0027#: Id #\u0027\u003e\r\n\r\n\u003ctd\u003e\r\n\r\n\u003cdiv class=\u0027repeats\u0027\u003e\r\n\r\n           \u003cdiv class=\u0027icon\u0027\u003e\r\n\r\n\r\n\r\n\u003cdiv class=\u0027profile\u0027 style=\u0027background-image:url(#:User.ProfileImageUrl#)\u0027\u003e\u003c/div\u003e\r\n\r\n\u003c/div\u003e\r\n\r\n\r\n\r\n\r\n\u003cdiv class=\u0027repeat\u0027\u003e\r\n\r\n    \u003ch3\u003e\u003ca href=\u0027/Account/Profile/#:User.Id#\u0027\u003e#:User.Nickname#\u003c/a\u003e\u003c/h3\u003e\r\n\r\n\r\n\r\n\u003cp\u003e\r\n\r\n #:NumberOfTries #\r\n\r\n\u003c/p\u003e\r\n\r\n\r\n\r\n\r\n\u003cp\u003e\r\n\r\nGrade: #:Grade #\r\n\r\n\u003c/p\u003e\r\n\r\n\u003cp\u003e\r\n\r\nClimbed: #:DateClimbedAsString#\r\n\r\n\u003c/p\u003e\r\n\u003cp\u003e\r\n\r\n\r\n   #if(Comment != null){#\r\n#:Comment#\r\n\r\n            #}#\r\n\r\n\r\n\r\n\u003c/p\u003e\r\n\u003c/div\u003e\u003c/div\u003e\r\n\r\n\u003c/td\u003e\u003c/tr\u003e"});});
</script>

<script type="text/javascript">
    function grdRepeatsBound(e) {

        $('#hdrRepeatsTotal').text(toDisplayText("Repeat", e.sender.dataSource.total()));


    }

</script>

            </div>

            <div id="moonboard" style="touch-action: pan-y; user-select: none; -webkit-user-drag: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);">




            <canvas width="650" height="1000" style="touch-action: none; width: 791px; height: 1216.92px; cursor: inherit;"></canvas></div>




        </div>





    </div>
    <div id="mb-sidemenu">


  <button id="btnMbFloatMnu">
      <img src="/Content/images/Buttons/information.png" alt="Show information"></button>
    


    <button id="btnMbFloatMnuComment">
        <img src="/Content/images/Buttons/comment.png" alt="Show comments">
    </button>


</div>




<script>


    $("#btnMbFloatMnu").on("click", function () {



        toggleSlideMenu();


    });



    $("#btnMbFloatMnuComment").on("click", function () {


        if (currentProblem) {

            var $win = $("#commentsWrapper");

            if ($win.isInvisible()) {
                $win.visible();
            }
            else {
                $win.invisible();
            }
        }
    });




    function toggleSlideMenu() {


        $('body').toggleClass('moon-slide-menu-open');
    }

</script>



</div>



<script type="text/javascript">





    (function () {
        var isTouch = 'ontouchstart' in document.documentElement ||
            window.navigator.msPointerEnabled;

        $(document).on('touchstart click', '[data-moon-slide-menu-toggle]', function (evt) {
            evt.preventDefault();

            $('body').toggleClass('moon-slide-menu-open');
        });
    })();

    var ticks_labels = ["5+","6A","6A+","6B","6B+","6C","6C+","7A","7A+","7B","7B+","7C","7C+","8A","8A+","8B","8B+"];

    var moonSlider = document.getElementById('slider');

    noUiSlider.create(moonSlider, {
        start: [0, 16],
        step: 1,
        connect: true,
        range: {
            'min': [0],
            'max': [16]
        },
        pips: {
            mode: 'values',
            values: [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16],
            density: 17
        }
    });

    var minGrade, maxGrade;


    var $sliderMin = $(".noUi-handle-lower");
    var $sliderMax = $(".noUi-handle-upper");



    function sliderValueChanged(values, handle, unencoded, tap, positions) {

        var tMin = ticks_labels[parseInt(values[0])];
        var tMax = ticks_labels[parseInt(values[1])];

        if (minGrade != tMin || maxGrade != tMax) {



            minGrade = tMin;
            maxGrade = tMax;

            var filters = updateFilters('MinGrade', "equals", minGrade);

            filters = updateFilters('MaxGrade', "equals", maxGrade, filters);

            problemsDs.filter(filters);

            settersDs.filter(filters);
        }

    }

    function sliderIsSliding(values, handle, unencoded, tap, positions) {

        if ($sliderMin.position().left === $sliderMax.position().left) {

            if (handle == 0) {
                $sliderMax.css("z-index", 4);
            }
            else {
                $sliderMax.css("z-index", 5);
            }
        }
    }


    moonSlider.noUiSlider.on('slide', sliderIsSliding);
    moonSlider.noUiSlider.on('change', sliderValueChanged);





    function updateSliderTicks()
    {
        var $nodes = $(".noUi-value-large");

        $nodes.each(function (index, e) {


            if (index % 2 === 0) {

                e.innerHTML = ticks_labels[index];
            }
            else {
                e.innerHTML = " ";
            }

        });
    }

    updateSliderTicks();


    $("button.btnGrade").on("click", function () {
        var $button = $(this);


        $button.toggleClass("unselected");

        var grades = $("button.btnGrade:not('.unselected')")
            .map(function () {
                return this.innerText;
            })
            .get()
            .join(",");

        var filters = updateFilters('Grade', "equals", grades);


        problemsDs.filter(filters);

        settersDs.filter(filters);



    });

    $("button.btnHoldset").on("click", function () {


        var $button = $(this);



        $button.toggleClass("selected");


        moonBoardObj.holdContainers[$button.data("key")].visible = $button.hasClass("selected");


        moonBoardObj.clear();

        moonBoardObj.resetProblem();


        var hs = $("button.btnHoldset.selected:visible").map(function () {
            return $(this).data("key");
        }).get().join(",");


        var filters = updateFilters("Holdsets", "equals", hs);


        problemsDs.filter(filters);
        settersDs.filter(filters);


    });

    $("button.tabButton").on("click", function () {

        var $tabButton = $(this);

        $("button.tabButton").removeClass("selected");
        $("div.moon-tab").removeClass("active");


        var id = $tabButton.data("id");

        $tabButton.addClass('selected');

        $('div.moon-tab[data-id="' + id + '"]').addClass('active');


    });


    var $grdProblems;
    var problemsDs;

    var $grdSetters;
    var settersDs;

    $(window).resize(function () {

        sizeContent();

    });



    function sizeContent() {
        var MARGIN = 15
        var GRIDOFFSET = 35;

        var h = $(".moonTabstrip:visible").outerHeight(true) || 1;

        var size = mn_sizebody();

        $("#grdProblems").height(document.body.clientHeight - $("#grdProblems").offset().top - GRIDOFFSET);

        $("#grdProblems").find('.k-grid-content').height($("#grdProblems").height() - GRIDOFFSET);

        var innerHeight = size- h;

        $("#commentsWrapper").innerHeight(size);

        $("#grdRepeats").data("kendoGrid").resize();


        $(".moon-tab").height(innerHeight);



        if (moonBoardObj) {
            moonBoardObj.resize();

        }

    }





    var selectedIndex = -1;
    var currentProblem;

    $(function () {


        moonBoardObj.init();

        //  Size the header here, not in document load. Mobile
        sizeContent();

        activateMenu(['m-problems', 'm-viewproblem']);
        setMenuExpanded(['lProblems', 'probsSubMenu']);



        $(".moonTabstrip .closeButton").on("click", function () {

            toggleSlideMenu();

        });





        moonBoardObj.problemRendered = function (model) {


            currentProblem = model;

            var $grdRepeats = $("#grdRepeats").data("kendoGrid");

            var Id = getSetupId();


            var filters = [];

            filters.push(createFilter('setupId', "equals", Id));

            filters.push(createFilter('Id', "equals", currentProblem.Id));

            $grdRepeats.dataSource.filter(filters);

        }



        getHoldsetConfig();






        $("#Holdsetup").change(function (e) {

            var $this = $(this);




            var filters = updateFilters('setupId', "equals", $this.val());

            removeFilter(filters, "Holdsets");

            $("button.btnHoldset:not(.selected)").addClass("selected");

            problemsDs.filter(filters);

            settersDs.filter(filters);


            getHoldsetConfig();


            ajax("/Problems/GetGrades/" + $this.val(), "GET", null, function (data) {



                moonSlider.noUiSlider.updateOptions({
                    start: [0, data.length - 1],
                range: {
                    'min': 0,
                    'max': data.length -1
                },
                   pips: {
                    mode: 'values',
                    values: data,
                    density: data.length
                }
                });

            ticks_labels = data;


            updateSliderTicks();





        });


        });


        function getHoldsetConfig()
        {
            var Id = getSetupId();

            $("ul.holdsetups").hide();

            $("ul.holdsetups[data-id='" + Id + "']").show();

            ajax("/Problems/GetHoldsets/" + Id, "GET", null, function (data) {

                moonBoardObj.clearHolds();

                moonBoardObj.clear();

                moonBoardObj.loadHoldsets(data);


            });




        }




        var moonboard = document.getElementById('moonboard');


        var mc = new Hammer(moonboard);
        var scrollTop = 0;
        var panright = false;


        mc.on('panleft panright', function (ev) {


            if (ev.isFinal) {
                var shouldPageback = false;


                if (ev.additionalEvent == "panright") {

                    panright = true;

                    selectedIndex--;


                    if (dataSource.page() > 1 && selectedIndex < 0)
                    {
                        shouldPageback = true;
                    }


                    if (selectedIndex < 0) {
                        selectedIndex = 0;
                        scrollTop = 0;
                    }
                }
                else {

                    panright = false;

                    shouldPageback = false;

                    selectedIndex++;
                }


                var index = selectedIndex % problemsDs.take();


                if (index == 0 && selectedIndex > 0 || shouldPageback) {



                    if (ev.additionalEvent == "panleft") {

                        problemsDs.page(problemsDs.page() + 1);
                    }
                    else {
                        problemsDs.page(problemsDs.page() -1);
                    }

                    $grdProblems.wrapper.find(".k-scrollbar-vertical").scrollTop(0);
                    $grdProblems.wrapper.find(".k-grid-content").scrollTop(0);
                }
                else
                {

                    var model = problemsDs.at(index);

                    if ($lastProblemTr) {
                        $lastProblemTr.removeClass('selected');

                        if (panright) {
                            scrollTop -= $lastProblemTr.outerHeight(true);
                        }
                        else {
                            scrollTop += $lastProblemTr.outerHeight(true);
                        }

                    }


                    var $tr = $grdProblems.tbody.find('tr[data-uid="' + model.Id + '"]');

                    $lastProblemTr = $tr;

                    $grdProblems.wrapper.find(".k-scrollbar-vertical").scrollTop(scrollTop);

                    $grdProblems.wrapper.find(".k-grid-content").scrollTop($tr.outerHeight() * index);
                    $tr.addClass('selected');

                    setProblemHeader(model);
                    moonBoardObj.renderProblem(model);
                }
            }
        });



        $(".sortBtn").click(function () {

            var $btn = $(this);

            $(".sortBtn").removeClass('selected');

            $btn.addClass('selected');


            var currentSort = problemsDs.sort();


            if (currentSort && currentSort[0].field === $btn.data("field")) {
                return;
            }

            var dsSort = [];

            $("#sortedBy").text("Sorted by: " + $btn.text());


            dsSort.push({ field: $btn.data("field"), dir: $btn.data("dir") });

            problemsDs.sort(dsSort);




        });


        $("#btnSetterSearch").click(function () {

            var filters = updateFilters('SetBy', "equals", $("#TxtSetterName").val());


            removeFilter(filters, "SetById");

            problemsDs.filter(filters);

            settersDs.filter(filters);

        });


        $("#btnProblemSearch").click(function () {

            var filters = updateFilters('Name', "contains", $("#TxtProblemName").val());

            problemsDs.filter(filters);

            settersDs.filter(filters);

        });

        $(".filter").click(function () {


            var $btn = $(this);

            $(".filter").removeClass('selected');

            var field = $btn.data("field");
            var filters = [];

            if (field != 'None') {

                $btn.addClass('selected');

                filters = removeFilters(getCurrentFilters(), ["Myascents", "Setbyme", "Benchmarks"]);

                filters = updateFilters(field, "equals", "");

            }
            else {

                filters = createFilter("setupId", "equals", getSetupId());


                $("button.btnHoldset:not(.selected)").addClass("selected");

                moonBoardObj.clear();
                moonBoardObj.resetProblem();
                moonBoardObj.showHoldsets();


                $("#TxtSetterName").val('');


            }


            problemsDs.filter(filters);

            settersDs.filter(filters);


        });



    });


    function grdProblemsLoaded() {

        if (!$grdProblems) {
            $grdProblems = $("#grdProblems").data("kendoGrid");
        }

        problemsDs = $grdProblems.dataSource;

        dataSource = $grdProblems.dataSource;

        $('#totalProblems').text(toDisplayText('PROBLEM', problemsDs.total()));



            selectedIndex = -1;


    }


    function grdSettersLoaded() {

        if (!$grdSetters) {
            $grdSetters = $("#grdSetters").data("kendoGrid");
        }

        settersDs = $grdSetters.dataSource;

        $('#totalSetters').text('SET BY: (' + toDisplayText('setter', settersDs.total()) + ')');
    }





    var $lastProblemTr;

    function problemSelected(model) {


        var $problemTr = $(event.target).closest("tr");

        model = $grdProblems.dataItem($problemTr);

        moonBoardObj.renderProblem(model);

        $problemTr.addClass('selected');

        if ($lastProblemTr) {

            $lastProblemTr.removeClass('selected');
        }

        $lastProblemTr = $problemTr;

        setProblemHeader(model);

        toggleSlideMenu();

    }


    function setProblemHeader(model) {
        $("#moonBrand").text(model.Name + ", " + model.Grade);

        $("#pdSetby").text("SET BY: " + model.Setter.Nickname);
    }

    var $lastSetterTr;


    function filterBySetter() {


        var $setterTr = $(event.target).closest("tr");

        var model = $grdSetters.dataItem($setterTr);


        $setterTr.find('.setter').addClass('selected');

        if ($lastSetterTr) {

            $lastSetterTr.find('.setter').removeClass('selected');
        }

        $lastSetterTr = $setterTr;

        var filters = updateFilters('SetById', "equals", model.Id);

        problemsDs.filter(filters);

        settersDs.filter(filters);


        $("#TxtSetterName").val(model.SetBy);


    }


    function tog(v) { return v ? 'addClass' : 'removeClass'; }


    $(document).on('input', '.clearable', function () {
        $(this)[tog(this.value)]('x');

    }).on('touchstart click', '.x', function (ev) {


        ev.preventDefault();

        $(this).removeClass('x').val('').change();


        var filters = [];


        if (this === $("#TxtProblemName").get(0)) {
            if (filterContains(problemsDs.filter().filters, "Name")) {

                filters = removeFilter(problemsDs.filter().filters, "Name");

                problemsDs.filter(filters);

                settersDs.filter(filters);
            }

        }
        else {

            if (filterContains(settersDs.filter().filters, "SetBy")) {

                filters = removeFilter(settersDs.filter().filters, "SetBy");

                problemsDs.filter(filters);

                settersDs.filter(filters);
            }

        }



        });











</script>


                </div>

          


            </div>




            <div class="row main-section-header-wrap">
                <div class="col-xs-12">
                    <div id="main-section-header">
                        <div class="header-content">
                            

                            <div class="detail">
                                


    
<h1 class="moon-brand">

    <a id="moonBrand" href="https://www.moonclimbing.com" target="_blank" title="Visit Moon Climbing">MOON CLIMBING</a>

</h1>


    <h2 id="pdSetby"></h2>



                            </div>

                        </div>

                    </div>

                </div>


                </div>



            <div class="account-profile">

        <form method="post" action="/Account/LogOff" id="logoutForm">

            <input name="__RequestVerificationToken" type="hidden" value="7S0DmWjc5SS8ZW-lH_w4Ha6ckv0krwPF_czjHr7pwyX0L5AYBIFfgpkrtkgDd2kOSxfAXFQNpO324COiZrcfR3BNQUDNWQBZZvIRUWbhDm5D63inUcmKIQ4e_W0BmuG46-M0lmvd6pnWb6zT6UoCjg2">




            <div class="profile">
                <div class="profile-pic" style="background-image:url('/Content/Account/Images/default-profile.png?636481710069217897');"></div>
                <div class="detail">

                    <h1><a href="/Dashboard/Index" title="Go to dashboard">Cody Jones</a></h1>
                    <h2><a href="javascript:document.getElementById('logoutForm').submit()" title="Sign out of the MoonBoard dashboard">Sign out</a></h2>

                </div>
            </div>


        </form>


</div>


        </div>
    </div>


    

    <script>
        $(document).ready(function () {
            $('[data-toggle=offcanvas]').click(function () {
                $('.row-offcanvas').toggleClass('active');
            });

        });
    </script>

    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async="" src="https://www.googletagmanager.com/gtag/js?id=UA-73435918-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag() { dataLayer.push(arguments); }
        gtag('js', new Date());

        gtag('config', 'UA-73435918-1');
    </script>


<ul class="k-overflow-container k-list-container k-popup k-group k-reset" data-role="popup" data-uid="1f99acea-5081-4296-8975-36821efe550d" style="display: none; position: absolute;"><li id="tbtnComments_overflow" data-uid="178b64a8-16b5-479b-b580-697992c46355" data-overflow="auto" class="k-item k-state-default k-overflow-hidden"><a href="" tabindex="0" class="k-button-icontext k-overflow-button k-button"><span class="k-icon k-i-comment"></span><span class="k-text">Comments/Repeats</span></a></li></ul></body></html>"""
HTMLCODE = """<div class="k-grid-content" style="height: 2095.56px;"><table role="grid"><colgroup></colgroup><tbody role="rowgroup"><tr data-uid="308026" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308026/brother-louie" target="_blank">BROTHER LOUIE</a></h3><p>            Jan.dooo        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308025" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308025/hyul-001" target="_blank">HYUL 001</a></h3><p>            ki won Nam        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308024" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308024/chundercut" target="_blank">CHUNDERCUT</a></h3><p>            Remus Knowles        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7B        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308023" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308023/kreuzung" target="_blank">KREUZUNG</a></h3><p>            Danny Maldener        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308022" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308022/judgement-rains" target="_blank">JUDGEMENT RAINS</a></h3><p>            Gus Carter        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308021" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308021/second-place-1st-lou-ser" target="_blank">SECOND PLACE, 1ST LOU-SER</a></h3><p>            Gus Carter        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7C+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308020" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308020/right-left-up-down" target="_blank">RIGHT, LEFT, UP, DOWN</a></h3><p>            Tim Teylan        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308019" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308019/dyno-fit" target="_blank">DYNO FIT</a></h3><p>            Chuchi Climber        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308018" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308018/crossword" target="_blank">CROSSWORD</a></h3><p>            Jon Pål Hamre        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308017" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308017/habibi-direkt" target="_blank">HABIBI DIREKT</a></h3><p>            Daniel Pliegl        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7A+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308016" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308016/test-a1" target="_blank">TEST A1</a></h3><p>            iTTE Climbing        </p>        <p>            Be the first to repeat this problem           </p>        <p>            7A        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308015" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308015/ror" target="_blank">ROR</a></h3><p>            abi        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308014" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308014/oh-rock-beautiful" target="_blank">OH ROCK BEAUTIFUL</a></h3><p>            abi        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308013" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308013/fun-stuff" target="_blank">FUN STUFF</a></h3><p>            Tauty        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6C+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr><tr data-uid="308011" onclick="problemSelected();"><td><div class="problem">      <div class="problem-inner">        <h3><a href="/Problems/View/308011/たい" target="_blank">たい</a></h3><p>            DAI NUMATA        </p>        <p>            Be the first to repeat this problem           </p>        <p>            6B+        </p><p>Feet follow hands</p><ul><li>    <img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li><li><img src="/Content/images/starempty.png"></li></ul>   <p class="bold">  </p></div><div class="add"><button class="moon-roundbutton"><img src="/Content/images/Buttons/add.png"></button><span>Add</span>       </div></div></td></tr></tbody></table></div>"""
soupProblems = BeautifulSoup(HTMLCODE1, 'html.parser')
#problems = soupProblems.find_all("a", href=True)

for divs in soupProblems.find_all("div", class_="problem"):
    for a in divs.find_all("a", href=True):
        print("Found the URL:", a['href'])
pageClick = driver.find_element_by_css_selector('[data-page="%d"]' % index)
print(pageClick)
# for pages in soupProblems.find_all("a", tabindex="-1"):
#     print(pages)
# problemsButton = driver.find_element_by_id("lProblems")
# problemsButton.click()
# viewProblem = driver.find_element_by_id("m-viewproblem").click()

#problemList = driver.find_element_by_class_name("problem")
#print problemList