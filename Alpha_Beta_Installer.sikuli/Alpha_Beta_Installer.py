from sikuli import*

import os
import javax.swing.JOptionPane as JOP



#--------------------------------------------------------------------------------------
#This is an array to choose if this is a Alpha/Beta install version or Standard install version
Phases.tInstallPhaseE = [ "ALPHA/BETA" ,"Standard"]

def alpha_combo():
    Phases.InstallPhase = JOP.showInputDialog(None,
            "Which phase of the installation do you want?",
            "Phase",
            JOP.QUESTION_MESSAGE,
            None,
            Settings.tInstallPhaseE,
            Settings.tInstallPhaseE[0])


#This is a separate installer for when we are in alpha/beta phase of development. 
def alpha_beta_installer():
    #section below browses out to network path on build machine and starts the alpha/beta build you specify 
        #installer launches here
    Settings.tssetup.open()
    wait("SageTlmeslip-1.png", 240)
    click(Pattern("InstallSageT-1.png").similar(0.81), 240)
    if exists("Doyouwanttor.png", 90):
        type('n', KeyModifier.ALT)
    if exists("AdobeReaderc.png", 90):
        type(Key.ESC)
        waitVanish("AdobeReaderc.png", 30)
    wait(Pattern("Welcometothe.png").similar(0.83), 240)
    type("n", KeyModifier.ALT)
    wait(Pattern("LicenseAgree.png").similar(0.77), 240)
    type("a")
    wait(1)
    type("n", KeyModifier.ALT)
    waitVanish(Pattern("LicenseAgree.png").similar(0.77))
    type("n", KeyModifier.ALT)
    waitVanish(Pattern("Verification-2.png").similar(0.91))
    type("n", KeyModifier.ALT)
    wait(1)
    type("r", KeyModifier.ALT)
    wait(Pattern("Pleaseselect.png").similar(0.84), 240)
    type("p", KeyModifier.ALT)
    paste(r'c:\tssmoketest\\' + Settings.Version)
    type(Key.ENTER)
    waitVanish(Pattern("Pleaseselect.png").similar(0.84))
    type("n", KeyModifier.ALT)
    wait(Pattern("Pleaseselect-1.png").similar(0.81), 90)
    type("n", KeyModifier.ALT)
    wait("Thesetupprog-1.png", 30)
    type("i", KeyModifier.ALT)
    if exists("Beforecontin.png"):
        type(Key.ENTER)
    wait(Pattern("Pleaseselect-4.png").similar(0.94), 900)
    type("n", KeyModifier.ALT)
    wait(Pattern("Pleaseselect-5.png").similar(0.89), 120)
    type("d", KeyModifier.ALT)
    wait(.5)
    type("r", KeyModifier.ALT)
    wait(.5)
    type("u", KeyModifier.ALT)
    wait(.5)
    type("f", KeyModifier.ALT)
    waitVanish(Pattern("Pleaseselect-5.png").similar(0.89))
        #section below is to close all apps opened during installation
    Settings.tssetup.close()