#This is my main function for anything I want to use as global variables. Make sure to
#always import this script into your functions if you want to call anything in it.



def ts_settings():
    settings.tsVersion = input("Enter your version ie.. 2013, 2014 etc:", "2014")
    settings.tsBuild = input("Enter your build ie..Build 22.0.0.76:", "Build ")
    settings.tsSerial = input("Enter your serial# ie..13800000:")
        #Defined Applications to call to open and close in script
    settings.tscode = App(os.path.join(r"\\gaqtsbuild01", "TSStorage", "Builds", tsVersion, "utilities", "TSCodes.exe"))
    settings.tssetup = App(os.path.join(r"\\gaqtsbuild01", "TSStorage", "Builds", tsVersion, tsBuild, "setup.exe"))