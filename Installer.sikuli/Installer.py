#this is a script to install any build of timeslips from the network build machine

from sikuli import*

import mySettings
import CreateTSDB
import logging
import os

    #we have imported a Settings script that contains several global variables that can pull data from user input.
    #anything that has Settings.XXXX is a global item from the mySettings script.


#we will structure this script so that we call the specific apps we want to use in the script and then close later when we no longer need them. 
#Make sure in pop up prompts that you input the proper year as a 4 digit number, build as "Build XX.X.X.XX
#and the proper serial # for that version



    #need to call the settings script for global variables first
#mySettings.ts_settings_build() 
    #use this on machien that doesnt have access to QTS machines
#mySettings.ts_settings_archive() 
    #this is the function for the installer script that makes several calls to the above 
    #global variables script

#This is a separate installer setup when using the single file installer
def single_installer():
    #section below browses out to network path on build machine and starts coe generator as well as launches the build you specify 

    Settings.tscode.open()
    wait("1360952841007.png", 240)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.SPACE)
    wait(Pattern("Createaprodu.png").similar(0.89))
    type(Key.SPACE, KeyModifier.ALT)
    type("n")
    waitVanish(Pattern("SageTimeslip-1.png").similar(0.84))
    #installer launches here
    Settings.single_file_setup.open()
    wait(Pattern("1384201737141.png").similar(0.96), 240)
    type('y')
    wait(Pattern("SageTlmeslip.png").similar(0.84), 300)
    click(Pattern("InstallSageT-1.png").similar(0.81), 240)
    if exists("Doyouwanttor.png", 90):
        type('n', KeyModifier.ALT)
    if exists("AdobeReaderc.png", 90):
        type(Key.ESC)
        waitVanish("AdobeReaderc.png", 30)
    wait(Pattern("Welcomelnthe.png").similar(0.84), 240)
    type("n", KeyModifier.ALT)
    wait(Pattern("LicenseAgree.png").similar(0.77), 240)
    type("a")
    wait(1)
    type("n", KeyModifier.ALT)
    waitVanish(Pattern("LicenseAgree.png").similar(0.77))
    type("n", KeyModifier.ALT)
    waitVanish("Configuratio-1.png")
    type("n", KeyModifier.ALT)
        #this line below needs to be tweaked later to handle user profiles temp folder
    #App.focus(r'C:\Users\srobertson\AppData\Local\Temp\{3DD2E857-0F3F-4515-A5D8-CB7E86CF61C2}\ISBEW64.exe')
    waitVanish("Verification.png")
    type("r", KeyModifier.ALT)
    wait(Pattern("Pleaseselect.png").similar(0.84), 360)
    type("p", KeyModifier.ALT)
    paste(r'c:\tssmoketest\\' + Settings.Version)
    type(Key.ENTER)
    waitVanish(Pattern("Pleaseselect.png").similar(0.84))
    type("n", KeyModifier.ALT)
    wait(Pattern("Pleaseselect-1.png").similar(0.81), 90)
    type("n", KeyModifier.ALT)
    wait(.5)
    type("u", KeyModifier.ALT)
    wait(.5)
    paste('Sikuli Tester')
    wait(.5)
    type("c", KeyModifier.ALT)
    wait(.5)
    paste('Sage')        
    wait(.5)
    type("s", KeyModifier.ALT)
    wait(.5)
    paste(Settings.tsSerial)
    wait(.5)
    type("n", KeyModifier.ALT)
    type("i", KeyModifier.ALT)
    if exists("Beforecontin.png"):
        type(Key.ENTER)
    waitVanish(Pattern("Thesetupprog.png").similar(0.84))
    wait(Pattern("Pleaseselect-2.png").similar(0.98), 900)
    type("n", KeyModifier.ALT)
    wait(Pattern("Pleaseselect-3.png").similar(0.83), 90)
    type("d", KeyModifier.ALT)
    wait(.5)
    type("r", KeyModifier.ALT)
    wait(.5)
    type("u", KeyModifier.ALT)
    wait(.5)
    type("f", KeyModifier.ALT)
    waitVanish(Pattern("Pleaseselect-3.png").similar(0.83))
        #section below is to close all apps opened during installation
    Settings.tscode.close()
    Settings.tssetup.close()
    




#This is a separate installer setup when using the CD image installer
def cd_installer():
    #section below browses out to network path on build machine and starts coe generator as well as launches the build you specify 
    Settings.tscode.open()
    wait("1360952841007.png", 240)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.SPACE)
    wait(Pattern("Createaprodu.png").similar(0.89))
    type(Key.SPACE, KeyModifier.ALT)
    type("n")
    waitVanish(Pattern("SageTimeslip-1.png").similar(0.84))
    wait(1)
        #installer launches here
    Settings.tssetup.open()
    wait(Pattern("SageTlmeslip.png").similar(0.92), 240)
    click(Pattern("InstallSageT-1.png").similar(0.81), 240)
    if exists("Doyouwanttor.png", 90):
        type('n', KeyModifier.ALT)
    if exists("AdobeReaderc.png", 90):
        type(Key.ESC)
        waitVanish("AdobeReaderc.png", 30)
    wait(Pattern("Welcomelnthe.png").similar(0.84), 240)
    type("n", KeyModifier.ALT)
    wait(Pattern("LicenseAgree.png").similar(0.77), 240)
    type("a")
    wait(1)
    type("n", KeyModifier.ALT)
    waitVanish(Pattern("LicenseAgree.png").similar(0.77))
    type("n", KeyModifier.ALT)
    waitVanish("Configuratio-1.png")
    type("n", KeyModifier.ALT)
        #this line below needs to be tweaked later to handle user profiles temp folder
    #App.focus(r'C:\Users\srobertson\AppData\Local\Temp\{3DD2E857-0F3F-4515-A5D8-CB7E86CF61C2}\ISBEW64.exe')
    waitVanish("Verification.png")
    type("r", KeyModifier.ALT)
    wait(Pattern("Pleaseselect.png").similar(0.84), 240)
    type("p", KeyModifier.ALT)
    paste(r'c:\tssmoketest\\' + Settings.Version)
    type(Key.ENTER)
    waitVanish(Pattern("Pleaseselect.png").similar(0.84))
    type("n", KeyModifier.ALT)
    wait(Pattern("Pleaseselect-1.png").similar(0.81), 90)
    type("n", KeyModifier.ALT)
    wait(.5)
    type("u", KeyModifier.ALT)
    wait(.5)
    paste('Sikuli Tester')
    wait(.5)
    type("c", KeyModifier.ALT)
    wait(.5)
    paste('Sage')        
    wait(.5)
    type("s", KeyModifier.ALT)
    wait(.5)
    paste(Settings.tsSerial)
    wait(.5)
    type("n", KeyModifier.ALT)
    type("i", KeyModifier.ALT)
    if exists("Beforecontin.png"):
        type(Key.ENTER)
    waitVanish(Pattern("Thesetupprog.png").similar(0.84))
    wait(Pattern("Pleaseselect-2.png").similar(0.98), 900)
    type("n", KeyModifier.ALT)
    wait(Pattern("Pleaseselect-3.png").similar(0.83), 90)
    type("d", KeyModifier.ALT)
    wait(.5)
    type("r", KeyModifier.ALT)
    wait(.5)
    type("u", KeyModifier.ALT)
    wait(.5)
    type("f", KeyModifier.ALT)
    waitVanish(Pattern("Pleaseselect-3.png").similar(0.83))
        #section below is to close all apps opened during installation
    Settings.tscode.close()
    Settings.tssetup.close()
    
    
  
   
#ts_installer()

#This is a separate installer for when we are in alpha/beta phase of development. 


def alpha_beta_installer():
    #section below browses out to network path on build machine and starts the alpha/beta build you specify 
        #installer launches here
    Settings.tssetup.open()
    wait(Pattern("SetupandInst.png").similar(0.95), 240)
    click(Pattern("InstallSageT-1.png").similar(0.81), 240)
    if exists("Doyouwanttor.png", 90):
        type('n', KeyModifier.ALT)
    if exists("AdobeReaderc.png", 90):
        type(Key.ESC)
        waitVanish("AdobeReaderc.png", 30)
    wait(Pattern("Welcometothe-1.png").similar(0.91), 240)
    type("n", KeyModifier.ALT)
    wait(Pattern("LicenseAgree.png").similar(0.77), 240)
    type("a")
    wait(1)
    type("n", KeyModifier.ALT)
    waitVanish(Pattern("LicenseAgree.png").similar(0.77))
    type("n", KeyModifier.ALT)
    waitVanish(Pattern("Verification-3.png").similar(0.89))
    wait(Pattern("DestinationF-1.png").similar(0.91), 30)
    type("r", KeyModifier.ALT)
    wait(Pattern("Pleaseselect.png").similar(0.84), 240)
    type("p", KeyModifier.ALT)
    paste(r'c:\tssmoketest\\' + Settings.Version)
    type(Key.ENTER)
    waitVanish(Pattern("Pleaseselect.png").similar(0.84))
    type("n", KeyModifier.ALT)
    wait(Pattern("Pleaseselect-1.png").similar(0.81), 90)
    type("n", KeyModifier.ALT)
    wait(Pattern("ReadytoInsta.png").similar(0.92), 90)
    type("i", KeyModifier.ALT)
    if exists("Beforecontin.png"):
        type(Key.ENTER)
    wait(Pattern("Selecttheloc.png").similar(0.92), 900)
    type("n", KeyModifier.ALT)
    wait(Pattern("SetupComplet.png").similar(0.92), 120)
    type("d", KeyModifier.ALT)
    wait(.5)
    type("r", KeyModifier.ALT)
    wait(.5)
    type("u", KeyModifier.ALT)
    wait(.5)
    type("f", KeyModifier.ALT)
    waitVanish(Pattern("Pleaseselect-5.png").similar(0.89) or Pattern("Pleaseselect-11.png").similar(0.97))
        #section below is to close all apps opened during installation
    Settings.tssetup.close()

#----------------------------------------------------------------------------------------------------------#

