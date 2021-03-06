from sikuli import*
import os
import DBChecks

timeslip = App(os.path.join(r'C:\tssmoketest', '2015', 'timeslip.exe'))

def menu_test():
    timeslip.open()
    DBChecks.checkFor_Preferror()
    DBChecks.checkFor_BillingDate()  
    DBChecks.checkFor_SPS()
    DBChecks.checkFor_PEP()
    waitVanish(Pattern("ProductEnhan-1.png").similar(0.87))
    #--------------------------file menu-------------------------#
    type('f', KeyModifier.ALT)
    type('nd')
    assert exists("EIaIaIProfes.png")
    type(Key.ESC)
    waitVanish("EIaIaIProfes.png")
    type('f', KeyModifier.ALT)
    type('nc')
    assert exists("Yournewdatab.png")
    type(Key.ESC)
    waitVanish("Yournewdatab.png")
    type('f', KeyModifier.ALT)
    type('o')
    assert exists("FilenameFile.png")
    type(Key.ESC)    
    type('f', KeyModifier.ALT)        
    type('s')
    assert exists("Thislistdeta.png")
    type(Key.F4, KeyModifier.CTRL)
    type('f', KeyModifier.ALT)
    type('b')
    assert exists("Thisprocessc.png")
    type(Key.F4, KeyModifier.ALT)
    type('f', KeyModifier.ALT)
    type('r')
    assert exists("CurrentDatab.png")
    type(Key.ESC)
    type('f', KeyModifier.ALT)
    type('d')
    assert exists("Alltablesint.png")
    type(Key.ESC)
    type('f', KeyModifier.ALT)
    type('p')
    assert exists("SelectDatato.png")
    type(Key.ESC)
    type('f', KeyModifier.ALT)
    type('e')
    assert exists("Newandchange.png")
    type(Key.ESC)
    type('f', KeyModifier.ALT)
    type('a')
    assert exists("Thedatabases.png")
    type(Key.ESC)
    type('f', KeyModifier.ALT)
    type('h')
    assert exists("NewarchiveAg.png")
    type(Key.ESC)
    type('f', KeyModifier.ALT)
    type('c')
    if not exists("DlUlIIICusto-1.png"):
        click("1398456287209-1.png")
    assert exists("DlUlIIICusto-1.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish("DlUlIIICusto-1.png")
    timeslip.focus()
    type('f', KeyModifier.ALT)
    type('i')
    if not exists("sSIn1TE7KkmI.png"):
        click("1398456287209-1.png")
    assert exists("sSIn1TE7KkmI.png")
    waitVanish("sSIn1TE7KkmI.png")
    type(Key.ESC)
    type(Key.F4, KeyModifier.ALT)
    timeslip.focus()
    type('f', KeyModifier.ALT)
    type('t')
    assert exists("Welcometothe.png")
    type(Key.ESC)
    type('f', KeyModifier.ALT)
    type('u')
    wait("PrinterNameS.png", 30)
    assert exists("PrinterNameS.png")
    type(Key.ESC)
    type('f', KeyModifier.ALT)
    type('x')
    if exists("YourSageTime.png"):
        type(Key.RIGHT)
        type(Key.SPACE)
    waitVanish("IiiitjgEEQSI.png")
    assert not exists("IiiitjgEEQSI.png")
    timeslip.open() 
    DBChecks.checkFor_Preferror()
    DBChecks.checkFor_BillingDate()  
    DBChecks.checkFor_SPS()
    DBChecks.checkFor_PEP()
    waitVanish(Pattern("ProductEnhan-1.png").similar(0.87))
    #-------------------------Slips menu-------------------------------------#
    type('s', KeyModifier.ALT)
    type('s')
    assert exists("WewBySelecti.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("WewBySelecti.png")
    type('s', KeyModifier.ALT)
    type('ts')
    assert exists("Q.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("Q.png")
    type('s', KeyModifier.ALT)
    type('tt')
    assert exists("ViewbydiveN.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("ViewbydiveN.png")
    type('s', KeyModifier.ALT)
    type('m')
    assert exists("TimeValueCli.png")
    type(Key.SPACE, KeyModifier.ALT)
    type('x')
    waitVanish("TimeValueCli.png")
    wait("eelsmmemlmye.png", 30)
    type('s', KeyModifier.ALT)
    type('e')
    assert exists("NewslipsSlip.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("NewslipsSlip.png")
    type('s', KeyModifier.ALT)
    type('n')
    assert exists("Alsousestemp.png")
    type(Key.ESC)
    waitVanish("Alsousestemp.png")
    type('s', KeyModifier.ALT)
    type('l')
    assert exists("Youcanusethi.png")
    type(Key.ESC)
    waitVanish("Youcanusethi.png")
    type('s', KeyModifier.ALT)
    type('f')
    assert exists("WhenSageTime.png")
    type('o')
    waitVanish("WhenSageTime.png")
    type('s', KeyModifier.ALT)
    type('p')
    assert exists("StatusSentDa.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("StatusSentDa.png")
    type('s', KeyModifier.ALT)
    type('i')
    assert exists("Areyousureyo.png")
    type('n')
    waitVanish("Areyousureyo.png")
    type('s', KeyModifier.ALT)
    type('a')
    assert exists("Areyousureyo-1.png")
    type('n')
    waitVanish("Areyousureyo-1.png")
    type('s', KeyModifier.ALT)
    type('c')
    assert exists("TheCloseSlip.png")
    type(Key.ESC)
    waitVanish("TheCloseSlip.png")
    type('s', KeyModifier.ALT)
    type('r')
    assert exists("TheReopenSli.png")
    type(Key.ESC)
    waitVanish("TheReopenSli.png")
    type('s', KeyModifier.ALT)
    type('u')
    assert exists("Youcanusethi-1.png")
    type(Key.ESC)
    waitVanish("Youcanusethi-1.png")
    type('s', KeyModifier.ALT)
    type('d')
    assert exists("Therearenote.png")
    type(Key.ESC)
    waitVanish("Therearenote.png")
    #-----------------Transactions Menu--------------------#
    type('t', KeyModifier.ALT)
    type('a')
    assert exists("Hinhlinhherl.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("Hinhlinhherl.png")
    type('t', KeyModifier.ALT)
    type('f')
    assert exists("ClientFundsA.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("ClientFundsA.png")
    type('t', KeyModifier.ALT)
    type('b')
    assert exists("Therearenoba.png")
    type('n')
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("Therearenoba.png")
    type('t', KeyModifier.ALT)
    type('e')
    assert exists("Thislistprov.png")
    type(Key.ESC)
    waitVanish("Thislistprov.png")
    #------------------Names Menu--------------------#
    type('n', KeyModifier.ALT)
    type('i')
    assert exists("J2wmwvUPBWTc.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("J2wmwvUPBWTc.png")
    type('n', KeyModifier.ALT)
    type('h')
    assert exists("IIIhIQuarter-1.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("IIIhIQuarter-1.png")
    type('n', KeyModifier.ALT)
    type('r')
    assert exists("Thislistshow.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("Thislistshow.png")
    type('n', KeyModifier.ALT)
    type('d')
    assert exists("Slipcreation.png")
    type(Key.ESC)
    waitVanish("Slipcreation.png")
    type('n', KeyModifier.ALT)
    type('n')
    assert exists("IliIaUDBlTem.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("IliIaUDBlTem.png")
    type('n', KeyModifier.ALT)
    type('s')
    assert exists("TimekeeperMo.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("TimekeeperMo.png")
    type('n', KeyModifier.ALT)
    type('f')
    assert exists("MrUPBYIITemp.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("MrUPBYIITemp.png")
    type('n', KeyModifier.ALT)
    type('o')
    assert exists("IIrrewezUPBY.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("IIrrewezUPBY.png")
    type('n', KeyModifier.ALT)
    type('b')
    wait("FirmIB9Ellen.png", 30)
    assert exists("FirmIB9Ellen.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("FirmIB9Ellen.png")
    #---------------------------Bills Menu-----------------------------#
    type('b', KeyModifier.ALT)
    type('b')
    if exists("SelectwhichB.png"):
        assert exists("SelectwhichB.png")
        type(Key.ENTER)
        waitVanish("SelectwhichB.png")       
        assert exists("BillingAssis.png")
        type(Key.F4, KeyModifier.CTRL)
        waitVanish("BillingAssis.png")
    else:
        assert exists("BillingAssis-1.png")
        type(Key.F4, KeyModifier.CTRL)
        waitVanish("BillingAssis-1.png")
    type('b', KeyModifier.ALT)
    type('f')
    assert exists("DateFlangeSt.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("DateFlangeSt.png")
    type('b', KeyModifier.ALT)
    type('t')
    assert exists("Youcanusethi-2.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("Youcanusethi-2.png")
    type('b', KeyModifier.ALT)
    type('i')
    assert exists("PrimaryClien.png")
    type(Key.ESC)
    waitVanish("PrimaryClien.png")
    type('b', KeyModifier.ALT)
    type('p')
    assert exists(Pattern("NamePrebiWor.png").similar(0.92))
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("NamePrebiWor.png")
    type('b', KeyModifier.ALT)
    type('g')
    assert exists(Pattern("NameGenerate.png").similar(0.90))
    type(Key.F4, KeyModifier.CTRL)
    waitVanish(Pattern("NameGenerate.png").similar(0.89))
    type('b', KeyModifier.ALT)
    type('s')
    assert exists(Pattern("NameGenerate-1.png").similar(0.89))
    type(Key.F4, KeyModifier.CTRL)
    waitVanish(Pattern("NameGenerate-1.png").similar(0.89))
    type('b', KeyModifier.ALT)
    type('a')
    assert exists("Proofstagebi.png")
    type(Key.ESC)
    waitVanish("Proofstagebi.png")
    type('b', KeyModifier.ALT)
    type('c')
    assert exists("Flevisionsta.png")
    type(Key.ESC)
    waitVanish("Flevisionsta.png")
    type('b', KeyModifier.ALT)
    type('u')
    assert exists("Thisisalisto.png")
    type(Key.ESC)
    waitVanish("Thisisalisto.png")
    type('b', KeyModifier.ALT)
    type('r')
    assert exists("Thisdialogbo.png")
    type(Key.ESC)
    waitVanish("Thisdialogbo.png")
    type('b', KeyModifier.ALT)
    type('d')
    assert exists("Thisisthedat.png")
    type(Key.ESC)
    waitVanish("Thisisthedat.png")
    #----------------------Reports Menu-------------------------#
    type('r', KeyModifier.ALT)
    type('b')
    assert exists("Mlm.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("Mlm.png")
    type('r', KeyModifier.ALT)
    type('s')
    assert exists("ingSlipsIA.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("ingSlipsIA.png")
    type('r', KeyModifier.ALT)
    type('a')
    assert exists("npsARTransac.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("npsARTransac.png")
    type('r', KeyModifier.ALT)
    type('f')
    assert exists("DmlFundsTran.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("DmlFundsTran.png")
    type('r', KeyModifier.ALT)
    type('c')
    assert exists("msIEllenITim.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("msIEllenITim.png")
    type('r', KeyModifier.ALT)
    type('t')
    assert exists("enrlTimekeep.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("enrlTimekeep.png")
    type('r', KeyModifier.ALT)
    type('i')
    assert exists("iperActivity.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("iperActivity.png")
    type('r', KeyModifier.ALT)
    type('y')
    assert exists("tyISystemIT.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("tyISystemIT.png")
    type('r', KeyModifier.ALT)
    type('x')
    assert exists("amlTaxlor.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("amlTaxlor.png")
    type('r', KeyModifier.ALT)
    type('h')
    assert exists("TaxElther.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("TaxElther.png")
    type('r', KeyModifier.ALT)
    type('n')
    assert exists("Thelistbelow.png")
    type(Key.ESC)
    waitVanish("Thelistbelow.png")
    type('r', KeyModifier.ALT)
    type('e')
    assert exists("Thiswizardwi.png")
    type(Key.ESC)
    waitVanish("Thiswizardwi.png")
    type('r', KeyModifier.ALT)
    type('o')
    assert exists("Theseoptions.png")
    type(Key.ESC)
    waitVanish("Theseoptions.png")
    type('r', KeyModifier.ALT)
    type('m')
    assert exists("Thislistshow-1.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish("Thislistshow-1.png")
    #--------------------Calendar Menu-------------------#
    type('l', KeyModifier.ALT)
    type('v')
    assert exists("1398804710702.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("1398804710702.png")
    type('l', KeyModifier.ALT)
    type('m')
    assert exists("Youdonothave.png")
    type('o')
    waitVanish("Youdonothave.png")
    type('l', KeyModifier.ALT)
    type('n')
    assert exists("Usethesefiel-1.png")
    type(Key.ESC)
    waitVanish("Usethesefiel-1.png")
    type('l', KeyModifier.ALT)
    type('e')
    assert exists("Usethesefiel.png")
    type(Key.ESC)
    waitVanish("Usethesefiel.png")
    type('l', KeyModifier.ALT)
    type('w')
    assert exists("1200AMAllday.png")
    type(Key.ESC)
    waitVanish("1200AMAllday.png")
    type('l', KeyModifier.ALT)
    type('t')
    assert exists("Usethesefiel-2.png")
    type(Key.ESC)
    waitVanish("Usethesefiel-2.png")
    type('l', KeyModifier.ALT)
    type('p')
    assert exists("Usethislistt.png")
    type(Key.ESC)
    waitVanish("Usethislistt.png")
    type('l', KeyModifier.ALT)
    type('ss')
    assert exists("Inorderforli.png")
    type(Key.ESC)
    waitVanish("Inorderforli.png")
    type('l', KeyModifier.ALT)
    type('se')
    assert exists("Inorderforli.png")
    type(Key.ESC)
    waitVanish("Inorderforli.png")
    #-----------------------Accounting------------------------#
    type('a', KeyModifier.ALT)
    type('c')
    assert exists("Idogotuseana.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish("Idogotuseana.png")
    #------------------------Special----------------------#
    type('c', KeyModifier.ALT)
    type('a')
    wait("TimekeeperDa.png", 30)
    assert exists("TimekeeperDa.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("TimekeeperDa.png")
    type('c', KeyModifier.ALT)
    type('r')
    assert exists("Pleaseidenti.png")
    type(Key.ESC)
    waitVanish("Pleaseidenti.png")
    type('c', KeyModifier.ALT)
    type('ts')
    wait("AlRTransacti.png", 30)
    assert exists("AlRTransacti.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("AlRTransacti.png")
    type('c', KeyModifier.ALT)
    type('te')
    wait("Usethisdialo-2.png", 30)
    assert exists("Usethisdialo.png")
    type('w', KeyModifier.CTRL)
    waitVanish("Usethisdialo.png")
    type('c', KeyModifier.ALT)
    type('ta')
    assert exists("Usethisdialo-1.png")
    type(Key.ESC)
    waitVanish("Usethisdialo-1.png")
    type('c', KeyModifier.ALT)
    type('em')
    wait("Alertrules.png", 30)
    assert exists("Alertrules.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("Alertrules.png")
    type('c', KeyModifier.ALT)
    type('el')
    assert exists("Thealertsbei.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("Thealertsbei.png")
    type('c', KeyModifier.ALT)
    type('ep')
    assert exists("Therearenoun.png")
    type(Key.ESC)
    waitVanish("Therearenoun.png")
    type('c', KeyModifier.ALT)
    type('c')
    assert exists("SpellingErro.png")
    type(Key.ESC)
    waitVanish("SpellingErro.png")
    type('c', KeyModifier.ALT)
    type('x')
    assert exists("Seard1for.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("Seard1for.png")
    type('c', KeyModifier.ALT)
    type('n')
    assert exists("ChangeTempla.png")
    type('c', KeyModifier.ALT)
    type('p')
    assert exists("GuidesUnNavi.png")
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("GuidesUnNavi.png")
    type('c', KeyModifier.ALT)
    type('l')
    assert exists("Usethiscomma.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish("Usethiscomma.png")
    type('c', KeyModifier.ALT)
    type('v')
    assert exists("ApplicationL.png")
    type(Key.ESC)
    waitVanish("ApplicationL.png")
    type('c', KeyModifier.ALT)
    type('o')
    wait("Locationofse.png", 30)
    assert exists("Locationofse.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish("Locationofse.png")
    type('c', KeyModifier.ALT)
    type('m')
    assert exists("limeCapturep.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish("limeCapturep.png")
    type(Key.F4, KeyModifier.ALT)
    waitVanish("EnnverttuSli.png")
    type('c', KeyModifier.ALT)
    type('g')
    wait(Pattern("Loqs.png").similar(0.84), 30)
    assert exists(Pattern("Loqs.png").similar(0.84))
    type(Key.F4, KeyModifier.ALT)
    waitVanish(Pattern("Loqs.png").similar(0.84))
    #---------------Setup Menu----------------------------#
    """
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()
    type('p', KeyModifier.ALT)
    type('')
    assert exists()
    type()
    waitVanish()"""
    

    

    
menu_test()
    
    