import random, sys

print("Rock, Paper, Scissors\n\n")
wins = 0
losses = 0
ties = 0

while True:
     print("%s Wins, %s Losses, %s Ties" %(wins,losses,ties))
     while True:
            print("Enter your move: (r)ock, (p)paper, (s)cissors, (q)uit")
            playerMove = input()
            if playerMove == "q":
                sys.exit()
            if playerMove == "r" or playerMove == "p" or playerMove == "s":
              break  
     
     computerMove = ""
     if playerMove == "r":
      print("Rock vs...")
     elif playerMove == "p":
      print("Paper vs...")
      playerMove == "s"
      print("Scissors vs...")
     randomNumber = random.randint(1,3)
     if randomNumber == 1:
        computerMove == "r"
        print("Rock")
     elif randomNumber == 2:
         computerMove == "p"
         print("Paper")
     elif randomNumber == 2:
                                        computerMove == "s"
                                        print("Scissors")

     if playerMove == computerMove:
                                        print("Is a tie!")
                                        ties += 1
                                        
     elif  playerMove == "r" and computerMove == "p":
                                        print("You lose!")
                                        losses+=1

     elif  playerMove == "r" and computerMove == "s":
                                        print("You win!")
                                        wins+=1

     elif  playerMove == "p" and computerMove == "s":
                                        print("You lose!")
                                        losses+=1

     elif  playerMove == "p" and computerMove == "r":
                                        print("You win!")
                                        wins+=1

     elif  playerMove == "s" and computerMove == "r":
                                        print("You lose!")
                                        losses+=1

     elif  playerMove == "s" and computerMove == "p":
                                        print("You win!")
                                        wins+=1
                
     
