import pygame
import random
import math
# initialization
pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 600))

# Background image
backgroundImg = pygame.image.load("background.png")

# Title and icon
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load("player.png")
playerX = 368
playerY = 480
playerX_change = 0

# Enemy
enemyImg = pygame.image.load("enemy.png")
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = -1

# Bullet
# Ready - you can't see the bullet on the screen
# Fire - the bullet is currently moving
bulletImg = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 490
bulletY_change = -6
bullet_state = "ready"

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def fire_bullet (x, y):
    global bullet_state
    bullet_state = "fire"

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX,2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False

# Infinite Game Loop
running = True

while running:

    # RGB = Red, Green, Blue
    # Filling background with color
    # screen.fill((0, 0, 0))
    # Filling background img
    screen.blit(backgroundImg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed or not
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_LEFT:
                playerX_change = -4

            if event.key == pygame.K_RIGHT:
                playerX_change = 4

            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


# bullet movement
    if bullet_state == "fire":
        screen.blit(bulletImg, (bulletX + 16, bulletY))
        bulletY += bulletY_change

    if bulletY <= 0:
        bulletY = 490
        bullet_state = "ready"

# enemy movement
    enemyX += enemyX_change
    if enemyX >= 736:
        enemyY +=50
        enemyX_change *= -1
    if enemyX <=0:
        enemyY +=50
        enemyX_change *= -1

# player movement
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    if playerX >=736:
        playerX = 736
    # Collision
    collision = isCollision(enemyX, enemyY, bulletX, bulletY)
    if collision:
        bulletY = 490
        bullet_state = "ready"
        score += 1
        print(score)
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
'''
# Collision
    # Distance between bullet and the enemy to detect collision
    DistanceX = pow((enemyX - bulletX), 2)
    DistanceY = pow((enemyY - bulletY), 2)
    distance = math.sqrt(DistanceX + DistanceY)
    print(distance)
    if distance <= 32:
        enemyX = random.randint(0, 736)
        enemyY = random.randint(50, 150)
        enemy(enemyX, enemyY)
'''


