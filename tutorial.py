lives=5
gold=10
damagem=1
special=[]
healthm=1
width=80
height=24
import time
import random
import math
def centerText(text, sidech):
    spacesOnSide = (width - (len(text) if len(text) % 2 == 0 else len(text) + 1) - (len(sidech) * 2)) / 2
    appendSpace = " "
    i = 1
    while i < spacesOnSide:
        appendSpace = appendSpace + " "
        i+=1
    retText = sidech + appendSpace + text + appendSpace + sidech
    return retText
def rendscreenx(text):
    cls()
    dashNum="-"
    i = 1
    while i < width:
        dashNum = dashNum + "-"
        i+=1
    print(dashNum);
    print(centerText("Adventure Game", "|"))
    print(dashNum);
    print(centerText("Gold: "+ str(gold) + "      Lives: " + str(lives), "|" + "      XP: " + str(xp)))
    print(centerText(" Special items: "+str(special), "|"))
    print(dashNum)
    lines = 6
    while lines < height - 2:
        print(centerText("  ", "|"))
        lines+=1
    print(centerText(text, "|"))
def randint(sinput,  einput):
    random.randint(sinput,einput)
def rendscreen(text):
    cls()
    dashNum="-"
    i = 1
    while i < width:
        dashNum = dashNum + "-"
        i+=1
    print(dashNum);
    print(centerText("Adventure Game", "|"))
    print(dashNum);
    print(centerText("Gold: "+ str(gold) + "      Lives: " + str(lives), "|"))
    print(centerText(" Special items: "+str(special), "|"))
    print(dashNum)
    lines = 6
    while lines < height - 2:
        print(centerText("  ", "|"))
        lines+=1
    print(centerText(text, "|"))
def rendscreenf():
    cls()
    dashNum="-"
    i = 1
    while i < width:
        dashNum = dashNum + "-"
        i+=1
    print(dashNum);
    print(centerText("Adventure Game", "|"))
    print(dashNum);
    print(centerText("Gold: "+ str(gold) + "      Lives: " + str(lives), "|"))
    print(centerText(" Special items: "+str(special), "|"))
    print(centerText("Health: "+str(health)+" Enemy Health: "+str(enemyh), "|"))
    print(dashNum)
    lines = 7
    while lines < height - 2:
        print(centerText("  ", "|"))
        lines+=1
def cls():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

cls()
print("Press enter to go to the next screen.")
input()
cls()
print("--------------------------------------------------------------------------------")
print("-----------Welcome to the forest------------------------------------------------")
print("-----------Are you ready?-------------------------------------------------------")
print("--------------------------------------------------------------------------------")
print("Press Enter to Continue...")
input("")
cls()
lives=5
gold=10
move="None"
rdone=0
ldone=0
while move!="L" and move!="l" and move!="R" and move!="R" and move!="s" and move!="S":
    rendscreen("You are walking in a forest.  You come to a part you don't know. You go ahead.")
    move=input("Do you go left(L), right(R) or straight(S)")
    if move=="L" or move=="l":
        if ldone==1:
            rendscreen("You've already gone here!")
            input()
            move="0"
        else:
            rendscreen("You found a chest! Inside it was 5 bars of gold.(enter to continue)")
            input()
            gold +=5
            rendscreen("It's at a dead end, however. You walk back.")
            input()
            move="0"
            ldone=1
    elif move=="R" or move=="r":
        if rdone==1:
            rendscreen("You've already gone here!")
            input()
            move="0"
        else:
            rendscreen("You walk into a trap and lose a life.(enter to continue)")
            input()
            lives+=-1
            rendscreen("You walk back.")
            input()
            move="0"
            rdone=1
rendscreen("You walk forward for a while.(enter to continue)")
input()
rendscreen("The ground begins to shake...(enter to continue)")
input()
cls()
print("Louder...")
time.sleep(1)
rendscreen("You come up to a monster!")
time.sleep(1)
rendscreen("'I will eat you!'")
time.sleep(1)
rendscreen("How to fight: Press K to kick and P to punch.")
input()
rendscreen("When it's your enemy's turn, hope for the best!")
input()
rendscreen("Press enter to start.")
input()
health=1000
enemyh=200
while enemyh>0:
    rendscreenf()
    fmove="0"
    while fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
        fmove=input("K to kick or P to punch")
    if fmove=="K" or fmove=="k":
        sub=math.floor(random.random()*10)+5
        enemyh=enemyh-sub*10
        print("Damage dealt: "+ str(sub*10))
        input()
    elif fmove=="adminpass":
        enemyh=0
    else:
        sub=math.floor(random.random()*10)
        enemyh+=-sub*18
        print("Damage dealt: "+ str(sub*18))
        input()
    rendscreenf()
    time.sleep(.2)
    if enemyh>0:
        health+=-math.floor(random.random()*100)
        health+=-60
        print("Monster attacks! Damage dealt: "+ str(sub+60))
        input()
rendscreen("You won the battle!")
input()
rendscreen("The monster had 20 gold and you gained two lives from defeating him!")
gold+=20
lives+=2
input()
rendscreen("You continue along the path.")
input()
ebhealth=0
special=[]
berries=0
while berries != "y" and berries != "Y" and berries != "N" and berries != "n":
    rendscreen("You find some berries.  Do you eat them? Y for yes and N for no.")
    berries=input()
if berries=="y" or berries=="Y":
    rendscreen("Under the leaves, you found a glove!  It grants +50 health in all battles!")
    ebhealth+=50
    special.append("Glove")
    input()
    rendscreen("After eating some berries, you continue walking.")
else:
    rendscreen("You continue walking.")
input()
river="0"
while river!="Y" and river!="y" and river!="N" and river!="n":
    rendscreen("After walking for quite some time, you come to a river.  There's a bear right behind you.  Do you try to cross the river? Y/N")
    river=input()
if river=="Y" or river=="y":
    rendscreen("You manage to cross the river, but you get sick and lose a life.")
    lives+=-1
else:
    rendscreen("You stay and fight the bear!")
    input()
    health=1000+ebhealth
    enemyh=400
    while enemyh>0:
        rendscreenf()
        fmove="0"
        while fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
            fmove=input("K to kick or P to punch")
        if fmove=="K" or fmove=="k":
            sub=math.floor(random.random()*10)+6
            enemyh=enemyh-sub*10
            print("Damage dealt: "+ str(sub*10))
            input()
        elif fmove=="adminpass":
            enemyh=0
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*1.85*10
            print("Damage dealt: "+ str(sub*1.85*10))
            input()
        rendscreenf()
        time.sleep(.2)
        if enemyh>0:
            sub=math.floor(random.random()*10)*1.4*10
            health+=-sub
            health+=-4*10
            print("Bear attacks! Damage dealt: "+ str(sub+4*10))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
    rendscreen("You won the battle!!!")
    input()
    rendscreen("You keep the fur coat from the bear.  It gives you +200 health in all battles!")
    input()
    ebhealth+=200
    special.append("Fur Coat")
    rendscreen("You decide to put down a log and cross the river.")
input()
rendscreen("Now that you're across the river, you decide to start exploring.")
input()
move="0"
lgone="0"
rgone="0"
while move!="L" and move!="l" and move!="R" and move!="R" and move!="s" and move!="S":
    rendscreen("Do you go left(L), right(R) or straight(S)")
    move=input()
    if move=="l" or move=="L":
        if lgone=="0":
            lgone="1"
            rendscreen("You go left. You find some food.  Do you eat it? Y/N")
            food1=0
            while food1 != "y" and food1 != "Y" and food1 != "N" and food1 != "n":
                food1=input()
            if food1=="y" or food1=="Y":
                rendscreen("It was poisoned!  Lose a life")
                lives+=-1
                input()
            else:
                rendscreen("You decide not to eat and you go back.")
                input()
        else:
            rendscreen("You've already gone this way!")
            input()
        move="0"
    elif move=="r" or move=="R":
        if rgone=="0":
            rgone="1"
            rendscreen("You found a chest!  Inside it is 25 gold!")
            gold+=25
            input()
        else:
            rendscreen("You've already gone this way!")
            input()
        move="0"
    else:
        rendscreen("There's a giant!")
        input()
        rendscreen("'I demand 40 gold or I will FIGHT YOU!'")
        input()
        fight="0"
        if gold<40:
            rendscreen("You must fight the giant.")
            giantf="1"
            input()
        else:
            watf="?"
            rendscreen("Do you want to fight? Y/N")
            while watf!="Y" and watf!="y" and watf!="N" and watf!="n":
                watf=input()
            if watf=="y" or watf=="Y":
                giantf="1"
            else:
                giantf="0"
if giantf=="1":
    health=1000+ebhealth
    enemyh=1300
    while enemyh>0:
        rendscreenf()
        fmove="0"
        while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
            fmove=input("K to kick or P to punch")
        if fmove=="k" or fmove=="K":
            sub=math.floor(random.random()*10)+6
            enemyh+=-sub*10
            print("Damage dealt: "+ str(sub*10))
            input()
        elif fmove=="adminpass":
            enemyh=0
        elif fmove=="l":
            health=-1
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*1.9*10
            print("Damage dealt: "+ str(sub*1.9*10))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*10)*1.5
            health+=-sub*10
            health+=-6*10
            print("Giant attacks!  Damage dealt: "+ str(sub+6*10))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
            print("You lost a life.")
            input()
    rendscreen("You defeated the giant!")
    input()
    rendscreen("The giant was hoarding 200 gold!")
    input()
    gold+=200
    rendscreen("You also gain a life from defeating the giant.")
    input()
    lives+=1
    rendscreen("The giant also had a spear.  It grants double damage in all battles!")
    damagem+=1
    special.append("Spear")
    input()
else:
    rendscreen("You decided not to fight the giant and pay him 40 gold.")
    gold+=-40
    input()
rendscreen("You continue walking, now that you're past the giant.")
input()
rendscreen("On the path, you find a bomb!  Use it once to destroy an enemy.  You can only use it once, however, so use it wisely")
special.append("Bomb")
input()
rendscreen("Now that you have the bomb, you continue walking.")
#special.remove("Bomb")###How to remove bomb!!!
input()
rendscreen("You come up to a dragon!")
print("    \ |  (  \ ( \.(               )")
print("                      _____")
print("  \  \ \  `  `   ) \             (  ___                 / _   \\")
print(" (_`    \+   . x  ( .\            \/   \____-----------/ (o)   \_")
print("- .-               \+  ;          (  O                           \____")
print("                          )        \_____________  `              \  /")
print("(__                +- .( -'.- <. - _  VVVVVVV VV V\                 \/")
print("  .    /./.+-  . .- /  +--  - .     \______________//_              \_______")
print("(_____            ._._: <_ - <- _  (--  _AAAAAAA__A_/                  |")
print("  (__ ' /x  / x _/ (                                  \___'          \     /")
print(" , x / ( '  . / .  /                                      |           \   /")
print("    /  /  _/ /    +                                      /              \/")
print("   '  (__/                                             /                  \\")
input()
if giantf=="1":
    rendscreen("'You killed my good friend the giant!  I will EAT YOU!'")
    input()
    health=1000+ebhealth
    enemyh=1500
    while enemyh>0:
        rendscreenf()
        fmove="0"
        if "Bomb" in special:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass" and fmove!="B" and fmove!="b":
                fmove=input("K to kick or P to punch or B to use bomb")
        else:
            while fmove!="l" and fmove!="k" and fmove!="K" and fmove!="p" and fmove!="P" and fmove!="adminpass":
                fmove=input("K to kick or P to punch")
        if fmove=="k" or fmove=="K":
            sub=math.floor(random.random()*10)+6
            enemyh+=-sub*damagem*10
            print("Damage dealt: "+ str(sub*damagem*10))
            input()
        elif fmove=="adminpass":
            enemyh=0
        elif fmove=="l":
            health=-1
        elif fmove=="B" or fmove=="b":
            special.remove("Bomb")
            enemyh=0
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*1.9*damagem*10
            print("Damage dealt: "+ str(sub*1.9*damagem*10))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*10)*1.5
            health+=-sub*10
            health+=-6*10
            print("Dragon attacks!  Damage dealt: "+ str(sub+6*10))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
            print("You lost a life.")
            input()
    rendscreen("You beat the dragon!")
    input()
else:
    rendscreen("Thank you for paying the giant.  You may pass.")
    input()
    rendscreen("The dragon lets you pass, and you continue on your way.")
    input()
rendscreen("You found another bomb on the path!")
special.append("Bomb")
input()
path=0
while path != "r" and path != "R" and path != "l" and path != "L":
    rendscreen("The path branches into 2 pathes: left(l) or right(r).  Which one do you take?")
    path=input()
if path == "r" or path == "R":
    #Stuff for right path here.
    rendscreen("You go on the right path.")
    input()
    rendscreen("There's a chest!")
    input()
    rendscreen("You open it, and there's 20 gold inside!")
    gold+=20
    input()
    rendscreen("You walk farther.")
    input()
    rendscreen("You come up to... a DRAGON!")
    print("                                        *$$$$$$eeee")
    print("                                          ***$$$$$$$$e")
    print("                                                **$$$$$e")
    print("           e$$$e                                   *$$$$$")
    print("          $$$$                                     e$$$$$")
    print("         $$$$                                  ee$$$$$$$")
    print("         $$$$               ee***ee***eeeee$$$$$$$$$$$*")
    print("         $$$$e        eee$$$     $     $$$$$$$$$$$$$*        ee")
    print("         *$$$$$$$$$$$$$$$$$$ $$$ $ $$$ $$$$$$$$**      ee****WW$")
    print(" eeeeee    *$$$$$$$$$$$$$$$$  $$ $  $$ $*****        e*!!!W**!W*")
    print("$!WWWW!***ee   *************eee$$**eee$             e*!W**!!!!$")
    print(" $!!!!***WW!**eee        e**!!!!!!!!!!!***e      e**!!W*!!!!!!$")
    print(" $!!!!!!!!!*W!!!!$      $!!!!W****WWWW!!!!!$     *W!!!*WW!!!!!$")
    print(" $!!!!!!!!!WW*!!!$      *W!!*W!!!!!!!!*W!!W*     e*!!!!!!*W!!!$")
    print(" $!!!!!W***!!WW!!*e       ******WWWWW*****       $!!!W***W!**W*")
    print(" $!!!W*WW****!!*W!!*eee    ee   $!!$   ee     ee*!!W*!!!!!*W!!$")
    print("  $W*!$!!!!!!!!!!*WW!!!****!W***!!!!***W!*****!!!!$!!!!!!!!*W$")
    print("  $!W*!!!!!!!!!!!W**!WW!!!!W*!!!!!!!!!!*WW*****W!!$!!!!!!!!!W*")
    print("   *WW!!!!!!!!!W*!W**!!***W$!!!!W!!!W!!!$!!!!!!$!W*!!!!!!W**")
    print("      ****WW!W*!W$WWW!!!!!!$!!!!*WWW*!!!$!!!!!!$W$!!!WWWW*")
    print("            *$W*!!!!!*WW!!!$!!!!!!$!!!!W*!!WW**!!!*$*")
    print("              $!!!!!!!!!*W!*W!!!!!$!!!!$!W*!!!!!!!!!$")
    print("              *W!!!!!!!!!!***W!!!!$!!!!$*!!!!!!!!!!!$")
    print("               $!!!!!!!!!!!!!$!!!!$!!!W*!!!!!!!!!!!$")
    print("                $!!!!!*W!!!!!$!!!!$!!!$!!!!!W!!!!!$")
    print("eeeeeeee         $!!!!!!$!!!!$!!!!$!!!$!!!!W*!!!!W*")
    print("$!!!!W*       ee$W$!!!!!!$!!!$!!!!$!!!$!!!W*!!!!W*")
    print("$!!!*ee**e**e*WW*!!$!!!!!!$!!$!!!!$!!!$!!!$!!!WW*")
    print("$!$WW!!*******!!WWW**W*W!!$WW*!!!!$!!!$!W$WW**W!*e")
    print("$*   **WWWWWW***e*!!$!!$**!W*!!!WW*$!!!*W!!*W!!*W!*e")
    print("              e*!!!$!!W*!W*!!!!$    $!!!!$!!!$!!!$!*e")
    print("              *WWW*WW*WWW*WWWW*      *WWW*WWW*WWW*WW*")
    input()
    rendscreen("Dragon: I WILL RIP YOU APART WITH MY CLAWS!")
    input()
    health=1000+ebhealth
    enemyh=2500
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
            enemyh=enemyh-1000
            input()
        else:
            sub=math.floor(random.random()*10)
            enemyh+=-sub*3.1*damagem*10
            print("Damage dealt: "+ str(sub*3.1*damagem*10))
            input()
        rendscreenf()
        if enemyh>0:
            sub=math.floor(random.random()*20)
            health+=-sub*10
            health+=-8*10
            print("Dragon attacks!  Damage dealt: "+ str(sub+8*10))
            input()
        if health<0:
            lives+=-1
            health=1000+ebhealth
            print("You lost a life.")
            input()
    rendscreen("You beat the dragon!")
    input()
    rendscreen("The dragon was hoarding:")
    input()
    rendscreen("200 gold...")
    gold+=200
    input()
    rendscreen("A golden vest... that grants double health in all battles.")
    healthm=healthm*2
    special.append("Golden Vest")
    input()
    rendscreen("A sword, that grants 2x damage in all battles.")
    damagem=damagem*2
    special.append("Sword")
    input()
    rendscreen("The path ends there, however.  You walk back.")
    input()
exitarena=0
rendscreen("You go on the left path.")
input()
rendscreen("You walk up to an arena.  There are five monsters.  Here are the arena rules:")
print("You must defeat all 5 enemies.")
print("To enter, you must pay 20 gold.")
input()
enterarena1=0
rendscreen("Do you want to enter? Y/N")
while enterarena1!="y" and enterarena1!="Y" and enterarena1!="n" and enterarena1!="N":
    enterarena1=input("Do you want to enter? Y/N: ")
if enterarena1=="y" or enterarena1=="Y":
    rendscreen("You choose to enter the arena.")
    input()
    gold+=-20
    rendscreen("Moster 1: health: 500")
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
            enemyh=-1
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
        rendscreen("You beat enemy one!")
        input()
        rendscreen("Enemy 2: health: 1000")
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
                enemyh=-1
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
            rendscreen("You beat enemy 2!")
            input()
            rendscreen("Enemy 3: health: 1250")
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
                    enemyh=-1000
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
                    rendscreen("You beat enemy 3!")
                    input()
                    rendscreen("Enemy 4: health: 1500")
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
                            enemyh=-1
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
                        rendscreen("You beat enemy 4")
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
                                enemyhs=enemyhs-500
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
                            rendscreen("You beat all the enemies!")
                            input()
if enterarena1=="y" or enterarena1=="Y" and exitarena==0:
    rendscreen("Prizes:")
    input()
    rendscreen("100 gold")
    gold+=100
    input()
    rendscreen("5 bombs")
    special.append("Bomb")
    special.append("Bomb")
    special.append("Bomb")
    special.append("Bomb")
    special.append("Bomb")
    input()
    rendscreen("A staff: double damage and double health in all battles")
    input()
    special.append("Staff")
    damagem=damagem*2
    healthm=healthm*2
    rendscreen("5 lives")
    lives+=5
    input()
rendscreen("You continue on the path.")
input()
rendscreen("Now, you've beaten the tutorial.  Keep playing against harder enemies and getting better.")
