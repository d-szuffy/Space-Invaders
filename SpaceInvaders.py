import pygame, sys
import random
import math
# initialization
pygame.init()

# creating screen
screen = pygame.display.set_mode((800, 600))


# Defining enemy class
class Enemy:

    def __init__(self, enemyImg, enemyX, enemyY, enemyX_change):
        self.enemyImg = enemyImg
        self.enemyX = enemyX
        self.enemyY = enemyY
        self.enemyX_change = enemyX_change


# Defining bullet class
class Bullet:

    def __init__(self, bulletImg, bulletX, bulletY, bulletY_change):
        self.bulletImg = bulletImg
        self.bulletX = bulletX
        self.bulletY = bulletY
        self.bulletY_change = bulletY_change


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

# Start button
StartBtnImg = pygame.image.load("start.png")

# Enemy
list_of_enemies = []
number_of_enemies = 5
prev_score = 0
new_score = 0
# number_of_bullets = 0
list_of_bullets = []
accuracy = 100
# Detecting Mouse button click
click = False

# Setting font
font = pygame.font.SysFont(None, 20)


for i in range(number_of_enemies):
    list_of_enemies.append(Enemy(pygame.image.load("enemy.png"), random.randint(0, 736), random.randint(50, 150), -1))


# Function which creates new bullets
def create_bullets(x):
    # print(number_of_bullets)
    list_of_bullets.append(Bullet(pygame.image.load("bullet.png"), x, 490, -6))


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


# Drawin text on the screen to display current score
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 2, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)


# MAIN MENU
def main_menu():
    while True:
        global backgroundImg, click
        screen.blit(backgroundImg, (0, 0))

        mx, my = pygame.mouse.get_pos()
        button_play = screen.blit(StartBtnImg, (272, 172))
        if button_play.collidepoint(mx, my):
            if click:
                game()
        screen.blit(StartBtnImg, (272, 172))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        pygame.display.update()


# Infinite Game Loop
def game():
    # Player
    global playerImg, playerX, playerY, playerX_change, backgroundImg, font
    # Enemy
    global list_of_enemies, number_of_enemies, new_score, list_of_bullets, accuracy

    running = True
    while running:

        # RGB = Red, Green, Blue
        # Filling background with color
        # screen.fill((0, 0, 0))
        # Filling background img
        screen.blit(backgroundImg, (0, 0))
        draw_text("Score: " + str(new_score), font, (255, 25, 255,), screen, 20, 20)
        draw_text("Bullets fired: " + str(len(list_of_bullets)), font, (255, 25, 255,), screen, 100, 20)
        draw_text("Accuracy: " + str(accuracy) + "%", font, (255, 25, 255,), screen, 220, 20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # if keystroke is pressed or not
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_LEFT:
                    playerX_change = -4

                if event.key == pygame.K_RIGHT:
                    playerX_change = 4

                if event.key == pygame.K_SPACE:

                    bulletX = playerX
                    # print(bulletX)
                    create_bullets(bulletX)

                if event.key == pygame.K_ESCAPE:
                    main_menu()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_change = 0

    # bullets movement
        for i in range(len(list_of_bullets)):
            screen.blit(list_of_bullets[i].bulletImg, (list_of_bullets[i].bulletX + 16, list_of_bullets[i].bulletY))
            list_of_bullets[i].bulletY += list_of_bullets[i].bulletY_change
            if list_of_bullets[i].bulletY <= 0:
                list_of_bullets[i].bulletY = 1000
                list_of_bullets[i].bulletY_change = 0

                # list_of_bullets[i].bulletState = "ready"

    # enemy movement
        for i in range(number_of_enemies):
            list_of_enemies[i].enemyX += list_of_enemies[i].enemyX_change
            if list_of_enemies[i].enemyX >= 736:
                list_of_enemies[i].enemyY += 50
                list_of_enemies[i].enemyX_change *= -1
            if list_of_enemies[i].enemyX <= 0:
                list_of_enemies[i].enemyY += 50
                list_of_enemies[i].enemyX_change *= -1
                # Collision
            for j in range(len(list_of_bullets)):
                collision = isCollision(list_of_enemies[i].enemyX, list_of_enemies[i].enemyY,
                                        list_of_bullets[j].bulletX, list_of_bullets[j].bulletY)
                if collision:
                    new_score += 1
                    list_of_enemies[i].enemyX = random.randint(1, 735)
                    list_of_enemies[i].enemyY = random.randint(50, 150)
                    list_of_bullets[j].bulletY = 1000
                    list_of_bullets[j].bulletY_change = 0
                    # list_of_bullets[i].bulletState = "ready"

            enemy(list_of_enemies[i].enemyX, list_of_enemies[i].enemyY, i)
        # player movement
        playerX += playerX_change

        if playerX <= 0:
            playerX = 0
        if playerX >= 736:
            playerX = 736

        if len(list_of_bullets) == 0:
            accuracy = 100
        else:
            accuracy = "{:.2f}".format(new_score / len(list_of_bullets) * 100)

        player(playerX, playerY)
        pygame.display.update()


main_menu()
