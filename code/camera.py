import pygame
from settings import *
from tile import Tile
from player import Player
from debug import *

class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        super().__init__()