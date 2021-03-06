from sikuli import*

def slip_description_shortcuts():    
        #spell check current word
    paste("correct ")
    type(Key.F4)
    wait(.5)
    assert exists(Pattern("Spellcheckdi-5.png").similar(0.94))
    wait(.5)
        #spell check entire field
    type(Key.ENTER)
    type(Key.RIGHT)
    paste("icorrect ")
    wait(1)
    type(Key.SHIFT + Key.F4)
    #wait("Errortypespe.png")
    assert exists("correctcorre.png")
    wait(.5)
    type("c", KeyModifier.ALT)
    wait("Spellcheckis.png")
    type(Key.ENTER)
    type(Key.RIGHT)
        #grammar check entire field
    wait(.5)
    paste(" can not ")
    wait(1)
    keyDown(Key.SHIFT)
    type(Key.F5)
    keyUp(Key.SHIFT)
    wait("Errortextcor-2.png")
    assert exists(Pattern("1349814214706.png").similar(0.90))
    wait(.5)
    type("c", KeyModifier.ALT)
    type(Key.ENTER)
        #spelling and grammar settings
    keyDown(Key.SHIFT)
    type(Key.F8)
    keyUp(Key.SHIFT)
    wait("SpellingGram.png")
    wait(.5)
    assert exists("lnEractivech.png")
    type(Key.ENTER)
    wait(.5)
        #increase font details section
    keyDown(Key.CTRL)
    type("=")
    type("=")
    type("=")
    type("=")
    type("=")
    type("=")
    type("=")
    keyUp(Key.CTRL)
    assert exists(Pattern("correctincor.png").similar(0.98))
    wait(1)
        #decrease font details section
    keyDown(Key.CTRL)
    type("-")
    type("-")
    type("-")
    type("-")
    type("-")
    type("-")
    type("-")
    keyUp(Key.CTRL)
    assert exists(Pattern("correctrncor.png").similar(0.94))
    wait(.5)
        #shortcut for undo
    paste("Undo")
    assert exists(Pattern("Undo.png").similar(0.87))
    wait(.5)
    type("z", KeyModifier.CTRL)
    assert not exists(Pattern("Undo.png").similar(0.88))
    wait(.5)
        #shortcut for cut
    paste("CUT")
    assert exists("CUT-2.png")
    doubleClick("CUT-2.png")
    type("x", KeyModifier.CTRL)
    assert not exists(Pattern("CUT-2.png").similar(0.88))
    wait(.5)
        #shortcut for copy and paste
    paste("COPY ")
    assert exists(Pattern("COF.png").similar(0.85))
    wait(.5)
    doubleClick(Pattern("COF.png").similar(0.87))
    type("c", KeyModifier.CTRL)
    wait(.5)
    type(Key.RIGHT)
    wait(.5)
    type("v", KeyModifier.CTRL)
    assert exists(Pattern("COFCOF.png").similar(0.94))
    wait(.5)
        #shortcut for select all and clear
    type("a", KeyModifier.CTRL)
    wait(.5)
    type(Key.CTRL + Key.DELETE)
    wait(.5)
    assert not exists(Pattern("Correctincor-6.png").similar(0.94))
    wait(.5)    
        #uppercase shortcut
    paste("correct incorrect cannot")
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("u")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    assert exists(Pattern("CUHHECTINCUH.png").similar(0.94))
        #lower case shortcut
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("l")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    assert exists("correctrncor-1.png")
    wait(.5)
        #sentence case short
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("s")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    type("n", KeyModifier.ALT)
    wait(.5)
    assert exists(Pattern("CD.png").similar(0.94))
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("s")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    type("y", KeyModifier.ALT)
    wait(.5)
    assert exists(Pattern("1351621737372.png").similar(0.94))
    wait(.5)
        #proper case shortcut
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("p")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    type("n", KeyModifier.ALT)
    wait(.5)
    assert exists(Pattern("Correctincor-2.png").similar(0.94))
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("p")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    type("y", KeyModifier.ALT)
    wait(.5)
    assert exists(Pattern("CorrectIncor-3.png").similar(0.94))
        #shortcut word count
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("w")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait("WordsChaacEr.png")
    assert exists(Pattern("WordsChaacEr.png").similar(0.94))
    wait(.5)
    type(Key.ENTER)
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
        #shortcut PTI
    type(Key.SPACE)
    keyDown(Key.ALT)
    type(Key.INSERT)
    keyUp(Key.ALT)
    wait(1)
    type(Key.SPACE)
    keyDown(Key.ALT)
    type(Key.INSERT)
    keyUp(Key.ALT)
    assert exists(Pattern("1349967901043.png").similar(0.78))
    type(Key.BACKSPACE)
    type(Key.BACKSPACE)
    assert not exists(Pattern("1349967901043.png").similar(0.78))
    wait(.5)
        #shortcut abbreviations
    keyDown(Key.CTRL)
    type(Key.F7)
    keyUp(Key.CTRL)
    assert exists(Pattern("gllcwspecial.png").similar(0.94))
    wait(.5)
    type(Key.ESC)
    wait(.5)
        #clear out text box\
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
        #shortcut formatting
    paste("BOLD")
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("b", KeyModifier.CTRL)
    type(Key.RIGHT)
    assert exists(Pattern("BDLD.png").similar(0.94))
    wait(.5)
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("b", KeyModifier.CTRL)
    wait(.5)
    type("a", KeyModifier.CTRL)
    type(Key.CTRL + Key.DELETE)
    wait(.5)
    paste("ITALIC")
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("i", KeyModifier.CTRL)
    type(Key.RIGHT)
    assert exists(Pattern("MIKE-1.png").similar(0.88))
    wait(.5)
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("i", KeyModifier.CTRL)
    type("a", KeyModifier.CTRL)
    type(Key.CTRL + Key.DELETE)
    wait(.5)
    paste("UNDERLINE")
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("u", KeyModifier.CTRL)
    type(Key.RIGHT)
    assert exists(Pattern("UNDERLINE.png").similar(0.95))
    wait(.5)
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("u", KeyModifier.CTRL)
    type("a", KeyModifier.CTRL)
    type(Key.CTRL + Key.DELETE)
    wait(.5)
    paste("BOLD ITALICS UNDERLINED")
    wait(.5)
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("b", KeyModifier.CTRL)
    type("i", KeyModifier.CTRL)
    type("u", KeyModifier.CTRL)
    type(Key.RIGHT)
    wait(.5)
    assert exists(Pattern("REEDffLLfZ5L.png").similar(0.94))
    wait(.5)
    type("a", KeyModifier.CTRL)
    rightClick("REEDffLLfZ5I.png")
    click("RemoveFormat.png")
    assert not exists(Pattern("REEDffLLfZ5L.png").similar(0.94))
    wait(.5)
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
        #shortcut insert date and time
    keyDown(Key.SHIFT)
    keyDown(Key.ALT)
    type("d")
    keyUp(Key.SHIFT)
    keyUp(Key.ALT)
    wait(.5)
    assert not exists("1349988115960.png")
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.ALT)
    type("m")
    keyUp(Key.SHIFT)
    keyUp(Key.ALT)
    wait(.5)
    assert not exists("1349988115960.png")
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    type("sikuli test description and sta ")
    wait(1)
    paste("Sikuli prompt 1")
    type(Key.TAB)
    type(Key.ENTER)
    wait(1)
    paste("Sikuli prompt 2")
    type(Key.TAB)
    type(Key.ENTER)
    wait(1)
    paste("Sikuli prompt 3")
    type(Key.TAB)
    type(Key.ENTER)
    wait(.5)
    assert exists(Pattern("sikulitestde-1.png").similar(0.94))
    wait(.5)
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste("This Description shortcut Test has Completed Successfully")



#slip_description_shortcuts()



#--------------------------------------------------------------------------------#

def slip_list_description_shortcuts():
    Region(344,262,573,255)
        #spell check current word
    paste("correct ")
    type(Key.F4)
    wait(.5)
    assert exists(Pattern("Spellcheckdi-6.png").similar(0.94))
    wait(.5)
        #spell check entire field
    type(Key.ENTER)
    type(Key.RIGHT)
    paste("icorrect ")
    wait(1)
    type(Key.SHIFT + Key.F4)
    #wait("Errortypespe-1.png")
    assert exists("correctcorre-1.png")
    wait(.5)
    type("c", KeyModifier.ALT)
    wait("Spellcheckis-1.png")
    type(Key.ENTER)
    type(Key.RIGHT)
        #grammar check entire field
    wait(.5)
    paste(" can not ")
    wait(1)
    keyDown(Key.SHIFT)
    type(Key.F5)
    keyUp(Key.SHIFT)
    wait("Errortextcor-3.png")
    assert exists(Pattern("1349814214706-1.png").similar(0.90))
    wait(.5)
    type("c", KeyModifier.ALT)
    type(Key.ENTER)
        #spelling and grammar settings
    keyDown(Key.SHIFT)
    type(Key.F8)
    keyUp(Key.SHIFT)
    wait("SpellingGram-1.png", 30)
    wait(.5)
    assert exists("lnEractivech-1.png")
    type(Key.ENTER)
    wait(.5)
        #increase font details section
    keyDown(Key.CTRL)
    type('=' + '=' + '=' + '=' + '=' + '=')
    keyUp(Key.CTRL)
    assert exists(Pattern("corrcctincor.png").similar(0.94))
    wait(1)
        #decrease font details section
    keyDown(Key.CTRL)
    type('-' + '-' + '-' + '-' + '-' + '-')
    keyUp(Key.CTRL)
    assert exists(Pattern("correctrncor-3.png").similar(0.94))
    wait(.5)
        #shortcut for undo
    paste("Undo")
    assert exists(Pattern("Undo-5.png").similar(0.86))
    wait(.5)
    type("z", KeyModifier.CTRL)
    assert not exists(Pattern("Undo-5.png").similar(0.88))
    wait(.5)
        #shortcut for cut
    paste("CUT")
    assert exists("CUT-3.png")
    doubleClick("CUT-3.png")
    type("x", KeyModifier.CTRL)
    assert not exists(Pattern("CUT-3.png").similar(0.94))
    wait(.5)
        #shortcut for copy and paste
    paste("COPY ")
    assert exists(Pattern("COF-1.png").similar(0.89))
    wait(.5)
    doubleClick(Pattern("COF-1.png").similar(0.88))
    type("c", KeyModifier.CTRL)
    wait(.5)
    type(Key.RIGHT)
    wait(.5)
    type("v", KeyModifier.CTRL)
    assert exists(Pattern("COFCOF-1.png").similar(0.94))
    wait(.5)
        #shortcut for select all and clear
    type("a", KeyModifier.CTRL)
    wait(.5)
    type(Key.CTRL + Key.DELETE)
    wait(.5)
    assert not exists(Pattern("Correctincor-7.png").similar(0.94))
    wait(.5)    
        #uppercase shortcut
    paste("correct incorrect cannot")
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("u")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    assert exists(Pattern("CUHHECTINCUH-1.png").similar(0.94))
        #lower case shortcut
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("l")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    assert exists("correctrncor-2.png")
    wait(.5)
        #sentence case short
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("s")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    type("n", KeyModifier.ALT)
    wait(.5)
    assert exists(Pattern("DCI.png").similar(0.93))
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("s")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    type("y", KeyModifier.ALT)
    wait(.5)
    assert exists(Pattern("Corr.png").similar(0.94))
    wait(.5)
        #proper case shortcut
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("p")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    type("n", KeyModifier.ALT)
    wait(.5)
    assert exists(Pattern("Correctincor-5.png").similar(0.94))
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("p")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait(.5)
    type("y", KeyModifier.ALT)
    wait(.5)
    assert exists(Pattern("CorrectIncor-4.png").similar(0.94))
        #shortcut word count
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.CTRL)
    type("w")
    keyUp(Key.SHIFT)
    keyUp(Key.CTRL)
    wait("WordsChaacEr-1.png")
    assert exists(Pattern("WordsChaacEr-1.png").similar(0.94))
    wait(.5)
    type(Key.ENTER)
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
        #shortcut PTI
    type(Key.SPACE)
    keyDown(Key.ALT)
    type(Key.INSERT)
    keyUp(Key.ALT)
    wait(1)
    type(Key.SPACE)
    keyDown(Key.ALT)
    type(Key.INSERT)
    keyUp(Key.ALT)
    assert exists(Pattern("1349967901043-1.png").similar(0.78))
    type(Key.BACKSPACE)
    type(Key.BACKSPACE)
    assert not exists(Pattern("1349967901043-1.png").similar(0.78))
    wait(.5)
        #shortcut abbreviations
    keyDown(Key.CTRL)
    type(Key.F7)
    keyUp(Key.CTRL)
    assert exists(Pattern("gllcwspecial-1.png").similar(0.94))
    wait(.5)
    type(Key.ESC)
    wait(.5)
        #clear out text box\
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
        #shortcut formatting
    paste("BOLD")
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("b", KeyModifier.CTRL)
    type(Key.RIGHT)
    assert exists(Pattern("BDLD-1.png").similar(0.94))
    wait(.5)
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("b", KeyModifier.CTRL)
    wait(.5)
    type("a", KeyModifier.CTRL)
    type(Key.CTRL + Key.DELETE)
    wait(.5)
    paste("ITALIC")
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("i", KeyModifier.CTRL)
    type(Key.RIGHT)
    assert exists(Pattern("MIKE-2.png").similar(0.88))
    wait(.5)
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("i", KeyModifier.CTRL)
    type("a", KeyModifier.CTRL)
    type(Key.CTRL + Key.DELETE)
    wait(.5)
    paste("UNDERLINE")
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("u", KeyModifier.CTRL)
    type(Key.RIGHT)
    assert exists(Pattern("UNDERLINE-1.png").similar(0.95))
    wait(.5)
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("u", KeyModifier.CTRL)
    type("a", KeyModifier.CTRL)
    type(Key.CTRL + Key.DELETE)
    wait(.5)
    paste("BOLD ITALICS UNDERLINED")
    wait(.5)
    type("a", KeyModifier.CTRL)
    wait(.5)
    type("b", KeyModifier.CTRL)
    type("i", KeyModifier.CTRL)
    type("u", KeyModifier.CTRL)
    type(Key.RIGHT)
    wait(.5)
    assert exists(Pattern("REEDffLLfZ5L-1.png").similar(0.94))
    wait(.5)
    type("a", KeyModifier.CTRL)
    rightClick("REEDffLLfZ5I-1.png")
    click("RemoveFormat-1.png")
    assert not exists(Pattern("REEDffLLfZ5L-1.png").similar(0.94))
    wait(.5)
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
        #shortcut insert date and time
    keyDown(Key.SHIFT)
    keyDown(Key.ALT)
    type("d")
    keyUp(Key.SHIFT)
    keyUp(Key.ALT)
    wait(.5)
    assert not exists("1349988115960-1.png")
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    keyDown(Key.SHIFT)
    keyDown(Key.ALT)
    type("m")
    keyUp(Key.SHIFT)
    keyUp(Key.ALT)
    wait(.5)
    assert not exists("1349988115960-1.png")
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    type("sikuli test description and sta ")
    wait(1)
    paste("Sikuli prompt 1")
    type(Key.TAB)
    type(Key.ENTER)
    wait(1)
    paste("Sikuli prompt 2")
    type(Key.TAB)
    type(Key.ENTER)
    wait(1)
    paste("Sikuli prompt 3")
    type(Key.TAB)
    type(Key.ENTER)
    wait(.5)
    assert exists(Pattern("sikulitestde.png").similar(0.87))
    wait(.5)
    type("a", KeyModifier.CTRL)
    type(Key.DELETE)
    wait(.5)
    paste("This Description shortcut Test has Completed Successfully")



#slip_list_description_shortcuts()


