'''
Paul Steiner
A02234580
CS 1400
Assignment 15
'''

from deck import Deck
import time


def main():
    moneyList = []
    numPlayer = eval(input("Enter Amount Of Players (1-5): "))
    if numPlayer == 1:
        playerOne = True
        playerTwo = False
        playerThree = False
        playerFour = False
        playerFive = False
        dealer = True

    elif numPlayer == 2:
        playerOne = True
        playerTwo = True
        playerThree = False
        playerFour = False
        playerFive = False
        dealer = True

    elif numPlayer == 3:
        playerOne = True
        playerTwo = True
        playerThree = True
        playerFour = False
        playerFive = False
        dealer = True

    elif numPlayer == 4:
        playerOne = True
        playerTwo = True
        playerThree = True
        playerFour = True
        playerFive = False
        dealer = True

    elif numPlayer == 5:
        playerOne = True
        playerTwo = True
        playerThree = True
        playerFour = True
        playerFive = True
        dealer = True

    for i in range(numPlayer):
        moneyList.append(100)

    play = True

    while play:
        deck = Deck()

        theHand = []

        numPlayer += 1

        for i in range(numPlayer):
            theHand.append([])

        wagerList = []
        if playerOne:
            keepPlayerOne = True
            playerMoney = moneyList[0]
            while keepPlayerOne:
                print("\nPlayer One: You have " + str(playerMoney) + " dollars.")
                betOne = eval(input("How much would you like to bet? "))

                if betOne < 5:
                    if playerMoney > 5:
                        print("Please Enter A Value Equal To Or Over Five")
                    elif str(playerMoney) < 5:
                        if playerMoney == betOne:
                            print("\nYour bet is " + str(betOne) + " dollars")
                            wagerList.append(betOne)
                            break
                        elif playerMoney > betOne:
                            print("If you have less than 5 dollars, you must bet the remainder of your money.")

                if betOne > playerMoney:
                    print("You don't have that much money. Try again.")

                if betOne >= 5 and (playerMoney > betOne) or (betOne == playerMoney):
                    print("\nYour bet is " + str(betOne) + " dollars")

                    wagerList.append(betOne)
                    break

        if playerTwo:
            keepPlayerTwo = True
            playerMoney = moneyList[1]
            while keepPlayerTwo:
                print("\nPlayer Two: You have " + str(playerMoney) + " dollars.")
                betTwo = eval(input("How much would you like to bet? "))

                if betTwo < 5:
                    if playerMoney > 5:
                        print("Please Enter A Value Over Five")
                    elif playerMoney < 5:
                        if playerMoney == betTwo:
                            print("\nYour bet is " + str(betTwo) + " dollars")
                            wagerList.append(betTwo)
                            break
                        elif playerMoney > betTwo:
                            print("If you have less than 5 dollars, you must bet the remainder of your money.")

                if betTwo > playerMoney:
                    print("You don't have that much money. Try again.")

                if betTwo >= 5 and (playerMoney > betTwo) or (betTwo == playerMoney):
                    print("\nYour bet is " + str(betTwo) + " dollars")

                    wagerList.append(betTwo)
                    break

        if playerThree:
            keepPlayerThree = True
            playerMoney = moneyList[2]
            while keepPlayerThree:
                print("\nPlayer Three: You have " + str(playerMoney) + " dollars.")
                betThree = eval(input("How much would you like to bet? "))

                if betThree < 5:
                    if playerMoney > 5:
                        print("Please Enter A Value Over Five")
                    elif playerMoney < 5:
                        if playerMoney == betThree:
                            print("\nYour bet is " + str(betThree) + " dollars")

                            wagerList.append(betThree)
                            break
                        elif playerMoney > betThree:
                            print("If you have less than 5 dollars, you must bet the remainder of your money.")

                if betThree > playerMoney:
                    print("You don't have that much money. Try again.")

                if betThree >= 5 and (playerMoney > betThree) or (betThree == playerMoney):
                    print("\nYour bet is " + str(betThree) + " dollars")

                    wagerList.append(betThree)
                    break

        if playerFour:
            keepPlayerFour = True
            playerMoney = moneyList[3]
            while keepPlayerFour:
                print("\nPlayer Four: You have " + str(playerMoney) + " dollars.")
                betFour = eval(input("How much would you like to bet? "))

                if betFour < 5:
                    if playerMoney > 5:
                        print("Please Enter A Value Over Five")
                    elif playerMoney < 5:
                        if playerMoney == betFour:
                            print("\nYour bet is " + str(betFour) + " dollars")

                            wagerList.append(betFour)
                            break
                        elif playerMoney > betFour:
                            print("If you have less than 5 dollars, you must bet the remainder of your money.")

                if betFour > playerMoney:
                    print("You don't have that much money. Try again.")

                if betFour >= 5 and (playerMoney > betFour) or (betFour == playerMoney):
                    print("\nYour bet is " + str(betFour) + " dollars")

                    wagerList.append(betFour)
                    break

        if playerFive:
            keepPlayerFive = True
            playerMoney = moneyList[4]
            while keepPlayerFive:
                print("\nPlayer Five: You have " + str(playerMoney) + " dollars.")
                betFive = eval(input("How much would you like to bet? "))

                if betFive < 5:
                    if playerMoney > 5:
                        print("Please Enter A Value Over Five")
                    elif playerMoney < 5:
                        if playerMoney == betFive:
                            print("\nYour bet is " + str(betFive) + " dollars")

                            wagerList.append(betFive)
                            break
                        elif playerMoney > betFive:
                            print("If you have less than 5 dollars, you must bet the remainder of your money.")

                if betFive > playerMoney:
                    print("You don't have that much money. Try again.")

                if betFive >= 5 and (playerMoney > betFive) or (betFive == playerMoney):
                    print("\nYour bet is " + str(betFive) + " dollars")

                    wagerList.append(betFive)
                    break

        for i in range(numPlayer):
            for j in range(2):
                for k in range(1):
                    theHand[i].append(deck.draw())

        print("\nThe second card in the dealers hand is", theHand[numPlayer - 1][1])

        if playerOne:
            bustOrHold = True
            while bustOrHold:
                sumHandOne = getHandValue(theHand, 0)
                print("\nPlayer One: This is your hand.")
                print(theHand[0])
                print("This is the current sum of your hand: ", sumHandOne)
                print("\n1) Hit")
                print("2) Hold")
                choice = eval(input("Would you like to hit, or hold? "))
                if choice == 1:
                    theHand[0].append(deck.draw())
                    sumHand = getHandValue(theHand, 0)
                    if sumHand > 21:
                        print("\n", theHand[0])
                        print("Your have busted. The current sum of your cards is " + str(sumHand))
                        break
                elif choice == 2:
                    print("\nYou have chosen to hold.")
                    break

        if playerTwo:
            bustOrHold = True
            while bustOrHold:
                sumHandTwo = getHandValue(theHand, 1)
                print("\nPlayer Two: This is your hand.")
                print(theHand[1])
                print("This is the current sum of your hand: ", sumHandTwo)
                print("\n1) Hit")
                print("2) Hold")
                choice = eval(input("Would you like to hit, or hold? "))
                if choice == 1:
                    theHand[1].append(deck.draw())
                    sumHand = getHandValue(theHand, 1)
                    if sumHand > 21:
                        print("\n", theHand[1])
                        print("Your have busted. The current sum of your cards is " + str(sumHand))
                        break
                elif choice == 2:
                    print("\nYou have chosen to hold.")
                    break

        if playerThree:
            bustOrHold = True
            while bustOrHold:
                sumHandThree = getHandValue(theHand, 2)
                print("\nPlayer Three: This is your hand.")
                print(theHand[2])
                print("This is the current sum of your hand: ", sumHandThree)
                print("\n1) Hit")
                print("2) Hold")
                choice = eval(input("Would you like to hit, or hold? "))
                if choice == 1:
                    theHand[2].append(deck.draw())
                    sumHand = getHandValue(theHand, 2)
                    if sumHand > 21:
                        print("\n", theHand[2])
                        print("Your have busted. The current sum of your cards is " + str(sumHand))
                        break
                elif choice == 2:
                    print("\nYou have chosen to hold.")
                    break

        if playerFour:
            bustOrHold = True
            while bustOrHold:
                sumHandFour = getHandValue(theHand, 3)
                print("\nPlayer Four: This is your hand.")
                print(theHand[3])
                print("This is the current sum of your hand: ", sumHandFour)
                print("\n1) Hit")
                print("2) Hold")
                choice = eval(input("Would you like to hit, or hold? "))
                if choice == 1:
                    theHand[3].append(deck.draw())
                    sumHand = getHandValue(theHand, 3)
                    if sumHand > 21:
                        print("\n", theHand[3])
                        print("Your have busted. The current sum of your cards is " + str(sumHand))
                        break
                elif choice == 2:
                    print("\nYou have chosen to hold.")
                    break

        if playerFive:
            bustOrHold = True
            while bustOrHold:
                sumHandFive = getHandValue(theHand, 4)
                print("\nPlayer Five: This is your hand.")
                print(theHand[4])
                print("This is the current sum of your hand: ", sumHandFive)
                print("\n1) Hit")
                print("2) Hold")
                choice = eval(input("Would you like to hit, or hold? "))
                if choice == 1:
                    theHand[4].append(deck.draw())
                    sumHand = getHandValue(theHand, 4)
                    if sumHand > 21:
                        print("\n", theHand[4])
                        print("Your have busted. The current sum of your cards is " + str(sumHand))
                        break
                elif choice == 2:
                    print("\nYou have chosen to hold.")
                    break

        if dealer:
            bustOrHold = True
            while bustOrHold:
                dealerHandSum = getHandValue(theHand, (numPlayer - 1))
                print("\nThis is the dealers hand.")
                print(theHand[numPlayer - 1])
                print("This is the current sum of the dealers hand: ", dealerHandSum)

                time.sleep(1)
                if dealerHandSum < 17:
                    time.sleep(1)
                    print("The dealer takes a card.")
                    theHand[numPlayer - 1].append(deck.draw())
                    if dealerHandSum > 21:
                        print("\nThis is the dealers hand.")
                        print(theHand[numPlayer - 1])
                        print("The dealer busted.")
                        break
                elif dealerHandSum >= 17:
                    print("\nThe dealer will hold.")
                    print("This is the dealers final hand.")
                    print(theHand[numPlayer - 1])
                    break

        if playerOne:
            time.sleep(1)
            sumHandOne = getHandValue(theHand, 0)
            dealerHandSum = getHandValue(theHand, (numPlayer - 1))

            if sumHandOne > 21:
                if dealerHandSum > 21:
                    print("\nPlayer One: The dealer busted, but you busted as well. You lost.")
                    print("You have lost " + str(betOne) + " dollars.")
                    moneyList[0] -= wagerList[0]
                    moneyListValueOne = moneyList[0]
                    if moneyListValueOne <= 0:
                        print("\nPlayer One: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerOne = False
                else:
                    print("\nPlayer One: You have busted. You lose.")
                    print("You have lost " + str(betOne) + " dollars.")
                    moneyList[0] -= wagerList[0]
                    moneyListValueOne = moneyList[0]
                    if moneyListValueOne <= 0:
                        print("\nPlayer One: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerOne = False

            elif dealerHandSum > 21:
                if sumHandOne <= 21:
                    print("\nPlayer One: You have won, because the dealer busted.")
                    print("You have won " + str(betOne) + " dollars.")
                    moneyList[0] += wagerList[0]

            elif dealerHandSum <= 21:
                if sumHandOne > dealerHandSum:
                    print("\nPlayer One: Your hand is of higher value than the hand of the dealer. You win.")
                    print("You have won " + str(betOne) + " dollars.")
                    moneyList[0] += wagerList[0]
                elif sumHandOne == dealerHandSum:
                    print("\nPlayer One: You tied with the dealer. You do not win or lose money.")
                elif sumHandOne < dealerHandSum:
                    print("\nPlayer One: Your hand is of lower value than the hand of the dealer. You lost.")
                    print("You have lost " + str(betOne) + " dollars.")
                    moneyList[0] -= wagerList[0]
                    moneyListValueOne = moneyList[0]
                    if moneyListValueOne <= 0:
                        print("\nPlayer One: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerOne = False

        if playerTwo:
            time.sleep(1)
            sumHandTwo = getHandValue(theHand, 1)
            dealerHandSum = getHandValue(theHand, (numPlayer - 1))

            if sumHandTwo > 21:
                if dealerHandSum > 21:
                    print("\nPlayer Two: The dealer busted, but you busted as well. You lost.")
                    print("You have lost " + str(betTwo) + " dollars.")
                    moneyList[1] -= wagerList[1]
                    moneyListValueTwo = moneyList[1]
                    if moneyListValueTwo <= 0:
                        print("\nPlayer Two: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerTwo = False
                else:
                    print("\nPlayer Two: You have busted. You lose.")
                    print("You have lost " + str(betTwo) + " dollars.")
                    moneyList[1] -= wagerList[1]
                    moneyListValueTwo = moneyList[1]
                    if moneyListValueTwo <= 0:
                        print("\nPlayer Two: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerTwo = False

            elif dealerHandSum > 21:
                if sumHandTwo <= 21:
                    print("\nPlayer Two: You have won, because the dealer busted.")
                    print("You have won " + str(betTwo) + " dollars.")
                    moneyList[1] += wagerList[1]

            elif dealerHandSum <= 21:
                if sumHandTwo > dealerHandSum:
                    print("\nPlayer Two: Your hand is of higher value than the hand of the dealer. You win.")
                    print("You have won " + str(betTwo) + " dollars.")
                    moneyList[1] += wagerList[1]
                elif sumHandTwo == dealerHandSum:
                    print("\nPlayer Two: You tied with the dealer. You do not win or lose money.")
                elif sumHandTwo < dealerHandSum:
                    print("\nPlayer Two: Your hand is of lower value than the hand of the dealer. You lost.")
                    print("You have lost " + str(betTwo) + " dollars.")
                    moneyList[1] -= wagerList[1]
                    moneyListValueTwo = moneyList[1]
                    if moneyListValueTwo <= 0:
                        print("\nPlayer Two: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerTwo = False

        if playerThree:
            time.sleep(1)
            sumHandThree = getHandValue(theHand, 2)
            dealerHandSum = getHandValue(theHand, (numPlayer - 1))

            if sumHandThree > 21:
                if dealerHandSum > 21:
                    print("\nPlayer Three: The dealer busted, but you busted as well. You lost.")
                    print("You have lost " + str(betThree) + " dollars.")
                    moneyList[2] -= wagerList[2]
                    moneyListValueThree = moneyList[2]
                    if moneyListValueThree <= 0:
                        print("\nPlayer Three: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerThree = False
                else:
                    print("\nPlayer Three: You have busted. You lose.")
                    print("You have lost " + str(betThree) + " dollars.")
                    moneyList[2] -= wagerList[2]
                    moneyListValueThree = moneyList[2]
                    if moneyListValueThree <= 0:
                        print("\nPlayer Three: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerThree = False

            elif dealerHandSum > 21:
                if sumHandThree <= 21:
                    print("\nPlayer Three: You have won, because the dealer busted.")
                    print("You have won " + str(betThree) + " dollars.")
                    moneyList[2] += wagerList[2]

            elif dealerHandSum <= 21:
                if sumHandThree > dealerHandSum:
                    print("\nPlayer Three: Your hand is of higher value than the hand of the dealer. You win.")
                    print("You have won " + str(betThree) + " dollars.")
                    moneyList[2] += wagerList[2]
                elif sumHandThree == dealerHandSum:
                    print("\nPlayer Three: You tied with the dealer. You do not win or lose money.")
                elif sumHandThree < dealerHandSum:
                    print("\nPlayer Three: Your hand is of lower value than the hand of the dealer. You lost.")
                    print("You have lost " + str(betThree) + " dollars.")
                    moneyList[2] -= wagerList[2]
                    moneyListValueThree = moneyList[2]
                    if moneyListValueThree <= 0:
                        print("\nPlayer Three: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerThree = False

        if playerFour:
            time.sleep(1)
            sumHandFour = getHandValue(theHand, 3)
            dealerHandSum = getHandValue(theHand, (numPlayer - 1))

            if sumHandFour > 21:
                if dealerHandSum > 21:
                    print("\nPlayer Four: The dealer busted, but you busted as well. You lost.")
                    print("You have lost " + str(betFour) + " dollars.")
                    moneyList[3] -= wagerList[3]
                    moneyListValueFour = moneyList[3]
                    if moneyListValueFour <= 0:
                        print("\nPlayer Four: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerFour = False
                else:
                    print("\nPlayer Four: You have busted. You lose.")
                    print("You have lost " + str(betFour) + " dollars.")
                    moneyList[3] -= wagerList[3]
                    moneyListValueFour = moneyList[3]
                    if moneyListValueFour <= 0:
                        print("\nPlayer Four: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerFour = False

            elif dealerHandSum > 21:
                if sumHandFour <= 21:
                    print("\nPlayer Four: You have won, because the dealer busted.")
                    print("You have won " + str(betFour) + " dollars.")
                    moneyList[3] += wagerList[3]

            elif dealerHandSum <= 21:
                if sumHandFour > dealerHandSum:
                    print("\nPlayer Four: Your hand is of higher value than the hand of the dealer. You win.")
                    print("You have won " + str(betFour) + " dollars.")
                    moneyList[3] += wagerList[3]
                elif sumHandFour == dealerHandSum:
                    print("\nPlayer Four: You tied with the dealer. You do not win or lose money.")
                elif sumHandFour < dealerHandSum:
                    print("\nPlayer Four: Your hand is of lower value than the hand of the dealer. You lost.")
                    print("You have lost " + str(betFour) + " dollars.")
                    moneyList[3] -= wagerList[3]
                    moneyListValueFour = moneyList[3]
                    if moneyListValueFour <= 0:
                        print("\nPlayer Four: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerFour = False

        if playerFive:
            time.sleep(1)
            sumHandFive = getHandValue(theHand, 4)
            dealerHandSum = getHandValue(theHand, (numPlayer - 1))

            if sumHandFive > 21:
                if dealerHandSum > 21:
                    print("\nPlayer Five: The dealer busted, but you busted as well. You lost.")
                    print("You have lost " + str(betFive) + " dollars.")
                    moneyList[4] -= wagerList[4]
                    moneyListValueFive = moneyList[4]
                    if moneyListValueFive <= 0:
                        print("\nPlayer Five: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerFive = False
                else:
                    print("\nPlayer Five: You have busted. You lose.")
                    print("You have lost " + str(betFive) + " dollars.")
                    moneyList[4] -= wagerList[4]
                    moneyListValueFive = moneyList[4]
                    if moneyListValueFive <= 0:
                        print("\nPlayer Five: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerFive = False

            elif dealerHandSum > 21:
                if sumHandFive <= 21:
                    print("\nPlayer Five: You have won, because the dealer busted.")
                    print("You have won " + str(betFive) + " dollars.")
                    moneyList[4] += wagerList[4]

            elif dealerHandSum <= 21:
                if sumHandFive > dealerHandSum:
                    print("\nPlayer Five: Your hand is of higher value than the hand of the dealer. You win.")
                    print("You have won " + str(betFive) + " dollars.")
                    moneyList[4] += wagerList[4]
                elif sumHandFive == dealerHandSum:
                    print("\nPlayer Five: You tied with the dealer. You do not win or lose money.")
                elif sumHandFive < dealerHandSum:
                    print("\nPlayer Five: Your hand is of lower value than the hand of the dealer. You lost.")
                    print("You have lost " + str(betFive) + " dollars.")
                    moneyList[4] -= wagerList[4]
                    moneyListValueFive = moneyList[4]
                    if moneyListValueFive <= 0:
                        print("\nPlayer Five: You have run out of money. You can no longer play.")
                        print("Thank you for playing.")
                        playerFive = False

        for i in range(len(moneyList)):
            time.sleep(1)
            print("\nThe remainder of Player " + str(i + 1) + "'s money is " + str(moneyList[i]) + " dollars.")

        if playerOne is False and playerTwo is False and playerThree is False and playerFour is False \
                and playerFive is False:
            print("\nAll the players have lost. Thank you for playing.")
            break

        print("\n1) Play Again")
        print("2) Quit")
        selection = eval(input("Choose A Selection: "))
        if selection == 2:
            print("Thank you for playing!")
            print("")
            moneyList.sort(reverse = True)

            for q in range(len(moneyList)):
                if moneyListValueOne == moneyList[q]:
                    print("Player one had a score of " + str(moneyList[q]))
                elif moneyListValueTwo == moneyList[q]:
                    print("Player two had a score of " + str(moneyList[q]))
                elif moneyListValueThree == moneyList[q]:
                    print("Player three had a score of " + str(moneyList[q]))
                elif moneyListValueFour == moneyList[q]:
                    print("Player four had a score of " + str(moneyList[q]))
                elif moneyListValueFive == moneyList[q]:
                    print("Player five had a score of " + str(moneyList[q]))

            break


def getHandValue(theList, value):
    sum = 0

    for i in theList[value]:
        currentValue = i.getCardValue()
        if currentValue > 10:
            currentValue = 10
        if currentValue == 1:
            currentValue = 11

        sum += currentValue

    if sum > 21:
        for i in theList[value]:
            currentValue = i.getCardValue()
            if currentValue == 1 and sum > 21:
                sum -= 10

    return sum


main()