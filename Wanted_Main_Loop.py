import pygame
pygame.init()

#Config stuff, holds a bunch of useful variables and the like.
res = (800, 1000)
fps = 60
squares = 100

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
fontsize = 48
ALIENS = ["images/Green_Alien.png","images/Yellow_Alien.png","images/Blue_Alien.png", "images/Red_Alien.png"]
gameover = pygame.mixer.Sound("sfx/game-over-arcade.mp3")
ding = pygame.mixer.Sound("sfx/retro-coin-4-236671.mp3")

font = pygame.font.Font(None,fontsize)