import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, position, groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = position)

        self.direction = pygame.math.Vector2()
        self.speed = 5

    def keyBoardInput(self):

        keys = pygame.key.get_pressed()

        if keys [pygame.K_UP]:
            self.direction.y = -1
        elif keys [pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys [pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys [pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
    
    def movement(self, speed):
        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
            
        self.rect.center += self.direction * speed

    def update(self):
        self.keyBoardInput()
        self.movement(self.speed)