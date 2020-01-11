import pygame

class Spaceship(pygame.sprite.Sprite):
    def __init__(self,group):
        super().__init__(group)

        self.image = pygame.image.load("data/spaceship.png").convert_alpha()
        self.image = pygame.transform.scale(self.image, [80,80])
        self.rect = self.image.get_rect()
        self.rect[0] = 0
        self.rect[1] = 300 

    def updateShip(self):
        keys = pygame.key.get_pressed()
        speedShip = 3
        if keys[pygame.K_w]:
            self.rect[1] -= speedShip 
        elif keys[pygame.K_s]:
            self.rect[1] += speedShip
        elif keys[pygame.K_d]:
            self.rect[0] += speedShip
        elif keys[pygame.K_a]:
            self.rect[0] -= speedShip  

        if self.rect[1] < 0:
            self.rect[1] = 0
        elif self.rect[1] > 600:
            self.rect[1] = 530
        elif self.rect[0] < 0:
            self.rect[0] = 0
        elif self.rect[0] > 800:
            self.rect[0] = 730