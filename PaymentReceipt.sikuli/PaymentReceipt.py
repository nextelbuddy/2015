from sikuli import*
import logging
import os
import subprocess
import TABFunction
import shutil
SCR0 = Screen(0)
SCR1 = Screen(1)
import datetime
startTime = datetime.datetime.now()
import os
import TestLogFile





cDefPayText = 'A payment of [Value] was applied to your balance on [Transaction Date].\n\nThank you for your business,\n[Firm Name]'
cDefRevPayText = 'Your payment dated [Transaction Date] of [Value] was reversed. Please contact us at your earliest convenience.\n\nThank you for your business,\n[Firm Name]'
cDefPfaText = 'A payment of [Value] was applied from your funds account to your balance on [Transaction Date].\n\nThank you for your business,\n[Firm Name]'
cDefPtaText = 'A payment of [Value] was applied to your funds account on [Transaction Date].\n\nThank you for your business,\n[Firm Name]'

cDefPaySubj = 'Thank you for your payment'
cDefRevPaySubj = 'A payment was reversed'
cDefPfaSubj = 'Money was transferred from your account'
cDefPtaSubj = 'Money was deposited into your account'



cCustomPayBody1 = 'Test Payment description for [Nickname 1]\n\nThank You,\n[Firm Name]'
cCustomRevPayBody1 = 'Test Reverse Payment description for [Nickname 1]\n\nThank You,\n[Firm Name]'
cCustomPfaBody1 = 'Test Payment From Account description for [Nickname 1]\n\nThank You,\n[Firm Name]'
cCustomPtaBody1 = 'Test Payment To Account description for [Nickname 1]\n\nThank You,\n[Firm Name]'


cCustomPaySubject1 = 'Test Payment Subject'
cCustomRevPaySubject1 = 'Test Reverse Payment Subject'
cCustomPfaSubject1 = 'Test Payment From Account Subject'
cCustomPtaSubject1 = 'Test Payment To Account Subject'

cPayDataToken = '[Firm Name][Firm Address Line 1][Firm Address Line 2][Firm City, State Zip]' + 
                '[Firm Other][Firm Name/Address: Standard][Firm Name/Address: w/o commas]' + 
                '[Firm Address: Standard][Firm Address: w/o commas][Firm Phone 1][Firm Phone 2]' + 
                '[Firm Fax 1][Firm Fax 2][Firm Email][Firm Website][Firm Custom 1][Firm Custom 2]' + 
                #'[Today''''s Date][Nickname 1][Nickname 2][Client Name][Client Address Line 1]' + 
                '[Client Address Line 2][Client Address Line 3][Client City][Client State]' + 
                '[Client Zip][Client City, State Zip][Client Country]' + 
                '[Client Name/Address: Standard][Client Name/Address: w/o commas]' + 
                '[Client Name/Address: USPS Style][Client Address][Client Other Address Line 1]' + 
                '[Client Other Address Line 2][Client Other Address Line 3][Client Other City]' + 
                '[Client Other State][Client Other Zip][Client Other City, State Zip]' + 
                '[Client Other Country][Client Name/Other Address: Standard]' + 
                '[Client Name/Other Address: w/o commas][Client Name/Other Address: USPS Style]' + 
                '[Client Other Address][Client Phone][Client Fax][Client Home][Client Other]' + 
                '[Email Address][CC Address][Custom Custom Date][Custom Custom Hours]' + 
                '[Custom Custom List][Custom Custom Money][Custom Custom Number]' + 
                '[Custom Custom Percent][Custom Custom Text][Custom Custom Timekeep][Balance]' + 
                '[Balance for Current Period][Balance for Period 1][Balance for Period 2]' + 
                '[Balance for Period 3][Balance for Period 4][Balance for Period 5]' + 
                '[Balance for Period 6][Unapplied Balance][Last Bill Date][Transaction ID]' + 
                '[Transaction Date][Value][Check Number][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type]'

cRevPayDataToken = '[Firm Name][Firm Address Line 1][Firm Address Line 2][Firm City, State Zip]' + 
                '[Firm Other][Firm Name/Address: Standard][Firm Name/Address: w/o commas]' + 
                '[Firm Address: Standard][Firm Address: w/o commas][Firm Phone 1][Firm Phone 2]' + 
                '[Firm Fax 1][Firm Fax 2][Firm Email][Firm Website][Firm Custom 1][Firm Custom 2]' + 
                #'[Today''''s Date][Nickname 1][Nickname 2][Client Name][Client Address Line 1]' + 
                '[Client Address Line 2][Client Address Line 3][Client City][Client State]' + 
                '[Client Zip][Client City, State Zip][Client Country]' + 
                '[Client Name/Address: Standard][Client Name/Address: w/o commas]' + 
                '[Client Name/Address: USPS Style][Client Address][Client Other Address Line 1]' + 
                '[Client Other Address Line 2][Client Other Address Line 3][Client Other City]' + 
                '[Client Other State][Client Other Zip][Client Other City, State Zip]' + 
                '[Client Other Country][Client Name/Other Address: Standard]' + 
                '[Client Name/Other Address: w/o commas][Client Name/Other Address: USPS Style]' + 
                '[Client Other Address][Client Phone][Client Fax][Client Home][Client Other]' + 
                '[Email Address][CC Address][Custom Custom Date][Custom Custom Hours]' + 
                '[Custom Custom List][Custom Custom Money][Custom Custom Number]' + 
                '[Custom Custom Percent][Custom Custom Text][Custom Custom Timekeep][Balance]' + 
                '[Balance for Current Period][Balance for Period 1][Balance for Period 2]' + 
                '[Balance for Period 3][Balance for Period 4][Balance for Period 5]' + 
                '[Balance for Period 6][Unapplied Balance][Last Bill Date][Transaction ID]' + 
                '[Transaction Date][Value][Check Number][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type][Payment Type]' + 
                '[Payment Type][Payment Type][Payment Type][Payment Type]'

cPfaDataToken = '[Firm Name][Firm Address Line 1][Firm Address Line 2]' + 
                '[Firm City, State Zip][Firm Other][Firm Name/Address: Standard]' + 
                '[Firm Name/Address: w/o commas][Firm Address: Standard]' + 
                '[Firm Address: w/o commas][Firm Phone 1][Firm Phone 2][Firm Fax 1]' + 
                '[Firm Fax 2][Firm Email][Firm Website][Firm Custom 1][Firm Custom 2]' + 
                #'[Today''''s Date][Nickname 1][Nickname 2][Client Name]' + 
                '[Client Address Line 1][Client Address Line 2][Client Address Line 3]' + 
                '[Client City][Client State][Client Zip][Client City, State Zip]' + 
                '[Client Country][Client Name/Address: Standard]' + 
                '[Client Name/Address: w/o commas][Client Name/Address: USPS Style]' + 
                '[Client Address][Client Other Address Line 1]' + 
                '[Client Other Address Line 2][Client Other Address Line 3]' + 
                '[Client Other City][Client Other State][Client Other Zip]' + 
                '[Client Other City, State Zip][Client Other Country]' + 
                '[Client Name/Other Address: Standard]' + 
                '[Client Name/Other Address: w/o commas]' + 
                '[Client Name/Other Address: USPS Style][Client Other Address]' + 
                '[Client Phone][Client Fax][Client Home][Client Other][Email Address]' + 
                '[CC Address][Custom Custom Date][Custom Custom Hours][Custom Custom List]' + 
                '[Custom Custom Money][Custom Custom Number][Custom Custom Percent]' + 
                '[Custom Custom Text][Custom Custom Timekeep][Balance]' + 
                '[Balance for Current Period][Balance for Period 1][Balance for Period 2]' + 
                '[Balance for Period 3][Balance for Period 4][Balance for Period 5]' + 
                '[Balance for Period 6][Unapplied Balance][Last Bill Date][Transaction ID]' + 
                '[Transaction Date][Value][Check Number][Funds Account Name]' + 
                '[Funds Account Applies To][Funds Account Balance]' + 
                '[Funds Account Auto Pay New Charges][Funds Account Replenish Minimum]' + 
                '[Funds Account Replenish To][Funds Account Bill Format Style][Bank Name]' + 
                '[Bank Account Applies To][Bank Account Type][Bank Account Type]' + 
                '[Bank Account Type][Bank Account Type][Bank Account Type]' + 
                '[Bank Account Type][Bank Account Type][Bank Account Type][Bank Account Type]' + 
                '[Bank Account Type][Bank Account Type][Bank Account Type][Bank Account Type]' + 
                '[Bank Account Type][Bank Account Type][Bank Account Type]['

cPtaDataToken = '[Firm Name][Firm Address Line 1][Firm Address Line 2]' + 
                '[Firm City, State Zip][Firm Other][Firm Name/Address: Standard]' + 
                '[Firm Name/Address: w/o commas][Firm Address: Standard]' + 
                '[Firm Address: w/o commas][Firm Phone 1][Firm Phone 2][Firm Fax 1]' + 
                '[Firm Fax 2][Firm Email][Firm Website][Firm Custom 1][Firm Custom 2]' + 
                #'[Today''''s Date][Nickname 1][Nickname 2][Client Name]' + 
                '[Client Address Line 1][Client Address Line 2][Client Address Line 3]' + 
                '[Client City][Client State][Client Zip][Client City, State Zip]' + 
                '[Client Country][Client Name/Address: Standard]' + 
                '[Client Name/Address: w/o commas][Client Name/Address: USPS Style]' + 
                '[Client Address][Client Other Address Line 1]' + 
                '[Client Other Address Line 2][Client Other Address Line 3]' + 
                '[Client Other City][Client Other State][Client Other Zip]' + 
                '[Client Other City, State Zip][Client Other Country]' + 
                '[Client Name/Other Address: Standard]' + 
                '[Client Name/Other Address: w/o commas]' + 
                '[Client Name/Other Address: USPS Style][Client Other Address]' + 
                '[Client Phone][Client Fax][Client Home][Client Other][Email Address]' + 
                '[CC Address][Custom Custom Date][Custom Custom Hours][Custom Custom List]' + 
                '[Custom Custom Money][Custom Custom Number][Custom Custom Percent]' + 
                '[Custom Custom Text][Custom Custom Timekeep][Balance]' + 
                '[Balance for Current Period][Balance for Period 1][Balance for Period 2]' + 
                '[Balance for Period 3][Balance for Period 4][Balance for Period 5]' + 
                '[Balance for Period 6][Unapplied Balance][Last Bill Date][Transaction ID]' + 
                '[Transaction Date][Value][Check Number][Funds Account Name]' + 
                '[Funds Account Applies To][Funds Account Balance]' + 
                '[Funds Account Auto Pay New Charges][Funds Account Replenish Minimum]' + 
                '[Funds Account Replenish To][Funds Account Bill Format Style][Bank Name]' + 
                '[Bank Account Applies To][Bank Account Type][Bank Account Type]' + 
                '[Bank Account Type][Bank Account Type][Bank Account Type]' + 
                '[Bank Account Type][Bank Account Type][Bank Account Type][Bank Account Type]' + 
                '[Bank Account Type][Bank Account Type][Bank Account Type][Bank Account Type]' + 
                '[Bank Account Type][Bank Account Type][Bank Account Type]['






def Set_Data_Token():
    type('p', KeyModifier.ALT)
    type('r')
    wait(Pattern("PaymentRever.png").similar(0.94), 30)
    for x in range(0, 4):
        type('a', KeyModifier.CTRL)
        type(Key.DELETE)
        type('t', KeyModifier.ALT)
        wait("groupllhlll.png", 30)
        type(Key.TAB)
        for x in range(0, 74):
            for x in range(0, 74):
                type(Key.DOWN)
            type(Key.ENTER)
            waitVanish("group.png")
        type(Key.F6)


def Test_Token(pIndex, pText, pSubject):
    type('p', KeyModifier.ALT)
    type('r')
    wait("PaymentRever-1.png", 30)
    for x in range(1, pIndex):
        type(Key.F6)        
    type('a', KeyModifier.CTRL)
    type('c', KeyModifier.CTRL)
    cb = Env.getClipboard()
    bodyok = cb == pText
    TestLogFile.Log_Result(bodyok, 'BODY ' + str(pIndex))
    
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type('c', KeyModifier.CTRL)
    cb = Env.getClipboard()
    subjectok = cb == pSubject
    TestLogFile.Log_Result(subjectok, 'SUBJECT ' + str(pIndex))
    if bodyok and subjectok:        
        type(Key.F4, KeyModifier.ALT) 
    return bodyok and subjectok



def Set_Default_Values():
    type('p', KeyModifier.ALT)
    type('r')
    wait(Pattern("PaymentRever.png").similar(0.94), 30)
    for x in range(0, 4):
        
        type('d', KeyModifier.ALT)
        wait("Thiswillrese.png", 30)
        type('y')
        waitVanish("Thiswillrese.png")    
        type(Key.F6)    
    keyDown(Key.SHIFT)
    type(Key.TAB)
    keyUp(Key.SHIFT)
    type(Key.ENTER)




def Test_Receipt(pTestName, pIndex, pText, pSubject):
    type('p', KeyModifier.ALT)
    type('r')
    wait("PaymentRever-1.png", 30)
    for x in range(1, pIndex):
        type(Key.F6)        
    type('a', KeyModifier.CTRL)
    type('c', KeyModifier.CTRL)
    cb = Env.getClipboard()
    bodyok = cb == pText
    TestLogFile.Log_Result(bodyok, pTestName + ' BODY ' + str(pIndex))
    
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type('c', KeyModifier.CTRL)
    cb = Env.getClipboard()
    subjectok = cb == pSubject
    TestLogFile.Log_Result(subjectok, 'SUBJECT ' + str(pIndex))
    if bodyok and subjectok:        
        type(Key.F4, KeyModifier.ALT) 
    return bodyok and subjectok




def Set_Custom_Receipt(pIndex, pNewText, pNewSubject):
    type('p', KeyModifier.ALT)
    type('r')
    wait(Pattern("PaymentRever.png").similar(0.94), 30)
    for x in range(1, pIndex):
        type(Key.F6)
    type('a', KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste(pNewText)   
    type(Key.TAB)
    type('a', KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste(pNewSubject)   
    type(Key.ENTER) 
 

                                            
                  

def Test_Default_Receipt():
    if Test_Receipt('Default 1', 1, cDefPayText, cDefPaySubj) == True:    
        if Test_Receipt('Default 2', 2, cDefRevPayText, cDefRevPaySubj) == True: 
            if Test_Receipt('Default 3', 3, cDefPfaText,cDefPfaSubj) == True: 
                Test_Receipt('Default 4', 4, cDefPtaText, cDefPtaSubj)



def Test_Custom_Receipt():
    Set_Custom_Receipt(1, cCustomPayBody1, cCustomPaySubject1)
    if Test_Receipt('Custom 1', 1, cCustomPayBody1, cCustomPaySubject1) == True: 
        Set_Custom_Receipt(2, cCustomRevPayBody1, cCustomRevPaySubject1)
        if Test_Receipt('Custom 2', 2, cCustomRevPayBody1, cCustomRevPaySubject1) == True: 
            Set_Custom_Receipt(3, cCustomPfaBody1, cCustomPfaSubject1)
            if Test_Receipt('Custom 3', 3, cCustomPfaBody1, cCustomPfaSubject1) == True: 
                Set_Custom_Receipt(4, cCustomPtaBody1, cCustomPtaSubject1)
                Test_Receipt('Custom 4', 4, cCustomPtaBody1, cCustomPtaSubject1)


def Test_DataToken_Receipt():
    Add_All_Data_Token()
    if Test_Receipt('DataToken 1', 1, cPayDataToken, 'Data Token Test') == True: 
        if Test_Receipt('DataToken 2', 2, cRevPayDataToken, 'Data Token Test') == True: 
            if Test_Receipt('DataToken 3', 3, cPfaDataToken, 'Data Token Test') == True: 
                Test_Receipt('DataToken 4', 4, cPtaDataToken, 'Data Token Test')
            
                                              

def Add_All_Data_Token():    
    type('p', KeyModifier.ALT)
    type('r')
    wait(Pattern("PaymentRever-2.png").similar(0.94), 30)
    for x in range(0, 4):
        add_all_receipt()
    type(Key.TAB + Key.ENTER)
                

def add_all_receipt():
    type('a', KeyModifier.CTRL)
    type(Key.DELETE)
    for x in range(0, 100):
        Set_Data_Token(x)
    type(Key.TAB)
    paste('Data Token Test')
    type(Key.TAB, KeyModifier.SHIFT)
    type(Key.F6)

    
def Set_Data_Token(pIndex):
    type('t', KeyModifier.ALT)
    wait("groupllhlll-1.png", 30)
    type(Key.TAB)
    for x in range(0, pIndex):            
        type(Key.DOWN)
    type(Key.ENTER)
    waitVanish("group-1.png")




def payment_receipt():
    Test_Default_Receipt()
    Test_Custom_Receipt()
    Test_DataToken_Receipt()
    Set_Default_Values()
    Test_Default_Receipt()
    




#Set_Default_Values()
#Test_Default_Receipt()
#Test_Custom_Receipt()
#Add_All_Data_Token()
#payment_receipt()