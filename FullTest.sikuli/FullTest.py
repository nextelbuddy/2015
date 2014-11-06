#make sure your Timeslips is installed to C:\tsshare\
#for this year we are on 2014 and the path is C:\tsshare\timeslips 2014
#follow the format of Timeslips XXXX and update the install path in the CreateTSDB script.
#always check and update the App.open path and the install path
#Db path is always C:\tsshare\timeslips\automation
#DB path is separate than application path

from sikuli import*

import CreateTSDB
import OpenTS_DB_Test
import CreateTimeSlipNewComplete
import CreateExpenseSlipNewComplete
import RestorePrefs
import ClearSlips
import SlipAssert
import CreateClient
import CreateTask
import CreateExpense
import CreateReference
import DBSetup
import SlipsExpandedFunctionalityComplete
import os
import mySettings
import DBChecks

    #App instance for timeslips
timeslip = App(os.path.join(r"C:\tssmoketest", Settings.tsVersion, "timeslip.exe"))



CreateTSDB.create_ts_db()
timeslip.open()
DBChecks.checkFor_BillingDate()  
DBChecks.checkFor_SPS()
DBChecks.checkFor_PEP()
wait("leibmaEEQSle.png", 60)
RestorePrefs.restore_prefs()
wait(1)
DBSetup.db_setup()
wait(1)
for x in range(1, 2):
    CreateClient.create_client(x)
    wait(1)
    CreateTask.create_task(x)
    wait(1)
    CreateExpense.create_expense(x)
    wait(1)
wait(1)
CreateReference.create_reference()
wait(2)
ClearSlips.clear_slips()
wait(1)
CreateTimeSlipNewComplete.create_timeslip_New()
wait(1)
CreateExpenseSlipNewComplete.create_expslip_New()
wait(1)

SlipsExpandedFunctionalityComplete.ts_expanded_functions()
wait(1)
SlipAssert.slip_assert()

