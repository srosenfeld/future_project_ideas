#graphics credits belong to https://kenney.nl/assets/hexagon-pack

import pgzrun
import time
import random

large_map = {}
tile_options = ['dirt_02','dirt_03','dirt_04']
#tile_options = ['dirt_01','dirt_02','dirt_03','dirt_04','dirt_05','dirt_06','dirt_07','dirt_08','dirt_09','dirt_10','dirt_11','dirt_12','dirt_13','dirt_14','dirt_15','dirt_16','dirt_17','dirt_18','dirt_19']
countx = 0

while countx < 1000:
    county = 0

    while county < 1000:
        large_map[str(countx), str(county)] = tile_options[random.randint(0,2)]
        county = county + 80
    
    countx = countx + 80

"""
for k,v in large_map.items():
    print(k)
    print(type(k))
"""

#Create main character alien at 100,56
alien = Actor('alien')
alien.pos = 100, 56
    
def draw():
    screen.clear()
    for k,v in large_map.items():
        itemlist = list(k)
        coordinates = []
        for i in itemlist:
            coordinates.append(int(i))
        act = Actor(v, center=coordinates)
        act.draw()
    alien.draw()

def update():
    speak()
    walky()
    if keyboard.left:
        alien.x -= 3
    elif keyboard.right:
        alien.x += 3
#    elif alien.collidepoint(Actor('dirt_02').x, Actor('dirt_02').y):
#        print("found it")
        
def walky():
    if keyboard.up:
        alien.y -= 3
    elif keyboard.down:
        alien.y += 3

def speak():
    if keyboard.a:
        print("hi!")
        

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        print("hit")




pgzrun.go()



