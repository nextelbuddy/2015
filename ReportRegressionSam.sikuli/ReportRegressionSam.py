from sikuli import*
import logging
reload(logging)
import datetime
import RestorePrefs
import DBSetup
import os
import subprocess
import DBChecks
import TABFunction
import shutil
import Toolbox
SCR0 = Screen(0)
SCR1 = Screen(1)
startTime = datetime.datetime.now()

cOutputcount = 7

cRepAgedarbal = 1
cRepGenbills = 2
cRepLast = cRepGenbills


#-------------make sure you have Microsoft Office 2013 installed inorder for the Print to
#-------------Excel options  work correctly and Print to DOC correctly.

def GetReportGroup(pID):
    if pID == cRepAgedarbal:
        return 0
    elif pID == cRepGenbills:
        return 0
    else:
        return 0

def GetReportIndex(pID):
    if pID == cRepAgedarbal:
        return 0
    elif pID == cRepGenbills:
        return 6
    else:
        return 0




def SelectReport(pGroup,pDown):
    Toolbox.Navigatepage(pGroup,'True')
    Toolbox.Navigatelist(pDown,'True')
  
def OpenReportList():
    type('r', KeyModifier.CTRL)
    wait(Pattern("Youcanchange.png").similar(0.90), 10)
       


def OpenReport(pF6,pDown):
    SelectReport(pF6,pDown) 
    type('o', KeyModifier.CTRL)
    wait(Pattern("ISortandSubt-1.png").similar(0.91), 20)

def CloseReport():
    type(Key.F4, KeyModifier.CTRL)
    if exists(Pattern("Youhavechang.png").similar(0.91)):
        type('n')

def CheckforNoData():
    if exists("Nodatawassel.png"):
        type(Key.ENTER)

def ReportMoveToPrintto():    
    keyDown(Key.SHIFT)
    type(Key.TAB + Key.TAB)
    keyUp(Key.SHIFT)



def ReportPrintDisplay(): 
    type(Key.HOME) #condition focus is on Print to
    type('display')
    wait(1)
    type('p', KeyModifier.CTRL)
    CheckforNoData()
    wait(Pattern("Preview.png").similar(0.91), 30)
    type(Key.ESC)
    waitVanish(Pattern("Preview.png").similar(0.91))

def ReportPrintPrinter():    
    type(Key.HOME)
    type('printer.')
    wait(1)
    type('p', KeyModifier.CTRL)
    CheckforNoData()
    wait(Pattern("PrinterNameS-1.png").similar(0.91), 30)
    if not exists(Pattern("Name-1.png").similar(0.96)):
        type('microsoft')
        wait(1)
    type(Key.ENTER)
    if not exists(Pattern("FilenameSave-1.png").similar(0.91)):
        click(Pattern("1402952731422.png").similar(0.88))
    assert exists(Pattern("FilenameSave-1.png").similar(0.91))
    wait(Pattern("FilenameSave-1.png").similar(0.91), 30)
    paste(r'c:\ReportRegressionPrinttest.xps')
    wait(.5)
    type(Key.ENTER)
    if exists(Pattern("Rep0rtRegres.png").similar(0.91)):
        type('y')
    waitVanish(Pattern("FilenameSave-1.png").similar(0.91))

def ReportPrintExcel():
    type(Key.HOME)
    type('micro')
    wait(1)
    type('p', KeyModifier.CTRL)
    CheckforNoData()
    wait(Pattern("FileOptionsA.png").similar(0.91), 30)
    type(Key.ENTER)
    if exists(Pattern("Doyouwanttor-1.png").similar(0.91), 30):
        type('y')
    wait("Paste-1.png", 120)
    type(Key.F4, KeyModifier.ALT)
    if exists("Wanttosaveyo.png", 30):
        type('n')
    waitVanish("Paste-1.png")

def ReportPrintRTF():
    type(Key.HOME)
    type('rtf')
    wait(1)
    type('p', KeyModifier.CTRL)
    CheckforNoData()
    wait(Pattern("NametheRTFfi.png").similar(0.91), 30)
    type('o', KeyModifier.ALT)
    wait(.5)
    type(Key.ENTER)
    if exists(Pattern("kbDoyouwantt.png").similar(0.91)):
        type('y')
    wait("IQPaste.png", 120)
    type(Key.F4, KeyModifier.ALT)
    if exists("Wanttosaveyo.png", 30):
        type('n')
    waitVanish("IQPaste.png")

def ReportPrintCSV():
    type(Key.HOME)
    type('csv')
    wait(1)
    type('p', KeyModifier.CTRL)
    CheckforNoData()
    wait(Pattern("VametheCSVti.png").similar(0.91), 30)
    type('o', KeyModifier.ALT)
    wait(.5)
    type(Key.ENTER)
    if exists(Pattern("Doyouwanttor-1.png").similar(0.91), 30):
        type('y')
    wait("Paste-1.png", 120)
    type(Key.F4, KeyModifier.ALT)
    if exists("Wanttosaveyo.png", 30):
        type('n')
    waitVanish("Paste-1.png")

def ReportPrintTAB():
    type(Key.HOME)
    type('tab')
    wait(1)
    type('p', KeyModifier.CTRL)
    CheckforNoData()
    wait(Pattern("VametheTABti.png").similar(0.91), 30)
    type('o', KeyModifier.ALT)
    wait(.5)
    type(Key.ENTER)
    if exists(Pattern("Doyouwanttor-1.png").similar(0.91), 30):
        type('y')
    
    wait("Paste-1.png", 120)
    type(Key.F4, KeyModifier.ALT)
    if exists("Wanttosaveyo.png", 30):
        type('n')
    waitVanish("Paste-1.png")

def ReportPrintPDF():
    type(Key.HOME)
    type('pdf')
    wait(1)
    type('p', KeyModifier.CTRL)
    CheckforNoData()
    wait(Pattern("Selectthenam.png").similar(0.91), 30)
    type('o', KeyModifier.ALT)
    wait(.5)
    type(Key.ENTER)
    if exists(Pattern("Doyouwanttor-1.png").similar(0.91), 30):
        type('y')
    
    wait(Pattern("AgedARBalanc.png").similar(0.91), 120)
    type(Key.F4, KeyModifier.ALT)
    waitVanish(Pattern("AgedARBalanc.png").similar(0.91))


def PrintReportTo(pOutput):
    if pOutput==1:
        ReportPrintDisplay()
    if pOutput==2:
        ReportPrintPrinter() 
    if pOutput==3:
        ReportPrintExcel() 
    if pOutput==4:
        ReportPrintRTF() 
    if pOutput==5:
        ReportPrintCSV()
    if pOutput==6:
        ReportPrintTAB()
    if pOutput==7:
        ReportPrintPDF()


def ReportSupportsOutput(pGroup, pIndex, pOutput):
    if (pGroup == 1) and (pIndex == 6) and (pOutput == 3):
        return False
    elif (pGroup == 1) and (pIndex == 6) and (pOutput == 5):
        return False
    else:
        return True
    



def PrintReport(pID):
    OpenReport(GetReportGroup(pID),GetReportIndex(pID))
    ReportMoveToPrintto()
    for x in range(1,cOutputcount):
        if ReportSupportsOutput(pGroup, pIndex, x):
            PrintReportTo(x)
    CloseReport()

def PrintReportGroup(pGroup,pCount):
    OpenReportList()
    for x in range(0,pCount):
        PrintReport(pGroup,x)


def PrintAll():
    for x in range(1, cRepLast+1):
        PrintReport(x)


#PrintReport(0,0)
PrintAll()