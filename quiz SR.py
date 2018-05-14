import webbrowser as wb
score = 0
answer1 = input("What's the best band in the world?")
if answer1 == "Eric Clapton":
    print("Correct!")
    score += 1
elif answer1 == "The Eagles":
    print("That's also one of my favorites!")
    score += 1
else:
    print("Wrong! Better luck next time.")

answer2 = input("What's the best food in the world?")
if answer2 == "Pizza":
    print("Obviously.")
    score += 1
elif answer2 == "Escargot":
    print("Yuck!")
    score -= 1
else:
    print("Absolutely not.")

answer3 = input("What's the best place to go on vacation?")
if answer3 == "Hawaii":
    print("Totally.")
    score += 1
else:
    print("That isn't what I was thinking.")

print("Here's your score:")
print(score)

if score >= 2:
    wb.open("")

elif score < 2:
    wb.open("")

