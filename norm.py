if __name__!="__main__":
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
#Original
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
if __name__ == "__main__":
    move=random.randint(1,9)
    #move=random.randint(1,9)
    if move==1 or move==2 or move==3 or move==4 or move==5:
        #path
        path=0
        rendscreenx("The path branches into three directions: left(L), right(R), and straight(S).  Which one do you take?")
        while path!="l" and path!="L" and path!="r" and path!="R" and path!="s" and path!="S":
            path=input()
        if path == "l" or path == "L":
            rendscreenx("You go on the left path.")
            input()
            lpath=random.randint(1,11)
            if lpath==1:
                goldgotten=math.floor(xp/100)
                rendscreenx("You found a chest with " + str(goldgotten) + " gold!")
                gold+=goldgotten
                xp+=1
            elif lpath==2:
                rendscreenx("You walk into a trap and lose a life.")
                lives+=-1
                xp+=2
            elif lpath==3:
                rendscreenx("A massive ant bites you!  Lose a life!")
                lives+=-1
                xp+=3
            elif lpath==4:
                rendscreenx("You found a bomb!")
                special.append("Bomb")
                xp+=1
            elif lpath==5:
                lpath5=random.randint(1,3)
                if lpath5==1:
                    rendscreenx("You found a sword!  It grants double damage in all battles!")
                    special.append("Sword")
                    damagem=damagem*2
                    xp+=10
                else:
                    rendscreenx("You continue on the path.")
                    xp+=1
            elif lpath==6:
                rendscreenx("You got hit by a sharp leaf!  You lose a life.")
                lives+=-1
                xp+=2
            elif lpath==7:
                rendscreenx("You find some food.  You gain 4 lives!")
                lives+=4
                xp+=3
            elif lpath==8:
                rendscreenx("You find a medkit!  Gain 5 lives.")
                lives+=5
                xp+=4
            elif lpath==9:
                #Random special item!
                #rsa=random.randint
                rsa=random.randint(1,5)
                if rsa==1:
                    rendscreenx("You got a bomb!")
                    special.append("Bomb")
                elif rsa==2:
                    rendscreenx("You found a sword!  It gives 2x damage in all battles!")
                    special.append("Sword")
                    damagem=damagem*2
                elif rsa==3:
                    rsa2=random.randint(1,100)
                    if rsa2==1:
                        rendscreenx("You found the epic staff!  It grants x10 health and x10 damage in all battles!")
                        special.append("Epic Staff")
                        damagem=damagem*10
                        healthm=healthm*10
                    else:
                        rendscreenx("You got a bomb!")
                        special.append("Bomb")
                elif rsa==4:
                    rendscreenx("You found a cape that grants +500 health in all battles!")
                    ebhealth+=500
                    special.append("Cape")
                elif rsa==5:
                    rendscreenx("You found a stockpile of bombs...5 of them!")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                xp+=20
            elif lpath==10:
                rendscreenx("You fall into a trap and lose a life.")
                lives+=-1
                xp=xp+5
            elif lpath==11:
                rendscreenx("You go to a villge.  They give you 50 gold to stay away from them.  You stay away.")
                gold+=50
                xp+=10
            input()
        elif path=="r" or path=="R":
            rpath=random.randint(1,10)
            if rpath==1:
                rendscreenx("You found a chest with " + str(100) + " gold!")
                gold+=100
                xp+=2
            elif rpath==2:
                rendscreenx("You step in quicksand. Lose a life!")
                lives+=-1
                xp+=3
            elif rpath==3:
                rendscreenx("A massive frog bites you!  Lose a life!")
                lives+=-1
                xp+=4
            elif rpath==4:
                rendscreenx("You found a bomb!")
                special.append("Bomb")
                xp+=1
            elif rpath==5:
                rpath5=random.randint(1,3)
                if rpath5==1:
                    rendscreenx("You found a staff!  It grants double health in all battles!")
                    healthm=healthm*2
                    special.append("Staff")
                    xp+=15
                else:
                    rendscreenx("You continue on the path.")
                    xp+=1
            elif rpath==6:
                rendscreenx("You got in poison ivy!  You lose a life.")
                lives+=-1
                xp+=2
            elif rpath==7:
                rendscreenx("You find some water.  You gain 2 lives!")
                lives+=2
                xp+=5
            elif rpath==8:
                rendscreenx("You find a medkit!  Gain 8 lives.")
                lives+=8
                xp+=1
            elif rpath==9:
                #Random special item!
                #rsa=random.randint
                rsa=random.randint(1,5)
                if rsa==1:
                    rendscreenx("You got 2 bombs!")
                    special.append("Bomb")
                    special.append("Bomb")
                elif rsa==2:
                    rendscreenx("You found a sword!  It gives 2x damage in all battles!")
                    special.append("Sword")
                    damagem=damagem*2
                elif rsa==3:
                    rsa2=random.randint(1,1000)
                    if rsa2==1:
                        rendscreenx("You found the epic sword!  It grants x100 health and x100 damage in all battles!")
                        special.append("Epic Sword")
                        damagem=damagem*100
                        healthm=healthm*100
                        xp+=500
                    else:
                        rendscreenx("You got a bomb!")
                        special.append("Bomb")
                elif rsa==4:
                    rendscreenx("You found a cloak that grants +500 health in all battles!")
                    ebhealth+=500
                    special.append("Cloak")
                elif rsa==5:
                    rendscreenx("You found a stockpile of bombs...10 of them!")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                    special.append("Bomb")
                xp+=20
            elif rpath==10:
                rendscreenx("You get sick and lose a life!")
                lives+=-1
                xp=xp+5
            input()
        else:
            cpath=random.randint(1,10)
            if cpath==1:
                rendscreenx("You found a book that's pretty good.  However, it does nothing.")
                book=random.randint(1,5)
                if book==1:
                    special.append("Harry Potter and the Sorcer's Stone")
                elif book==2:
                    special.append("The Name of this Book is Secret")
                elif book==3:
                    special.append("Surely You’re Joking, Mr. Feynman!")
                elif book==4:
                    special.append("Magnus Chase and the Gods of Asgard")
                elif book==5:
                    special.append("This book hasn't been written yet.")
                xp+=30
            elif cpath==2:
                berriese=0
                while berriese!="y" and berriese!="Y" and berriese!="n" and berriese!="N":
                    rendscreenx("You find some berries.  Do you eat them! Y/N")
                    berriese=input()
                if berriese=="y" or berriese=="Y":
                    rendscreenx("They were poisoned! Lose a life!")
                    lives+=-1
                    xp+=10
                else:
                    rendscreenx("You don't eat the berries.")
                    xp+=2
            elif cpath==3:
                berriese=0
                while berriese!="y" and berriese!="Y" and berriese!="n" and berriese!="N":
                    rendscreenx("You find some berries.  Do you eat them! Y/N")
                    berriese=input()
                if berriese=="y" or berriese=="Y":
                    rendscreenx("They tasted good! Gain a life!")
                    lives+=1
                    xp+=10
                else:
                    rendscreenx("You don't eat the berries.")
                    xp+=2
            elif cpath==4:
                berriese=0
                while berriese!="y" and berriese!="Y" and berriese!="n" and berriese!="N":
                    rendscreenx("You find some berries.  Do you eat them! Y/N")
                    berriese=input()
                if berriese=="y" or berriese=="Y":
                    rendscreenx("You found a bomb under them!")
                    special.append("Bomb")
                    xp+=10
                else:
                    rendscreenx("You don't eat the berries.")
                    xp+=2
            elif cpath==5:
                rendscreenx("You found a cloak!  It grants +300 health in all battles!")
                special.append("Cloak")
                ebhealth+=300
                xp+=5
            elif cpath==6:
                goldf=random.randint(1,xp)
                rendscreenx("You found " + str(goldf) + " gold!")
                gold+=goldf
                xp+=4
            elif cpath==7:
                livel=random.randint(2,4)
                rendscreenx("You fell into a snake hole.  The snake bit you!  Lose " + str(livel) + "lives!")
                lives+=-livel
                xp+=livel*4
            elif cpath==8:
                rendscreenx("You lie down for a nap.")
                input()
                rendscreenx("After you wake up, you see a staff ahead...")
                input()
                rendscreenx("You go to touch it...")
                input()
                rendscreenx("It zaps you! Lose 2 lives!")
                lives+=-2
                input()
                rendscreenx("However, you pick it up, and it's super powerful...")
                input()
                rendscreenx("The lightning staff grants 4x attack power!")
                damagem=damagem*4
                special.append("Lightning Staff")
                xp+=40
            else:
                rendscreenx("You fall down... lose 3 lives!")
                lives+=-3
                xp+=8
            input()
    elif move==6:
        #normal enemy
        #Types
        #Monster 5 HP per XP, bombs destroy Rewards 30 XP
        #Dragon 20 HP per XP, bombs do 500 damage Rewards 60 XP
        #Bear 10 HP per XP, bombs destroy Rewards 20 XP
        #Giant 30 HP per XP, bombs do 1500 damage Rewards 100 XP
        #Mars refugee 40 HP per xp, bombs destroy
        if mars==1:
            type=random.randint(1,5)
        else:
            type=random.randint(1,4)
        if type==1:
            enemy="monster"
            enemyh=5*xp
            bomba="destroy "
            xpe=30
            bombm=9999999999999999999999999999
        elif type==2:
            enemy="dragon"
            enemyh=20*xp
            bomba="do 1000 damage to "
            xpe=60
            bombm=1000
        elif type==3:
            enemy="bear"
            enemyh=10*xp
            bomba="destroy "
            xpe=20
            bombm=9999999999999999999999999999
        elif type==4:
            enemy="giant"
            enemyh=30*xp
            bomba="do 1500 damage to "
            xpe=100
            bombm=1500
        else:
            enemy="martian"
            enemyh=40*xp
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
        input()
    elif move==7:
        #arena!
        exitarena=0
        arenatype=random.randint(1,2)
        #up to ten in later updates
        if arenatype==1:
            #5 monters
            #same as original arena, no XP changes
            entry=random.randint(20,xp)
            rendscreenx("You walk up to an arena.  There are five monsters.  Here are the arena rules:")
            print("You must defeat all 5 enemies.")
            print("To enter, you must pay " + str(entry) + " gold.")
            input()
            rendscreenx("You enter the arena.")
            gold+=-20
            rendscreenx("You choose to enter the arena.")
            input()
            gold+=-20
            rendscreenx("Moster 1: health: 500")
            input()
            health=healthm*1000+ebhealth
            enemyh=500
            while enemyh>0:
                rendscreenf()
                fmove="0"
                if "Bomb" in special:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                        fmove=input("K to kick or P to punch or B to use bomb(bombs only do 1000 damage in this battle)")
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
                    enemyh+=-1000*damagem
                    input()
                else:
                    sub=math.floor(random.random()*10)
                    enemyh+=-sub*3.1*damagem*10
                    print("Damage dealt: "+ str(sub*3.1*damagem*10))
                    input()
                rendscreenf()
                if enemyh>0:
                    sub=math.floor(random.random()*100)
                    health+=-40
                    print("Monster attacks!  Damage dealt: "+ str(sub+40))
                    input()
                if health<0:
                    youlose=0
                    print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                    while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                        youlose=input()
                    if youlose=="A" or youlose=="a":
                        gold+=-300
                        health=healthm*1000+ebhealth
                    else:
                        enemyh=-1
                        exitarena=1
            if exitarena!=1:
                rendscreenx("You beat enemy one!")
                input()
                rendscreenx("Enemy 2: health: 1000")
                input()
                health=healthm*1000+ebhealth
                enemyh=1000
                while int(enemyh)>0:
                    rendscreenf()
                    fmove="0"
                    if "Bomb" in special:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                            fmove=input("K to kick or P to punch or B to use bomb(bombs only do 1000 damage in this battle)")
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
                        enemyh+=-1000*damagem
                        input()
                    else:
                        sub=math.floor(random.random()*10)
                        enemyh+=-sub*3.1*damagem*10
                        print("Damage dealt: "+ str(sub*3.1*damagem*10))
                        input()
                    rendscreenf()
                    if enemyh>0:
                        sub=math.floor(random.random()*100)
                        health+=-40
                        print("Monster attacks!  Damage dealt: "+ str(sub+40))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                        while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                            youlose=input()
                        if youlose=="A" or youlose=="a":
                            gold+=-300
                            health=healthm*1000+ebhealth
                        else:
                            enemyh=-1
                            exitarena=1
                if exitarena!=1:
                    rendscreenx("You beat enemy 2!")
                    input()
                    rendscreenx("Enemy 3: health: 1250")
                    input()
                    health=healthm*1000+ebhealth
                    enemyh=1250
                    while enemyh>0:
                        rendscreenf()
                        fmove="0"
                        if "Bomb" in special:
                            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                fmove=input("K to kick or P to punch or B to use bomb(bombs only do 1000 damage in this battle)")
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
                            enemyh+=-1000*damagem
                            input()
                        else:
                            sub=math.floor(random.random()*10)
                            enemyh+=-sub*3.1*damagem*10
                            print("Damage dealt: "+ str(sub*3.1*damagem*10))
                            input()
                        rendscreenf()
                        if enemyh>0:
                            sub=math.floor(random.random()*100)
                            health+=-40
                            print("Monster attacks!  Damage dealt: "+ str(sub+40))
                            input()
                        if health<0:
                            youlose=0
                            print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                            while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                youlose=input()
                                if youlose=="A" or youlose=="a":
                                    gold+=-300
                                    health=healthm*1000+ebhealth
                                else:
                                    enemyh=-1
                                    exitarena=1
                    if exitarena!=1:
                        rendscreenx("You beat enemy 3!")
                        input()
                        rendscreenx("Enemy 4: health: 1500")
                        health=healthm*1000+ebhealth
                        enemyh=1500
                        while enemyh>0:
                            rendscreenf()
                            fmove="0"
                            if "Bomb" in special:
                                while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                    fmove=input("K to kick or P to punch or B to use bomb(bombs only do 1000 damage in this battle)")
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
                                enemyh+=-1000*damagem
                                input()
                            else:
                                sub=math.floor(random.random()*10)
                                enemyh+=-sub*3.1*damagem*10
                                print("Damage dealt: "+ str(sub*3.1*damagem*10))
                                input()
                            rendscreenf()
                            if enemyh>0:
                                sub=math.floor(random.random()*100)
                                health+=-40
                                print("Monster attacks!  Damage dealt: "+ str(sub+40))
                                input()
                            if health<0:
                                youlose=0
                                print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                                while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                    youlose=input()
                                if youlose=="A" or youlose=="a":
                                    gold+=-300
                                    health=healthm*1000+ebhealth
                                else:
                                    enemyh=-1
                                    exitarena=1
                        if exitarena!=1:
                            rendscreenx("You beat enemy 4")
                            input("Final enemy: health: secret")
                            health=healthm*1000+ebhealth
                            enemyhs=2000
                            enemyh="Secret"
                            while enemyhs>0:
                                rendscreenf()
                                fmove="0"
                                if "Bomb" in special:
                                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                        fmove=input("K to kick or P to punch or B to use bomb(bombs only do 1000 damage in this battle)")
                                else:
                                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                                        fmove=input("K to kick or P to punch")
                                if fmove=="k" or fmove=="K":
                                    sub=math.floor(random.random()*10)+13
                                    enemyhs+=-sub*damagem*10
                                    print("Damage dealt: "+ str(sub*damagem*10))
                                    input()
                                elif fmove=="adminpass":
                                    enemyhs=0
                                    input()
                                elif fmove=="l":
                                    health=-1
                                    input()
                                elif fmove=="B" or fmove=="b":
                                    special.remove("Bomb")
                                    enemyhs+=-1000*damagem
                                    input()
                                else:
                                    sub=math.floor(random.random()*10)
                                    enemyhs+=-sub*3.1*damagem*10
                                    print("Damage dealt: "+ str(sub*3.1*damagem*10))
                                    input()
                                    rendscreenf()
                                if enemyhs>0:
                                    sub=math.floor(random.random()*100)
                                    health+=-40
                                    print("Monster attacks!  Damage dealt: "+ str(sub+40))
                                    input()
                                if health<0:
                                    youlose=0
                                    print("You lost!  You can pay 300 gold to try this arena again(A), or you can just lose(L).")
                                    while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                        youlose=input()
                                    if youlose=="A" or youlose=="a":
                                        gold+=-300
                                        health=healthm*1000+ebhealth
                                    else:
                                        enemyhs=-1
                                        enemyh=-1
                                        exitarena=1
                                if exitarena!=1:
                                    enemyh=-1
                                    rendscreenx("You beat all the enemies!")
                                    input()
            if enterarena1=="y" or enterarena1=="Y" and exitarena==0:
                rendscreenx("Prizes")
                input()
                rendscreenx(str(entry*5) + " gold")
                gold+=entry*5
                input()
                rendscreenx("5 bombs")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                input()
                rendscreenx("5 lives")
                lives+=5
                input()
                xp+200
        elif arenatype==2:
            #3 dragons
            #Huge XP
            #HP based on XP
            #1st dragon 10 HP per XP
            #2nd dragon 20 HP per XP
            #3rd dragon random.randint(20,40) HP per XP
            rendscreenx("You walk up to an arena.  There are three dragons.  Here are the arena rules:")
            print("You must defeat all 3 enemies.")
            print("To enter, you must pay 200 gold.")
            input()
            rendscreenx("You enter the arena.")
            exitarena=0
            gold+=-200
            health=healthm*1000+ebhealth
            enemyh=10*xp
            rendscreenx("Dragon 1: " + str(enemyh) + " health")
            input()
            while enemyh>0:
                rendscreenf()
                fmove="0"
                if "Bomb" in special:
                    while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                        fmove=input("K to kick or P to punch or B to use bomb(bombs only do 500 damage in this battle)")
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
                    enemyh+=-500*damagem
                    input()
                else:
                    sub=math.floor(random.random()*10)
                    enemyh+=-sub*3.1*damagem*10
                    print("Damage dealt: "+ str(sub*3.1*damagem*10))
                    input()
                rendscreenf()
                if enemyh>0:
                    sub=math.floor(random.random()*100)
                    health+=-40
                    print("Dragon attacks!  Damage dealt: "+ str(sub+40))
                    input()
                if health<0:
                    youlose=0
                    print("You lost!  You can pay 1000 gold to try this arena again(A), or you can just lose(L).")
                    while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                        youlose=input()
                    if youlose=="A" or youlose=="a":
                        gold+=-1000
                        health=healthm*1000+ebhealth
                    else:
                        enemyh=-1
                        exitarena=1
            if exitarena!=1:
                health=healthm*1000+ebhealth
                enemyh=20*xp
                rendscreenx("Dragon 2: " + str(enemyh) + " health")
                input()
                while enemyh>0:
                    rendscreenf()
                    fmove="0"
                    if "Bomb" in special:
                        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                            fmove=input("K to kick or P to punch or B to use bomb(bombs only do 500 damage in this battle)")
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
                        enemyh+=-500*damagem
                        input()
                    else:
                        sub=math.floor(random.random()*10)
                        enemyh+=-sub*3.1*damagem*10
                        print("Damage dealt: "+ str(sub*3.1*damagem*10))
                        input()
                    rendscreenf()
                    if enemyh>0:
                        sub=math.floor(random.random()*100)
                        health+=-40
                        print("Dragon attacks!  Damage dealt: "+ str(sub+40))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost!  You can pay 1000 gold to try this arena again(A), or you can just lose(L).")
                        while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                            youlose=input()
                        if youlose=="A" or youlose=="a":
                            gold+=-1000
                            health=healthm*1000+ebhealth
                        else:
                            enemyh=-1
                            exitarena=1
                if exitarena!=1:
                    health=healthm*1000+ebhealth
                    enemyh=random.randint(20,40)*xp
                    rendscreenx("Dragon 3: " + str(enemyh) + " health")
                    input()
                    while enemyh>0:
                        rendscreenf()
                        fmove="0"
                        if "Bomb" in special:
                            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                                fmove=input("K to kick or P to punch or B to use bomb(bombs only do 500 damage in this battle)")
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
                            enemyh+=-500*damagem
                            input()
                        else:
                            sub=math.floor(random.random()*10)
                            enemyh+=-sub*3.1*damagem*10
                            print("Damage dealt: "+ str(sub*3.1*damagem*10))
                            input()
                        rendscreenf()
                        if enemyh>0:
                            sub=math.floor(random.random()*100)
                            health+=-40
                            print("Dragon attacks!  Damage dealt: "+ str(sub+40))
                            input()
                        if health<0:
                            youlose=0
                            print("You lost!  You can pay 1000 gold to try this arena again(A), or you can just lose(L).")
                            while youlose!="A" or youlose!="a" or youlose!="L" or youlose!="l":
                                youlose=input()
                            if youlose=="A" or youlose=="a":
                                gold+=-1000
                                health=healthm*1000+ebhealth
                            else:
                                enemyh=-1
                                exitarena=1
            if exitarena!=1:
                rendscreenx("You won!")
                input()
                rendscreenx("Rewards:")
                input()
                rendscreenx("1000 gold!")
                gold+=1000
                input()
                rendscreenx("10 bombs")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                input()
                rendscreenx("2 lives")
                input()
                rendscreenx("A dragon staff: grants +1000 health in all battles!")
                special.append("Dragon Staff")
                ebhealth+=1000
                input()
                xp+=500
            else:
                rendscreenx("You lost the arena :(")
                input()
                xp+=10
    elif move==8:
        if xp>10000 and mars==0:
            #invasion from Mars!
            i=0
            while i<20:
                i+=1
                enemy="Martian Drone"
                enemyh=50000
                bomba="destroy "
                xpe=30
                bombm=9999999999999999999999999999
                mars=1
                rendscreeenx("You come up to a " + enemy + "!")
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
                        sub=math.floor(random.random()*10000)
                        health+=-4000
                        print(enemy + " attacks!  Damage dealt: "+ str(sub+4000))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost a life!")
                        lives+=-1
                rendscreenx("You beat the "+enemy+"!")
                input()
            i=0
            while i<20:
                i+=1
                enemy="Martian"
                enemyh=60000
                bomba="destroy "
                xpe=30
                bombm=9999999999999999999999999999
                mars=1
                rendscreeenx("You come up to a " + enemy + "!")
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
                        sub=math.floor(random.random()*10000)
                        health+=-4000
                        print(enemy + " attacks!  Damage dealt: "+ str(sub+4000))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost a life!")
                        lives+=-1
                rendscreenx("You beat the "+enemy+"!")
                input()
            i=0
            while i<10:
                i+=1
                enemy="Martian UFO"
                enemyh=100000
                bomba="destroy "
                xpe=30
                bombm=9999999999999999999999999999
                mars=1
                rendscreeenx("You come up to a " + enemy + "!")
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
                        sub=math.floor(random.random()*20000)
                        health+=-8000
                        print(enemy + " attacks!  Damage dealt: "+ str(sub+8000))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost a life!")
                        lives+=-1
                rendscreenx("You beat the "+enemy+"!")
                input()
            i=0
            while i<2:
                i+=1
                enemy="Martian Space Station"
                enemyh=500000
                bomba="deal 1000 damage to "
                xpe=30
                bombm=1000
                mars=1
                rendscreeenx("You come up to a " + enemy + "!")
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
                        sub=math.floor(random.random()*18000)
                        health+=-7000
                        print(enemy + " attacks!  Damage dealt: "+ str(sub+8000))
                        input()
                    if health<0:
                        youlose=0
                        print("You lost a life!")
                        lives+=-1
                rendscreenx("You beat the "+enemy+"!")
                input()
            enemy="Martian Leader"
            enemyh=500000
            bomba="deal 2000 damage to "
            xpe=30
            bombm=2000
            mars=1
            rendscreeenx("You come up to a " + enemy + "!")
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
                    sub=math.floor(random.random()*18000)
                    health+=-7000
                    print(enemy + " attacks!  Damage dealt: "+ str(sub+8000))
                    input()
                if health<0:
                    youlose=0
                    print("You lost a life!")
                    lives+=-1
            rendscreenx("You beat the "+enemy+"!")
            input()
            if lives>0:
                rendscreenx("You beat the Martian invasion!!!")
                input()
                rendscreenx("Your loot:")
                input()
                rendscreenx("100 Bombs")
                input()
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                special.append("Bomb")
                rendscreenx("10 swords that grant 2x damage in all battles each!")
                damagem=damagem*1024
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                special.append("Sword")
                input()
                rendscreenx("A ray gun... grants 100 damage in all battles!")
                damagem=damagem*100
                special.append("Ray Gun")
                input()
                rendscreenx("A martian cloak: gives +100000 health in all battles!")
                ebhealth+=100000
                input()
                mars=1
                xp+=5000
            else:
                rendscreenx("You were defeated by Mars :(")
                xp+=-1000
                input()
        else:
            rendscreenx("You continue on the path.")
            xp+=1
            input()
    elif move==9:
        rendscreenx("You walk up to a village!")
        input()
        village=random.randint(1,6)
        if village==1:
            #Gods
            rendscreenx("The villagers praise you as their god.  They give you 50 gold.")
            gold+=50
            xp+=10
        elif village==2:
            #Gods
            rendscreenx("The villagers praise you as their god.  They give a sword that grants 2x damage in all battles.")
            special.append("Sword")
            damagem=damagem*2
            xp+=10
        elif village==3:
            #Gods
            rendscreenx("The villagers praise you as their god.  Unfortuatly, they hate their gods.  Lose a life.")
            lives+=-1
            xp+=15
        elif village==4:
            #Gods
            rendscreenx("The villagers praise you as their god.  They find material objects usless, but experience priceless.")
            xp+=100
        elif village==5:
            #Gods
            rendscreenx("The villagers praise you as their god.  They give you 1000 gold.")
            gold+=1000
        elif village==6:
            rendscreenx("The villagers fight you!")
            enemy="villager"
            enemyh=10*xp
            bomba="destroy "
            xpe=10
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
                    sub=math.floor(random.random()*100*xp/40)
                    health+=-40*xp/40
                    print(enemy + " attacks!  Damage dealt: "+ str(sub+40*xp/40))
                    input()
                if health<0:
                    youlose=0
                    print("You lost a life!")
                    lives+=-1
            rendscreenx("You beat the "+enemy+"!")
            xp+=xpe
        input()