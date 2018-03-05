import random

words = ["cat","dog","bird","flower","monkey"]
hint1 = ["paws","paws","beak","stem","tail"]
hint2 = ["meow","bark","chirp","petals","banana"]

number = random.randint(0,4)

secretword = words[number]

counter = 0

while True:
    print("Guess the secret word! Type hint1, hint2, first letter, last letter, or length for a clue.")
    guess = input()
    counter += 1

    if guess == secretword:
        print("You win!")
        print("It took you " + str(counter) + " guesses.")
        break

    elif guess == "hint1":
        print(hint1[number])

    elif guess == "hint2":
        print(hint2[number])

    elif guess == "first letter":
        print(secretword[0])

    elif guess == "last letter":
        print(secretword[-1])

    elif guess == "length":
        print(len(secretword))

    else:
        print("Guess again!")
