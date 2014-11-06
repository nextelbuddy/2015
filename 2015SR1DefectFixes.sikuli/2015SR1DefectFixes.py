from sikuli import*

import TABFunction
import os
import logging
import subprocess
import datetime
import Toolbox
startTime = datetime.datetime.now()





#Variables used in create client function    
vClient_name_1 = 'splitclient15'
vClient_name_2 = 'splitclient16'
#Variables used in restore and backup functions
vBDBLocation = os.path.join(r'C:\tssmoketest', 'Backups', 'Smoketest_Reprint_PDF_Test_backup.bku')
vRDBLocation = os.path.join(r'C:\Sikuli Scripts VM X local copy for testing', '2015', 'Data', 'Reprint Bill incorrect PDF.bku')

#These parameters are for the slip creation function where we can pass in values to the slip create method. 
pTK = 'sikuli timekeeper'
pAct = 'sikuli task'
pClient = 'sikuli client'
pRef = 'none'
pExtra = 'extra'
pDescription = 'Slip Description should be visible'
pStartDate = 't'
pEndDate = 't'
pTimeEst = '1:00:00'
pTimeSpent = '1:00:00'
pRateValue = '150'





def SR1_2015_defect_fixes():
    
    #Starting from Timeslips home screen
    #Defect for Printing collated split bills
    Toolbox.create_test_client(vClient_name_1)
    Toolbox.create_test_client(vClient_name_2)
    type('b', KeyModifier.ALT)
    type('i')
    wait("1408371404528.png", 30)
    type('n', KeyModifier.ALT)
    wait("1408371471875.png", 30)
    type(vClient_name_1)
    type(Key.TAB)
    type('SR1 Test')
    type(Key.ENTER)
    waitVanish("1408373236033.png")
    for x in range(0, 7):
        TABFunction.tab(x)
    type(Key.ENTER)
    wait("1408373493377.png", 30)
    type(vClient_name_2)
    type(Key.TAB)
    type('SR1 test')
    type(Key.TAB)
    paste('50')
    type(Key.TAB)
    paste('50')
    type(Key.ENTER)
    waitVanish("1408373690690.png")
    type(Key.F4, KeyModifier.ALT)    
    waitVanish("1408373728324.png")
    type('m', KeyModifier.CTRL)
    wait("1408378294656.png", 30)
    type('n', KeyModifier.CTRL)
    wait("1408378320890.png", 30)    
    type(Key.TAB)
    type(Key.DOWN)
    type(Key.TAB)
    type(Key.DOWN)
    type(Key.TAB)
    type(vClient_name_1)
    for x in range(0, 7):
        TABFunction.tab(x)
    paste("1:00:00")
    for x in range(0, 7):
        TABFunction.tab(x)
    paste('1000')
    type('s', KeyModifier.CTRL)
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("1408382776753.png")
    type('w', KeyModifier.CTRL)    
    type('b', KeyModifier.CTRL)
    wait("1408384417093.png", 30)
    type(Key.TAB)
    type('cli')
    type(Key.TAB)
    type(Key.SPACE)
    wait("1408384512033.png", 30)
    type(vClient_name_1)
    type(Key.F4)
    type(Key.ENTER)
    waitVanish("1408384512033.png")
    
    keyDown(Key.SHIFT)
    for x in range(0, 3):
        TABFunction.tab(x)
    keyUp(Key.SHIFT)
    type('printer...')
    type('p', KeyModifier.CTRL)
    wait("1408384822716.png", 30)
    type('microsoft')
    for x in range(0, 3):
        TABFunction.tab(x)
    paste('5')
    if not exists("1408385345350.png"):
        type('o', KeyModifier.ALT)
    type(Key.ENTER)
    if exists(Pattern("1408385450858.png").similar(0.87)):
        click(Pattern("1408385450858.png").similar(0.87))
    wait("1408385485763.png", 30)
    paste('SR1 Defect Collate test')
    type('s', KeyModifier.ALT)
    if exists("1408386107497.png"):
        type('y', KeyModifier.ALT)
    waitVanish("1408385485763.png")
    click("1408385625824.png")
    type(Key.ENTER)
    onAppear("1408385861684.png", type(Key.ENTER))
    waitVanish("1408385861684.png")
    type('w', KeyModifier.CTRL)
    if exists("1408385931427.png"):
        type('n', KeyModifier.ALT)
    #----------------------------------------------------------------------#

    #Starting from Timeslips home screen
    #Defect for Date displaying 1899 in calendar entry and timecapture toolbits. 
    type('l', KeyModifier.ALT)
    type('n')
    wait("1408387917993.png", 30)
    type(Key.TAB + Key.TAB)
    type('c')
    wait("1408387963478.png", 30)
    type(Key.ENTER)
    waitVanish("1408387963478.png")
    assert not exists("1408388009755.png")
    type('w', KeyModifier.CTRL)
    onAppear("1408388055479.png", type('n'))
    waitVanish("1408388055479.png")
    #----------------------------------------------------------------------#

    #Starting from Timeslips home screen
    #Defect for Reprinting multiple bills to PDF can use the incorrect PDF names
    #we have to first backup the smoketest DB and then restore a DB that has data we can use to test several defects and then once verified restore the original smoke test DB to move on.
    

    
    #('- backing up Current Smoke test DB')
    Toolbox.Backup_DB(vBDBLocation)
    #('- Restoring PDF Reprint Bills Defect Backup')
    Toolbox.Restore_DB(vRDBLocation)
    wait(1)
    type('b', KeyModifier.ALT)
    type('r')
    wait("1408480754612.png", 30)
    
    type(Key.TAB + Key.TAB)
    if not exists(Pattern("1408480780555.png").similar(0.98)):
        click("1408480840367.png")
    if (Env.isLockOn(Key.NUM_LOCK)):
        type(Key.NUM_LOCK)
    keyDown(Key.SHIFT)
    type(Key.DOWN + Key.DOWN + Key.DOWN)
    keyUp(Key.SHIFT)
    type(Key.F4)
    assert exists("1408482292865.png")
    type(Key.TAB + Key.TAB)
    type('pdf')
    type(Key.TAB + Key.SPACE)
    wait("1408556853816.png", 30)
 
    click("1408562174353.png")
    type(Key.TAB)
    
    paste(os.path.join(r'C:\Sikuli Scripts VM X local copy for testing', '2015', 'Data', 'PDF Reprint Bill Testing'))  
    type(Key.ENTER)  
    if exists("1408557908502.png"):
        type('y', KeyModifier.ALT)
        waitVanish("1408557908502.png")
    wait(2)    
    type('r', KeyModifier.WIN)
    wait("1408556695227.png", 30)
    paste(os.path.join(r'C:\Sikuli Scripts VM X local copy for testing', '2015', 'Data', 'PDF Reprint Bill Testing'))  
    type(Key.ENTER)
    wait(Pattern("1408557839163.png").similar(0.86), 30)
    if not exists(Pattern("1408558635209.png").similar(0.97)):
        click(Pattern("1408558674898.png").similar(0.91))
    assert exists("1408558705115.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish(Pattern("1408557839163.png").similar(0.86))
    type('w', KeyModifier.CTRL)
    waitVanish("1408480754612.png")
    #----------------------------------------------------------------------#
    #Defect for Reprint bills can not be sorted by custom field
    type('p', KeyModifier.ALT)
    type('c')
    wait("1408565429189.png", 30)
    type('n', KeyModifier.ALT)
    type('t')
    type(Key.ENTER)
    wait("1408565501614.png", 30)
    paste('SortingCustom')
    type(Key.ENTER)
    waitVanish("1408565501614.png")
    for x in range(0, 6):
        TABFunction.tab(x)
    type(Key.ENTER)
    waitVanish("1408565429189.png")
    type('n', KeyModifier.ALT)
    wait(.5)
    type('i')
    wait("1407956749298.png", 30)
    type('abington')
    wait(1)
    type(Key.ENTER)
    wait("1408567750831.png", 30)
    type(Key.F6 + Key.F6 + Key.F6)
    paste("1408567876709.png", 'SortingCustom')
    type('s', KeyModifier.CTRL)
    type('w', KeyModifier.CTRL)
    type('b', KeyModifier.ALT)
    type('r')
    wait("1408646814298.png", 30)
    assert exists(Pattern("1408647519293.png").similar(0.93))
    type(Key.TAB + Key.SPACE)
    wait("1408647448546.png", 30)
    type('c')
    type(Key.TAB)
    for x in range(0, 13):
        type('c')
    type(Key.TAB + Key.SPACE)
    wait("1408653192311.png", 30)
    type('contains')
    type(Key.TAB)
    paste('SortingCustom')
    type(Key.ENTER)
    waitVanish("1408654653778.png")
    type('o', KeyModifier.ALT)
    waitVanish("1408654702143.png")
    assert not exists(Pattern("1408654793898.png").similar(0.96))
    assert exists(Pattern("1408654766923.png").similar(0.96))
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("1408654928512.png")
    #----------------------------------------------------------------------#
    # Defect to test slip list not able to sort by custom field
    
    type('m', KeyModifier.CTRL)
    wait("1408729373371.png", 30)
    type('s', KeyModifier.ALT)
    wait("1408729400665.png", 30)
    type('c')
    type(Key.TAB)
    for x in range(0, 13):
        type('c')
    type(Key.TAB + Key.SPACE)
    wait("1408653192311.png", 30)
    type('contains')
    type(Key.TAB)
    paste('SortingCustom')
    type(Key.ENTER)
    waitVanish("1408654653778.png")
    type('o', KeyModifier.ALT)
    waitVanish("1408654702143.png")
    type(Key.ENTER)
    waitVanish("1408729532208.png")
    assert exists(Pattern("1408729571365.png").similar(0.98))
    
    #----------------------------------------------------------------------#
        
    #('- Restoring original smoke test Backup')
    Toolbox.Restore_DB(vBDBLocation)
    
    #----------------------------------------------------------------------#
    #Defect for Project defaults are not always copied from master client. 

    type('p', KeyModifier.ALT)
    type('g')
    wait("1408731124361.png", 30)
    for x in range(0, 6):
        type(Key.F6)
    type('s', KeyModifier.ALT)
    if not exists("1408739581714.png"):        
        type(Key.DECIMAL)
        assert exists("1408731695461.png")
    type(Key.ENTER)
    waitVanish("1408731743027.png")

    type('n', KeyModifier.ALT)
    type('i')
    wait("1408731785640.png", 30)
    type('Sikuli Test Client 1')
    wait(1)
    type(Key.ENTER)
    wait("1408736433557.png", 30)
    type('n', KeyModifier.CTRL)
    paste('.')
    wait("1408736497329.png", 30)
    paste('Project1')
    type(Key.ENTER)
    wait(1)
    assert exists("1408736621529.png")
    type(Key.F4, KeyModifier.CTRL)
    onAppear("1408736698052.png", type('n', KeyModifier.ALT))
    waitVanish("1408736750368.png")
    type('n', KeyModifier.CTRL)
    wait("1408736937669.png", 30)
    paste('Sikuli Test Client.Project')
    type(Key.ENTER)
    waitVanish("1408736976034.png")
    paste('THIS SHOULD APPEAR 1')
    type('s', KeyModifier.CTRL)
    waitVanish("1408737071628.png")
    type('n', KeyModifier.CTRL)
    wait("1408738934509.png", 30)
    paste('.')
    onAppear("1408737135111.png", paste('Project 2'))
    type(Key.ENTER)
    waitVanish("1408737168326.png")
    wait(1)
    assert exists("1408739867016.png")
    paste('THIS SHOULD APPEAR 2')
    keyDown(Key.SHIFT)
    for x in range(0, 7):
        TABFunction.tab(x)
    keyUp(Key.SHIFT)
    type(Key.SPACE)
    assert exists("1408738858408.png")
    type('s', KeyModifier.CTRL)
    waitVanish("1408738899391.png")
    type('n', KeyModifier.CTRL)
    wait("1408738952227.png", 30)
    paste('.')
    wait("1408738988465.png", 30)
    paste('Project 3')
    type(Key.ENTER)
    waitVanish("1408739016479.png")
    assert exists("1408739912798.png")
    type('s', KeyModifier.CTRL)
    waitVanish("1408739200356.png")
    type('w', KeyModifier.CTRL)
    #----------------------------------------------------------------------#
    #testing defect where no dates import from Template client or normal client
    type('n', KeyModifier.ALT)
    type('i')
    wait("1408731785640.png", 30)
    type(Key.F6)
    wait("1408740755919.png", 30)
    type('n', KeyModifier.CTRL)
    wait("1408740789373.png", 30)
    paste('*Rate Template Test')
    type(Key.ENTER)
    waitVanish("1408740827153.png")
    type(Key.F6 + Key.F6)
    paste('100')
    type(Key.TAB)
    paste('200')
    for x in range(0, 19):
        type(Key.TAB)
    type('n', KeyModifier.CTRL + KeyModifier.SHIFT)
    wait("1408741077186.png", 30)
    type(Key.TAB)
    type('sikuli')
    type(Key.TAB)
    type('c')
    assert exists("1408741190587.png")
    type(Key.ENTER)
    waitVanish("1408741219217.png")
    type('n', KeyModifier.CTRL + KeyModifier.SHIFT)
    wait("1408741077186.png", 30)
    type(Key.TAB)
    type('slip')
    type(Key.TAB)
    type('c')
    type(Key.TAB + '2')
    assert exists("1408741429924.png")
    type(Key.ENTER)
    waitVanish("1408741435235.png")
    type('s', KeyModifier.CTRL)
    waitVanish("1408741518086.png")
    if exists("1408741538669.png"):
        type('n', KeyModifier.ALT)
        waitVanish("1408741538669.png")
    type('w', KeyModifier.CTRL)
    waitVanish("1408741623688.png")
    type('n', KeyModifier.ALT)
    type('i')
    wait("1408731785640.png", 30)
    type('n', KeyModifier.CTRL)
    wait("1408741720457.png", 30)
    paste('Rate Import Test Client')
    type(Key.ENTER)
    waitVanish("1408741790493.png")
    type('s', KeyModifier.CTRL)
    waitVanish("1408741518086.png")
    type(Key.F6 + Key.F6)
    click(Pattern("1408741854904.png").similar(0.97))
    wait("1408741911181.png", 30)
    type(Key.TAB, KeyModifier.SHIFT)
    type('template')
    type(Key.TAB)
    type('Rate Template')
    type(Key.TAB + Key.TAB + Key.ENTER)
    wait("1408742247663.png", 30)
    type(Key.ENTER)
    waitVanish("1408742247663.png")
    assert exists(Pattern("1408978819700.png").similar(0.95))
    assert exists(Pattern("1408978838634.png").similar(0.97))
    type('w', KeyModifier.CTRL)
    wait("1408742382055.png", 30)
    type('y', KeyModifier.ALT)
    waitVanish("1408742382055.png")
    if exists("1408741538669.png"):
        type('n', KeyModifier.ALT)
        waitVanish("1408741538669.png")
    
    #----------------------------------------------------------------------#

    #Defect for text search filtering not working
    type('m', KeyModifier.CTRL)   
    #using assigned parameters at top of script. if values need to be changed change them up there.
    Toolbox.Create_Time_Slip(pTK,pAct,pClient,pRef,pExtra,pDescription,pStartDate,pEndDate,pTimeEst,pTimeSpent,pRateValue)
    type('w', KeyModifier.CTRL)
    type('c', KeyModifier.ALT)
    type('x')
    wait("1408987482143.png", 30)
    paste(pDescription)
    type('s', KeyModifier.ALT)
    wait("1408987546930.png", 30)
    type('g', KeyModifier.ALT)
    type('m')
    type(Key.TAB)
    type('c')
    type(Key.TAB + Key.ENTER)
    wait("1408987674354.png", 30)
    type('pClient')
    type(Key.F4)
    type(Key.ENTER)
    waitVanish("1408987674354.png")
    type('o', KeyModifier.ALT)
    waitVanish("1408987674354.png")
    type('e', KeyModifier.ALT)
    wait(1)
    assert exists("1408989593975.png")
    type('c', KeyModifier.ALT)
    type(Key.F4, KeyModifier.ALT)
    #----------------------------------------------------------------------#
    #Deferct to test Email receipt to multiple CC address when separated using carriage returns causes AV2
    type('w', KeyModifier.CTRL)
    Toolbox.create_test_client('EmailReceiptTest')
    type('n', KeyModifier.ALT)
    type('i')
    wait("1408731785640.png", 30)
    type('EmailReceiptTest')
    wait(1)
    type(Key.ENTER)
    wait("1408736433557.png", 30)
    keyDown(Key.SHIFT)
    for x in range(0, 6):
        type(Key.TAB)
    keyUp(Key.SHIFT)
    paste('Receipt@example.com')
    type(Key.TAB)
    paste('Receipt1@example.com')
    type(Key.ENTER)
    paste('Receipt2@example.com')
    type('s', KeyModifier.CTRL)
    waitVanish("1408741518086.png")
    type('w', KeyModifier.CTRL)
    type('t', KeyModifier.CTRL)
    if exists("1408998619403.png"):
        type(Key.TAB + Key.TAB)
        type('c')
        type(Key.TAB)
        type('EmailReceiptTest')
        type(Key.ENTER)
    elif exists("1408998757258.png"):
        type(Key.TAB + Key.TAB)
        type('c')
        type(Key.TAB)
        type('EmailReceiptTest')
        type(Key.ENTER)
    elif exists("1408998951149.png"):
        type(Key.TAB + Key.TAB + Key.TAB)
        type('EmailReceiptTest')
        type(Key.ENTER)
        
    wait("1408993277258.png", 30)
    for x in range(0, 3):
        type(Key.TAB)
    type('EmailReceiptTest')
    wait("1408993461295.png", 30)
    type(Key.ENTER)
    waitVanish("1408993461295.png")
    type('n', KeyModifier.CTRL)
    wait("1408994170377.png", 30)
    for x in range(0, 6):
        type(Key.TAB)
    paste('150')
    type('s', KeyModifier.CTRL)
    waitVanish("1408741518086.png")
    type('e', KeyModifier.CTRL)
    wait("1408994299632.png", 30)
    type('e', KeyModifier.ALT)
    wait("1408994841974.png", 30)
    assert exists(Pattern("1408994913569.png").similar(0.98))
    type(Key.ESC)
    waitVanish("1408994841974.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish(Pattern("1408994299632.png").similar(0.95))
    type('w', KeyModifier.CTRL)

    #----------------------------------------------------------------------#
    
    #defect to check if the insert data token option is availalable in the right click pop up menu
    type('n', KeyModifier.ALT)
    type('i')
    wait("1408731785640.png", 30)
    type('EmailReceiptTest')
    wait(1)
    type(Key.ENTER)
    wait("1408736433557.png", 30)

    for x in range(0, 8):
        type(Key.F6)
    for x in range(0, 5):
        type(Key.TAB)
    type('o', KeyModifier.CTRL)
    wait("1408996532697.png",30)
    rightClick("1408996596301.png")
    wait(1)
    assert exists(Pattern("1408996640355.png").similar(0.97))
    click(Pattern("1408996640355.png").similar(0.97))
    wait("1408996688815.png", 30)
    type(Key.ESC)
    waitVanish("1408996688815.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish("1408996532697.png")
    type('w', KeyModifier.CTRL)
    
            
    
    
    
    
            
    


SR1_2015_defect_fixes()