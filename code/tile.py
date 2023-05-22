import pygame
from pygame.sprite import _Group
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.rect = self.image.get_rect(topleft = position)