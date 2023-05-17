import pygame
from tiles import Tile, Bounce, Half
from settings import tile_size, screen_width,screen_height
from player import Player

class Level:
    def __init__(self,level_data,surface):

        # level setup
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
        
    def setup_level(self,layout,):
        self.tiles = pygame.sprite.Group()
        self.bounce = pygame.sprite.Group()
        self.half = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
           for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Player((x,y + 32))
                    self.player.add(player_sprite)
                if cell == 'B':
                    bounce = Bounce((x,y),tile_size)
                    self.bounce.add(bounce)
                if cell == 'H':
                    half = Half((x,y - 48),tile_size)
                    self.half.add(half)

    def scoll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width - screen_width / 4 and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        for sprite in self.bounce.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right
        for sprite in self.half.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right


        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.jump_count = False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
                player.jump_count = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False
                player.jump_count = False
                
        for sprite in self.bounce.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.jump_count = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                    player.jump_count = False
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
                player.jump_count = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False
                player.jump_count = False

        for sprite in self.half.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                    player.jump_count = False
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
                player.jump_count = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False
                player.jump_count = False
    
    def death(self):
        player = self.player.sprite
        if player.direction.y > 50 and player.direction.y < 51:
            image = pygame.image.load("H:\CP2/phog/character/dead.png")
            
        

    def run(self):

        # level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scoll_x()
        # bounce tiles
        self.bounce.update(self.world_shift)
        self.bounce.draw(self.display_surface)

        # half tiles
        self.half.update(self.world_shift)
        self.half.draw(self.display_surface)

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.death()
        self.player.draw(self.display_surface)

