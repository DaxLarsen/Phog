import pygame, timer, random, sys
from settings import *
from level import Level


pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
clock = pygame.time.Clock()
level = Level(level_map,screen)
pygame.display.set_caption("Phog")
icon = pygame.image.load("H:\CP2/phog/Phogicon.png")
pygame.display.set_icon(icon)
pygame.font.init()
font = pygame.font.Font('H:\CP2/phog/Gloria_Hallelujah/GloriaHallelujah-Regular.ttf', 48)


"""for row_index,row in enumerate(layout):
    for col_index,cell in enumerate(row):
        x = col_index * tile_size
        y = row_index * tile_size

        if cell = 'X':
            tile = Tile((x,y),tile_size)
            self.tiles.add(tile)"""


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
