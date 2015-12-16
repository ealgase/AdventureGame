ender=0
moonmon=0
healthm=1
damagem=1
ebhealth=0
import math
mars=0
special=[]
gold=400
lives=10
xp=100
from commands import *
import random
worlds=[["Normal","norm.py"],["Frozen Tundra", "frozen.py"], ["Moon", "moon.py"], ["Minecraft", "blocked.py"]]
worldn=len(worlds)
worldc=random.randint(0,worldn-1)
while True:
    exec(open(worlds[worldc][1]).read())
    cw=random.randint(1,100)
    if cw==1:
        rendscreenx("Changing world...")
        worldc=random.randint(0,worldn-1)