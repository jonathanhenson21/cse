import random
word_bank = ['Do', "yOu", "KnOw", "dE", "wAY", "hOmE", "My", "BrOtHeR", "cLiCk", "ClIcK"]
print(word_bank)
the_word = random.choice(word_bank)
print(the_word)
guess_taken = ''
letters_guessed = []
while guess_taken != 'quit':
    guess_taken = input("Guess a letter: ")
guess_taken (10)
