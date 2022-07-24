import pygame
from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('img/graphics/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
        self.direction = pygame.math.Vector2()

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.direction = -1
        elif keys[pygame.K_DOWN]:
            self.direction = 1
        else:
            self.direction = 0

        if keys[pygame.K_RIGHT]:
            self.direction = -1
        elif keys[pygame.K_LEFT]:
            self.direction = 1
        else:
            self.direction = 0

    def update(self):
        self.input()

        

