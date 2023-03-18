def style_text(text: str, style: str = "normal", title: bool = False, justify: str = "left"):
    if justify == "center" and title == True:
        horizontal_line = "-" * 80
        lines = text.split("\n")
        centered_lines = [line.center(80) for line in lines]
        result = "\n".join(centered_lines)
        if result.endswith("\nNone"):
            result = result[:-5]
        return f"{horizontal_line}\n{result}\n{horizontal_line}"
    elif style == "bold":
        print("\033[1m"+text+"\033[0m")
    elif style == "italic":
        print("\033[3m"+text+"\033[0m")
    elif style == "underline":
        print("\033[4m"+text+"\033[0m")

def print_paragraph(name : str):
    if name == "023":
        print(style_text("ProgressCLI95 0.2.3 Updates!", style="bold")+"""
            Were happy to introduce you the new features of the game!

            - More languages
            - Fixed some bugs
            - Added the credits Section

            Thanks for enjoying our game!""")
    elif name == "0231":
        print("We have added the id_SH translation for easier use, Hope you enjoy!\n\n"+style_text("This was scrapped due to the translations not working and made me take a break for a few months :)", style="bold"))