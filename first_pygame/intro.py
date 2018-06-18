#Make sure your computer has installed pgzero with pip install pgzero
#Tutorials available at http://pygame-zero.readthedocs.io/en/stable/index.html#courses
import pgzrun

alien = Actor('alien')
alien.pos = 250, 400

WIDTH = 500
HEIGHT = 500

def draw():
    screen.clear()
    alien.draw()



pgzrun.go()
