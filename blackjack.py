import random

deck = []
currentCard = []
suits = ["♠", "♥", "♦", "♣"]

cardRender = []

dealerHandValue = []
playerHandValue = []
dealerHandDisplay = []
playerHandDisplay = []
dealerScore = 0
playerScore = 0
dealerBust = False
playerBust = False
playerStand = False
dealerStand = False
playerWallet = 1500


def drawplayercard():
    cardrender = deck.pop(0)
    if cardrender[2] == "A":
        acevalue = (int(input("You've Drawn An Ace. Count it as 1, or 11?\n")))
        if acevalue == 11:
            cardrender[2] = 11
            print("Your Ace has been counted as 11")
        elif acevalue == 1:
            cardrender[2] = 1
            print("Your Ace has been counted as 1")
        else:
            print("ERROR: incorrect input")
    playerHandValue.append(cardrender.pop(2))
    playerHandDisplay.append(cardrender)


def drawdealercard():
    cardrender = deck.pop(0)
    if cardrender[2] == "A":
        if dealerScore + 11 >= 21:
            cardrender[2] = 1
        else:
            cardrender[2] = 11
    dealerHandValue.append(cardrender.pop(2))
    dealerHandDisplay.append(cardrender)


##Produces The Deck
for i in range(0, 4):
    for j in range(0, 13):
        if j == 0:
            currentCard = ["A", suits[i], "A"]
        elif j == 10:
            currentCard = ["J", suits[i], 10]
        elif j == 11:
            currentCard = ["Q", suits[i], 10]
        elif j == 12:
            currentCard = ["K", suits[i], 10]
        else:
            currentCard = [(str(j + 1)), suits[i], j + 1]
        deck.append(currentCard)

random.shuffle(deck)

print("\n\n ---BLACKJACK---\n\n")


while True:
    print("You have: $", playerWallet)
    if playerWallet == 0:
        print("No Money Lmao")
        input("")
        break

    while True:
        bet = int(input("How much do you want to bet? "))
        if playerWallet - bet < 0:
            print("Not Enough Money")
        else:
            break

    dealerHandValue = []
    playerHandValue = []
    dealerHandDisplay = []
    playerHandDisplay = []
    playerBust = False
    dealerBust = False
    playerStand = False
    dealerStand = False
    blackjack = False
    playerScore = 0
    dealerScore = 0

    drawplayercard()
    drawplayercard()
    playerScore = sum(playerHandValue)
    print("Your Hand:", playerHandDisplay)
    print("Your Hand's Value", playerScore)

    drawdealercard()
    dealerScore = sum(dealerHandValue)
    print("Dealer's 1st Card:", dealerHandDisplay)
    print("Dealer's 1st Card Value:", dealerScore)
    drawdealercard()
    dealerScore = sum(dealerHandValue)

    while True:
        if playerScore == 21:
            blackjack = True
            break
        if not playerStand:
            playerInput = input("Hit or STAND?\n")
            if (playerInput == "Hit") or (playerInput == "hit"):
                print("You have chosen to hit.")
                drawplayercard()
                playerScore = sum(playerHandValue)
                print(playerHandDisplay)
                print(playerScore)
                if playerScore >= 22:
                    playerBust = True
                    break
            else:
                print("You have chosen to stand.")
                playerStand = True

        if not dealerStand:
            if dealerScore <= 17:
                print("Dealer Hits")
                drawdealercard()
                dealerScore = sum(dealerHandValue)
                if dealerScore >= 22:
                    dealerBust = True
                    break
            else:
                print("Dealer Stands")
                dealerStand = True
        if playerStand and dealerStand:
            break

    if not playerBust and not dealerBust:
        if playerScore <= dealerScore:
            print("You Lose (no busts)")
            print("You Lose: $", bet)
            playerWallet = playerWallet - bet
        else:
            print("You Win (no busts)")
            print("You Win: $", bet + (bet * 0.25))
            playerWallet = playerWallet + (bet + (bet * 0.25))
    elif not playerBust and dealerBust:
        print("You Win (dealer busts)")
        print("You Win: $", bet + (bet * 0.5))
        playerWallet = playerWallet + (bet + (bet * 0.5))
    elif playerBust and not dealerBust:
        print("You Lose (you bust)")
        print("You Lose: $", bet)
        playerWallet = playerWallet - bet
    else:
        print("No One Wins (both bust)")

    print("You have: $", playerWallet)
    leave = bool(input("Leave?\n(put True, if you will, nothing if you don't)\n"))
    if leave:
        break
    elif not leave:
        pass
    else:
        pass
