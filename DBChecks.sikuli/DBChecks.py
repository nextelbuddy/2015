from sikuli import*

import os



# - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkFor_PEP():
# - - - - - - - - - - - - - - - - - - - - - - - - - #    
    if exists(Pattern("ProductEnhan-1.png").similar(0.87)):
        wait(1)
        type(Key.ENTER)        

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkFor_SPS():
# - - - - - - - - - - - - - - - - - - - - - - - - - #    
    if exists(Pattern("SaqePavmentS.png").similar(0.83)):
        wait(1)
        type(Key.ENTER)        

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkFor_BillingDate():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
   
    if exists(Pattern("isisthedatet.png").similar(0.87)):
        wait(1)
        type(Key.ENTER)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkFor_Preferror():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
   
    if exists(Pattern("hedefaultpre.png").similar(0.88)):
        wait(1)
        type(Key.ENTER)

# - - - - - - - - - - - - - - - - - - - - - - - - - #
def checkFor_BkuPopup():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
   
    if exists(Pattern("Thisdatabase.png").similar(0.89)):
        type(Key.TAB)
        type(Key.ENTER)
        onAppear("Youshouldnot.png", type('n', KeyModifier.ALT))

