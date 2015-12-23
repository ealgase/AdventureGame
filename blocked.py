#Minecraft
#A world based off minecraft
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
if __name__!="__main__":
    ender=0
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
    mcm=random.randint(1,3)
    if mcm==1:
        if ender==1:
            type=random.randint(1,16)
        else:
            type=random.randint(1,15)
        if type==1:
            enemy="Blaze"
            enemyh=10*xp
            bomba="don't affect "
            xpe=10
            bombm=0
        elif type==2:
            enemy="Chicken Jockey"
            enemyh=3*xp
            bomba="destroy "
            xpe=30
            bombm=9999999999999999999999999999
        elif type==3:
            enemy="Creeper"
            enemyh=50*xp
            bomba="don't affect "
            xpe=20
            bombm=0
        elif type==4:
            enemy="Elder Guardian"
            enemyh=20*xp
            bomba="do 1500 damage to "
            xpe=100
            bombm=1500
        elif type==5:
            enemy="Ghast"
            enemyh=3*xp
            bomba="don't affect "
            xpe=70
            bombm=0
        elif type==6:
            enemy="Guardian"
            enemyh=90*xp
            bomba="don't affect "
            xpe=20
            bombm=0
        elif type==7:
            enemy="Magma Cube"
            enemyh=10*xp
            bomba="do 500 damage to "
            xpe=10
            bombm=500
        elif type==8:
            enemy="Silverfish"
            enemyh=10*xp
            bomba="destroy "
            xpe=30
            bombm=9999999999999999999999999999
        elif type==9:
            enemy="Skeleton"
            enemyh=200*xp
            bomba="don't affect "
            xpe=200
            bombm=0
        elif type==10:
            enemy="Slime"
            enemyh=100*xp
            bomba="do 2500 damage to "
            xpe=100
            bombm=2500
        elif type==11:
            enemy="Spider Jockey"
            enemyh=200*xp
            bomba="don't affect "
            xpe=20
            bombm=0
        elif type==12:
            enemy="Witch"
            enemyh=900*xp
            bomba="don't affect "
            xpe=500
            bombm=0
        elif type==13:
            enemy="Wither Skeleton"
            enemyh=20*xp
            bomba="do 500 damage to "
            xpe=30
            bombm=500
            enemy="Zombie"
            enemyh=20*xp
            bomba="destroy "
            xpe=20
            bombm=9999999999999999999999999999
        elif type==14:
            enemy="Zombie Villager"
            enemyh=10*xp
            bomba="don't affect "
            xpe=10
            bombm=0
        elif type==15:
            enemy="Endermite"
            enemyh=random.randint(1,3)*xp
            bomba="destroy "
            xpe=5
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
    elif mcm==2:
        rendscreenx("You find a block!")
        input()
        blockg=random.randint(0,22)
        blocks=["Stone", "Grass", "Dirt", "Bedrock", "Sand", "Gravel", "Gold Ore", "Iron Ore", "Coal Ore", "Log", "Leaves", "Lapis Ore", "Sandstone", "Tallgrass", "Deadbush", "Yellow Flower", "Red Flower", "Brown Mushroom", "Red Mushroom", "Diamond Ore", "Redstone Ore", "Emerald Ore", "Packed Ice"]
        special.append(blocks[blockg])
        rendscreenx("You found a " + blocks[blockg] + " block!")
    elif mcm==3:
        #special item
        item=random.randint(1,4)
        if item==1:
            rendscreenx("You found a wood sword!")
            input()
            rendscreenx("It grants x1.2 damage in all battles!")
            damagem=damagem*1.2
            special.append('Wood sword')
        elif item==2:
            rendscreenx("You found an iron sword!")
            input()
            rendscreenx("It grants x1.6 damage in all battles!")
            damagem=damagem*1.6
            special.append('Iron sword')
        elif item==3:
            rendscreenx("You found a gold sword!")
            input()
            rendscreenx("It grants double damage in all battles!")
            damagem=damagem*2
            special.append("Gold sword")
            #hello
        xp+=30
    input()
