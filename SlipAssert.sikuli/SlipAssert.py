from sikuli import*



def slip_assert():    
    type("s", KeyModifier.ALT)
    type("s")
    wait(1)
    type(Key.TAB)
    type("client")
    wait(.5)
    type(Key.TAB)
    type("sikuli")    
    type(Key.ENTER)
    wait("ActivityRefe.png")
    Region(314,327,664,433)
    #with Region(find("ChargesHours.png")):
    #Pattern("Charges28519.png").similar(0.96) #original value assertion image excluding extended functionality method
    if not exists(Pattern("ChargesHours-1.png").similar(0.96)): exit(1) #if = 1 means failed:
    else: exit(0) #this means passed::
    
#slip_assert()    