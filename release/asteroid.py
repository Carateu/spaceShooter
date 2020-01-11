import pygame

class Asteroid(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)

        self.image = pygame.image.load("data/asteroid.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [75,75])
        self.rect = self.image.get_rect() 

    def update(self):
        self.rect[0] -= 2

        if self.rect[0] < -100:
            self.kill()