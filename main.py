import pygame
import timer
import random
import sys

screenx = 1200
screeny = 900
fps = 100
ani = 4
x = 0
y = 0
screen = pygame.display.set_mode([screenx, screeny])
pygame.display.set_caption("Phog")
icon = pygame.image.load("H:\CP2/phog/Phogicon.png")
pygame.display.set_icon(icon)
pygame.init()
pygame.font.init()
main = True

while main:
    #Create Backdrop Color
    screen.fill(0,0,0)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.KEYDOWN:
            if event.key == ord('q'):
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False


    pygame.display.update()
    pygame.display.flip()
