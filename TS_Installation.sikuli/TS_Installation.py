from sikuli import*
import mySettings
import Installer
import logging
import os
import subprocess
import shutil
#import Alpha_Beta
import logging
reload(logging)
import datetime
SCR0 = Screen(0)
SCR1 = Screen(1)
startTime = datetime.datetime.now()



# setup logging and folder paths
if not os.path.exists(r'C:\tssmoketest\Logs'):
    os.makedirs(r'C:\tssmoketest\Logs')

if not os.path.exists(r'C:\tssmoketest\Reports'):
    os.makedirs(r'C:\tssmoketest\Reports')

if not os.path.exists(r'C:\tssmoketest\Backups'):
    os.makedirs(r'C:\tssmoketest\Backups')

#--------------------------------------------------------#
  
logging.basicConfig(filename=os.path.join(r'C:\tssmoketest', 'Logs', startTime.strftime('InstallerTestLog %Y_%m_%d %H_%M_%S.log')), level=logging.DEBUG, format='%(message)s', filemode='w')
#logging.basicConfig(filename=os.path.join(r"C:\tssmoketest", 'Logs', "SmokeTestLog.log"), level=logging.DEBUG, format='%(message)s', filemode='w')
# Level = DEBUG, INFO, WARNING, ERROR, CRITICAL

#--------------------------------------------------------#


# stamp start time
logging.debug(' ')
logging.debug('- - - - - - - - - - - - - - -')
logging.debug(startTime.strftime("Started at: %Y-%m-%d %H:%M:%S"))
logging.debug('- - - - - - - - - - - - - - -')

#--------------------------------------------------------#
logging.debug('- - - - - - - - - - - - - - -')
    #first part of smoke test is deleting prior installation
logging.debug(' ')
logging.debug('Timeslips_Removal_Begin')
if os.path.exists(os.path.join(r'C:\tssmoketest', Settings.Version)):
    shutil.rmtree(os.path.join(r'C:\tssmoketest', Settings.Version))
logging.debug(' ')
logging.debug('Timeslips_Removal_End')
#--------------------------------------------------------#
logging.debug('- - - - - - - - - - - - - - -')
    #first part of smoke test is installation by calling the installer function
logging.debug(' ')
logging.debug('Timeslips_installer_Begin')

if Settings.InstallPhase == Settings.tInstallPhaseE[0]:
    Installer.alpha_beta_installer()
elif Settings.InstallType == Settings.tInstallTypesE[1]:
    Installer.single_installer()
elif Settings.InstallType == Settings.tInstallTypesE[0]:
    Installer.cd_installer()



#--------------------------------------------------------#
logging.debug('- - - - - - - - - - - - - - -')
    #End of installation
logging.debug(' ')
logging.debug('Timeslips_installer_End')
#----------------------------------------#
endTime = datetime.datetime.now()
logging.debug(' ')
logging.debug('- - - - - - - - - - - - - - -')
logging.debug(endTime.strftime("Stopped at: %Y-%m-%d %H:%M:%S"))
logging.debug('- - - - - - - - - - - - - - -')

elapsedTime = endTime - startTime
logging.debug("Elapsed:    %s" %elapsedTime)

exit()