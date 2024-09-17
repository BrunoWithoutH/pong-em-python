import pygame
import sys
pygame.init()

image = pygame.image.load('images/francisca.png')
image2 = pygame.image.load('images/cris.png')
screen = pygame.display.set_mode((600,600))
pygame.display.set_caption("Pong")
bolatam = 10
alturaj = 80
larguraj = 10
bolax = 300
bolay= 300
vel_bolax = 1.5
vel_bolay = 1.5
velocidade_jogador = 3
coordx1 = 0
coordy1 = 260
coordx2 = 590
coordy2 = 260
pontos1 = 0
pontos2 = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill((0,0,0))
    screen.blit(image, (0, 0))
    screen.blit(image2, (260, 0))
    pygame.draw.line(screen, (255, 255, 255), [300, 0], [300, 600], 5)
    player_1 = pygame.draw.rect(screen, (255,255,255), (coordx1, coordy1, larguraj, alturaj))
    rect1 = pygame.Rect(coordx1, coordy1, larguraj, alturaj)
    player_2 = pygame.draw.rect(screen, (255,255,255), (coordx2, coordy2, larguraj, alturaj))
    rect2 = pygame.Rect(coordx2, coordy2, larguraj, alturaj)
    bola = pygame.draw.circle(screen, (255,255,255), (int(bolax), int(bolay)), bolatam)
    rect3 = pygame.Rect((bolax - bolatam), (bolay - bolatam), bolatam, bolatam)
     
    
    #movimentação bola
    bolax += vel_bolax
    bolay += vel_bolay
    
    #movimentação jogadores
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and coordy1 > 0:
        coordy1 -= velocidade_jogador
    elif keys[pygame.K_s] and coordy1 < 520:
        coordy1 += velocidade_jogador


    if keys[pygame.K_UP] and coordy2 > 0:
        coordy2 -= velocidade_jogador
    elif keys[pygame.K_DOWN] and coordy2 < 520:
        coordy2 += velocidade_jogador


    #colisão com a parede
    if bolay <= 0:
        vel_bolay = -vel_bolay
    elif bolay >= 590:
        vel_bolay = -vel_bolay
        

    #colisão com as raquetes
    if player_1.colliderect(bola):
        vel_bolax = abs(vel_bolax) + 0.05
    elif player_2.colliderect(bola):
        vel_bolax = -abs(vel_bolax) - 0.05
    
    #se bola sair de cena
    if bolax <= 0:
        bolax = 300
        bolay = 300
        vel_bolay = -abs(vel_bolax)
        vel_bolax = 1.5

    if bolax >= 600:
        bolax = 300
        bolay = 300
        vel_bolay = vel_bolay
        vel_bolax = -1.5

    
    
    pygame.display.update()
