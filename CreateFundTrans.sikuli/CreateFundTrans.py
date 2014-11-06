from sikuli import*
import TABFunction


def create_fundtransaction():
    type('t', KeyModifier.ALT)
    type('f')
    wait("ViewbyAllIFu.png", 20)
    type('n', KeyModifier.CTRL)
    wait(Pattern("IDFundsaccou.png").similar(0.87))
    type('deposit')
    wait("HMtmlQpc1siL.png", 20)
    type(Key.TAB)
    type(Key.TAB)
    type('sikuli test client')
    wait("ISikuiTestCl-1.png", 20)
    for x in range(1, 5):
        TABFunction.tab(x)
    paste('100.00')
    type('s', KeyModifier.CTRL)
    waitVanish(Pattern("1362609133757.png").similar(0.94))
    type(Key.F4, KeyModifier.CTRL)
    waitVanish("TypeDepositS.png")
    type(Key.F4, KeyModifier.CTRL)
    
    
    
#create_fundtransaction()   