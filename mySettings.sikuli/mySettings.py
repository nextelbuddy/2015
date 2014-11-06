from sikuli import*


#This is my main function for anything I want to use as global variables. Make sure to
#always import this script into your functions if you want to call anything in it.
import os
import javax.swing.JOptionPane as JOP


#--------------------------------------------------------------------------------------

#Constants
# Use this path when you are on a network machine "\\gaqtsbuild01\TSStorage"
# Use this path when you are on a VM r"\\tsclient\p"
cBuildMachine = r"\\gaqtsbuild01\TSStorage"
cArchiveMachine = r"\\tsarchive"




#--------------------------------------------------------------------------------------
#Variables
vMinor = 0
vSR = 1
vBuild = 0

Settings.vInstallpath = ""
Settings.vUtilityPath = ""


#--------------------------------------------------------------------------------------
#This is an array to choose if this is a Alpha/Beta install version or Standard install version
Settings.tInstallPhaseE = [ "ALPHA/BETA", "Standard"]

Settings.InstallPhase = JOP.showInputDialog(None,
        "Which phase of the installation do you want?",
        "Phase",
        JOP.QUESTION_MESSAGE,
        None,
        Settings.tInstallPhaseE,
        Settings.tInstallPhaseE[0])


#--------------------------------------------------------------------------------------
#This is an array to choose if this is a single file install version of full install version
Settings.tInstallTypesE = [ "CD Image", "Single File Install"]

Settings.InstallType = JOP.showInputDialog(None,
        "What type of installation do you want?",
        "Installation",
        JOP.QUESTION_MESSAGE,
        None,
        Settings.tInstallTypesE,
        Settings.tInstallTypesE[0])


#--------------------------------------------------------------------------------------
# Array for Combo box to choose your year
tInstallYearE = [ "2015", "2014", "2013", "2012", "2011"]


Settings.Version = JOP.showInputDialog(None,
        "What version of Timeslips?",
        "Version",
        JOP.QUESTION_MESSAGE,
        None,
        tInstallYearE,
        tInstallYearE[0])

#--------------------------------------------------------------------------------------
# Serial number range will be different for each version
if Settings.Version == "2015":
    Settings.vMajor = 23
    defserial = '23300000'
elif Settings.Version == "2014":
    Settings.vMajor = 22
    defserial = '13613732'
elif Settings.Version == "2013":
    Settings.vMajor = 21
    defserial = '13800000'    
elif Settings.Version == "2012":
    Settings.vMajor = 20
    defserial = '13800000'
elif Settings.Version == "2011":
    Settings.vMajor = 19 
    defserial = '13700000'

Settings.tsSerial = defserial
#--------------------------------------------------------------------------------------
#Search build machine for latest build
#Requires Settings.Major to be setup
for vI in reversed(range(3)):
    for vJ in reversed(range(300)):            
        vBuildNumber = str(Settings.vMajor) + "." + str(vMinor) + "." + str(vI) + "." + str(vJ)
        vFilePath = os.path.join(cBuildMachine, "Builds", Settings.Version, "build " + vBuildNumber, "setup.exe")        
        #popup(vFilePath)
        if os.path.isfile(vFilePath):
            Settings.vSR = vI
            Settings.vBuild = vJ
            Settings.vInstallpath = vFilePath
            Settings.vUtilityPath = os.path.join(cBuildMachine, "Builds", Settings.Version, "utilities", "tscodes.exe")                                                
            break
    if os.path.isfile(vFilePath):
        break

#--------------------------------------------------------------------------------------
#Defined Applications to call to open and close in script 
#Requires Settings.Installpath and Settings.UtilityPath
Settings.tscode = App(Settings.vUtilityPath)
Settings.tssetup = App(Settings.vInstallpath)
Settings.single_file_setup = App(os.path.join(cBuildMachine,"Builds", Settings.Version, "Single File Install", "SageTimeslips" + Settings.Version + ".exe"))
                            

def ts_settings_archive():
        #Defined Applications to call to open and close in script
    Settings.tscode = App(os.path.join(cArchiveMachine, "Storage", "Timeslips", "Installations", Settings.tsVersion, "utilities", "TSCodes.exe"))
    Settings.tssetup = App(os.path.join(cArchiveMachine, "Storage", "Timeslips", "Installations", Settings.tsVersion, Settings.tsBuild, "setup.exe"))   





    