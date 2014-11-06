from sikuli import*
import TABFunction


def create_calendar_entry():
    type("l", KeyModifier.ALT)
    type("n")
    wait(Pattern("NewMeeting.png").similar(0.97))
    paste("Sikuli Test Calendar Entry")
    wait(.5)
    for x in range(1, 10):
        TABFunction.tab(x)
    type(Key.SPACE)
    type(Key.TAB)
    type(Key.RIGHT)
    type(Key.RIGHT)
    wait(.5)
    type(Key.TAB)
    type("Sikuli Test Client")
    type(Key.TAB)
    type("Sikuli Test Reference")
    type(Key.TAB)
    type("Sikuli Test Task")
    wait(.5)
    keyDown(Key.SHIFT)
    for x in range(1, 4):
        TABFunction.tab(x)
    keyUp(Key.SHIFT)
    type(Key.LEFT)
    type(Key.LEFT)
    for x in range(1, 4):
        TABFunction.tab(x)
    type("none")
    for x in range(1, 3):
        TABFunction.tab(x)
    type(Key.ENTER)
    wait(Pattern("ThisnewMeeti.png").similar(0.96))
    type("y")
    wait(Pattern("SlipEntry.png").similar(0.92))
    type("s", KeyModifier.CTRL)
    wait(.5)
    assert exists(Pattern("1355182489566.png").similar(0.96))
    wait(.5)
    click(Pattern("lg.png").similar(0.95))
    wait(Pattern("Meeting.png").similar(0.97))
    assert exists(Pattern("Meeting.png").similar(0.97))
    wait(.5)
    type(Key.F4, KeyModifier.CTRL)

#create_calendar_entry()