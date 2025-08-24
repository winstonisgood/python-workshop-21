import pgzrun
import random
from pgzero.keyboard import keyboard

# player setup
p3 = Actor("p3_stand")
p3.images = [
    'p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05',
    'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09', 'p3_walk10', 'p3_walk11'
]
p3.imageindex = 0
p3.pos = (60, 400) # 100x70 resolution
p3.velocity_y = 0
gravity = 1

# obstacle and score setup
obstacles = []
obstacles_timeout = 0
score = 0
game_over = False


# background color and fonts
def draw():
    if game_over:
        screen.draw.text("Game over",center = (400,200),color="yellow",fontname ="bauhs93",fontsize=35)
        screen.draw.text(f"Score:{score}",center=(400,240),color="white",fontname="bauhs93", fontsize=25)
    else:
        screen.draw.filled_rect(Rect(0, 0, 800, 400), (163, 232, 254))
        screen.draw.filled_rect(Rect(0, 400, 800, 200), (88, 242, 152))

    p3.draw()
    for obstacle in obstacles:
        obstacle.draw()

def update():
    global obstacles_timeout,game_over,score

    if game_over:
        return
    
    p3.image = p3.immag[p3.imageindex]
    p3.imageindex += 1
    if p3.imageindex>=len(p3.images):
        p3.imageindex=0


def update():
    if keyboard.space:
        print("This is space")
    p3.velocity_y = 20
    # gravity
    p3.y -=p3.velocity_y*1
    p3.velocity_y -= gravity
    if p3.y > 400:
        sounds.jump.play()
        p3.y = 400
        p3.velocity_y = 0

# skip the obstacles
    obstacles_timeout += 1
    if obstacles_timeout > 75:
        obstacles = Actor('cactus')
        obstacle.x = 850
        obstacle.y = 400
        obstacles.append(obstacle)
        obstacles_timeout = random.randint(0,35)
        obstacles_timeout = 0

# move the obstacles 
    for obstacle in obstacles:
        obstacle.x -= 5
        if obstacle.x <= 50 and not game_over:
            sounds.point.play()
            obstacles.remove(obstacle)
            score += 1
            print(f"Score:{score}")
    # Collision detection
    if p3.collidelist(obstacles) != -1:
        sounds.die.play()
        game_over = True
        print('Game over')

pgzrun.go()