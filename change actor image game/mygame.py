import pgzrun

HEIGHT = 500
WIDTH = 500

sprite = Actor("alien")
sprite.pos = HEIGHT/2, WIDTH/2

def draw():
    screen.clear()
    sprite.draw()

def on_mouse_down(pos, button):
    if button == mouse.LEFT and sprite.collidepoint(pos):
        if sprite.image == "alien":
            sprite.image = "bear"
        elif sprite.image == "bear":
            sprite.image = "buffalo"
        elif sprite.image == "buffalo":
            sprite.image = "alien"

pgzrun.go()
