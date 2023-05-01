import pygame, sys
from settings import *
from level import Level


pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
level = Level(level_map,screen)
pygame.display.set_caption("Phog")
icon = pygame.image.load("H:\CP2/phog/character/Phogicon.png")
pygame.display.set_icon(icon)

main = True

while main:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    #Create Backdrop Color  
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)
