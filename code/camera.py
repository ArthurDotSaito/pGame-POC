import pygame
from settings import *
from tile import Tile
from player import Player
from debug import *

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()    

    def drawSprites(self):
        for sprite in self.sprites():
            self.display_surface.blit(sprite.image,sprite.rect)