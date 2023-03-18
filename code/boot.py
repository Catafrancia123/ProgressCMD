from saveloader import detectSave, detectSettings, loadSystemSave, loadSettingsSave
from rich import print as rprint
from clear import clear
from checkbadge import calculateBadge
from player import startup, updateLog
from lang import langset
from functions import style_text
import sys
import os
import random

# no touchy!!! (ver and date)
version = "0.2.4 Beta"
compileDate = "18-03-2023"

# find systems and generate list
osdirs = "./opsys/"
sys.path.insert(0, osdirs)
sys.path.insert(0, './lang/')
osesDir = os.listdir(osdirs)

# sanitize list
osArrayUnsorted = []
for x in osesDir:
    if x == "__pycache__":
        continue
    else:
        x = x.replace('.py', '')
        osArrayUnsorted.append(x)

# import systems
for x in osArrayUnsorted:
    globals()[x] = __import__(x)

# sort array into new array (this is probably inefficient but whatever)
finished = False
arrayCounter = 0
osArray = []
while finished == False:
    arraySelect = random.randrange(0, len(osArrayUnsorted))
    xobj = eval(osArrayUnsorted[arraySelect]).system()
    if xobj.listinbootmenu == arrayCounter:
        osArray.append(osArrayUnsorted[arraySelect])
        osArrayUnsorted.pop(arraySelect)
        arrayCounter +=1
    else:
        continue

    if len(osArrayUnsorted) == 0:
        finished = True

def loadSettings(system):
    xsys = osArray[system]
    xobj = eval(xsys).system()
    x = loadSystemSave(xobj.shortname)
    if x == False:
        print()
    else:
        xlevel = x
        xbadge = calculateBadge(xlevel, xobj.prolevel)

        if hasattr(xobj, "systemunlock"):
            xu = "system" + xobj.systemunlock
            xun = osArray.index(xu)
            xunlo = eval(osArray[xun]).system()
            xunlock = xunlo.unlocklevel
            xsystem = xobj.systemunlock
        else:
            xsystem = False
            xunlock = False

        startup(xobj.shortname, xlevel, xobj.prolevel, xbadge, xobj.startupstring, xsystem, xunlock)

def boot():
    langobj = loadSettingsSave("lang")
    if langobj == False:
        langobj = langset()
    globals()[langobj] = __import__(langobj)

    detectSettings()
    detectSave()

    global lang
    lang = eval(langobj).language()

    while True:
        clear()
        
        try:
            rprint(lang.sparrow)
            rprint(lang.version.format(version, compileDate))
            rprint(lang.dev)
        except ModuleNotFoundError:
            norich()

        bmc = 1 # boot menu counter
        for x in osArray:
            xobj = eval(x).system()
            systemexists = loadSystemSave(xobj.shortname)
            if systemexists == False:
                rprint(lang.notUnlocked.format(bmc, xobj.name, xobj.unlocklevel, xobj.requiredstring))
                bmc += 1
            else:
                systembadge = calculateBadge(systemexists, xobj.prolevel)
                print(str(bmc) + '. ' + xobj.name, systembadge)
                bmc += 1

        choice = input()
        if choice == "":
            print()
        elif choice == "credits":
            clear()
            rprint(lang.credits1)
            print()
            rprint("[#5865f2]Catafrancia123[/#5865f2]")
            print()
            rprint(lang.credits2)
            rprint("🇺🇸 English (en_US) - [#5865f2]Catafrancia123[/#5865f2]")
            rprint("🇵🇱 Polski (Polish) (pl_PL) - [#fff400]gamingwithpivin[/#fff400]")
            rprint("🇷🇴 Româna (Romanian) (ro_RO) - [#f6b97a]setapdede[/#f6b97a], [#ff5045]AlexandruUnu[/#ff5045]")
            rprint("🇫🇷 Français (French) (fr_FR) - [#2fda00]5jiji[/#2fda00]")
            rprint("🇧🇷 Português Brasileiro (Brazilian Portuguese) (pt_BR) - [#1462d9]Luihum[/#1462d9]")
            rprint("🇮🇹 Italiano (Italian) (it_IT) - [#206694]Christian230102[/#206694]")
            rprint("🇧🇬 български (Bulgarian) (bg_BG) - [#9966cc]markverb1[/#9966cc]")
            rprint("🇹🇷 Türkçe (Turkish) (tr_TR) - [#c27c0e]UstaYussuf[/#c27c0e]")
            rprint("🇸🇪 Svenska (Swedish) (sw_SE) - [#0000FF]Cranky[/#0000FF]")
            print()
            print("As of 2023, the original game developers have ended game development and im the only one!\nWith translators.\nCatafrancia123 - March 2023")
            print(lang.con1)
            print()
            input()
        elif choice == "chlang":
            langobj = langset()
            globals()[langobj] = __import__(langobj)
            lang = eval(langobj).language()
        elif choice == "update" or choice.lower() == "upd":
            updateLog()
        else:
            choice = int(choice) - 1
            loadSettings(choice)

def norich():
    print(style_text("You dont have the necessary dependencies (package) to run this app.", style="bold")+"""Do you want to install the package(s) or continue without it? (Y/N)
    Y - Install the package(s)
    N - Go to an non-3rd party package application""")
    choice = input("> ")
    if choice.lower() == "y":
        os.system("pip install rich")
        clear()
        print("Restart the app.")
    if choice.lower() == "n":
        raise ModuleNotFoundError("You have chosen to not install the package(s) there will be a similar game with no packages soon....")

boot()
