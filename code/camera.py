import pygame
from settings import *
from tile import Tile
from player import Player
from debug import *

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()    
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

    def drawSprites(self, player):

        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        for sprite in self.sprites():
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_position)
