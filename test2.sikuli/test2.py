import os
import subprocess

dir = os.path.join('c:', os.sep, 'tssmoketest')
os.popen('start explorer "%s" ' % dir)