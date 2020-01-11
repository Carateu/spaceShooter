import pygame

import random

class EnemyShip(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)

        self.image = pygame.image.load("data/enemyship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [80,80])
        self.rect = self.image.get_rect()
    

    def update(self):
        self.rect[0] -= 3


    
    


        

