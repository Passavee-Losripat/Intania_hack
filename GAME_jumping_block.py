import pygame
import sys

# Init
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.display.set_caption("Mini Mario")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 100, 255)
GREEN = (0, 200, 0)

# Player
player = pygame.Rect(100, 500, 50, 50)
vel_y = 0
on_ground = False

# Platforms
platforms = [
    pygame.Rect(0, HEIGHT - 40, WIDTH, 40),
    pygame.Rect(200, 450, 150, 20),
    pygame.Rect(400, 350, 150, 20),
    pygame.Rect(600, 250, 150, 20)
]

# Physics
GRAVITY = 1
JUMP_POWER = -15
MOVE_SPEED = 5

def move_player(keys):
    global vel_y, on_ground

    dx = 0
    if keys[pygame.K_LEFT]:
        dx -= MOVE_SPEED
    if keys[pygame.K_RIGHT]:
        dx += MOVE_SPEED
    if keys[pygame.K_SPACE] and on_ground:
        vel_y = JUMP_POWER
        on_ground = False

    # Apply gravity
    vel_y += GRAVITY
    dy = vel_y

    # Move horizontally
    player.x += dx

    # Move vertically and check collisions
    player.y += dy
    on_ground = False
    for plat in platforms:
        if player.colliderect(plat):
            if dy > 0:  # Falling
                player.bottom = plat.top
                vel_y = 0
                on_ground = True
            elif dy < 0:  # Jumping up into platform
                player.top = plat.bottom
                vel_y = 0

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    move_player(keys)

    # Draw
    pygame.draw.rect(screen, BLUE, player)
    for plat in platforms:
        pygame.draw.rect(screen, GREEN, plat)

    pygame.display.flip()
    clock.tick(60)
