import pygame
import random
import math
# initialization
pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 600))

# enemy class
class Enemy:

    def __init__(self, enemyImg, enemyX, enemyY, enemyX_change):
        self.enemyImg = enemyImg
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = enemyX_change


class Bullet:

    def __init__(self, bulletImg, bulletX, bulletY, bulletY_change, bullet_state):
        # Bullets
        # Ready - you can't see the bullet on the screen
        # Fire - the bullet is currently moving
        self.bulletImg = bulletImg
        self.bulletX = bulletX
        self.bulletY = bulletY
        self.bulletY_change = bulletY_change
        self.bullet_state = bullet_state

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

# Enemies
list_of_enemies = []
number_of_enemies = 5


# Bullets
# Ready - you can't see the bullet on the screen
# Fire - the bullet is currently moving
list_of_bullets = []
number_of_bullets = 0


# bulletImg = pygame.image.load("bullet.png")
# bulletX = 0
# bulletY = 490
# bulletY_change = -6
# bullet_state = "ready"

for i in range(number_of_enemies):
    list_of_enemies.append(Enemy(pygame.image.load("enemy.png"), random.randint(0, 736), random.randint(50, 150), -1))

score = 0

def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, i):

    screen.blit(list_of_enemies[i].enemyImg, (x, y))


def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
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

                    bulletX = playerX
                    list_of_bullets.append(Bullet(pygame.image.load("bullet.png"), bulletX, 490, -6, "ready"))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


# bullet movement
    for i in range(0, len(list_of_bullets)):

        screen.blit(list_of_bullets[i].bulletImg, (list_of_bullets[i].bulletX + 16, list_of_bullets[i].bulletY))
        list_of_bullets[i].bulletY += list_of_bullets[i].bulletY_change

# enemy movement
    for i in range(number_of_enemies):
        list_of_enemies[i].enemyX += list_of_enemies[i].enemyX_change
        if list_of_enemies[i].enemyX >= 736:
            list_of_enemies[i].enemyY +=50
            list_of_enemies[i].enemyX_change *= -1
        if list_of_enemies[i].enemyX <=0:
            list_of_enemies[i].enemyY +=50
            list_of_enemies[i].enemyX_change *= -1
            for j in range(0, len(list_of_bullets)):
                collision = [[], []]
                collision[i][j].append(isCollision(list_of_enemies[i].enemyX, list_of_enemies[i].enemyY, list_of_bullets[j].bulletX, list_of_bullets[j].bulletY))
                print(collision)
                if collision[i][j]:
                    score += 1
                    print(score)
                    list_of_enemies[i].enemyX = random.randint(0, 736)
                    list_of_enemies[i].enemyY = random.randint(50, 150)
        enemy(list_of_enemies[i].enemyX, list_of_enemies[i].enemyY, i)

    # player movement
    playerX += playerX_change

    if playerX <=0:
        playerX = 0
    if playerX >=736:
        playerX = 736

    player(playerX, playerY)
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
