from art import tprint
from pyinjector import inject
import os
import shutil
from colorama import init, Fore, Back, Style
import psutil
import time
# gets the pid of the process (Fortnite)
def getPid(name):
    for process in psutil.process_iter():
        try:
            if name == process.name():
                return(process.pid)
        except: pass

init()
print(Fore.GREEN + "Running servers and installing modules...")
os.system("install_packages.bat")
os.chdir("./LawinServer-main")
os.system("install_packages.bat")
os.startfile("lawinserver.exe")
os.startfile("start.bat")
os.chdir("./../")
os.system("cls")
tprint("Raider Launcher Py")



def main():
    print(Fore.GREEN + "Please paste the folder to 3.5..")
    path = input("> ")

    if not os.path.exists(path):
        print(Fore.RED + "Error: Path not found! \n\n")
        main()
    else:
        print(Fore.GREEN + "Found path! Checking for binaries folder now... ")
        try: 
            shutil.move("Raider.dll", path)
        except: 
             pass
        try:
            shutil.move("Fortnite_Console.dll", path)
        except:
            pass
        # this is checking twice because it could skip one of the two
            
            


        os.chdir(path)

        binaries = rf"{path}//FortniteGame//Binaries//Win64"
        if os.path.exists(binaries):
            print(Fore.GREEN + "Found binaries folder! Checking for launcher now...")
            os.chdir(binaries)
            launcher = rf"{binaries}//Launcher.bat"
            if os.path.exists(launcher):
                print(Fore.GREEN + "Found launcher! Launching now...")
                os.startfile(launcher)
                hamachi = f"C:\Program Files (x86)\LogMeIn Hamachi"
                if os.path.exists(hamachi):
                    print(Fore.GREEN + "Found Hamachi! Launching now...")
                    os.startfile(rf"{hamachi}//hamachi-2-ui.exe")
                else:
                    print(Fore.RED + "Error: Hamachi not found! Download it here! ")
                    os.system("https://www.vpn.net/")
                print(Fore.GREEN + "Launcher launched! Please type in 1 when you are in lobby.")
                lobby = input("> ")
                if lobby == "1":
                    fortnitePid = getPid("FortniteClient-Win64-Shipping.exe")
                    
                    # inject raider
                    os.chdir("./../../../")
                    inject(fortnitePid, "Raider.dll" )

                    print("Would you like to start a second fortnite client? (y/n)")
                    second = input("> ")
                    if second == "y":
                        os.chdir(binaries)
                        shutil.copy(launcher, rf"{binaries}//Launcher2.bat")
                        launcher2 = rf"{binaries}//Launcher2.bat"
                        os.startfile(launcher2)

                        print(Fore.GREEN + "Launcher launched! Please type in 1 when you are in lobby.")
                        lobby2 = input("> ")
                        if lobby2 == "1":
                            os.chdir("./../../../")
                            fortnitePid2 = getPid("FortniteClient-Win64-Shipping.exe")
                            inject(fortnitePid2, "Fortnite_Console.dll" )
                            inject(fortnitePid2, "Fortnite_Console.dll" )




            else: 
                print(Fore.RED + "Error: Launcher not found! \n\n")
                main()
        else: 
            print(Fore.RED + "Error: Binaries folder not found! \n\n")
            main()
        
    Fore.RESET
    
        
main()


