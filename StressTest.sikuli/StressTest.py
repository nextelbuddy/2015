from sikuli import*
import logging
reload(logging)
import datetime
import os
import subprocess
import TABFunction
import shutil
SCR0 = Screen(0)
SCR1 = Screen(1)
startTime = datetime.datetime.now()


def billassist_open_close(id):
    type('b', KeyModifier.ALT)
    type('b')
    if exists("SelectwhichB.png"):
        type('l')
        wait(.5)
        type(Key.ENTER)
        waitVanish("SelectwhichB.png")
    if exists("CurrentFlcad.png"):
        type(Key.ENTER)
        waitVanish("CurrentFlcad.png")
    wait("BillingAssis.png", 120)
    wait(Pattern("1366839698774.png").similar(0.89), 160)
    type('w', KeyModifier.CTRL)
    waitVanish("BillingAssis.png")

def sliplist_open_close(id):
    type('s', KeyModifier.ALT)
    type('s')
    wait(Pattern("WewBySelecti.png").similar(0.91), 120)
    if exists(Pattern("Show.png").similar(0.96)):
        type(Key.TAB + Key.TAB + Key.TAB + Key.TAB)
        wait(.5)
        type(Key.SPACE)
        wait("ClidUpdatewh.png", 120)
        type(Key.ENTER)
        waitVanish("ClidUpdatewh.png")
        wait("BothExpense.png", 120)       
    wait(.5)
    type('w', KeyModifier.CTRL)
    waitVanish(Pattern("WewBySelecti.png").similar(0.91))


def firmassist_open_close(id):
    type('b', KeyModifier.ALT)
    type('f')
    wait(Pattern("DateFlangeSt.png").similar(0.96), 120)
    type(Key.TAB + Key.TAB + Key.TAB)
    type(Key.ENTER)
    wait(Pattern("Details.png").similar(0.97), 160)
    type('w', KeyModifier.CTRL)
    waitVanish(Pattern("DateFlangeSt.png").similar(0.96))

    
def arlist_open_close(id):
    type('t', KeyModifier.ALT)
    type('a')
    wait(Pattern("ViewbySelec.png").similar(0.94), 120)
    type('w', KeyModifier.CTRL)
    waitVanish(Pattern("ViewbySelec.png").similar(0.94))


def clist_open_close(id):
    type('n', KeyModifier.ALT)
    type('i')
    wait("UPBWTcmpIalc.png", 120)
    type(Key.ENTER)
    wait(Pattern("NameandaddrN.png").similar(0.92), 120)
    type('w', KeyModifier.CTRL)
    waitVanish(Pattern("NameandaddrN.png").similar(0.92))
        


def stress_test(id):
    for x in range(0, 2):
        billassist_open_close(x)
        
    for x in range (0, 2):
        clist_open_close(x)

    for x in range(0, 2):
        sliplist_open_close(x)

    for x in range(0, 2):
        firmassist_open_close(x)

    for x in range(0, 2):
        arlist_open_close(x)




"""
# finite loop command
for x in range(0, 10):
    stress_test(x)"""


# infinite loop command    

x = 1
while True:
    stress_test(x)
    x +=1