#-------Script for creating quick Data liek clients/tasks/expenses etc------#

from sikuli import*
import logging
reload(logging)
import datetime
import os
import subprocess
import shutil
import TABFunction

startTime = datetime.datetime.now()
#----------Create Timekeeper method-----------#
def quick_timekeeper(id):
    type("n", KeyModifier.ALT)
    type("n")
    type("n", KeyModifier.CTRL)
    wait("iziClassific.png")
    #startTime = datetime.datetime.now()
    paste ("TK " + str(id))
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    paste("Regression Timekeeper")
   
    type("s", KeyModifier.CTRL)
    if exists("Whenyousavea.png"):
        type("o", KeyModifier.ALT)
        if exists("SetupResulSe.png"):
            type(Key.F4, KeyModifier.CTRL)
        else:
            wait("Noconflictsw.png", 60)
            type(Key.ENTER)
            type(Key.F4, KeyModifier.CTRL)
    wait(1)
    type(Key.F4, KeyModifier.CTRL)   
    wait(1)
    type(Key.F4, KeyModifier.CTRL) 

#----------Create client method-----------#

def quick_client(id):
    type("n", KeyModifier.ALT)
    type("i")
    type("n", KeyModifier.CTRL)
    wait("MClassificat.png", 30)
    #startTime = datetime.datetime.now()
    paste ("Client " + str(id))
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    wait(.5)
    paste("Regression Client")
    type("s", KeyModifier.CTRL)
    waitVanish(Pattern("1351792567535.png").similar(0.98))
    if exists("Whenyousavea.png"):
        type("o", KeyModifier.ALT)
        if exists("SetupResulSe.png"):
            type(Key.F4, KeyModifier.CTRL)
        else:
            wait("1374698639597.png", 60)
            type(Key.ENTER)
            type(Key.F4, KeyModifier.CTRL)
    wait(1)
    type(Key.F4, KeyModifier.CTRL)   
    wait(1)
    type(Key.F4, KeyModifier.CTRL) 


#----------Create Task method-----------#
def quick_task(id):
    type("n", KeyModifier.ALT)
    type("f")
    type("n", KeyModifier.CTRL)
    wait("IZI1IClassif.png")
    #startTime = datetime.datetime.now()
    paste ("Task " + str(id))
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    paste("Regression Task")
    type("s", KeyModifier.CTRL)
    waitVanish(Pattern("1351792567535-1.png").similar(0.98))
    type(Key.F4, KeyModifier.CTRL)   
    wait(1)
    type(Key.F4, KeyModifier.CTRL) 
    
#----------Create Expense method-----------#

def quick_expense(id):
    type("n", KeyModifier.ALT)
    type("o")
    type("n", KeyModifier.CTRL)
    wait("IZI1IClassif-1.png")
    #startTime = datetime.datetime.now()
    paste ("Expense " + str(id))
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    paste("Regression Expense")
    type("s", KeyModifier.CTRL)
    waitVanish(Pattern("1351792567535-2.png").similar(0.98))
    type(Key.F4, KeyModifier.CTRL)   
    wait(1)
    type(Key.F4, KeyModifier.CTRL) 