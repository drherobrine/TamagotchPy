print("Welcome to TamagotchPy!")

timesStarted = 0
hungry = 0
thirsty = 0
bathroomNeeded = 0
fatigued = 0
tamagNum = 0
timeUntilHungry = 0
timeUntilThirsty = 0
timeUntilBRoom = 0
name = 0
happy = 0
money = 0
food = 0
water = 0

BedroomFuncs = ["sleep", "goto Kitchen","goto Bathroom", "goto Playroom", "goto Shop", "nothing"]
KitchenFuncs = ["eat", "drink", "goto Bedroom", "goto Bathroom", "goto Playroom", "goto Shop", "nothing"]
BathroomFuncs = ["use", "goto Bedroom", "goto Kitchen", "goto Playroom", "goto Shop", "nothing"]
PlayroomFuncs = ["play", "goto Bedroom", "goto Kitchen", "goto Bathroom", "goto Shop", "nothing"]
ShopFuncs = ["buy food", "buy water", "goto Bedroom", "goto Kitchen", "goto Bathroom", "goto Playroom", "nothing"]


def loadData():
    loadfile = open("save", "r")
    load = loadfile.readlines()
    timesStarted = load[0]
    hungry = int(load[1])
    thirsty = int(load[2])
    bathroomNeeded = int(load[3])
    fatigued = int(load[4])
    tamagNum = int(load[5])
    timeUntilHungry = int(load[6])
    timeUntilThirsty = int(load[7])
    timeUntilBRoom = int(load[8])
    name = load[9]
    happy = int(load[10])
    money = int(load[11])
    food = int(load[12])
    water = int(load[13])
    loadfile.close()

loadData()

def saveData():
    savefile = open("save", "w")
    savefile.truncate()
    savefile.write(str(timesStarted) + "\n")
    savefile.write(str(hungry) + "\n")
    savefile.write(str(thirsty) + "\n")
    savefile.write(str(bathroomNeeded) + "\n")
    savefile.write(str(fatigued) + "\n")
    savefile.write(str(tamagNum) + "\n")
    savefile.write(str(timeUntilHungry) + "\n")
    savefile.write(str(timeUntilThirsty) + "\n")
    savefile.write(str(timeUntilBRoom) + "\n")
    savefile.write(str(name) + "\n")
    savefile.write(str(happy) + "\n")
    savefile.write(str(money) + "\n")
    savefile.write(str(food) + "\n")
    savefile.write(str(water) + "\n")
    savefile.close()

if timesStarted == 0:
    print("Pick your TamagotchPy:")
    print("X O 0 T")
    print("0 1 2 3")
    tamagNum = int(input("Type the number that is under the TamagotchPy you would like to pick "))
    name = input("What will be your TamagotchPy's name? ")

if timesStarted == 9:
    print("10th loadup!")
if timesStarted == 99:
    print("100th loadup!")
if timesStarted == 999:
    print("Srsly tho? 1000th loadup?")
if timesStarted == 999999:
    print("You... 1000000th loadup?!?!?")

timesStarted += 1

room = 0

while True:
    #saveData()
    if room == 0:
        print("Room: Bedroom")
    elif room == 1:
        print("Room: Kitchen")
    elif room == 2:
        print("Room: Bathroom")
    elif room == 3:
        print("Room: Playroom")
    elif room == 4:
        print("Shop")
    else:
        print("Room: Glitchroom!")

    print("\n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n Fatigue: %s"%fatigued)
    print(" Hunger: %s"%hungry)
    print(" Thirst: %s"%thirsty)
    print(" Bathroom need: %s"%bathroomNeeded)
    print(" Happiness: %s"%happy)
    print(" Money: $ %s \n"%money)
    print("\n \n \n \n \n \n")
    if tamagNum == 0:
        print("                 X \n \n")
    elif tamagNum == 1:
        print("                 O \n \n")
    elif tamagNum == 2:
        print("                 0 \n \n")
    elif tamagNum == 3:
        print("                 T \n \n")

    if room == 0:
        print("Use these commands: ")
        print(BedroomFuncs)
        command = input("Command: ")
        if command == "sleep":
            if fatigued == 0:
                print("%s is not tired."%name)
                continue
            else:
                fatigued = 0
                if happy == 0:
                    pass
                else:
                    happy -= 0.1
                continue
        elif command =="goto Kitchen":
            room = 1
            continue
        elif command =="goto Bathroom":
            room = 2
            continue
        elif command =="goto Playroom":
            room = 3
            continue
        elif command =="goto Shop":
            room = 4
            continue
    elif room == 1:
        print("Use these commands: ")
        print(KitchenFuncs)
        command = input("Command: ")
        if command == "eat":
            if food == 0:
                print("You don't have an food")
                continue
            elif hungry == 0:
                print("%s is not hungry."%name)
            else:
                if fatigued == 0:
                    pass
                else:
                    fatigued -= 0.1
                happy += 0.1
                hungry = 0
                food -= 1
                timeUntilBRoom -= 1
                continue
        elif command == drink:
            if water == 0:
                print("You don't have any water")
                continue
            elif thirsty == 0:
                print("%s is not thirsty."%name)
            else:
                happy += 0.1
                thirsty = 0
                water -= 1
                continue
        elif command =="goto Bedroom":
            room = 0
            continue
        elif command =="goto Bathroom":
            room = 2
            continue
        elif command =="goto Playroom":
            room = 3
            continue
        elif command =="goto Shop":
            room = 4
            continue
    elif room == 2:
        print("Use these commands: ")
        print(BathroomFuncs)
        command = input("Command: ")
        if command == "use":
            if bathroomNeeded == 0:
                print("%s does not currently need the bathroom."%name)
                continue
            else:
                bathroomNeeded = 0
                hungry += 0.1
                thirsty += 0.1
        elif command =="goto Bedroom":
            room = 0
            continue
        elif command =="goto Kitchen":
            room = 1
            continue
        elif command =="goto Playroom":
            room = 3
            continue
        elif command =="goto Shop":
            room = 4
            continue
    elif room == 3:
        print("Use these commands: ")
        print(PlayroomFuncs)
        command = input("Command: ")
        if command == "play":
            if fatigued >= 1:
                print("%s is too tired to play."%name)
                continue
            else:
                fatigued += 0.1
                happy += 0.1
                money += 1
                continue
        elif command =="goto Bedroom":
            room = 0
            continue
        elif command =="goto Kitchen":
            room = 1
            continue
        elif command =="goto Bathroom":
            room = 2
            continue
        elif command =="goto Shop":
            room = 4
            continue
    elif room == 4:
        print("Use these commands: ")
        print(ShopFuncs)
        command = input("Command: ")
        if command == "buy food":
            if money < 5:
                print("You do not have enough money.")
                continue
            else:
                money -= 5
                food += 1
                continue
        elif command == "buy water":
            if money < 5:
                print("You do not have enough money.")
                continue
            else:
                money -= 5
                water += 1
                continue
        elif command =="goto Bedroom":
            room = 0
            continue
        elif command =="goto Kitchen":
            room = 1
            continue
        elif command =="goto Bathroom":
            room = 2
            continue
        elif command =="goto Playroom":
            room = 3
            continue

    timeUntilBRoom -= 1
    timeUntilHungry -= 1
    timeUntilThirsty -= 1

    if timeUntilBRoom <= -1:
        timeUntilBRoom = 60
        bathroomNeeded += 0.1

    if timeUntilHungry <= -1:
        timeUntilHungry = 30
        hungry += 0.1

    if timeUntilThirsty <= -1:
        timeUntilThirsty = 15
        thirsty += 0.1
