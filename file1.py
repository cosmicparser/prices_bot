import random

class player:
    def __init__(self,hp,damage,x,y):
        self.hp=hp
        self.damage=damage
        self.x=x
        self.y=y

    def heal(hp):
        hp+= 50
        print("вы пополнили здоровье на 50, ваше здоровье: ", hp)

class monstr:
    def __init__(self,hp, damage, x, y):
        self.hp=hp
        self.damage=damage
        self.x=x
        self.y=y


jose = player(100,15,0,0)
yeti = monstr(100,10,3,10)

x1 = 2
y1 = 2
exp = 100

flag_m = False

x4 = 10
y4 = 10
print("Привет ты в игре")
while True:
    print("Твоя позиция x", jose.x, "y", jose.y)
    a = input("Ты должен ввести куда хочешь пойти  WASD")
    if (a == "W" or a == "w"):
        jose.y += 1
    elif (a == "S"):
        jose.y -= 1
    elif (a == "D"):
        jose.x += 1
    elif (a == "A"):
        jose.x -= 1

    if (jose.x == 2 and jose.y == 2):
        print("Ты нашел клад, здоровье и урон увеличены")
        jose.damage += 5
        jose.hp += 50

    if (jose.x == 3 and jose.y == 8):
        print("ты нашел принцессу")

    if (jose.x == 4 and jose.y == 10):
        print("Ты встретил монстра")
        for i in range(200):
            if (flag_m == False):
                flag_m = True
                print("Подумай что сделать у тебя есть 2 секунды 1.укланиться от встречи 2.начать драку")
        v = int(input("Ну что подумал, выбирай: "))
        if (v == 1):
            flag_m = False
            x += 1
        elif (v == 2):
            print("Драка")

            while jose.hp > 0 and yeti.hp > 0:
                a = random.randint(1, 2)
                print(a)
                choice = int(input("выбирай 1. попытаться нанести урон и 2. уклониться от атаки"))
                if choice == 1 and a == 1:
                    yeti.hp -= jose.damage
                    print("ты нанёс ", jose.damage ," уронa монстру, здоровье монстра: ", yeti.hp)
                if choice == 2 and a == 2:
                    print("Ты уклонился от атаки, твоё здоровье: ", jose.hp)
                if choice == 1 and a == 2:
                    jose.hp -= yeti.damage
                    print("ты получил урон!, твоё здоровье: ", jose.hp)
                if choice == 2 and a == 1:
                    print("ты уклонился от несуществующей атаки, так держать!")

            if yeti.hp <= 0:
                print("ты убил монстра, твоя награда 100hp!")
                jose.hp += 100
            elif jose.hp <= 0:
                print("ты был убит, game over!")
                break
