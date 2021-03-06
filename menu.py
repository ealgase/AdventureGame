#!/bin/python3
#developed by ealgase
#menuingin python3
#MENU LIST:
#Way this list works:
#Each menu item is a list:
#Item 1:
#Name(what it appears as)
#Item 2:
#What it returns when selected
import sys
import tty,termios
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
def cls():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def menu(menulist,select,prompt):
    selected=int(select)
    enter=False
    menul=len(menulist)
    while enter==False:
        print(prompt)
        print('-')
        for menur in range(menul):
            if menur==selected:
                print("[" + menulist[menur][0] + "]")
            else:
                print(menulist[menur][0])
        move=get()
        cls()
        if move=="up":
            if selected<len(menulist) and selected>0:
                selected+=-1
        elif move=="down":
            if selected<len(menulist)-1 and selected>-1:
                selected+=1
        elif move=="return":
            enter=True
    cls()
    ret=menulist[selected][1]
    return ret