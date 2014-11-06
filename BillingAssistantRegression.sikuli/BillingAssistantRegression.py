#-----------------Generate bills script-----------------#




from sikuli import*
import logging
reload(logging)
import datetime
import os
import subprocess
import shutil
import Toolbox
import IMGToolbox
import TABFunction
import QuickDataCreate
SCR0 = Screen(0)
SCR1 = Screen(1)
startTime = datetime.datetime.now()

#----------------------------------------------------------#

#----- string to use for date/time string ---------%Y_%m_%d %H_%M_%S

#---Create new Quick Data for Billing which only includes names and nothing more---#
"""
for x in range(1, 2):
    QuickDataCreate.quick_timekeeper(x)
    wait(1)
    QuickDataCreate.quick_client(x)
    wait(1)
    QuickDataCreate.quick_task(x)
    wait(1)
    QuickDataCreate.quick_expense(x)"""

#-------------------------------------------------------------#
#Open an existing client such as Sikuli test client 1

#------Open Billing Assistant ENTRY MODE--------#
keyDown(Key.SHIFT)
type('b', KeyModifier.CTRL)
keyUp(Key.SHIFT)
if exists(IMGToolbox.IMG_ba_view_prompt):
    type('E', KeyModifier.ALT)
    type(Key.ENTER)

wait(IMGToolbox.IMG_ba_entry_view, 30)
assert exists(IMGToolbox.IMG_ba_entry_view)
type('sikuli test client 1')
wait(.5)




wait(1)
paste('1')
for x in range(1, 8):
    TABFunction.tab(x)










