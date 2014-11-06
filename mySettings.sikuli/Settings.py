#This is my main function for anything I want to use as global variables. Make sure to
#always import this script into your functions if you want to call anything in it.
import os


def ts_settings():
    tsVersion = input("Enter your version ie.. 2013, 2014 etc:", "2014")
    tsBuild = input("Enter your build ie..Build 22.0.0.76:", "Build ")
    tsSerial = input("Enter your serial# ie..13800000:")
        #Defined Applications to call to open and close in script
    Settings.tscode = App(os.path.join(r"\\gaqtsbuild01", "TSStorage", "Builds", tsVersion, "utilities", "TSCodes.exe"))
    Settings.tssetup = App(os.path.join(r"\\gaqtsbuild01", "TSStorage", "Builds", tsVersion, tsBuild, "setup.exe"))
    #print "tscode",Settings.tscode


#ts_settings()