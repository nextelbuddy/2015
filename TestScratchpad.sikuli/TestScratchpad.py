from sikuli import*
import CreateClient
import DBSetup
import CreateTask
import CreateTimekeeper
SCR0 = Screen(0)
SCR1 = Screen(1)
import logging
reload(logging)
import datetime
import os
import subprocess
import TABFunction
import shutil
import javax.swing.JOptionPane as JOP
startTime = datetime.datetime.now()



"""
browsers = [App(os.path.join(r'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')), App(os.path.join(r'C:\Program Files (x86)\Mozilla Firefox\firefox.exe')), App(os.path.join(r'C:\Program Files (x86)\Internet Explorer\iexplore.exe')), App(os.path.join(r'C:\Program Files (x86)\Safari\Safari.exe'))]
selected = None
while not selected:
    prompt = "select a browser by entering Its number\n1 - chrome\n2 - firefox\n3 - ie\n4 - safari"
    selected = input(prompt, "1")
    try:
        selected = int(selected)
    except:
        selected = None
        continue
    if (selected < 1 or selected > 4): continue
app = browsers[selected -1]
"""


tInstallPhaseE = [ "ALPHA/BETA" ,"Standard"]

def alpha_combo():
    InstallPhase = JOP.showInputDialog(None,
            "Which phase of the installation do you want?",
            "Phase",
            JOP.QUESTION_MESSAGE,
            None,
            Settings.tInstallPhaseE,
            Settings.tInstallPhaseE[0])


#alpha_combo()