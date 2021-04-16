# Mizatorian's Peashooter
# Low Effort Jam 9 (April 2021)
# https://itch.io/jam/low-effort-jam-9
import pygame, sys, io
import math, random

def rotatePlayer(ctrX, ctrY, playerRect, angle=0 ):
    newPlayerRect = None
    return newPlayerRect

def clip(x, min, max) :
    if( min > max ) :  return x    
    elif( x < min ) :  return min
    elif( x > max ) :  return max
    else :             return x



################################################
clock = pygame.time.Clock()

pygame.init() # initiates pygame
pygame.display.set_caption('Mizatorian LowEffortJam9 Peashooter')

WIDTH=600
HEIGHT=400
WINDOW_SIZE = (WIDTH,HEIGHT)

COLOR_WHITE = (255,255,255)
COLOR_BLACK = (0,0,0)
COLOR_RED = (255,0,0)
COLOR_BLUE = (0,0,255)
COLOR_GREEN = (0,255,0)
COLOR_YELLOW = (255,255,0)
COLOR_GRAYDARK = (90,90,90)
COLOR_GRAYMED = (120,120,120)
COLOR_GRAYLIGHT = (190,190,190)
FPS = 60

screen = pygame.display.set_mode(WINDOW_SIZE,0,32) # initiate the window

gamescreen = pygame.Surface(WINDOW_SIZE) # initiate the surface
menuscreen   = pygame.Surface(WINDOW_SIZE) # initiate the surface

ismenu=True

player_rect = pygame.Rect(0,0,36,36)

rotation = math.pi/40
frame=0
score=0
firsttime=True
playerangle = 0

pygame.mixer.music.load("music.mid") #music from https://www.link.cs.cmu.edu/melody-generator/
pygame.mixer.music.play(-1)
ohohsound   = pygame.mixer.Sound("sfxr_ohoh.wav")
bouncesound = pygame.mixer.Sound("sfxr_bounce.wav")
scoresound  = pygame.mixer.Sound("sfxr_score.wav")
shootsound  = pygame.mixer.Sound("sfxr_shoot.wav")

while True: # main game loop
    gamescreen.fill(COLOR_GRAYDARK) # Grey background
    menuscreen.fill(COLOR_GRAYDARK)
    frame += 1

    if not ismenu:
        Player = rotatePlayer(80,80, player_rect, angle=playerangle )

        # Draw walls
        pygame.draw.rect(gamescreen, COLOR_GRAYMED, pygame.Rect(0, 0, 10, 400))
        pygame.draw.rect(gamescreen, COLOR_GRAYMED, pygame.Rect(590, 0, 10, 400))
        pygame.draw.rect(gamescreen, COLOR_GRAYMED, pygame.Rect(0, 0, 600, 40 ))
        pygame.draw.rect(gamescreen, COLOR_GRAYMED, pygame.Rect(0, 390, 600, 10 ))

        # Display Player and Ball (rects)
        # gamescreen.blit(player_img,(player_rect.x-scroll[0],player_rect.y-scroll[1]))
        pygame.draw.rect(gamescreen, COLOR_GREEN, player_rect)

        font = pygame.font.Font('at01.ttf', 32)
        text = font.render('Score: ' + str(score), True, COLOR_BLACK, COLOR_GRAYMED )
        textRect = text.get_rect()
        textRect.center = (WIDTH/2,20)
        gamescreen.blit(text, textRect)


    if ismenu:
        if not firsttime:
            pygame.draw.rect(menuscreen, COLOR_GRAYDARK, (50,50,300,100))
            font = pygame.font.Font('at01.ttf', 32)
            text = font.render('Score: ' + str(score), True, COLOR_WHITE, COLOR_GRAY1 )
            textRect = text.get_rect()
            textRect.center = (WIDTH/2,100)
            menuscreen.blit(text, textRect)

#        pygame.draw.rect(menuscreen, COLOR_GRAYMED, (50,200,300,300))
        font = pygame.font.Font('at01.ttf', 24)
        textlist = ["Mizatorian's Low Effort Jam 9",
                    " ",
                    "Peashooter",
                    "Sorry, this is incomplete.",
                    "Press UPARROW when the player is rotated in the",
                    "correct direction to shoot",
                    " ",
                    "Press SPACE to start",
                    " ",
                    "Q = Quit"]
        start = 50

        for item in textlist:
            text = font.render(item, True, COLOR_WHITE, COLOR_GRAYDARK)
            textRect = text.get_rect()
            textRect.center = (WIDTH/2,start)
            start += 20
            menuscreen.blit(text, textRect)

    # Event handler loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and ismenu == False:
                shoot = True
            if event.key == pygame.K_SPACE and ismenu == True:
                ismenu = True # should we wait for user to keyup
            if event.key == pygame.K_q:
                pygame.quit()
                sys.exit()
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                shoot=False
            if event.key == pygame.K_SPACE and ismenu == True:
                ismenu = False
                rotate = True
                #Reset game variables, start game
                firsttime = False
                player_rect = pygame.Rect(100,500,200,10)
                score=0
        
    if ismenu:
        screen.blit(pygame.transform.scale(menuscreen,WINDOW_SIZE),(0,0))
    else:
        screen.blit(pygame.transform.scale(gamescreen,WINDOW_SIZE),(0,0))
    pygame.display.update()
    clock.tick(FPS)
