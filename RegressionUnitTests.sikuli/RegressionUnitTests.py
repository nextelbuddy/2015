from sikuli import*
import logging
import os
import subprocess
reload(logging)
import datetime
import DBChecks
import TABFunction
import shutil
import Alerts

SCR0 = Screen(0)
SCR1 = Screen(1)
startTime = datetime.datetime.now()


#---------------------This is a Unit/Module to contain all of our Regression tests.
#---------------------This module can be run alongside the smoketest or by itself.

