from sikuli import*

def open_ts():
    App.open("C:\TSSHARE\Timeslips 2014\Timeslip.exe")
    wait("isisthedatet-1.png")
    type(Key.ENTER)
    wait("TimesipsToda-1.png")
    type("f", KeyModifier.ALT)
    wait(1)
    type("o")
    wait(2)
    find("minps.png")
    type("a", KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste("1348684767545.png", 'c:\\tsshare\\timeslips 2014\Original System DB 2013')
    click("Open.png")
    doubleClick(Pattern("DATA01.png").similar(0.84))
    doubleClick(Pattern("MAINDB.png").similar(0.81))
    waitVanish("TimesipsToda.png")
    click("LGettingStar-1.png")
    wheel(WHEEL_DOWN, 7)
    click(Pattern("SRobertson-2.png").similar(0.97))
    click("Finish.png")
    waitVanish("SelectTimeke.png")
    wait("TimesipsToda-2.png")












