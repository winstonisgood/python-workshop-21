import pygame
import random
import sys
import os

# Initialize Pygame
pygame.init()

# Game window settings
WIDTH = 800
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Side Scroller Jump Game")

# Color definitions
SKY_BLUE = (135, 206, 235)
GROUND_COLOR = (101, 67, 33)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load image resources
def load_image(name, scale=1):
    try:
        # Try to load image
        image_path = f"images/{name}.png"
        image = pygame.image.load(image_path).convert_alpha()
        if scale != 1:
            new_size = (int(image.get_width() * scale), int(image.get_height() * scale))
            image = pygame.transform.scale(image, new_size)
        return image
    except pygame.error as e:
        # If image loading fails, create a colored rectangle
        print(f"Cannot load image: {name}.png - {e}, using placeholder")
        if name == "p3_stand":
            surf = pygame.Surface((50, 70), pygame.SRCALPHA)
            # Draw pink character
            pygame.draw.rect(surf, (255, 105, 180), (5, 10, 40, 50), border_radius=10)
            # Eyes
            pygame.draw.circle(surf, WHITE, (15, 25), 8)
            pygame.draw.circle(surf, WHITE, (35, 25), 8)
            pygame.draw.circle(surf, BLACK, (15, 25), 4)
            pygame.draw.circle(surf, BLACK, (35, 25), 4)
            # Mouth
            pygame.draw.arc(surf, BLACK, (15, 40, 20, 15), 0, 3.14, 2)
            return surf
        elif name == "cactus":
            surf = pygame.Surface((30, 60), pygame.SRCALPHA)
            # Draw cactus
            pygame.draw.rect(surf, (34, 139, 34), (0, 10, 30, 50))
            # Cactus spikes
            pygame.draw.rect(surf, (34, 139, 34), (0, 20, 10, 5))
            pygame.draw.rect(surf, (34, 139, 34), (20, 20, 10, 5))
            pygame.draw.rect(surf, (34, 139, 34), (0, 40, 10, 5))
            pygame.draw.rect(surf, (34, 139, 34), (20, 40, 10, 5))
            return surf
        else:
            # Generic placeholder
            surf = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.rect(surf, (255, 0, 0), (0, 0, 50, 50))
            return surf

# Make sure images directory exists
if not os.path.exists("images"):
    os.makedirs("images")
    print("Please place player image as 'p3_stand.png' and obstacle as 'cactus.png' in images folder")

# Load images
player_img = load_image("p3_stand", 0.8)
cactus_img = load_image("cactus", 0.8)

# Create ground texture
ground_img = pygame.Surface((WIDTH, 50))
ground_img.fill(GROUND_COLOR)
# Add ground texture details
for i in range(0, WIDTH, 20):
    pygame.draw.line(ground_img, (80, 50, 20), (i, 0), (i, 50), 1)
for i in range(0, 50, 5):
    pygame.draw.line(ground_img, (120, 80, 40), (0, i), (WIDTH, i), 1)

# Game variables
clock = pygame.time.Clock()
FPS = 60
GRAVITY = 0.8
SCROLL_SPEED = 5
GROUND_HEIGHT = 50
OBSTACLE_FREQUENCY = 1500  # milliseconds
score = 0
game_over = False
last_obstacle = pygame.time.get_ticks()

# Player class
class Player:
    def __init__(self):
        self.image = player_img
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = 100
        self.y = HEIGHT - GROUND_HEIGHT - self.height
        self.vel_y = 0
        self.jumping = False
        self.jump_power = -16
        # Create collision rectangle (smaller than image for fair gameplay)
        self.rect = pygame.Rect(self.x + 10, self.y + 5, self.width - 20, self.height - 10)
    
    def update(self):
        # Gravity effect
        self.vel_y += GRAVITY
        self.y += self.vel_y
        
        # Check if landed
        if self.y >= HEIGHT - GROUND_HEIGHT - self.height:
            self.y = HEIGHT - GROUND_HEIGHT - self.height
            self.vel_y = 0
            self.jumping = False
        
        # Update collision rectangle position
        self.rect.x = self.x + 10
        self.rect.y = self.y + 5
    
    def jump(self):
        if not self.jumping:
            self.vel_y = self.jump_power
            self.jumping = True
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        # Optional: draw collision rectangle for debugging
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)

# Obstacle class
class Obstacle:
    def __init__(self, x):
        self.image = cactus_img
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.x = x
        self.y = HEIGHT - GROUND_HEIGHT - self.height
        self.passed = False
        # Create collision rectangle (smaller than image for fair gameplay)
        self.rect = pygame.Rect(self.x + 5, self.y + 5, self.width - 10, self.height - 10)
    
    def update(self):
        self.x -= SCROLL_SPEED
        # Update collision rectangle position
        self.rect.x = self.x + 5
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))
        # Optional: draw collision rectangle for debugging
        # pygame.draw.rect(screen, (255, 0, 0), self.rect, 1)

# Cloud class (for background decoration)
class Cloud:
    def __init__(self):
        self.x = WIDTH + random.randint(0, 100)
        self.y = random.randint(50, 200)
        self.speed = random.uniform(0.5, 1.5)
        self.size = random.uniform(0.5, 1.2)
        self.image = self.create_cloud_image()
    
    def create_cloud_image(self):
        surf = pygame.Surface((80, 40), pygame.SRCALPHA)
        pygame.draw.circle(surf, (255, 255, 255, 200), (20, 20), 20)
        pygame.draw.circle(surf, (255, 255, 255, 200), (40, 15), 15)
        pygame.draw.circle(surf, (255, 255, 255, 200), (60, 20), 20)
        return pygame.transform.scale(surf, (int(80 * self.size), int(40 * self.size)))
    
    def update(self):
        self.x -= self.speed
        if self.x < -100:
            self.x = WIDTH + random.randint(0, 100)
            self.y = random.randint(50, 200)
    
    def draw(self):
        screen.blit(self.image, (self.x, self.y))

# Create player, obstacles list and clouds
player = Player()
obstacles = []
clouds = [Cloud() for _ in range(5)]

# Game main loop
running = True
while running:
    clock.tick(FPS)
    
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                player.jump()
            if event.key == pygame.K_r and game_over:
                # Reset game
                game_over = False
                score = 0
                player = Player()
                obstacles = []
                SCROLL_SPEED = 5
            if event.key == pygame.K_ESCAPE:
                running = False
    
    if not game_over:
        # Update player
        player.update()
        
        # Update clouds
        for cloud in clouds:
            cloud.update()
        
        # Generate obstacles
        time_now = pygame.time.get_ticks()
        if time_now - last_obstacle > OBSTACLE_FREQUENCY:
            obstacles.append(Obstacle(WIDTH))
            last_obstacle = time_now
        
        # Update obstacles
        for obstacle in obstacles[:]:
            obstacle.update()
            
            # Check collision
            if player.rect.colliderect(obstacle.rect):
                game_over = True
            
            # Check if passed obstacle and score
            if not obstacle.passed and obstacle.x < player.x:
                obstacle.passed = True
                score += 1
                # Increase speed every 5 points
                if score % 5 == 0:
                    SCROLL_SPEED += 0.5
            
            # Remove off-screen obstacles
            if obstacle.x + obstacle.width < 0:
                obstacles.remove(obstacle)
    
    # Draw background - gradient sky
    for y in range(HEIGHT):
        # From light blue at top to slightly darker at bottom
        color_factor = y / HEIGHT
        color = (
            int(135 * (1 - color_factor) + 100 * color_factor),
            int(206 * (1 - color_factor) + 180 * color_factor),
            int(235 * (1 - color_factor) + 210 * color_factor)
        )
        pygame.draw.line(screen, color, (0, y), (WIDTH, y))
    
    # Draw clouds
    for cloud in clouds:
        cloud.draw()
    
    # Draw distant mountains
    for i in range(5):
        mountain_height = random.randint(50, 100)
        pygame.draw.polygon(screen, (100, 100, 100), [
            (i * 200, HEIGHT - GROUND_HEIGHT),
            (i * 200 + 100, HEIGHT - GROUND_HEIGHT - mountain_height),
            (i * 200 + 200, HEIGHT - GROUND_HEIGHT)
        ])
    
    # Draw ground
    screen.blit(ground_img, (0, HEIGHT - GROUND_HEIGHT))
    
    # Draw player and obstacles
    for obstacle in obstacles:
        obstacle.draw()
    player.draw()
    
    # Display score
    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f'Score: {score}', True, BLACK)
    screen.blit(score_text, (10, 10))
    
    # Display controls hint
    if not game_over:
        controls_font = pygame.font.SysFont(None, 24)
        controls_text = controls_font.render('Press SPACE to jump', True, BLACK)
        screen.blit(controls_text, (WIDTH - controls_text.get_width() - 10, 10))
    
    # Game over display
    if game_over:
        # Semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        overlay.fill((0, 0, 0, 150))
        screen.blit(overlay, (0, 0))
        
        game_over_font = pygame.font.SysFont(None, 72)
        game_over_text = game_over_font.render('Game Over', True, RED)
        screen.blit(game_over_text, (WIDTH//2 - game_over_text.get_width()//2, HEIGHT//2 - 50))
        
        score_font = pygame.font.SysFont(None, 48)
        score_display = score_font.render(f'Final Score: {score}', True, WHITE)
        screen.blit(score_display, (WIDTH//2 - score_display.get_width()//2, HEIGHT//2 + 10))
        
        restart_font = pygame.font.SysFont(None, 36)
        restart_text = restart_font.render('Press R to restart', True, WHITE)
        screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT//2 + 70))
    
    # Update display
    pygame.display.update()

pygame.quit()
sys.exit()