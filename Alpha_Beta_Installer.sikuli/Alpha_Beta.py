from sikuli import*

import os
import javax.swing.JOptionPane as JOP



#--------------------------------------------------------------------------------------
#This is an array to choose if this is a Alpha/Beta install version or Standard install version
Phases.tInstallPhaseE = [ "ALPHA/BETA" ,"Standard"]

Phases.InstallPhase = JOP.showInputDialog(None,
        "Which phase of the installation do you want?",
        "Phase",
        JOP.QUESTION_MESSAGE,
        None,
        Settings.tInstallPhaseE,
        Settings.tInstallPhaseE[0])