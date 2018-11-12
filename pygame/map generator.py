import random

small_map = []
tilemap = []

x = 0
mapsize = int(input("How large would you like the map to be?"))

while x < mapsize:
    y = 0

    while y < mapsize:
        small_map.append(random.randint(0,1))
        y += 1

    tilemap.append(small_map)
    small_map = []
    x += 1

for row in tilemap:
    print(row)


import pgzrun
import time

tiles = ['medieval_archway', 'medieval_archery', 'medieval_archery']
posxy = [[250,250],[500,250],[600,300]]

WIDTH = 1000
HEIGHT = 1000

def draw():
    count = 0
    screen.clear()
    for i in tiles:
        n = tiles.index(i)
        act = Actor(i)
        act.pos = posxy[count]
        act.draw()
        count += 1

pgzrun.go()
