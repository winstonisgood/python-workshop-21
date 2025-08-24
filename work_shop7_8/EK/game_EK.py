import pgzrun
import random
from pgzero.keyboard import keys

WIDTH = 800
HEIGHT = 600

# Player setup
p3 = Actor("p3_stand")
p3.images = [
    'p3_walk01', 'p3_walk02', 'p3_walk03', 'p3_walk04', 'p3_walk05',
    'p3_walk06', 'p3_walk07', 'p3_walk08', 'p3_walk09', 'p3_walk10', 'p3_walk11'
]
p3.imageindex = 0
p3.pos = (60, 400)
p3.velocity_y = 0
p3.gravity = 1

# Game state
obstacles = []
obstacles_timeout = 0
score = 0
high_score = 0
game_over = False

def reset_game():
    """Reset everything to start a new game."""
    global obstacles, obstacles_timeout, score, game_over, p3
    obstacles = []
    obstacles_timeout = 0
    score = 0
    game_over = False
    p3.pos = (60, 400)
    p3.velocity_y = 0
    p3.imageindex = 0

def draw():
    screen.clear()
    # Background
    screen.draw.filled_rect(Rect(0, 0, WIDTH, 400), (163, 232, 254))
    screen.draw.filled_rect(Rect(0, 400, WIDTH, 200), (88, 242, 152))

    # Player and obstacles
    p3.draw()
    for obstacle in obstacles:
        obstacle.draw()

    # HUD
    screen.draw.text(f"Score: {score}", (10, 10), fontsize=40, color="white")
    screen.draw.text(f"High Score: {high_score}", (10, 50), fontsize=35, color="yellow")

    # Game over message
    if game_over:
        screen.draw.text("Game Over", center=(WIDTH/2, HEIGHT/2-30), fontsize=60, color="red")
        screen.draw.text(f"Score: {score}", center=(WIDTH/2, HEIGHT/2+20), fontsize=40, color="white")
        screen.draw.text("Press Enter to Restart", center=(WIDTH/2, HEIGHT/2+70), fontsize=30, color="yellow")

def update():
    global obstacles_timeout, score, game_over, high_score

    if game_over:
        return  # Stop game update if over

    # Animate player
    p3.image = p3.images[p3.imageindex]
    p3.imageindex = (p3.imageindex + 1) % len(p3.images)

    # Gravity
    p3.y -= p3.velocity_y
    p3.velocity_y -= p3.gravity
    if p3.y > 400:
        p3.y = 400
        p3.velocity_y = 0

    # Spawn obstacles
    obstacles_timeout += 1
    if obstacles_timeout > 75:
        obstacle = Actor('cactus')
        obstacle.x = WIDTH + 50
        obstacle.y = 400
        obstacles.append(obstacle)
        obstacles_timeout = random.randint(0, 35)

    # Move obstacles
    for obstacle in obstacles[:]:
        obstacle.x -= 5
        if obstacle.x <= -50:
            sounds.point.play()
            obstacles.remove(obstacle)
            score += 1

    # Collision detection
    if p3.collidelist(obstacles) != -1:
        sounds.die.play()
        game_over = True
        if score > high_score:
            high_score = score

# Key press handling (stable reset with Enter key)
def on_key_down(key):
    global p3
    # Jump if space is pressed and game is not over
    if key == keys.SPACE and not game_over and p3.y == 400:
        sounds.jump.play()
        p3.velocity_y = 20
    # Reset game if Enter is pressed and game is over
    elif key == keys.RETURN and game_over:
        reset_game()

pgzrun.go()
