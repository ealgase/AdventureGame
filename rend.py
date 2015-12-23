
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