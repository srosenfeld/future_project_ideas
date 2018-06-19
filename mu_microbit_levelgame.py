from microbit import *

def levelone():
    display.scroll('Choose your path: A or B',delay=80)
    while True:
        if button_a.is_pressed():
            print("You chose A!")
            display.show(Image.HEART)
            sleep(1000)
            display.show(Image.HEART_SMALL)
            sleep(1000)
            leveltwo()
        elif button_b.is_pressed():
            print("You chose B")
            display.show(Image.SKULL)
            sleep(1000)
            display.show(Image.GHOST)
            sleep(1000)
        
def leveltwo():
    display.scroll('Level Two: A or B',delay=80)
    while True:
        if button_a.is_pressed():
            print("You chose A!")
            display.show(Image.HEART)
            sleep(1000)
            display.show(Image.HEART_SMALL)
            sleep(1000)
        elif button_b.is_pressed():
            print("You chose B")
            display.show(Image.SKULL)
            sleep(1000)
            display.show(Image.GHOST)
            sleep(1000)
    
levelone()