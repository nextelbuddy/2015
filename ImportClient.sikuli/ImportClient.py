from sikuli import *
import logging
import mySettings
import os




tsimport = App(os.path.join(r"C:\tssmoketest", Settings.Version, "tsimport.exe"))


# - - - - - - - - - - - - - - - - - - - - - - - - - #
def import_client():
# - - - - - - - - - - - - - - - - - - - - - - - - - #
    logging.debug(' ')
    logging.debug('Import_Clients')
# start tsimport
    logging.debug('- start TSImport')
    tsimport.open()
    wait(Pattern("EileIemplate.png").similar(0.86), 160)
    keyDown(Key.ALT)
    keyDown(Key.SPACE)
    type('x')
    keyUp(Key.ALT)
    keyUp(Key.SPACE)
    logging.debug('- set up client template')
    time.sleep(1)
    type("f",KEY_ALT)
    type("n")
    time.sleep(1)
    type("co")
    type('n', KeyModifier.ALT)
    time.sleep(1)
    type("cl")
    type('f', KeyModifier.ALT)

    #choose source
    wait("PutdataintoZ.png")
    time.sleep(1)
    type("g",KEY_ALT)
    time.sleep(1)
    paste(os.path.join(r'C:\Sikuli Scripts vm x', '2015', 'Data', 'SmokeTestClientExport.csv'))

    # choose fields
    doubleClick("Nickname1.png")
    doubleClick("9Nickname2.png")
    doubleClick("9FullName.png")    
    doubleClick("9AddressLine.png")

    # city
    type("c")
    time.sleep(1)    
    type(Key.ENTER)
    doubleClick("9State.png")
    doubleClick("ZIPCode-1.png")

    # move to address 1
    type("a")
    time.sleep(1)
    doubleClick("9AddressLine-1.png")
    doubleClick("PhoneNumberI.png")

    # in reference to
    type("i")
    time.sleep(1)    
    type(Key.ENTER)
    doubleClick("9Notes.png")

    # rate 01
    doubleClick("9RateLevelU1.png")
    time.sleep(1)        

# omit 1st record
    click("Limitrecords.png")
    type(Key.TAB)
    time.sleep(1)    
    type("2")

# import data
    logging.debug('- import data')
    click("1352092489137.png")
    wait("1352092526314.png", 30)
    click("1352092535682.png")
     
# verify data
    wait("EndOfImport.png",FOREVER)
    if exists(Pattern("FailedImport.png").similar(0.95)):
        logging.debug('- import complete - no failed names')
    else:
        logging.debug('- import complete - some failed names')

# close tsimport
    logging.debug('- close TSImport')
    tsimport.close()       


#import_clients()