import pyautogui as pg
import time
import webbrowser

points = 0

answer = pg.prompt(
"""
Which would you rather do?

a) Eat beets
b) Eat M&Ms
c) Watch cat videos

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3

answer = pg.prompt(
"""
Where would you like to live?

a) A beet farm/karate studio
b) Willy Wonka's Chocolate Factory
c) Little House on the Prairie

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3


answer = pg.prompt(
"""
What is your greatest achievement?

a) Becoming assistant (to the) regional manager
b) Playing drums in my band
c) Running the party planning committee

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3



#END OF SURVEY
pg.alert("You are...")

#Dwight
if points < 5:
    pg.alert("Dwight K Schrute")
    webbrowser.open("https://goo.gl/images/DRFJ5Z")
    
#Kevin
if points >= 5 and points <8:
    pg.alert("Kevin Malone")
    webbrowser.open("https://goo.gl/images/ok3Qzo")

#Angela
if points >=8:
    pg.alert("Angela Martin")
    webbrowser.open("https://goo.gl/images/WE8ouH")
