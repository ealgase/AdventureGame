ender=0
moonmon=0
healthm=4
damagem=8
ebhealth=250
import math
mars=0
special=['Glove', 'Fur Coat', 'Spear', 'Bomb', 'Bomb', 'Golden Vest', 'Sword', 'Bomb', 'Bomb', 'Bomb', 'Bomb', 'Bomb', 'Staff']
gold=400
lives=10
xp=100
import random
worlds=[["Normal","norm.py"],["Frozen Tundra", "frozen.py"], ["Moon", "moon.py"], ["Minecraft", "blocked.py"]]
worldn=len(worlds)
worldc=random.randint(0,worldn-1)
while True:
    exec(open(worlds[worldc][1]).read())
    cw=random.randint(1,100)
    if cw==1:
        rendscreenx("Changing world...")
        input()
        worldc=random.randint(0,worldn-1)
        print("Switching to world " + worlds[worldc][0])
        input()
