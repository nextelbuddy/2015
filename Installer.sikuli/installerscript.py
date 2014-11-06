#this is a script to install any build of timeslips from the network build machine

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
import logging
import os





#we will structure this script so that we always browse out to the build path for the
#current year. 
#Make sure in pop up prompts that you input the proper year as a 4 digit number, build as "Build XX.X.X.XX
#and the proper serial # for that version

tsVersion = input("Enter your version ie.. 2013, 2014 etc:")
tsBuild = input("Enter your build ie..Build 22.0.0.76:")
tsSerial = input("Enter your serial# ie..13800000:")

def ts_installer():
        #section below browses out to network path on build machine and starts coe generator as well as launches the build you specify
    type("r", KeyModifier.WIN)
    wait(Pattern("Typethenameo.png").similar(0.86), 60)
    paste(r'\\gaqtsbuild01\TSStorage\Builds\\' +tsVersion)
    wait(1)
    type(Key.ENTER)
    wait(Pattern("qaqtsbuid01T.png").similar(0.94), 60)
    type("utilities")
    wait(Pattern("Utilities.png").similar(0.96), 60)
    type(Key.ENTER)
    wait(Pattern("Utilities-2.png").similar(0.96), 60)
    type("tscodes")
    wait(Pattern("IQTSCOdesexe.png").similar(0.97), 60)
    type(Key.ENTER)
    wait(Pattern("SageTimeslip-1.png").similar(0.84), 120)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.SPACE)
    wait(Pattern("Createaprodu.png").similar(0.89))
    type(Key.SPACE, KeyModifier.ALT)
    type("n")
    waitVanish(Pattern("SageTimeslip-1.png").similar(0.84))
    wait(1)
    type(Key.BACKSPACE)
    wait(1.5)
    type(tsBuild)
    wait(2)
    type(Key.ENTER)
    wait(Pattern("Setupexe.png").similar(0.82))
    type("setup")
    wait(Pattern("3Setupexe-1.png").similar(0.89))
    type(Key.ENTER)
        #installer launches here
    wait(Pattern("SageTlmeslip.png").similar(0.84), 120)
    click(Pattern("InstallSageT-1.png").similar(0.81), 120)
    wait(Pattern("Welcomelnthe.png").similar(0.84), 120)
    type("n", KeyModifier.ALT)
    wait(Pattern("LicenseAgree.png").similar(0.77), 120)
    type("a")
    type("n", KeyModifier.ALT)
    type("n", KeyModifier.ALT)
    type("n", KeyModifier.ALT)
    type("r", KeyModifier.ALT)
    wait(Pattern("Pleaseselect.png").similar(0.84), 120)
    type("p", KeyModifier.ALT)
    paste(r'c:\tssmoketest\\' +tsVersion)
    type(Key.ENTER)
    waitVanish(Pattern("Pleaseselect.png").similar(0.84))
    type("n", KeyModifier.ALT)
    wait(Pattern("Pleaseselect-1.png").similar(0.81), 60)
    type("n", KeyModifier.ALT)
    wait(.5)
    type("s", KeyModifier.ALT)
    wait(.5)
    paste(tsSerial)
    wait(.5)
    type("n", KeyModifier.ALT)
    type("i", KeyModifier.ALT)
    if exists("Beforecontin.png"):
        type(Key.ENTER)
    waitVanish(Pattern("Thesetupprog.png").similar(0.84))
    wait(Pattern("Pleaseselect-2.png").similar(0.98), 300)
    type("n", KeyModifier.ALT)
    wait(Pattern("Pleaseselect-3.png").similar(0.83), 60)
    type("d", KeyModifier.ALT)
    wait(.5)
    type("r", KeyModifier.ALT)
    wait(.5)
    type("u", KeyModifier.ALT)
    wait(.5)
    type("f", KeyModifier.ALT)
    waitVanish(Pattern("Pleaseselect-3.png").similar(0.83))
        #section below is to close all items opened during installation
    keyDown(Key.CTRL)
    keyDown(Key.SHIFT)
    type(Key.ESC)
    keyUp(Key.CTRL)
    keyUp(Key.SHIFT)
    wait(Pattern("ADPIICBUOTTS.png").similar(0.77), 120)
    rightClick(Pattern("Build.png").similar(0.96))
    onAppear(Pattern("SwitchToBrin.png").similar(0.79), click(Pattern("EndTask.png").similar(0.86)))
    waitVanish(Pattern("Build.png").similar(0.96), 60)
    rightClick(Pattern("L9sew.png").similar(0.86))
    onAppear(Pattern("SwitchToBrin-1.png").similar(0.85), click(Pattern("EndTask-1.png").similar(0.83)))
    waitVanish(Pattern("L9sew.png").similar(0.86), 60)
    rightClick(Pattern("Tscodes.png").similar(0.83))
    onAppear(Pattern("SwitchToBrin-2.png").similar(0.86), click(Pattern("EndTask-1.png").similar(0.83)))
    onVanish(Pattern("Tscodes-1.png").similar(0.83), type(Key.F4, KeyModifier.ALT))
    
    
ts_installer()





