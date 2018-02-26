import pyautogui as pg
import random

#These are the possible answers
words = ["cat","dog","bird"]

#Hints need to match order of words list
hint1 = ["four paws", "four paws", "wings"]
hint2 = ["whiskers","plays fetch","beak"]

#Initialize counter to zero at start
counter = 0

#Initialize guess to be blank
guess = ""

#Initialize random number
number = random.randint(0,2)

#Select random word
answer = words[number]

while guess != answer:
    guess = pg.prompt("What word am I thinking of? Type 'hint1' or 'hint2' if you need help.")
    counter += 1

    if guess == answer:
        pg.alert("You got it! You made " + str(counter) + " guesses.")
        break
    elif guess == "hint1":
        pg.alert(hint1[number])
    elif guess == "hint2":
        pg.alert(hint2[number])
    else:
        pg.alert("Keep guessing!")
        
