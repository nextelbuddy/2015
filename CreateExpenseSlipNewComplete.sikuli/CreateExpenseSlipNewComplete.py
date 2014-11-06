from sikuli import*

    #always remember if you are calling a method in a script then you need to import it 
    #into that script, even if you are calling a master method first. In this case we are 
    #calling SlipDescription with in the create_Timeslip_New() method so we MUST import 
    #SlipDescription in this script.

import SlipDescription


#slip entry method below

    
#RestorePrefs.restore_prefs()
#ClearSlips.clear_slips()


def create_expslip_New():
    wait(1)
    click("1349207959804.png")
    wait(.5)
    type("e")
    type(Key.TAB)
    type("s. robertson")
    type(Key.ENTER)
    type(Key.TAB)
    type("sikuli test expense")
    type(Key.ENTER)
    type(Key.TAB)
    type("sikuli test client")
    type(Key.ENTER)
    type(Key.TAB)
    type("sikuli test reference")
    type(Key.ENTER)
    type(Key.TAB)
    type("sikuli extra")
    type(Key.TAB)
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    SlipDescription.slip_description_shortcuts()
    #Next section begins date
    type(Key.TAB)
    type("6/23/2004")
    type(Key.TAB)
    type("6/24/2004")
    """
    type("c")
    click("1349292786849.png")
    click("1349292832471.png")
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)"""
    #next section begins Quantity Price
    type(Key.TAB)
    paste("3")
    type(Key.TAB)
    #type("4") alternative way to input price level
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.TAB)
    type(Key.TAB)
    #assert exists("1351707005727.png") #for now not working due to defect enable when type search is fixed
        #Next line starts billing status
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.DOWN)
    type(Key.UP)
    type(Key.UP)
    type(Key.UP)
    type(Key.TAB)
        #Next line disables enables Hold
    type(Key.SPACE)
    type(Key.SPACE)
    wait(.5)
        #next line disables enables recurring
    type(Key.TAB)
    type(Key.SPACE)
    type(Key.SPACE)
    wait(.5)      
    #Next section begins Markup and Attachments
    click("Makummdkdius.png")
    click("Attadrnents-1.png")
    type(Key.TAB)
    paste("5.00")
    type(Key.TAB)
    paste("2.00")
    wait(.5)
    type("s", KeyModifier.CTRL)
    wait(.5)
    click("Makummdkdius.png")
    click("Attadrnents-2.png")
    wait(.5)
    keyDown(Key.CTRL)
    type(Key.F4)
    keyUp(Key.CTRL)