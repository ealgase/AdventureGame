#Moon
#another world, in this one you teleport to the moon
import random
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
    print("Gold: "+ str(gold) + " Lives: " + str(lives))
    print("Special items: "+str(special))
    print("Health: "+str(health)+" Enemy Health: "+str(enemyh))
    print("--------------------------------------------------------------------------------")
def cls():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
moonm=random.randint(1,3)
if moonm==1:
    rendscreenx("You walk around on the moon.")
    xp+=10
elif moonm==2:
    if moonmon==1:
        type=random.randint(1,5)
    else:
        type=random.randint(1,4)
    if type==1:
        enemy="monster"
        enemyh=5*xp
        bomba="destroy "
        xpe=40
        bombm=9999999999999999999999999999
    elif type==2:
        enemy="dust bunny"
        enemyh=2*xp
        bomba="destroy "
        xpe=30
        bombm=9999999999999999999999999999
    elif type==3:
        enemy="moon dragon"
        enemyh=40*xp
        bomba="don't affect "
        xpe=200
        bombm=0
    elif type==4:
        enemy="moon stalker"
        enemyh=20*xp
        bomba="do 1500 damage to "
        xpe=100
        bombm=1500
    else:
        enemy="cow"
        enemyh=90*xp
        bomba="destroy "
        xpe=200
        bombm=9999999999999999999999999999
    rendscreenx("You come up to a " + enemy + "!")
    input()
    rendscreenx("It wants to fight you!")
    health=healthm*1000+ebhealth
    while enemyh>0:
        rendscreenf()
        fmove="0"
        if "Bomb" in special:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                fmove=input("K to kick or P to punch or B to use bomb(bombs "+bomba+"to the enemy.")
        else:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                fmove=input("K to kick or P to punch")
        if fmove=="k" or fmove=="K":
            sub=math.floor(random.random()*10)+13
            enemyh+=-sub*damagem*10
            print("Damage dealt: "+ str(sub*damagem*10))
            input()
        elif fmove=="adminpass":
            enemyh=0
            input()
        elif fmove=="l":
            health=-1
            input()
        elif fmove=="B" or fmove=="b":
            special.remove("Bomb")
            enemyh+=-bombm*damagem
            input()
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*3.1*damagem*10
            print("Damage dealt: "+ str(sub*3.1*damagem*10))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*100*xp/50)
            health+=-40*xp/50
            print(enemy + " attacks!  Damage dealt: "+ str(sub+40*xp/50))
            input()
        if health<0:
            youlose=0
            print("You lost a life!")
            lives+=-1
    rendscreenx("You beat the "+enemy+"!")
    xp+=xpe
elif moonm==3:
    rendscreenx("You find some cheese!")
    input()
    rendscreenx("You you eat it? Y/N")
    eatc=0
    while eatc!='y' or eatc!='Y' or eatc!='n' or eatc!='N':
        eatc=input()
    cheeseg=random.randint(1,2)
    if eatc=='y' or eatc=='Y':
        rendscreenx("You eat the cheese.")
        input()
        if cheeseg==1:
            rendscreenx("It was good! Gain a life!")
            lives+=1
        elif cheeseg==2:
            rendscreenx("It was posioned!  Lose a life!")
input()