import pgzrun
from pgzero.rect import Rect

p3=Actor("p3_stand")
p3.pos=(35,50)

def draw():
    screen.draw.filled_rect(Rect(0,0,800,400),(163,232,254))
    screen.draw.filled_rect(Rect(0,400,800,200),(88,242,152))
    p3.draw()
    print("1")

def update():
    print(2)

pgzrun.go()
