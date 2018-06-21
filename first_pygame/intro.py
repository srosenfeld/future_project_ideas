#Make sure your computer has installed pgzero with pip install pgzero
#Tutorials available at http://pygame-zero.readthedocs.io/en/stable/index.html#courses
import pgzrun

alien = Actor('alien')
alien.topright = 0,10

WIDTH = alien.width + 500
HEIGHT = alien.height + 200

def draw():
    screen.clear()
    alien.draw()

def update():
    alien.right +=2
    alien.y += 2
    if alien.left > WIDTH:
        alien.right = 0
    if alien.y > HEIGHT:
        alien.y = 10

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'

pgzrun.go()
