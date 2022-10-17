import random

random_number = random.randint(0, 10)

guesses = 0

while True:
    user_guess = input("Pick a number between 0 and 10: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        # print("Random number was: " + str(random_number))
        if user_guess == random_number:
            guesses += 1
            print("WOW! You got it right in", guesses , "guesses")
            break
        elif user_guess > random_number:
            print("Your guess was higher than the number!\n")
            guesses += 1
        else:
            print("Your guess was lower than the number!\n")
            guesses += 1
    else:
        print("Type a number next time silly...")
        continue