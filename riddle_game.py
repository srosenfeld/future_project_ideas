#Here's a list of kid-friendly riddles: https://www.everythingmom.com/parenting/45-riddles-and-brain-teasers-for-kids
guesscounter = 0
while True:
    riddle1 = input("I'm tall when I'm young and I'm short when I'm old. What am I? \n")
    if riddle1.lower() == "hint1":
        print("I give light.")
    elif riddle1.lower() == "hint2":
        print("I'm made of wax")
    elif riddle1.upper() == "I GIVE UP":
        print("You give up already? I'm a candle!")
        break
    elif "candle" in riddle1:
        print("You got it! It took you " + str(guesscounter) + " tries.")
        break
    else:
        print("Guess again! You can also type 'hint1', 'hint2', or 'I give up'")
        
        
