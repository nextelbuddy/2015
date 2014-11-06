from sikuli import*

import logging
reload(logging)
import os
import subprocess
import TABFunction
import shutil

cLogin = 'sagetsqatester'
cPassword = 'TimeslipsQA'
cRecipient = 'shawn.robertson@sage.com'
cSubject = 'Smoketest Completed Successfully'
cMessage = 'Smoketest Completed Successfully, your Log results are attached'

browser = App(os.path.join(r"C:\Program Files (x86)", "Internet Explorer", "iexplore.exe"))


def email_results():
    browser.open()
    wait("http.png", 30)
    if exists("Wouldyoulike.png"):
        type('n', KeyModifier.ALT)
        type(Key.END)
        type(Key.DOWN)
        type('d')
        type(Key.ENTER)
    if exists("1404136125966.png"):
        type('o', KeyModifier.ALT)
        waitVanish("1404136125966.png")
    type('l', KeyModifier.CTRL)
    wait(1)
    paste('www.gmail.com')
    type(Key.ENTER)
    wait("https.png", 30)
    if not exists("https.png"):        
        type('l', KeyModifier.CTRL)
        wait(1)
        paste('www.gmail.com')
    if exists("1404136125966.png"):
        type('o', KeyModifier.ALT)
        waitVanish("1404136125966.png")
    wait("httoszf.png", 120) 
    if exists("leG00Signint-1.png"):
        paste("Email-1.png", cLogin)
        paste("Password.png", cPassword)
        type(Key.ENTER)
        if exists("Wouldyoulike-1.png"):
            type('n', KeyModifier.ALT)
            type(Key.END)
            type('n')
            type(Key.SPACE)
        wait("1404138138326.png", 30)
    if exists("qatestersage-1.png"):
        paste("1404139889932.png", cPassword)
        wait(1)
        type(Key.ENTER)
        wait("1404138138326.png", 30)
    click("1404138138326.png")
    wait("NewMessageT0.png", 120)
    onAppear("NewMessageT0.png", paste(cRecipient))
    type(Key.TAB)
    paste(cSubject)
    type(Key.TAB)
    paste(cMessage)
    click("1404142098543-1.png")
    wait("AllFiles-1.png", 30)
    paste(os.path.join(r"C:\tssmoketest", "logs"))
    type(Key.ENTER)
    wait("TSSMOKETESTL-2.png", 30)
    if not exists(Pattern("Datemodified-3.png").similar(0.98)):
        click("Datemodified-5.png")
        wait(Pattern("Datemodified-4.png").similar(0.98), 30)
        type(Key.TAB, KeyModifier.SHIFT)
        type(Key.TAB, KeyModifier.SHIFT)
        type('smoke')
        type(Key.SPACE + Key.ENTER)
        waitVanish(Pattern("Datemodified-3.png").similar(0.98))
        type(',', KeyModifier.CTRL)
        type(',', KeyModifier.CTRL)
        type(Key.ENTER, KeyModifier.CTRL)
        wait("Yourmessageh-1.png", 120)
    else:
        wait(Pattern("Datemodified-4.png").similar(0.98), 30)
        type(Key.TAB, KeyModifier.SHIFT)
        type(Key.TAB, KeyModifier.SHIFT)
        type(Key.SPACE + Key.ENTER)
        waitVanish(Pattern("Datemodified-3.png").similar(0.98))
        type(',', KeyModifier.CTRL)
        type(',', KeyModifier.CTRL)
        type(Key.ENTER, KeyModifier.CTRL)
        wait("Yourmessageh-1.png", 120)
    browser.close()
    
    
    
    
   
        




#email_results()



