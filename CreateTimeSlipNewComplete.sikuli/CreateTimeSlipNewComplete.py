from sikuli import*


    #always remember if you are calling a method in a script then you need to import it 
    #into that script, even if you are calling a master method first. In this case we are 
    #calling SlipDescription with in the create_Timeslip_New() method so we MUST import 
    #SlipDescription in this script.
    
import SlipDescription
#import RestorePrefs
#import ClearSlips

#slip entry method below

    
#RestorePrefs.restore_prefs()
#ClearSlips.clear_slips()
def create_timeslip_New():
    wait(1)
    click("1349207959804.png")
    wait(.5)
    type("t")
    type(Key.TAB)
    type("s. robertson")
    type(Key.ENTER)
    type(Key.TAB)
    type("sikuli test task")
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
    type(Key.ENTER)
    """
    type(Key.TAB)
    paste("00:30:00")
    type(Key.TAB)
        #change the below value to test assertion, correct value should be 1:00:00
    paste("1:00:00")
    type(Key.TAB)
        #Next line starts Timer
    type(Key.SPACE)
    wait(2.05)
    type(Key.SPACE)
    type(Key.TAB)
    type(Key.DOWN)
    wait(.1)
    type(Key.DOWN)
    wait(.1)
    type(Key.DOWN)
    wait(.1)
    type(Key.UP)
    wait(.1)
    type(Key.UP)
    wait(.1)
    type(Key.UP)
    type(Key.TAB)
        #Next line enables and disables Hold and recurring
    type(Key.SPACE)
    type(Key.SPACE)
    wait(.5)
    type(Key.TAB)
    type(Key.SPACE)
    type(Key.SPACE)
    wait(.5)  
        #next section is setting rate source and levels
    type(Key.TAB)
    type(Key.UP)
    type(Key.TAB)
    type(Key.DOWN)
    type(Key.TAB)
    paste("225.00")
    type(Key.TAB)
        #Next section begins Markup and Attachments
    click("MahAditstmen-1.png")
    click("Attadrnents.png")
    type(Key.TAB)
    paste("5.00")
    type(Key.TAB)
    paste("2.00")
    type(Key.TAB)
    paste("0:15:59")
    click("01559-1.png")
    click("1Starttime.png")
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    wait(.5)
    type("s", KeyModifier.CTRL)
    wait(.5)
    click("MahAditstmen-1.png")
    click("Attadrnents.png")
    wait(1)
        #assert exists(Pattern("22513.png").similar(0.95))
    keyDown(Key.CTRL)
    type(Key.F4)
    keyUp(Key.CTRL)



#create_timeslip_New()