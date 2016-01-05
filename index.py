#!/bin/python3
#index.py
#developed by ealgase and mcjack123
#ealgase.github.io
#cppconsole.bruinne.com
#copyright 2015
#all rights reserved
#all scripts in this project are owned by ealgase and mcjack123
#DO NOT REMOVE THE ABOVE LINES
#if you wish to copy any/all of this code, make sure to include the above comments
#thank you,
#ealgase

####Imports
from time import *
from os import *
from menu import *
import random
from commands import *
from rend import *
from vfg import *
####Vars
global special
global lives
global gold
global ebhealth
global damagem
global healthm
global ender
global moonmon
global mars
global xp
special=['Glove', 'Fur Coat', 'Spear', 'Bomb', 'Bomb', 'Golden Vest', 'Sword', 'Bomb', 'Bomb', 'Bomb', 'Bomb', 'Bomb', 'Staff']
lives=13
gold=560
ebhealth=250
damagem=8
healthm=4
ender=0
moonmon=0
mars=0
xp=100
tut=menu([['Play Tutorial','t'],['Start playing','s'],['Exit','e']],1,'What do you want to do?')
if tut=='t':
    import tutorial
    pass
elif tut=='s':
    pass
else:
    exit()
from norm import *
from frozen import *
from moon import *
from blocked import *
worlds=[["Normal","norm.py","normal"],["Frozen Tundra", "frozen.py","frozen"], ["Moon", "moon.py","moon"], ["Minecraft", "blocked.py","blocked"]]
worldn=len(worlds)
worldc=random.randint(0,worldn-1)
while True:
    exec(str(worlds[worldc][2])+'()')
    cw=random.randint(1,100)
    if cw==1:
        rendscreenx("Changing world...")
        input()
        worldc=random.randint(0,worldn-1)
        print("Switching to world " + worlds[worldc][0])
        input()
