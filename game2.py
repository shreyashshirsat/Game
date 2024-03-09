import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Obstacle Avoiding Game")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.centerx = SCREEN_WIDTH // 4
        self.rect.bottom = SCREEN_HEIGHT - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += self.speed

# Define the obstacle class
class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((random.randint(20, 50), random.randint(20, 50)))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH + random.randint(50, 200)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed = random.randint(3, 7)

    def update(self):
        self.rect.x -= self.speed
        if self.rect.right < 0:
            self.rect.x = SCREEN_WIDTH + random.randint(50, 200)
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
            self.speed = random.randint(3, 7)

# Create sprite groups
all_sprites = pygame.sprite.Group()
obstacles = pygame.sprite.Group()

# Create the player
player = Player()
all_sprites.add(player)

# Game loop
running = True
clock = pygame.time.Clock()
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()

    # Generate obstacles
    if random.randint(1, 100) < 5:
        obstacle = Obstacle()
        all_sprites.add(obstacle)
        obstacles.add(obstacle)

    # Check for collisions
    hits = pygame.sprite.spritecollide(player, obstacles, False)
    if hits:
        running = False

    # Draw
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
