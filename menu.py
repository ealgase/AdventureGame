#Main menu
import sys
import os
import os.path
import tty,termios
import argparse
from os import listdir
args = argparse.ArgumentParser(description='The menu for AdventureGame.')
width = length = 0
args.add_argument('width', default=80, type=int, help='The width of the menu.', nargs='?')
args.add_argument('length', default=24, type=int, help='The length of the menu.', nargs='?')
inpu = args.parse_args()
width = inpu.width
length = inpu.length
print(width)
print(length)
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                if ch == '\r':
                    return "return"
                else:
                    ch = ch + sys.stdin.read(2)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                return "up"
        elif k=='\x1b[B':
                return "down"
        elif k=='\x1b[C':
                return "right"
        elif k=='\x1b[D':
                return "left"
        elif k=='return':
                return "return"
        else:
                print(k)
                print("not an arrow key!")
def centerText(text, sidech="|"):
    spacesOnSide = (width - (len(text) if len(text) % 2 == 0 else len(text) + 1) - (len(sidech) * 2)) / 2
    appendSpace = " "
    i = 1
    while i < spacesOnSide:
        appendSpace = appendSpace + " "
        i+=1
    retText = sidech + appendSpace + text + appendSpace + sidech
    return retText
def cls():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
cls()
menuScreens=[[0 for x in range(24)] for x in range(3)]
menuScreens[0] = ["-" * width,centerText("AdventureGame - Menu", "|"),"-" * width,"|" + (" " * (width-2)) + "|",centerText("[Tutorial]", "|"),"|" + (" " * (width-2)) + "|",centerText("Select World","|"),"|" + (" " * (width-2)) + "|",centerText("Quit","|")]
i = 8
while i < length - 3:
    menuScreens[0].append("|" + (" " * (width - 2)) + "|")
    i+=1
menuScreens[1] = ["-" * width,centerText("AdventureGame - Menu", "|"),"-" * width,"|" + (" " * (width - 2)) + "|",centerText("Tutorial", "|"),"|" + (" " * (width - 2)) + "|",centerText("[Select World]","|"),"|" + (" " * (width - 2)) + "|",centerText("Quit","|")]
i = 8
while i < length - 3:
    menuScreens[1].append("|" + (" " * (width - 2)) + "|")
    i+=1
menuScreens[2] = ["-" * width,centerText("AdventureGame - Menu", "|"),"-" * width,"|" + (" " * (width - 2)) + "|",centerText("Tutorial", "|"),"|" + (" " * (width - 2)) + "|",centerText("Select World","|"),"|" + (" " * (width - 2)) + "|",centerText("[Quit]","|")]
i = 8
while i < length - 3:
    print(str(i))
    menuScreens[2].append("|" + (" " * (width - 2)) + "|")
    i+=1
i = 0
while i < len(menuScreens[0]):
    print(menuScreens[0][i])
    i+=1
validButton = 0
print("Use the arrow keys (return requires 3 clicks): ")
inl = get()
while inl != "return":
    if inl == "up":
        if validButton > 0:
            validButton-=1
    elif inl == "down":
        if validButton < 2:
            validButton+=1
    else:
        print("Invalid")
    cls()
    i=0
    while i < len(menuScreens[validButton]):
        print(menuScreens[validButton][i])
        i+=1
    inl = get()
if validButton == 0:
    os.system("python3 tutorial.py " + str(width) + " " + str(length))
elif validButton == 2:
    sys.exit()
else:
    files = os.listDir("worlds")
    cls()
    print("-" * width)
    print(centerText("AdventureGame - Select World","|"))
    print("-" * width)
    print("|" + (" " * (width - 2)) + "|")
    print(centerText("Choose a world:","|"))
    print("|" + (" " * (width - 2)) + "|")
    worlines = 6
    worlds = 0
    for world in files:
        fp = open("worlds/" + world)
        for i, line in enumerate(fp):
            if i == 1:
                first_line = line
            elif i > 1:
                break
        fp.close()
        print(centerText(str(worlds) + ". " + first_line))
        print("|" + (" " * (width - 2)) + "|")
        worlines += 2
        worlds+=1
    while worlines < length:
        print("|" + (" " * (width - 2)) + "|")
    selworld = input("Choose a number: ")
    os.system("python3 " + files[int(selworld)] + " " + width + " " + length)
sys.exit()
