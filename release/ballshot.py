import pygame

class Ballshot(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)

        self.image = pygame.image.load("data/ball.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [15,15])
        self.rect = self.image.get_rect() 
        

    def update(self):
        speedshot = 4
        self.rect[0] += speedshot

        if self.rect[0] > 900:
            self.kill()