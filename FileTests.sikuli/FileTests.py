from sikuli import*

import Globals
import os

def search_build():
    for vI in reversed(range(3)):
        for vJ in reversed(range(300)):            
            vBuildNumber = str(Globals.vMajor) + "." + str(Globals.vMinor) + "." + str(vI) + "." + str(vJ)
            vFilePath = os.path.join(Globals.cBuildMachine, "TSStorage", "Builds", Globals.vVersion, "build " + vBuildNumber, "setup.exe")
            #popup(vFilePath)
            if os.path.isfile(vFilePath):
                Globals.vSR = vI
                Globals.vBuild = vJ
                Globals.vInstallpath = vFilePath
                Globals.vUtilityPath = os.path.join(Globals.cBuildMachine, "TSStorage", "Builds", Globals.vVersion, "utilities", "tscodes.exe")    
                break
        if os.path.isfile(vFilePath):
            break
   

#debug code below
#search_build()
#popup(Globals.vInstallpath)




