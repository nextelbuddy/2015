from sikuli import*
import logging
reload(logging)
import datetime
import os
import subprocess
import shutil
import TABFunction
SCR0 = Screen(0)
SCR1 = Screen(1)
startTime = datetime.datetime.now()

choose_browser = input('Choose your Browser ie.. chrome, firefox, ie, safari:', 'chrome')


if choose_browser == "chrome":
    app = App(os.path.join(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
elif choose_browser == "firefox":
    app = App(os.path.join(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'))
elif choose_browser == "ie":
    app = App(os.path.join(r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'))
elif choose_browser == "safari":
    app = App(os.path.join(r'C:\Program Files (x86)\Safari\Safari.exe'))



"""
chrome = App(os.path.join(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))
firefox = App(os.path.join(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe'))
ie = App(os.path.join(r'C:\Program Files (x86)\Internet Explorer\iexplore.exe'))
safari = App(os.path.join(r'C:\Program Files (x86)\Safari\Safari.exe'))
"""


logging.basicConfig(filename=os.path.join(r'C:\tssmoketest', 'Logs', startTime.strftime('eCenterSmokeTestLog %Y_%m_%d %H_%M_%S.log')), level=logging.DEBUG, format='%(message)s', filemode='w')


def ecenter_login():
    logging.debug('- - - - - - - - - - - - - - -')
    #logging into eCenter website
    logging.debug(' ')
    logging.debug('----Opening Browser')
    app.open()
    if choose_browser == "chrome":
        wait(Pattern("NewTab-1.png").similar(0.93), 120)
        type(Key.SPACE, KeyModifier.ALT)
        wait("MoveSizeMini.png", 120)
        type("x")
        wait(1)
        type('l', KeyModifier.CTRL)
        paste("http://www.sagetimeslipsecenter.com")
        type(Key.ENTER)
    elif choose_browser == "firefox":
        wait("MozillaFiref-1.png", 120)
        type(Key.SPACE, KeyModifier.ALT)
        wait("MoveSizeMini.png", 120)
        type("x")
        wait(1)
        type('l', KeyModifier.CTRL)
        paste('www.sagetimeslipsecenter.com')
        type(Key.ENTER)
    elif choose_browser == "ie":
        wait("FileEditView.png", 120)
        type(Key.SPACE, KeyModifier.ALT)
        wait("MoveSizeMini.png", 120)
        type("x")
        wait(1)
        type('l', KeyModifier.CTRL)
        paste("http://www.sagetimeslipsecenter.com")
        type(Key.ENTER)
    elif choose_browser == "safari":
        wait("EEEsamiii.png", 120)
        type(Key.SPACE, KeyModifier.ALT)
        wait("MoveSizeMini.png", 120)
        type("x")
        wait(1)
        type('l', KeyModifier.CTRL)
        paste("http://www.sagetimeslipsecenter.com")
        type(Key.ENTER)
    wait("SageTimeslip-2.png", 120)
    find("Username.png")
    type("a", KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste("jknox1")
    wait(1)
    type(Key.TAB)
    paste("password")
    wait(.5)
    type(Key.ENTER)
    wait(2)    
    if choose_browser == "firefox":
        if exists("Wouldyoulike.png"):
            type(Key.ESC)  
    elif choose_browser == "safari":
        if exists("Wouldyoulike-1.png"):
            type(Key.ESC)

    wait(Pattern("Sagelimeslip.png").similar(0.89), 120)



    
def ecenter_create_data():
#-----------------------Create Client-----------------------#
    click("Administrato.png")
    wait(Pattern("ShowSettings.png").similar(0.91), 120)
    click(Pattern("AddNewClient.png").similar(0.86))
    click(Pattern("AridNewClien.png").similar(0.86))
    type(Key.TAB)
    type(Key.ENTER)
    wait(Pattern("NewClient.png").similar(0.82), 120)
    paste(Pattern("Nickname-1.png").similar(0.93), startTime.strftime('Client %Y_%m_%d %H_%M_%S'))
    type(Key.TAB)
    paste('client')
    type(Key.TAB)
    paste('client')
    for x in range(1, 13):
        TABFunction.tab(x)
    paste('example@example.com')
    for x in range(1, 7):
        TABFunction.tab(x)
    paste('100')
    type(Key.TAB)
    paste('200')
    type(Key.TAB)
    paste('300')
    for x in range(1, 20):
        TABFunction.tab(x)
    type(Key.ENTER)
    wait(Pattern("Newclientsuc.png").similar(0.87), 120)
#-----------------------Create Task-----------------------#
    click(Pattern("AddNewClient.png").similar(0.86))
    type(Key.DOWN + Key.ENTER)
    type(Key.TAB + Key.ENTER)
    wait("NewTask-1.png", 120)
    paste(Pattern("Nickname-1.png").similar(0.93), startTime.strftime('Task %Y_%m_%d %H_%M_%S'))
    type(Key.TAB)
    paste('task')
    type(Key.TAB)
    paste('task')
    type(Key.TAB + Key.TAB + Key.TAB)
    paste('25')
    type(Key.TAB)
    paste('50')
    type(Key.TAB)
    paste('75')
    for x in range(1, 20):
        TABFunction.tab(x)
    paste('1:00:00')
    type(Key.TAB + Key.TAB + Key.TAB)
    paste('test activity for smoke test') 
    type(Key.TAB + Key.TAB + Key.ENTER)
    wait(Pattern("Newtasksucce.png").similar(0.88), 120)
#-----------------------Create Expense-----------------------#    
    click(Pattern("AddNewClient.png").similar(0.86))
    type(Key.DOWN + Key.DOWN + Key.ENTER)
    type(Key.TAB + Key.ENTER)
    wait(Pattern("NewExpense.png").similar(0.83), 120)
    paste(Pattern("Nickname-1.png").similar(0.93), startTime.strftime('exp %Y_%m_%d %H_%M_%S'))
    type(Key.TAB)
    paste('expense')
    type(Key.TAB)
    paste('expense')
    type(Key.TAB + Key.TAB + Key.ENTER)
    wait(Pattern("llewCategory.png").similar(0.86), 120)
    paste(Pattern("Nickname-1.png").similar(0.93), startTime.strftime('categ %Y_%m_%d %H_%M_%S'))
    type(Key.TAB + Key.TAB + Key.ENTER)
    wait(Pattern("NicknameNick.png").similar(0.86), 120)
    paste(Pattern("Quantity.png").similar(0.85), '1')
    type(Key.TAB)
    paste('25')
    type(Key.TAB + Key.TAB + Key.TAB)
    paste('test expense for smoketest')
    type(Key.TAB + Key.TAB + Key.ENTER)
    wait(Pattern("Newexpensesu.png").similar(0.88), 120)      
#-----------------------Create Reference-----------------------#
    click(Pattern("AddNewClient.png").similar(0.86))
    type(Key.DOWN + Key.DOWN + Key.DOWN + Key.ENTER)
    type(Key.TAB + Key.ENTER)
    wait(Pattern("NewReference.png").similar(0.87), 120)
    click(Pattern("Client.png").similar(0.84))
    type('client 2013')
    type(Key.ENTER)
    type(Key.TAB)
    paste(startTime.strftime('ref %Y_%m_%d %H_%M_%S'))
    type(Key.TAB)
    paste('ref')
    type(Key.TAB + Key.TAB + Key.ENTER)
    wait(Pattern("Newreference-1.png").similar(0.87), 120)
            



     
def ecenter_createslip():
    click("CreateNewTim.png")
    wait(Pattern("TimeSlip.png").similar(0.93), 120)
    type("client 2013")
    wait(.5)
    type(Key.TAB)
    type("task 2013")
    wait(.5)
    type(Key.TAB)
    type(Key.TAB)
    paste("Testing Extra")
    type(Key.TAB)
    type(Key.END)
    paste(" Testing description")
    type(Key.TAB)
    paste(startTime.strftime('%m/%d/%y'))
    click("1349122994860.png")
    click(Pattern("T.png").similar(0.93))
    paste("00000TimeSpe-2.png", '1:25:00')
    click(Pattern("1349123612274.png").similar(0.87))
    wait(3)
    click(Pattern("1349123612274.png").similar(0.88))
    click(Pattern("TSDefault-1.png").similar(0.89))
    type("client")
    wait(.5)
    type(Key.ENTER)
    for x in range(1, 9):
        TABFunction.tab(x)
    type(Key.ENTER)
    wait("CorrectSpell.png", 120)
    click(Pattern("1371848080573.png").similar(0.87))
    
    
  
    

ecenter_login()

ecenter_create_data()

ecenter_createslip()

    
    