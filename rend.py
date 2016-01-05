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
from vfg import *
def cls():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
def rendscreenx(text):
    cls()
    print("--------------------------------------------------------------------------------")
    print("Gold: "+ str(gold) + " Lives: " + str(lives) + " XP: "+ str(xp))
    print("Special items: "+str(special))
    print("--------------------------------------------------------------------------------")
    print(text)
def rendscreenf():
    cls()
    print("--------------------------------------------------------------------------------")
    print("Gold: "+ str(gold) + " Lives: " + str(lives) + " XP: "+str(xp))
    print("Special items: "+str(special))
    print("Health: "+str(health)+" Enemy Health: "+str(enemyh))
    print("--------------------------------------------------------------------------------")
def rendscreen(text):
    cls()
    print("--------------------------------------------------------------------------------")
    print("Gold: "+ str(gold) + " Lives: " + str(lives))
    print("Special items: "+str(special))
    print("--------------------------------------------------------------------------------")
    print(text)