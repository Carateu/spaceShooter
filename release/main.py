import os,sys
dirpath = os.getcwd()
sys.path.append(dirpath)

if getattr(sys, "frozen", False):
    os.chdir(sys._MEIPASS)

# importando o módulo pygame
import pygame 
import sys
from asteroid import Asteroid
from spaceship import Spaceship
from ballshot import Ballshot
from enemyship import EnemyShip
from enemyshot import Enemyshot
from pygame.locals import * 

import random

# inicialiazando o pygame   
pygame.init()

SCREEN_RES = [800,600]

# criando a tela 
game_display = pygame.display.set_mode(SCREEN_RES)
pygame.display.set_caption("space shooter")

#background
backgroundGroup = pygame.sprite.Group()

backgroundImage = pygame.sprite.Sprite(backgroundGroup) 
backgroundImage.image = pygame.image.load("data/spaceImage.png")
backgroundImage.image = pygame.transform.scale(backgroundImage.image, SCREEN_RES)
backgroundImage.rect = backgroundImage.image.get_rect()

# asteroid
asteroidGroup = pygame.sprite.Group()

# nave
shipGroup = pygame.sprite.Group()
spaceship = Spaceship(shipGroup)

# nave inimiga
enemyGroup = pygame.sprite.Group()

# shots
shotGroup = pygame.sprite.Group()
enemyshotGroup = pygame.sprite.Group()

# sons do jogo
shotSound = pygame.mixer.Sound("data/shot_01.ogg")

pygame.mixer.music.load("data/throughSpace.ogg")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()
tickTimer = 1000
game_loop = True 

# score do jogo
score = 0
# fonte do score
myfont = pygame.font.SysFont("comicsansms", 28)

# loop principal do jogo
while game_loop:
    clock.tick(120)

    # identificando evento de saída do loop do jogo(clique no exit da tela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_loop = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                shotSound.play()
                newshot = Ballshot(shotGroup)
                newshot.rect.center = spaceship.rect.center

    #logica
    tickTimer += 1
    if tickTimer > 45:
        tickTimer = 0 
        if random.random() < 0.50:
            asteroid = Asteroid(asteroidGroup)
            x = SCREEN_RES[0]
            y = random.randint(0,SCREEN_RES[1] - 100 )
            asteroid.rect.move_ip(x,y)
    
        if random.random() < 0.30:
            enemyship = EnemyShip(enemyGroup)
            x = SCREEN_RES[0]
            y = random.randint(100,SCREEN_RES[1] - 80 )
            enemyship.rect.move_ip(x,y)

            
            enemyshot = Enemyshot(enemyshotGroup)
            enemyshot.rect.center = enemyship.rect.center
        
    backgroundGroup.update()
    asteroidGroup.update()
    shipGroup.update()
    shotGroup.update()
    enemyGroup.update()
    enemyshotGroup.update()

    # colisoes
    colisoes = pygame.sprite.spritecollide(spaceship,asteroidGroup,False)
    colisoes2 = pygame.sprite.spritecollide(spaceship,enemyshotGroup,False)
    if colisoes:
        print("Game Over")
        game_loop = False
    elif colisoes2:
        print("Game Over")
        game_loop = False


    if pygame.sprite.groupcollide(shotGroup, asteroidGroup, True , True):
        score += 1
    elif pygame.sprite.groupcollide(shotGroup, enemyGroup, True , True):
        score += 3


    # definindo o texto com score
    scoretext = myfont.render("Score "+ str(score), 1, (224,224,224))

    # desenhando os objetos na tela
    backgroundGroup.draw(game_display)

    asteroidGroup.draw(game_display)
    shotGroup.draw(game_display)
    shipGroup.draw(game_display)

    enemyGroup.draw(game_display)
    enemyshotGroup.draw(game_display)

    # atualizando a tela do jogo e a navado jogo a cada loop
    game_display.blit(scoretext, (5, 10))
    spaceship.updateShip()
    pygame.display.update()
