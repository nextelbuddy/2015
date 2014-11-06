from sikuli import*

import TABFunction
import os
import logging
import subprocess
import datetime
import Toolbox
import IMGToolbox
startTime = datetime.datetime.now()







"""
def ar_entry_regression(pType,pCheckT,pCheckNo,pClient,pDate,pAmount,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    wait(.5)
    type(Key.TAB)   
    type(pCheckT)
    type(Key.TAB)
    paste(pCheckNo)
    type(Key.TAB)
    type('s', KeyModifier.CTRL)
    wait(.5)
    assert exists(IMGToolbox.IMG_ar_client_require)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_client_require)
    wait(.5)
    type(pClient)
    type(Key.ENTER)
    #-------------------My Lists--------------------------------------#
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("m")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(1)
    rightClick(IMGToolbox.IMG_ar_client_combo_highlight)
    wait(.2)
    assert exists(IMGToolbox.IMG_ar_client_mylists_myclients)
    type(Key.ESC)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("a")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    rightClick(IMGToolbox.IMG_ar_client_combo_highlight)
    wait(.2)
    assert exists(IMGToolbox.IMG_ar_client_mylists_allclients)
    type(Key.ESC)
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("2")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(1)
    rightClick(Pattern("SbExtendedFu-1.png").similar(0.86))
    wait(.2)
    assert exists(Pattern("JNickname2.png").similar(0.94))
    type(Key.ESC)
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("1")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(1)
    rightClick(Pattern("SlipExtended-2.png").similar(0.86))
    wait(.2)
    assert exists(Pattern("JNicknamel-1.png").similar(0.94))
    type(Key.ESC)
    wait(.5)
    #----------------------------------------------------------------------------------#
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    type(Key.SPACE)
    wait(IMGToolbox.IMG_bank_dep, 30)
    type('n')
    waitVanish(IMGToolbox.IMG_bank_dep)
    wait(IMGToolbox.IMG_bank_dep, 30)
    type('n')
    waitVanish(IMGToolbox.IMG_bank_dep)
    type(Key.TAB)
    wait(.5)
    type('s', KeyModifier.CTRL)
    wait(.5)
    assert exists(IMGToolbox.IMG_ar_value_too_low)
    wait(.5)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_value_too_low)
    wait(.5)
    paste(pAmount)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    ARDescription.ar_description_shortcuts()


    
    #------------------Test
    type("l", KeyModifier.CTRL)
    wait(Pattern("TimeandExpen.png").similar(0.94))
    assert exists(Pattern("ViewByD.png").similar(0.96))
    type(Key.F4, KeyModifier.CTRL)
    waitVanish(Pattern("ViewByD.png").similar(0.96))
        #-----have to test save shortcut first to avoiding "save" pop up from occuring when changing pages with other shortcuts----#
    type("s", KeyModifier.CTRL)
    waitVanish(Pattern("IDNew.png").similar(0.94))
    assert not exists(Pattern("IDNew.png").similar(0.94))
    wait(.5)
    type(Key.PAGE_UP, KeyModifier.CTRL)
    assert exists(Pattern("ID.png").similar(0.94))
    wait(.5)
    type(Key.PAGE_DOWN, KeyModifier.CTRL)
    assert exists(Pattern("ID3.png").similar(0.95))
    wait(.5)
    type(Key.PAGE_UP)
    assert exists(Pattern("ID2.png").similar(0.96))
    wait(.5)
    type(Key.PAGE_DOWN)
    assert exists(Pattern("ID3.png").similar(0.95))
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("g")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    assert exists(Pattern("Movetotgookm.png").similar(0.98))
    wait(.5)
    type(Key.TAB)
    type("1")
    type(Key.ENTER)
    waitVanish(Pattern("MovetoglipMo.png").similar(0.94))
    assert exists(Pattern("ID.png").similar(0.94))
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("g")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.UP)
    type(Key.ENTER)
    waitVanish(Pattern("MovetoglipMo-2.png").similar(0.97))
    assert exists(Pattern("D2.png").similar(0.98))
    wait(.5)
    #--------------testing Search right click shortcuts----------------#
    type('t', KeyModifier.SHIFT + KeyModifier.CTRL)
    WaitToolbox.wait_invoice_search()
    type(Key.ESC)
    WaitToolbox.wait_vanish_invoice_search()
    type('f', KeyModifier.SHIFT + KeyModifier.CTRL)
    WaitToolbox.wait_ar_filter_selections()
    type(Key.TAB)
    type("c")
    type(Key.TAB)
    type(Key.SPACE)
    WaitToolbox.wait_ar_client_filter()   
    
    type('Sikuli')
    type(Key.F4)
    type(Key.ENTER)
    WaitToolbox.wait_vanish_ar_client_filter()
    type('o', KeyModifier.ALT)
    WaitToolbox.wait_vanish_ar_filter_selections()
    if exists():
        
    assert exists(Pattern("ViewingSelec.png").similar(0.97))
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("f")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(Pattern("Theselection.png").similar(0.96))
    for x in range(1, 4):
        TABFunction.tab(x)
    type(Key.SPACE)
    type("o", KeyModifier.ALT)
    waitVanish(Pattern("Theselection.png").similar(0.96))
   
    wait(.5)
    
    
    
    
    
    
    
      
    
    
    
    
    #----------------Test/Assert revert function---------------------#
        click("1353010884751.png")
    wait("SlipEntry-2.png")
    type("e")
    type(Key.ESC)
    onAppear(Pattern("SageTimeslip-1.png").similar(0.96), type("n"))
    
    waitVanish(Pattern("SageTimeslip-1.png").similar(0.96))
    assert exists(Pattern("Expense.png").similar(0.97))
    type(Key.ESC)
    wait(.5)
    onAppear(Pattern("SageTimeslip-1.png").similar(0.96), type("y"))
    assert exists(Pattern("Time.png").similar(0.97))
    wait(.5)"""





<<<<<<< HEAD

Toolbox.payment_entry('payment','check','65432','sikuli test client','9/10/2014','678','Test Descriptions')
"""
=======
"""
Toolbox.payment_entry('payment','check','65432','sikuli test client','9/10/2014','678','Test Descriptions')

>>>>>>> origin/master
Toolbox.payment_entry('payment','check','8079','sikuli','9/11/2014','110','Test description')

Toolbox.credit_entry('credit','sikuli','9/8/2014','1010','test credit description')

Toolbox.writeoff_entry('write','sikuli','9/7/2014','50','write off test description')

Toolbox.refund_entry('refund','sikuli','9/8/2014','25','refund test description')

Toolbox.invoice_entry('invoice','sikuli','9/8/2014','invoice test description','1009','100','25','50','15','5','n')

Toolbox.reverse_entry('reverse','sikuli','9/8/2014','reverse test description')

Toolbox.transfer_entry('transfer','sikuli','9/8/2014','15','transfer test description')

Toolbox.discount_entry('discount','sikuli','9/8/2014','10','discount test description')

Toolbox.special_entry('special')

Toolbox.increase_details_entry('increase','sikuli','9/8/2014','increase invoice details test description')

Toolbox.decrease_details_entry('decrease','sikuli','9/8/2014','decrease invoice details test description')
"""