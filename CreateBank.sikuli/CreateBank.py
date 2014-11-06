from sikuli import*
import TABFunction


def create_bank():
    type('p', KeyModifier.ALT)
    type('b')
    wait("Youusebankac.png", 20)
    type('n', KeyModifier.ALT)
    wait("NameAppliest.png", 20)
    paste('Sikuli Bank Account')
    type(Key.TAB)
    type(Key.TAB)
    type(Key.TAB)
    paste('Test Bank Account for Smoke Test')
    for x in range(1, 8):
        TABFunction.tab(x)
    type(Key.ENTER)
    waitVanish("SikuliBankAc.png")
    for x in range(1, 6):
        TABFunction.tab(x)
    type(Key.ENTER)
    


#create_bank()