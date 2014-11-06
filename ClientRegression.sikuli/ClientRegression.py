from sikuli import*
import CreateClient
import DBSetup
import CreateTask
import CreateTimekeeper
import CreateCustomField
SCR0 = Screen(0)
SCR1 = Screen(1)
import logging
reload(logging)
import datetime
import os
import subprocess
import TABFunction
import shutil
startTime = datetime.datetime.now()



#-------Make sure you use an empty DB as this script will create the necessary data------#

#----We have to create a custom field first so that the custom tab is available on the client information screen.
#----Make sure to run while Timeslips is open and started at the enhanced navigator screen with no dialogs open----#
#-------Need to go into general settings and setup items-------#
#-----Disable Conflict checking first------#
DBSetup.db_setup()
#-----Terminology for Client change-------#
type('p', KeyModifier.ALT)
type('g')
wait("FirmAddressI.png", 20)
type(Key.F6)
type('c', KeyModifier.ALT)
paste('Person')
type(Key.TAB)
paste('People')
#-----Project separator-------#
type(Key.F6 + Key.F6 + Key.F6 + Key.F6 + Key.F6)
type('s', KeyModifier.ALT)
type('.')
wait("rojectSepara.png", 20)
type('f', KeyModifier.ALT)
type(Key.TAB + Key.TAB)
type('30')
type(Key.ENTER)
waitVanish("NamesNicknam.png")
type('w', KeyModifier.CTRL)
#----------Create Client Custom Field----------------#

CreateCustomField.create_custom_field()

#---------create Data such as Timekeeper and Tasks-----------#
for x in range(1, 2):
    CreateTimekeeper.create_timekeeper(x)
for x in range(1, 2):
    CreateTask.create_task(x)
#-----------Client regression Test-----------------#
#-----This is a loop command for your clients, 
#-----change the 2nd numerical value to define how many clients you want to create. 
#This creates client or clients and creates data on all tabs, verifies that data is saved
#correctly as well as changes classifications for open to inactive, open to closed and back
for x in range(1, 2):
    CreateClient.create_client_regression(x)
#------Opening Client list to verify right click and tool bit buttons------#
type('n', KeyModifier.ALT)
assert exists(Pattern("PersonMistor-2.png").similar(0.91))
type('i')
wait("UPBYIITempla-1.png", 20)
type('sikuli regre')
wait(1)
rightClick(Pattern("SikuliFleore-2.png").similar(0.97))
click("RecordCount-1.png")
wait("Numberofreco-1.png", 20)
type(Key.ENTER)
waitVanish("Numberofreco-1.png")
#--------Using Enter button to verify open existing client-----------#
type(Key.ENTER)
wait(Pattern("NameandacNam.png").similar(0.90), 20)
type(Key.F4, KeyModifier.CTRL)
waitVanish(Pattern("NameandacNam.png").similar(0.90))
type('o', KeyModifier.CTRL)
wait(Pattern("NameandacNam.png").similar(0.90), 20)
type(Key.TAB)
#--------Adding 30 character name to NN2---------#
paste('This is exactly 30 characters.')
type('s', KeyModifier.CTRL)
waitVanish(Pattern("1351792567535.png").similar(0.98))
type(Key.F4, KeyModifier.CTRL)
waitVanish(Pattern("NameandacNam.png").similar(0.90))
#-------Testing client project creation--------#
type('o', KeyModifier.CTRL)
wait(Pattern("NameandacNam.png").similar(0.90), 20)
type('n', KeyModifier.CTRL)
wait("Setupthisrec.png", 20)
type('.Pro')
type(Key.ENTER)
waitVanish("Setupthisrec.png")
type('s', KeyModifier.CTRL)
waitVanish(Pattern("1351792567535.png").similar(0.98))
type(Key.F4, KeyModifier.CTRL)
waitVanish(Pattern("NameandacNam.png").similar(0.90))
type('w', KeyModifier.CTRL)
#-----------------Create Client References------------------#
type("n", KeyModifier.ALT)
type("r")
wait(Pattern("PersonUDBWlI.png").similar(0.87), 20)
type("Sikuli Reg")
type(Key.ENTER)
type("n", KeyModifier.CTRL)
wait("ClientNickna-2.png", 20)
paste("Sikuli Test Reference")
wait(Pattern("SikuliTestRe-1.png").similar(0.94))
type(Key.ENTER)
waitVanish("ClientNickna-3.png")
#------Creating Duplicate Reference----------#
type('n', KeyModifier.CTRL)
wait("ClientNickna-3.png", 20)
paste("Sikuli Test Reference")
wait(Pattern("SikuliTestRe-1.png").similar(0.94))
type(Key.ENTER)
if exists("Thisreferenc-1.png"):
    type('y', KeyModifier.ALT)
waitVanish("ClientNickna-3.png") 
type(Key.TAB)
type(Key.DELETE, KeyModifier.CTRL)
wait("Areyousureth-1.png", 20)
type('y', KeyModifier.ALT)
assert exists(Pattern("ElpenNicknam-1.png").similar(0.90))
type('o', KeyModifier.CTRL)
wait("ClientNickna-3.png")
paste('Sikuli Test Reference Changes')
wait(Pattern("SikuliTestRe-6.png").similar(0.84))
type(Key.ENTER)
waitVanish("ClientNickna-3.png")
assert exists(Pattern("UDBWlInactiv.png").similar(0.91))
rightClick(Pattern("UDBWlInactiv.png").similar(0.91))
click("RecordCount.png")
wait("Numberofreco.png", 20)
type(Key.ENTER)
waitVanish("Numberofreco.png")
click(Pattern("IJLI-1.png").similar(0.91))
wait("ClientNickna-4.png", 20)
type('d', KeyModifier.ALT)
type('sik')
wait(.5)
type(Key.ENTER)
waitVanish("ClientNickna-4.png")
type('w', KeyModifier.CTRL)
waitVanish("Thislistshow.png")
#--------------Launching slip entry to test default references-----------------#
type('m', KeyModifier.CTRL)
wait("WewBySelect.png", 20)
type('n', KeyModifier.CTRL)
wait("IDNewType.png", 20)
type(Key.TAB)
type('sik')
type(Key.TAB)
type('sik')
type(Key.TAB)
type('sik')
assert exists(Pattern("SikuliTestRe-3.png").similar(0.90))
type(Key.F4, KeyModifier.CTRL)
if exists("Doyouwantsav.png"):
    type('y', KeyModifier.ALT)
waitVanish("IDType.png")
type('w', KeyModifier.CTRL)
waitVanish("WewBySelect.png")
#------Launching Timesheet template to test reference defaults------------#
type('s', KeyModifier.ALT)
type('tt')
wait("Viewby.png", 20)
type('n', KeyModifier.CTRL)
wait("TimekeeperAI.png", 20)
type(Key.TAB + Key.TAB + Key.TAB + Key.TAB)
type('sikuli reg')
type(Key.TAB + Key.TAB)
assert exists(Pattern("SikuliTestRe-4.png").similar(0.92))
type(Key.F4, KeyModifier.CTRL)
if exists("Doyouwanttos.png"):
    type('n', KeyModifier.ALT)
waitVanish("TemplatedeNa.png")
type('w', KeyModifier.CTRL)








