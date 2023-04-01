from time import sleep
from clear import clear
from functions import print_paragraph
from saveloader import loadSettingsSave
from lang import langset

langobj = loadSettingsSave("lang")
if langobj == False:
    langobj = langset()
globals()[langobj] = __import__(langobj)
global lang
lang = eval(langobj).language()

def main():
    clear()
    while True:
        cmdinput = input("C:> ")
        if cmdinput.lower() == "hello":
            print("Hello World!")
        elif cmdinput.lower() == "exit":
            print(lang.cmd2)
            sleep(3)
            break
        elif cmdinput.lower() == "cls":
            clear()
        elif cmdinput.lower() == "help":
            print_paragraph("helpcmd")
        elif cmdinput.lower() == "dir":
            print_paragraph("cmddir1")
        elif cmdinput.lower() == "cd..":
            print("You are in the first directory lol")
        else:
            print(f"{cmdinput}, {lang.cmd3}")
    return

main()