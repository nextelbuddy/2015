from sikuli import*
import Abbreviations



def db_setup():
    type("p", KeyModifier.ALT)
    type("g")
    wait(Pattern("FirmAddrcssI.png").similar(0.96), 30)
    keyDown(Key.SHIFT)
    type(Key.F6 + Key.F6 + Key.F6 + Key.F6 + Key.F6 + Key.F6)
    keyUp(Key.SHIFT)
    if exists(Pattern("IZlheckforCh.png").similar(0.98)):
        type(Key.ENTER)
    else:
        type(Key.SPACE)
        type(Key.DOWN + Key.SPACE)
        wait(1)
        type(Key.ENTER)
    wait(1)
    Abbreviations.abbreviations()


#db_setup()