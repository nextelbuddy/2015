from sikuli import*

import os

def Log_Result(pResult, pText):
    if pResult == True:
        print('PASS: ' + pText)
    else:
         print('FAIL: ' + pText)
    