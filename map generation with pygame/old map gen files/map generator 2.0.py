import random

tile_options = ['medieval_archway','medieval_archery']
small_map = []
large_map = []

x = 0
mapsize = int(input("How large would you like the map to be?"))

while x < mapsize:
    y = 0

    while y < mapsize:
        small_map.append(tile_options[random.randint(0,1)])
        y += 1

    large_map.append(small_map)
    small_map = []
    x += 1

for row in large_map:
    print(row)


import pgzrun
import time

posxy = []

WIDTH = 1000
HEIGHT = 1000

def draw():
    screen.clear()
    for x in largemap:
        count = 0
        for i in x:
            act = Actor(i)
            act.pos = posxy[count]
            act.draw()
            count += 1

pgzrun.go()
