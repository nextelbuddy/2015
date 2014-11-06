from sikuli import*

def create_reference():
    type("n", KeyModifier.ALT)
    type("r")
    type("sikuli test client 1")
    type(Key.ENTER)
    type("n", KeyModifier.CTRL)
    wait("ClientNickna.png", 20)
    paste("Sikuli Test Reference")
    wait(Pattern("SikuliTestRe.png").similar(0.94))
    type(Key.ENTER)
    wait(1)
    keyDown(Key.CTRL)
    type(Key.F4)
    keyUp(Key.CTRL)
    wait(1)
    type("w", KeyModifier.CTRL) 



