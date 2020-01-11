import pygame
import random

class Enemyshot(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)

        self.image = pygame.image.load("data/ball.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [10,10])
        self.rect = self.image.get_rect() 
        

    def update(self):
        speedshot = 4
        self.rect[0] -= speedshot
        
        if self.rect[0] < -200:
            self.kill()

   