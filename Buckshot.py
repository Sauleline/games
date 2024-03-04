import random
import time
import os
import tabulate as tab
import numpy as np

# Currently this only goes up to the player's turn on the 2nd round, in which items are first introduced.

def underline(text):
    return "\033[4m" + text + "\033[0m"


def sayrounds(liveround, blankround):
    if liveround == 1 and blankround == 1:
        output = str((liveround, "LIVE ROUND.", blankround, "BLANK."))
    elif liveround == 1 and not blankround == 1:
        output = str((liveround, "LIVE ROUND.", blankround, "BLANKS."))
    elif not liveround == 1 and blankround == 1:
        output = str((liveround, "LIVE ROUNDS.", blankround, "BLANK."))
    else:
        output = str((liveround, "LIVE ROUNDS.", blankround, "BLANKS."))
    output = output.replace("(", "")
    output = output.replace(",", "")
    output = output.replace("'", "")
    output = output.replace(")", "")
    return output


def loadgundisplay(liveround, blankround):
    output = ""
    for p in range(liveround):
        output += "█ "
    for p in range(blankround):
        output += "▒ "
    output += "\n"
    return output


def loadgun(liveround, blankround):
    output = []
    for p in range(liveround):
        output.append(1)
    for p in range(blankround):
        output.append(0)
    return output


def shoot(who, at, bullet, sawn):
    output = [0, 2, "waste"]
    if sawn and bullet == 1:
        damage = 2
        output[2] = "█"
        for k in range(100):
            print("████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        time.sleep(0.075)
        os.system('cls')
        time.sleep(0.5)
    elif sawn and bullet == 0:
        damage = 0
        print("*click*")
        input()
        output[2] = "▒"
    elif not sawn and bullet == 1:
        damage = 1
        output[2] = "█"
        for k in range(100):
            print("████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
        time.sleep(0.075)
        os.system('cls')
        time.sleep(0.5)
    else:
        damage = 0
        print("*click*")
        input()
        output[2] = "▒"
    output[0] = damage
    if who == "you" and at == "you" and bullet == 0:
        output[1] = 0
    elif who == "dealer" and at == "dealer" and bullet == 0:
        output[1] = 1
    elif who == "dealer":
        output[1] = 0
    elif who == "you":
        output[1] = 1
    return output


def glass():
    shell = deck[0]
    if shell == 1:
        print("█")
    else:
        print("▒")
    return shell


def cigs():
    return 1


def beer(bullet):
    if bullet == 1:
        return "█"
    else:
        return "▒"


deck = []
items = np.array([["Magnifying Glass", "Cigarette Pack", "Beer", "Hand Saw", "Handcuffs"], ["CHECK THE CURRENT\nROUND IN THE CHAMBER.", "TAKES THE EDGE OFF.\nREGAIN 1 CHARGE.", "YOU RACK THE SHOTGUN.\nENDS ROUND ON LAST SHELL.", "SHOTGUN DEALS 2 DAMAGE", "DEALER SKIPS THE NEXT TURN."]])


playerName = ""
playerNameDisplay = ""

playerOption = ""
playerAim = ""

livesDisplay = np.array([["DEALER", ""], ["", ""]])
flashDisplay = np.array([["DEALER", ""], ["", ""]])
stageDisplay = np.array([["I", "II", "III"], ["█", "▒▒", "▒"]])
levelFlash = np.array([["I", "II", "III"], ["▒", "▒▒", "▒"]])

playerInv = [["Shotgun"], ["SHOOTING YOURSELF WITH\nA BLANK SKIPS THE\nDEALER'S TURN"]]
dealerInv = ["Shotgun"]

wasted = []
wastedDisplay = ""
loaded = 0
fired = 0
results = []

turn = 0
# 0 for player, 1 for dealer

shot = False

live = 1
#█, 1
blank = 2
#▒, 0

lose = False

print("\n\n\n\t\t     BUCKSHOT\n\t\t     ROULETTE\n\n")
print("\n\t\tA COMPUTER GAME\n\t\tBY MIKE KLUBINKA\n\n\t\tPORTED TO PYTHON\n\t\t  BY SAULELINE\n\n")
if(input("\t\t      START\n\t\t      EXIT\n\n\t").lower() == "exit"):
    exit()

print("HEAVY (No Visuals, other than flashing lights) TWs FOR:")
print("\t- Guns")
print("\t- Shooting yourself (You are (mostly) fine)")
print("\t- Alcohol")
print("\t- Knives")
print("\t- Cigarettes")
print("\t- Flashing Lights")
input()
os.system('cls')
print("(imma be real i need a way to display who the dealer is shooting at this is the best i can do rn)")
print("\nText in tables with 2 lines is the Defibrillator")
print("\nText in tables with 1 line is stuff you see")
print("\nUnderlined text is the Dealer")
input("\nIf you aren't already, please run this with py.exe, in full screen.")
os.system('cls')
input(underline("\nPLEASE SIGN THE WAIVER.\n"))
os.system('cls')

for i in range(1):
    print("\n\n\tThis General Release (\"Release\") is made on 22 day of January, 2018 between ████████ at \n\t████████████████████████████████ (\"Releasor\") and ████████ at ████████████████████████ (\"Releasee\").\n")
    print("\n\t\t1. Releasor and anyone claiming on Releasor's behalf releases and forever discharges \n\t\tReleasees and its affiliates, successors, officers, employees, representatives, \n\t\tpartners, agents and anyone claiming through them (collectively, the \"Released Parties\") \n\t\tin their individual and/or corporate capacities from any and all claims, liabilities, \n\t\tobligations, promises, agreements, disputes, demands, damages, causes of action of any \n\t\tnature and kind, known or unknown, which Releasor has or ever had or may in the future \n\t\thave against Releasees or any of the Released Parties arising out of or relating to: the \n\t\ttermination of a contractual relationship between the Releasor and the Releasee (\"Claims\").")
    print("\n\t\t2. In exchange for the release of Claims, Releasee will provide Releasor a payment in the \n\t\tamount of $10,000.00. In consideration of such payment, Releasor agrees to accept the payment \n\t\tas full and complete settlement and satisfaction of any present and prospective claims.")
    print("\n\t\t3. This Release shall not be in any way construed as an admission by the Releasee that \n\t\tit has acted wrongfully with respect to Releasor or any other preson, that it admits \n\t\tliability or responsibility at any time for any purpose, or that Releasor has any rights \n\t\twhatsoever against the Releasee.")
    print("\n\t\t4. This release shall be binding upon the parties and their respective heirs, administrators, \n\t\tpersonal representatives, executors, successors and assigns. Releasor has the authority to \n\t\trelease the Claims and has not assigned or transferred any Claims to any other party. The \n\t\tprovisions of this Release are severable. If any provision is held to be invalid or \n\t\tunenforceable, it shall not affect the validity or enforceability of any other provision. \n\t\tThis Release constitutes the entire agreement between the parties and supersedes any and \n\t\tall prior oral or written agreements or understandings between the parties.")
    print("\n\n\tSIGN HERE:\n")
    playerName = (input("\t")).upper()

while True:
    if ((len(playerName) >= 7) or (len(playerName) <= 0)) or ((playerName == "GOD") or (playerName == "DEALER")):
        print("\n\tBAD INPUT")
        print("\n\tSIGN HERE:\n")
        playerName = (input("\t")).upper()
    else:
        break

livesDisplay[0, 1] = ""
for i in range(len(playerName)):
    flashDisplay[0, 1] += " "
    livesDisplay[0, 1] += " "
    playerNameDisplay += " "

dealerLives = 2
playerLives = 2

for i in range(dealerLives):
    livesDisplay[1, 0] += "*"
    flashDisplay[1, 0] += "*"
for i in range(playerLives):
    livesDisplay[1, 1] += "*"
    flashDisplay[1, 1] += "*"

os.system('cls')

for i in range(len(playerName)):
    #waitTime = (random.randint(i + 1, i + 3) / 10)
    waitTime = (len(playerName)-(i+1))/100
    playerNameDisplay = playerNameDisplay.replace(" ", playerName[i], 1)
    livesDisplay[0, 1] = playerNameDisplay
    print(tab.tabulate(flashDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
    print(tab.tabulate(levelFlash, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
    time.sleep(waitTime)
    os.system('cls')
    print(tab.tabulate(livesDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
    print(tab.tabulate(stageDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
    time.sleep(waitTime)
    os.system('cls')

print(tab.tabulate(livesDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
print(tab.tabulate(stageDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))

deck = loadgun(live, blank)
print(underline(sayrounds(live, blank)))
print()
print(loadgundisplay(live, blank))

random.shuffle(deck)

input()
os.system('cls')

input(underline("\nI INSERT THE SHELLS IN AN UNKNOWN ORDER\n"))

##ROUND 1
while True:
    shot = False
    picked = False
    if turn == 0:
        os.system('cls')
        print(underline("\nYOUR TURN.\n"))
        while not picked:
            if len(wasted) >= 1:
                print("SPENT SHELLS:")
                wastedDisplay = ""
                for i in range(len(wasted)):
                    wastedDisplay += wasted[i]
                    wastedDisplay += " "
                print(wastedDisplay)
            print("Your options:")
            print(tab.tabulate(playerInv, headers="firstrow", tablefmt="orgtbl", stralign="center"))
            playerOption = input().lower()
            os.system('cls')
            print(wasted)
            if playerOption == "shotgun":
                picked = True
                while not shot:
                    playerAim = input("\n\n\tDEALER / YOU\n\n").lower()
                    if playerAim == "you" or playerAim == "dealer":
                        fired = deck.pop(0)
                        shot = True
                        results = (shoot("you", playerAim, fired, False))
                        if fired == 1:
                            if playerAim == "dealer":
                                dealerLives = dealerLives - results[0]
                            else:
                                playerLives = playerLives - results[0]
                        wasted.append(results[2])
                        turn = results[1]
                    else:
                        os.system('cls')
                        input(underline("\nPICK. 2"))
                        os.system('cls')
            else:
                os.system('cls')
                input(underline("\nPICK. 1"))
                os.system('cls')
    elif turn == 1:
        os.system('cls')
        input(underline("MY TURN"))
        lastShell = deck[len(deck) - 1]
        fired = deck.pop(0)
        if random.randint(0, 1) == 1:
            dealerAim = "dealer"
        else:
            dealerAim = "you"
        if wasted == (live + blank) - 1:
            if lastShell == 1:
                dealerAim = "you"
            else:
                dealerAim = "dealer"
        if dealerAim == "dealer":
            print("The Dealer Takes the shotgun, and turns it at himself.")
        else:
            print("The Dealer Takes the shotgun, and turns it toward you.")
        results = shoot("dealer", dealerAim, fired, False)
        if dealerAim == "dealer":
            dealerLives = dealerLives - results[0]
        else:
            playerLives = playerLives - results[0]
        wasted.append(results[2])
        turn = results[1]
    else:
        print("uh oh")
        print(turn)
        input()
        break
    if playerLives <= 0:
        os.system('cls')
        time.sleep(3)
        print("YOU'RE LUCKY IT LEFT YOU WITH A CHARGE!")
        print("GET UP,", playerName, ". THE NIGHT IS YOUNG.")
        input()
        exit()
    else:
        for j in range(1):
            livesDisplay[1, 0] = ""
            livesDisplay[1, 1] = ""
            for i in range(dealerLives):
                livesDisplay[1, 0] += "*"
            for i in range(playerLives):
                livesDisplay[1, 1] += "*"
            print(tab.tabulate(livesDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
            print(tab.tabulate(stageDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
            input()

    if dealerLives <= 0:
        os.system('cls')
        print(tab.tabulate([(playerName, " WINS!")], tablefmt="fancy_grid", stralign="center"))
        input()
        break

    if len(deck) == 0:
        os.system('cls')
        live = 3
        blank = 2
        print(tab.tabulate(livesDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
        print(tab.tabulate(stageDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
        deck = loadgun(live, blank)
        random.shuffle(deck)
        wasted = []
        print(underline(sayrounds(live, blank)), "\n")
        print(loadgundisplay(live, blank))
        input(underline("THEY ENTER THE CHAMBER IN A HIDDEN SEQUENCE"))
        turn = 0

    stageDisplay = np.array([["I", "II", "III"], ["▒", "██", "▒"]])
    levelFlash = np.array([["I", "II", "III"], ["█", "▒", "▒"]])

    for i in range(3):
        waitTime = 0.05
        os.system('cls')
        print(tab.tabulate(levelFlash, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
        time.sleep(waitTime)
        os.system('cls')
        print(tab.tabulate(stageDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))

    input()
    os.system('cls')

    input(underline("\nLETS MAKE THIS A LITTLE MORE INTERESTING..."))
    input(underline("\nTWO ITEMS EACH"))
    input(underline("\nMORE ITEMS BEFORE EACH LOAD"))
    os.system('cls')

    for i in range(2):
        itemDrawn = random.randint(0, 4)
        playerInv[0].append(items[0, itemDrawn])
        playerInv[1].append(items[1, itemDrawn])
        print(tab.tabulate(playerInv, headers="firstrow", tablefmt="orgtbl", stralign="center"))
        input()
        os.system('cls')

dealerLives = 4
playerLives = 4

for j in range(1):
    livesDisplay[1, 0] = ""
    livesDisplay[1, 1] = ""
    for i in range(dealerLives):
        livesDisplay[1, 0] += "*"
    for i in range(playerLives):
        livesDisplay[1, 1] += "*"
    print(tab.tabulate(livesDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
    print(tab.tabulate(stageDisplay, headers="firstrow", tablefmt="fancy_grid", stralign="center"))
input()
turn = 0

while True:
    shot = False
    picked = False
    saw = False
    handcuffed = False
    if turn == 0:
        os.system('cls')
        print(underline("\nYOUR TURN.\n"))
        while not picked:
            if len(wasted) >= 1:
                print("SPENT SHELLS:")
                for i in range(len(wasted)):
                    wastedDisplay += wasted[i]
                    wastedDisplay += " "
                print(wastedDisplay)
            print("Your options:")
            print(tab.tabulate(playerInv, headers="firstrow", tablefmt="orgtbl", stralign="center"))
            playerOption = input().lower()
            os.system('cls')
            if playerOption == "shotgun":
                picked = True
                while not shot:
                    playerAim = input("\n\n\tDEALER / YOU\n\n").lower()
                    if playerAim == "you" or playerAim == "dealer":
                        fired = deck.pop(0)
                        shot = True
                        results = (shoot("you", playerAim, fired, saw))
                        if fired == 1:
                            if playerAim == "dealer":
                                dealerLives = dealerLives - results[0]
                            else:
                                playerLives = playerLives - results[0]
                        wasted.append(results[2])
                        turn = results[1]
                    else:
                        os.system('cls')
                        input(underline("\nPICK."))
                        os.system('cls')
            elif playerOption == "magnifying glass" and "Magnifying Glass" in playerInv[0, :]:
                glass()
            elif playerOption == "cigarette pack" and "Cigarette Pack" in playerInv[0, :]:
                playerLives = playerLives + cigs()
            elif playerOption == "beer" and "Beer" in playerInv[0, :]:
                wasted.append(beer(deck.pop(0)))
            elif playerOption == "hand saw" and "Hand Saw" in playerInv[0, :]:
                saw = True
            elif playerOption == "handcuffs" and "Handcuffs" in playerInv[0, :]:
                handcuffed = True
            else:
                os.system('cls')
                input(underline("\nPICK."))
                os.system('cls')
        if handcuffed:
            turn = 0
