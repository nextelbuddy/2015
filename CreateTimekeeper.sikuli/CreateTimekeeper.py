from sikuli import*
import TABFunction

def create_timekeeper(id):
    type("n", KeyModifier.ALT)
    type("n")
    type("n", KeyModifier.CTRL)
    wait("iziClassific.png")
    paste ("Sikuli Test Timekeeper " + str(id))
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)
    paste("Sikuli Test  Full Name")
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    paste("example@example.com")
    type(Key.TAB)
    type(Key.TAB)
    paste("100")
    type(Key.TAB)
    paste("200")
    type(Key.TAB)
    paste("300")
    type(Key.TAB)
    paste("400")
    type(Key.TAB)
    paste("500")
    type(Key.TAB)
    paste("600")
    type(Key.TAB)
    paste("700")
    type(Key.TAB)
    paste("800")
    type(Key.TAB)
    paste("900")
    type(Key.TAB)
    paste("1000")
    type(Key.TAB)
    paste("1100")
    type(Key.TAB)
    paste("1200")
    type(Key.TAB)
    paste("1300")
    type(Key.TAB)
    paste("1400")
    type(Key.TAB)
    paste("1500")
    type(Key.TAB)
    paste("1600")
    type(Key.TAB)
    paste("1700")
    type(Key.TAB)
    paste("1800")
    type(Key.TAB)
    paste("1900")
    type(Key.TAB)
    paste("2000")
    wait(1)
    type("s", KeyModifier.CTRL)
    """
    if exists("Whenyousavea.png"):
        type("o", KeyModifier.ALT)
        if exists("SetupResulSe.png"):
            type(Key.F4, KeyModifier.CTRL)
        else:
            wait("Noconflictsw.png", 60)
            type(Key.ENTER)
            type(Key.F4, KeyModifier.CTRL)"""
    if exists("Whenyousavea-1.png"):
        type('o')
        waitVanish("Whenyousavea-1.png")
        if exists("Noconflictsw-1.png"):
            type(Key.ENTER)
        if exists("ScopeOptions.png"):
            type(Key.F4, KeyModifier.CTRL)           
            waitVanish("ScopeOptions.png")
    wait(1)
    type(Key.F4, KeyModifier.CTRL)   
    wait(1)
    type(Key.F4, KeyModifier.CTRL) 
    
    
    
    
    


#create_timekeeper(id)

#for x in range(1, 2):
    #create_timekeeper(x)

