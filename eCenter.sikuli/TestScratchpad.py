def ecenter_login():
    App.open("C:\Users\srobertson\AppData\Local\Google\Chrome\Application\chrome.exe")
    wait("NewTabC-1.png")
    paste("http://www.sagetimeslipsecenter.com")
    type(Key.ENTER)
    wait("SageTimeslip-2.png")
    find("jKnox1Userna.png")
    type("a", KeyModifier.CTRL)
    type(Key.BACKSPACE)
    paste("jknox1")
    type(Key.TAB)
    paste("password")
    type(Key.ENTER)
    
   
def ecenter_createslip():
    click("CreateNewTim.png")
    click("ESelectOneCl.png")
    type("client")
    type(Key.ENTER)
    type(Key.TAB)
    type("advise")
    type(Key.ENTER)
    type(Key.TAB)
    type(Key.TAB)
    paste("Testing Extra")
    type(Key.TAB)
    type(Key.END)
    paste(" Testing description")
    type(Key.TAB)
    paste("10/1/2012")
    click("1349122994860.png")
    click("1349125478290.png")
    click("00000TimeSpe-2.png")
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    type("01:10:30")
    click("1349123612274.png")
    click("ETSDefaultRa.png")
    type("client")
    type(Key.ENTER)
    click("E110000RateL.png")
    type("11")
    type(Key.ENTER)
    click("SpellCheck-1.png")
    click("1349123612274.png")
    click("1349123847876.png")
    
  
    


ecenter_createslip()

    
    