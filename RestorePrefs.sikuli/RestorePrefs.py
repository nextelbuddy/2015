from sikuli import*

def restore_prefs():
    type("p", KeyModifier.ALT)
    wait(.2)
    type("p")
    wait(Pattern("IntcrfaccSta.png").similar(0.94), 30)
    type(Key.F6)
    type(Key.F6)
    type(Key.F6)
    wait(Pattern("InterfaceApp.png").similar(0.93), 30)
    type("a")
    wait(Pattern("Doyouwanttos.png").similar(0.96), 30)
    type("y")
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    type(Key.ENTER)