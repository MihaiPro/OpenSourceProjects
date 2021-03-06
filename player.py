"""
This file contains the Player class with any necessary methods
to control the player which is by the way a sprite object.
"""
import pygame
from main import *


class Player(pygame.sprite.Sprite):

    # Think of this as the velocity of the player
    change_x = 1
    change_y = 1

    def __init__(self, x, y, width, height, tile_size):
        pygame.sprite.Sprite.__init__(self)

        # Create player image and set the coordinates
        # of image rectangle
        self.image = pygame.Surface([width, height])
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.tile_size = tile_size
        self.inventory = {
                            'gold': 0,
                            'pouch': []
                        }

    def get_pos(self):
        return self.x, self.y

    def set_pos(self, x, y):
        self.x, self.y = x, y

    def move(self, x, y, tiles):
        """
        Changes the location of the player
        """
        if x != 0:
            new_x = self.x + x
            if not tiles[self.y][new_x] in (WALL, DOOR):
                self.x = new_x
        if y != 0:
            new_y = self.y + y
            if not tiles[new_y][self.x] in (WALL, DOOR):
                self.y = new_y
                
    def search_area(self, tiles, item):
        if item == tiles[self.y][self.x + 1]:
            return self.x + 1, self.y
        elif item == tiles[self.y][self.x - 1]:
            return self.x - 1, self.y 
        elif item == tiles[self.y + 1][self.x]:
            return self.x, self.y + 1
        elif item == tiles[self.y - 1][self.x]:
            return self.x, self.y - 1 
        else:
            return None, None
                
    def get_item(self, tiles):
        """
        If item under player, put item in inventory and remove item from map
        """
        if tiles[self.y][self.x] == GOLD:
            self.inventory['gold'] += 1
        if tiles[self.y][self.x] == KEY:
            self.inventory['pouch'].append(KEY)
        if tiles[self.y][self.x] != '.':
            tiles[self.y][self.x] = '.'
            
    def get_inventory(self):
        return self.inventory

    def use_key(self, tiles):
        if KEY in self.inventory['pouch']:
            x, y = self.search_area(tiles = tiles, item = DOOR)
            if x != None:
                tiles[y][x] = '.'
                self.inventory['pouch'].remove(KEY)
                
    def draw(self, screen):
        """
        Draws the player on the screen
        """
        pygame.draw.rect(screen, BLACK, [self.x * self.tile_size, self.y * self.tile_size, self.tile_size, self.tile_size], 0);
            
