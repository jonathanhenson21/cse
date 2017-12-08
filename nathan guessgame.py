# REMEMBER, INPUT FROM USERS ARE ALWAYS (!!!)
# OF TYPE STRING!!!!
#
# generate a number
# ask the user for an input(number)
# does the guess match the number ?
# add "Higher" and "Lower"
# add 5 guesses

# A guess game program made in python


import random

guessesTaken = 6

print('Hello! What is your name, may i ask?')
myName = input()

number = random.randint(1, 50)
print('Well, ' + myName + ', I am thinking of a number between 1 and 50')

while guessesTaken < 6:
    print('Take a guess..')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('Your number guess is too low, guess again')

    if guess > number:
        print('Your number is too high! guess lower or something!')

    if guess == number:
        break

    if guess == number:
        guessesTaken = str(guessesTaken)
        print('Good job, ' + myName + '! You guessed the right number in' + guessesTaken + 'guesses!')

    if guess != number:
            number = str(number)
            print('Nah, The number i was thinking of was ' + number)
