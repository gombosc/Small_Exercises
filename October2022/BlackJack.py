import random

print("Welcome to BlackJack")
print("Insert your name")
def userHand():
    user = input()
    handtotal = 0
    while handtotal < 21:
        userHand = random.randint(1,12)
        handtotal = userHand + handtotal
        print('Your card is ' + str(handtotal))
        print("Type 'again' for another card or 'stop' to exit draw")
        userChoice = ''
        if userChoice == "again" or userChoice == "":
              userHand = random.randint(1,12)
              handtotal = userHand + handtotal
              if handtotal == 21:
                 print("BlackJack for " + user)
                 break
        elif handtotal > 21:
            print("You lost")
            break
        elif userChoice == "stop":
            print("Your hand is:")
userHand()
        
        
    
    
