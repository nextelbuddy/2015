from sikuli import*





#--------------------------------------------------------------------------------------
#This is an array to choose if this is a Alpha/Beta install version or Standard install version
Settings.tInstallPhaseE = [ "ALPHA/BETA" ,"Standard"]

def alpha_combo():
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

def install_type_combo():
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

def version_combo():
    Settings.Version = JOP.showInputDialog(None,
            "What version of Timeslips?",
            "Version",
            JOP.QUESTION_MESSAGE,
            None,
            tInstallYearE,
            tInstallYearE[0])