import pygame
import sys
import random
from pygame.locals import *
from pygame.math import Vector2

pygame.init()
main_clock = pygame.time.Clock()

WINDOWWIDTH = 800
HALFWINDOWWIDTH = WINDOWWIDTH / 2
WINDOWHEIGHT = 400
HALFWINDOWHEIGHT = WINDOWHEIGHT / 2
surf = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Pong With No Walls')


def vector2(xy_tuple, scale):
    vector = Vector2()
    vector[0], vector[1] = xy_tuple[0], xy_tuple[1]
    return vector * scale


# Set up keyboard variables.
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 6
COMPUTERMOVESPEED = 3.1
COMPUTERMOVESPEEDS = 1.7
BALLSPEED = 5

v = vector2((random.choice([BALLSPEED, BALLSPEED]), random.choice([BALLSPEED, -BALLSPEED])), 1)

# Set up the block data structure.
ball = pygame.Rect(HALFWINDOWWIDTH, HALFWINDOWHEIGHT, 10, 10)
ballImage = pygame.image.load('Pong Ball.png')
ballStretchImage = pygame.transform.scale(ballImage, (10, 10))

# Player Paddle
player = pygame.Rect(WINDOWWIDTH - 10, HALFWINDOWHEIGHT, 10, 100)
playerImage = pygame.image.load('Pong Paddle Green.png')
playerStretchImage = pygame.transform.scale(playerImage, (10, 100))

# Player Top Paddle
player1 = pygame.Rect(WINDOWWIDTH - 100, 0, 100, 10)
player1Image = pygame.image.load('Pong Paddle Green.png')
player1StretchImage = pygame.transform.scale(playerImage, (100, 10))

# Player Bottom Paddle
player2 = pygame.Rect(WINDOWWIDTH - 100, WINDOWHEIGHT - 10, 100, 10)
player2Image = pygame.image.load('Pong Paddle Green.png')
player2StretchImage = pygame.transform.scale(playerImage, (100, 10))

# Computer Paddle
computer = pygame.Rect(0, HALFWINDOWHEIGHT, 10, 100)
computerImage = pygame.image.load('Pong Paddle Pink.png')
computerStretchImage = pygame.transform.scale(computerImage, (10, 100))

# Computer Top Paddle
computer1 = pygame.Rect(0, 0, 100, 10)
computerImage = pygame.image.load('Pong Paddle Pink.png')
computer1StretchImage = pygame.transform.scale(computerImage, (100, 10))

# Computer Bottom Paddle
computer2 = pygame.Rect(0, WINDOWHEIGHT - 10, 100, 10)
computerImage = pygame.image.load('Pong Paddle Pink.png')
computer2StretchImage = pygame.transform.scale(computerImage, (100, 10))

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sound
win = pygame.mixer.Sound('Win Sound.wav')
lost = pygame.mixer.Sound('Loss Sound.wav')
hit = pygame.mixer.Sound('Hit Sound.wav')
playSound = True

# Tracker
playerScore = 0
computerScore = 0

# Score
basicFont = pygame.font.SysFont(None, 48)
victoryFont = pygame.font.SysFont(None, 100)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT or event.key == K_a:
                moveRight = False
                moveLeft = True
            if event.key == K_RIGHT or event.key == K_d:
                moveLeft = False
                moveRight = True
            if event.key == K_DOWN or event.key == K_s:
                moveUp = False
                moveDown = True
            if event.key == K_UP or event.key == K_w:
                moveDown = False
                moveUp = True
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == K_LEFT or event.key == K_a:
                moveLeft = False
            if event.key == K_RIGHT or event.key == K_d:
                moveRight = False
            if event.key == K_UP or event.key == K_w:
                moveUp = False
            if event.key == K_DOWN or event.key == K_s:
                moveDown = False
            if event.key == K_y:
                v = vector2((random.choice([BALLSPEED, -BALLSPEED]), random.choice([BALLSPEED, -BALLSPEED])), 1)
                ball = pygame.Rect(HALFWINDOWWIDTH, HALFWINDOWHEIGHT, 10, 10)
                playerScore = 0
                computerScore = 0
                playSound = True

    surf.fill(BLACK)

    # Dash Lines down middle
    pygame.draw.line(surf, WHITE, (HALFWINDOWWIDTH, 0), (HALFWINDOWWIDTH, 40), 3)
    pygame.draw.line(surf, WHITE, (HALFWINDOWWIDTH, 60), (HALFWINDOWWIDTH, 100), 3)
    pygame.draw.line(surf, WHITE, (HALFWINDOWWIDTH, 120), (HALFWINDOWWIDTH, 160), 3)
    pygame.draw.line(surf, WHITE, (HALFWINDOWWIDTH, 180), (HALFWINDOWWIDTH, 220), 3)
    pygame.draw.line(surf, WHITE, (HALFWINDOWWIDTH, 240), (HALFWINDOWWIDTH, 280), 3)
    pygame.draw.line(surf, WHITE, (HALFWINDOWWIDTH, 300), (HALFWINDOWWIDTH, 340), 3)
    pygame.draw.line(surf, WHITE, (HALFWINDOWWIDTH, 360), (HALFWINDOWWIDTH, 400), 3)

    score = basicFont.render(str(playerScore), True, WHITE, BLACK)
    score2 = basicFont.render(str(computerScore), True, WHITE, BLACK)
    surf.blit(score, (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT / 8))
    surf.blit(score2, (WINDOWWIDTH / 4, WINDOWHEIGHT / 8))
    if playerScore > 10 and (playerScore - computerScore) > 2:
        victory = basicFont.render('Player Wins!', True, WHITE, BLACK)
        surf.blit(score, (WINDOWWIDTH * 3 / 4, WINDOWHEIGHT / 8))
        surf.blit(victory, (WINDOWWIDTH * 2.5 / 4, WINDOWHEIGHT / 5))
        v[0] = 0
        v[1] = 0
        victory = basicFont.render('Do you want to continue? Y/ESCAPE', True, WHITE, BLACK)
        surf.blit(victory, (100, WINDOWHEIGHT / 2))
        if playSound:
            win.play()
            playSound = not playSound
    if computerScore > 10 and (playerScore - computerScore) < -2:
        victory = basicFont.render('Computer Wins!', True, WHITE, BLACK)
        surf.blit(score2, (WINDOWWIDTH / 4, WINDOWHEIGHT / 8))
        surf.blit(victory, (WINDOWWIDTH / 8, WINDOWHEIGHT / 5))
        v[0] = 0
        v[1] = 0
        victory = basicFont.render('Do you want to continue? Y/ESCAPE', True, WHITE, BLACK)
        surf.blit(victory, (100, WINDOWHEIGHT / 2))
        if playSound:
            lost.play()
            playSound = not playSound

    # Ball moving
    ball.left += v[0]
    ball.top += v[1]

    surf.blit(ballStretchImage, ball)

    if ball.right > computer1.left:
        if computer1.right < HALFWINDOWWIDTH:
            computer1.right += COMPUTERMOVESPEED
            computer2.right += COMPUTERMOVESPEED
    if ball.left < computer1.left:
        if computer1.left > 0:
            computer1.left -= COMPUTERMOVESPEED
            computer2.left -= COMPUTERMOVESPEED
    if ball.top < computer.top:
        if computer.top > 0:
            computer.top -= COMPUTERMOVESPEEDS
    if ball.top > computer.top:
        if computer.bottom < WINDOWHEIGHT:
            computer.top += COMPUTERMOVESPEEDS
    surf.blit(computerStretchImage, computer)
    surf.blit(computer1StretchImage, computer1)
    surf.blit(computer2StretchImage, computer2)

    # Moving of player
    if moveDown and player.bottom < WINDOWHEIGHT - 10:
        player.top += MOVESPEED
    if moveUp and player.top > 10:
        player.top -= MOVESPEED
    if moveLeft and player1.left and player2.left > HALFWINDOWWIDTH + 8:
        player1.left -= MOVESPEED
        player2.left -= MOVESPEED
    if moveRight and player1.left and player2.left < WINDOWWIDTH - 100:
        player1.right += MOVESPEED
        player2.right += MOVESPEED

    surf.blit(playerStretchImage, player)
    surf.blit(player1StretchImage, player1)
    surf.blit(player2StretchImage, player2)

    if player.colliderect(ball) or computer.colliderect(ball):
        hit.play()
        v[0] *= -1
    if player1.colliderect(ball) or player2.colliderect(ball) or computer1.colliderect(ball) or \
            computer2.colliderect(ball):
        hit.play(0)
        v[1] *= -1

    if ball.right < HALFWINDOWWIDTH:
        if ball.right < 0:
            playerScore += 1
            v = vector2((random.choice([BALLSPEED, -BALLSPEED]), random.choice([BALLSPEED, -BALLSPEED])), 1)
            ball = pygame.Rect(HALFWINDOWWIDTH, HALFWINDOWHEIGHT, 10, 10)
        if ball.bottom < 0:
            playerScore += 1
            v = vector2((random.choice([BALLSPEED, -BALLSPEED]), random.choice([BALLSPEED, -BALLSPEED])), 1)
            ball = pygame.Rect(HALFWINDOWWIDTH, HALFWINDOWHEIGHT, 10, 10)
        if ball.top > WINDOWHEIGHT:
            playerScore += 1
            v = vector2((random.choice([BALLSPEED, -BALLSPEED]), random.choice([BALLSPEED, -BALLSPEED])), 1)
            ball = pygame.Rect(HALFWINDOWWIDTH, HALFWINDOWHEIGHT, 10, 10)
    if ball.left > HALFWINDOWWIDTH:
        if ball.left > WINDOWWIDTH:
            computerScore += 1
            v = vector2((random.choice([BALLSPEED, -BALLSPEED]), random.choice([BALLSPEED, -BALLSPEED])), 1)
            ball = pygame.Rect(HALFWINDOWWIDTH, HALFWINDOWHEIGHT, 10, 10)
        if ball.bottom < 0:
            computerScore += 1
            v = vector2((random.choice([BALLSPEED, -BALLSPEED]), random.choice([BALLSPEED, -BALLSPEED])), 1)
            ball = pygame.Rect(HALFWINDOWWIDTH, HALFWINDOWHEIGHT, 10, 10)
        if ball.top > WINDOWHEIGHT:
            computerScore += 1
            v = vector2((random.choice([BALLSPEED, -BALLSPEED]), random.choice([BALLSPEED, -BALLSPEED])), 1)
            ball = pygame.Rect(HALFWINDOWWIDTH, HALFWINDOWHEIGHT, 10, 10)

    pygame.display.update()
    main_clock.tick(40)
