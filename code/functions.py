from saveloader import loadSettingsSave
from lang import langset

def style_text(text: str, style: str = "normal", title: bool = False, justify: str = "left"):
    if justify == "center" and title == True:
        horizontal_line = "-" * 80
        lines = text.split("\n")
        centered_lines = [line.center(80) for line in lines]
        result = "\n".join(centered_lines)
        if result.endswith("\nNone"):
            result = result[:-5]
        return f"{horizontal_line}\n{result}\n{horizontal_line}"
    elif style == "normal":
        return text
    elif style == "bold":
        return f"\033[1m{text}\033[0m"
    elif style == "italic":
        return f"\033[3m{text}\033[0m]"
    elif style == "underline":
        return f"\033[4m{text}\033[0m"
    elif title == True:
        return text.title()

def print_paragraph(name : str):
    langobj = loadSettingsSave("lang")
    if langobj == False:
        langobj = langset()
    globals()[langobj] = __import__(langobj)
    global lang
    lang = eval(langobj).language()
    if name == "023":
        print(style_text("ProgressCLI95 0.2.3 Updates!", style="bold")+"""
            Were happy to introduce you the new features of the game!

            - More languages
            - Fixed some bugs
            - Added the credits Section

            Thanks for enjoying our game!""")
        input()
    elif name == "0231":
        print("We have added the id_SH translation for easier use, Hope you enjoy!\n\n"+style_text("This was scrapped due to the translations not working and made me take a break for a few months :)", style="bold"))
        input()
    elif name == "024":
        print(style_text("ProgressCLI95 0.2.4 Updates!", style="bold")+"""
            Sorry for the long wait, but now its here! with:

            - New begin menu
            - Failsafe for no rich  users (later on updated)
            - New language: Deutsch
            - Update log and Instructions page
            - Bug fixes and more

            Hope you enjoy our BIG update!

            Catafrancia - 24 March 2023""")
        input()
    elif name == "bin-figure-happy":
        print("""\                /
                  \    0    0    /
                   \            /
                    \  \____/  /
                     \        /
                      \______/""")
    elif name == "bin-figure-normal":
        print("""\                /
                  \    0    0    /
                   \            /
                    \  ______  /
                     \        /
                      \______/""")
    elif name == "bin-figure-sad":
        print("""\                /
                  \    0    0    /
                   \            /
                    \   ____   /
                     \ /    \ /
                      \______/""")
    elif name == "cmddir1":
        title = style_text(f"C:/ {lang.cmd1}", style="italic")
        print(f"{title}\nProgressbar - <DIR>\nDocuments - <DIR>\nPrograms - <DIR>\nBin - <DIR>\nDocs - <DIR>\nREADME - TXT")
    elif name == "helpcmd":
        print(f"exit - {lang.cmdhelp1}\ndir - {lang.cmdhelp2}\ncls - {lang.cmdhelp3}\nhelp - {lang.cmdhelp4}")
        
def draw_bar(value : int):
    return ''.join(['[]' for _ in range(value)])