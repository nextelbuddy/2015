from sikuli import*
import IMGToolbox
import ARDescription

def DownXtimes(pDown):
    for x in range(1, pDown+1):
        type(Key.DOWN)


def Navigatepage(pPagecount,pForward):
    if pForward=='True':
        for x in range(0, pPagecount):
            type(Key.F6)       
    else:
        for x in range(0, pPagecount):
            keyDown(Key.SHIFT)
            type(Key.F6)
            keyUp(Key.SHIFT)


def Navigatelist(pListcount,pDown):
    if pDown=='True':
        for x in range(0, pListcount):
            type(Key.DOWN)
    else:
        for x in range(0, pListcount):
            type(Key.UP)

#------------------------------------------------------------------------------------#
# 
def create_test_client(pName):
    type('n', KeyModifier.ALT)
    wait(.5)
    type('i')
    wait("1407956749298.png", 30)
    type('n', KeyModifier.CTRL)
    wait("1407956797812.png", 30)
    paste(pName)
    type('s', KeyModifier.CTRL)
    waitVanish(Pattern("1407957845265.png").similar(0.90), 30)
    if exists("1408567408763.png"):
        type(Key.ENTER)
    
    type('w', KeyModifier.CTRL)
    waitVanish("1407957983846.png")





#------------------System Related tasks------------------------------------#

def Backup_DB(pDBLocation):
    type('f', KeyModifier.ALT)
    type('b')
    wait(Pattern("Thisprocessc-4.png").similar(0.91), 30)
    type(Key.ENTER)
    wait("SaveasmeSage.png", 30)
    #('- Saving file path and name')
    wait(.5)
    paste(pDBLocation)
    wait(1)
    type('s', KeyModifier.ALT)
    if exists("Abackupfilea-1.png"):
        type('y', KeyModifier.ALT)
    wait(Pattern("Thebackupofy-2.png").similar(0.89), 120)
    type(Key.ENTER)
    waitVanish(Pattern("Thebackupofy-2.png").similar(0.89))



def Restore_DB(pDBLocation):
    #('- Restoring PDF Reprint Bills Defect Backup')
    type('f', KeyModifier.ALT)
    type('r')
    wait(Pattern("Choosewheret-1.png").similar(0.91), 30)
    paste(pDBLocation)
    type('u', KeyModifier.ALT)
    type(Key.ENTER)
    wait(Pattern("SageTimeslip-3.png").similar(0.91), 120)
    type(Key.ENTER)
    waitVanish(Pattern("Choosewheret-1.png").similar(0.91))


<<<<<<< HEAD
#---------------------------------Slip Related Tasks------------------------------------------#
=======
#---------------------------------Slip Rerlated Tasks------------------------------------------#
>>>>>>> origin/master
def Create_Time_Slip(pTK,pAct,pClient,pRef,pExtra,pDescription,pStartDate,pEndDate,pTimeEst,pTimeSpent,pRateValue):
    wait("1408986911027.png")
    type('n', KeyModifier.CTRL)
    wait("1408981839050.png", 30)
    type(Key.TAB)
    type(pTK)
    type(Key.TAB)
    type(pAct)
    type(Key.TAB)
    type(pClient)
    type(Key.TAB)
    type(pRef)
    type(Key.TAB)
    paste(pExtra)
    type(Key.TAB)
    paste(pDescription)
    type(Key.TAB)
    type(pStartDate)
    type(Key.TAB)
    type(pEndDate)
    type(Key.TAB)
    paste(pTimeEst)    
    type(Key.TAB)
    paste(pTimeSpent)
    for x in range(0, 7):
        type(Key.TAB)
    paste(pRateValue)
    type('s', KeyModifier.CTRL)
    type(Key.F4, KeyModifier.CTRL)
    
    
    





#-------------------AR Related Tasks--------------------------------------#


def ar_list():
    type('t', KeyModifier.CTRL)



def payment_entry(pType,pCheckT,pCheckNo,pClient,pDate,pAmount,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pCheckT)
    type(Key.TAB)
    paste(pCheckNo)
    type(Key.TAB)
    type(pClient)
    type(Key.ENTER)
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
    paste(pAmount)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)
    type('s', KeyModifier.CTRL)
    waitVanish(IMGToolbox.IMG_ar_id_new)
    type('w', KeyModifier.CTRL)
    
    
    
    
    
    
    



def credit_entry(pType,pClient,pDate,pAmount,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pClient)
    type(Key.ENTER)
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    paste(pAmount)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)
    type('s', KeyModifier.CTRL)
    waitVanish(IMGToolbox.IMG_ar_id_new)
    type('w', KeyModifier.CTRL)
    




def writeoff_entry(pType,pClient,pDate,pAmount,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pClient)
    type(Key.ENTER)
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    paste(pAmount)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)
    type('s', KeyModifier.CTRL)
    wait(.5)
    assert exists(IMGToolbox.IMG_ar_writeoff_applied_error)
    wait(.5)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_writeoff_applied_error)
    type('w', KeyModifier.CTRL)
    if exists(IMGToolbox.IMG_do_want_save_ar):
        type('n')
        





def refund_entry(pType,pClient,pDate,pAmount,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pClient)
    type(Key.ENTER)
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    paste(pAmount)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)
    type('s', KeyModifier.CTRL)
    wait(.5)
    assert exists(IMGToolbox.IMG_ar_refund_assign_message)
    wait(.5)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_refund_assign_message)
    type('w', KeyModifier.CTRL)
    if exists(IMGToolbox.IMG_do_want_save_ar):
        type('n')
    waitVanish(IMGToolbox.IMG_ar_id_new)

    




def invoice_entry(pType,pClient,pDate,pDescription,pInvoice,pFees,pFTax,pCosts,pCTax,pInterest,pApply):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pClient)
    type(Key.ENTER)
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)
    type(Key.TAB + Key.TAB)
    type(pInvoice)
    type(Key.TAB)
    type(pFees)
    type(Key.TAB)
    type(pFTax)
    type(Key.TAB)
    type(pCosts)
    type(Key.TAB)
    paste(pCTax)
    type(Key.TAB)
    type(pInterest)    
    type('s', KeyModifier.CTRL)
    if exists(IMGToolbox.IMG_ar_money_suspense):
        type(pApply)
        waitVanish(IMGToolbox.IMG_ar_money_suspense)
    waitVanish(IMGToolbox.IMG_ar_id_new)
    type('w', KeyModifier.CTRL)
    




    
def reverse_entry(pType,pClient,pDate,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pClient)
    type(Key.ENTER)
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)    
    type('s', KeyModifier.CTRL) 
    if exists(IMGToolbox.IMG_ar_reverse_empty):
        type(Key.ENTER)
        waitVanish(IMGToolbox.IMG_ar_reverse_empty)
    type(Key.F4, KeyModifier.CTRL)
    onAppear(IMGToolbox.IMG_do_want_save_ar, type('n'))
    waitVanish(IMGToolbox.IMG_ar_id_new)
    type('w', KeyModifier.CTRL)
    





def transfer_entry(pType,pClient,pDate,pAmount,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pClient)
    type(Key.ENTER)
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    type('s', KeyModifier.CTRL) 
    assert exists(IMGToolbox.IMG_ar_transfer_assign_empty)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_transfer_assign_empty)
    wait(.5)
    paste(pAmount)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)    
    type('s', KeyModifier.CTRL) 
    assert exists(IMGToolbox.IMG_ar_transfer_assign_empty)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_transfer_assign_empty)
    type(Key.F4, KeyModifier.CTRL)
    onAppear(IMGToolbox.IMG_do_want_save_ar, type('n'))
    waitVanish(IMGToolbox.IMG_ar_id_new)
    type('w', KeyModifier.CTRL)
    




def discount_entry(pType,pClient,pDate,pAmount,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pClient)
    type(Key.ENTER)
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    type('s', KeyModifier.CTRL)
    assert exists(IMGToolbox.IMG_ar_value_too_low)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_value_too_low)
    paste(pAmount)
    type('s', KeyModifier.CTRL)
    assert exists(IMGToolbox.IMG_ar_trans_fully_applied)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_trans_fully_applied)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)        
    type(Key.F4, KeyModifier.CTRL)
    onAppear(IMGToolbox.IMG_do_want_save_ar, type('n'))
    waitVanish(IMGToolbox.IMG_ar_id_new)
    type('w', KeyModifier.CTRL)
    




def special_entry(pType):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB) 
    wait(.5)
    assert exists(IMGToolbox.IMG_ar_special_credit_error)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_special_credit_error)
    wait(.5)
    assert exists(IMGToolbox.IMG_ar_combo_payment)    
    type('w', KeyModifier.CTRL)
   




def increase_details_entry(pType,pClient,pDate,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pClient)
    type(Key.ENTER)
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)    
    type('s', KeyModifier.CTRL) 
    wait(.5)
    assert exists(IMGToolbox.IMG_ar_invoice_details_validate_save_yes_invoice)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_invoice_details_validate_save_yes_invoice)
    type(Key.F4, KeyModifier.CTRL)
    onAppear(IMGToolbox.IMG_do_want_save_ar, type('n'))
    waitVanish(IMGToolbox.IMG_ar_id_new)
    type('w', KeyModifier.CTRL)
    




def decrease_details_entry(pType,pClient,pDate,pDescription):
    type('t', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_list, 30)
    type('n', KeyModifier.CTRL)
    wait(IMGToolbox.IMG_ar_entry, 30)
    type(pType)
    type(Key.TAB)   
    type(pClient)
    type(Key.ENTER)
    type(Key.TAB)
    type(pDate)
    wait(1)
    type('c')
    wait(IMGToolbox.IMG_ar_calendar, 30)
    type(Key.ESC)
    waitVanish(IMGToolbox.IMG_ar_calendar)
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste(pDescription)    
    type('s', KeyModifier.CTRL) 
    wait(.5)
    assert exists(IMGToolbox.IMG_ar_invoice_details_validate_save_yes_invoice)
    type(Key.ENTER)
    waitVanish(IMGToolbox.IMG_ar_invoice_details_validate_save_yes_invoice)
    type(Key.F4, KeyModifier.CTRL)
    onAppear(IMGToolbox.IMG_do_want_save_ar, type('n'))
    waitVanish(IMGToolbox.IMG_ar_id_new)
    type('w', KeyModifier.CTRL)
    












