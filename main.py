import pygame

from pygame.locals import *
from sys import exit

pygame.init()

largura= 640
altura= 480
x= largura / 2
y= altura / 2

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo sem nome ainda')
relogio = pygame.time.Clock()

while True:
        relogio.tick(120) #framerate
        tela.fill((0,0,0)) #tela preta para nao registrar rastros dos objetos
        for event in pygame.event.get():
                if event.type== QUIT:
                        pygame.quit()
                        exit()
        if y > altura:
                y= 0
        if x > largura:
                x= 0   
        if y < 0:
                y= altura
        if x < 0:
                x= largura
        
        if pygame.key.get_pressed()[K_a]:
                x=x -10
        if pygame.key.get_pressed()[K_d]:
                x=x +10
        if pygame.key.get_pressed()[K_w]:
                y=y -10
        if pygame.key.get_pressed()[K_s]:
                y=y +10
        blueCircle= pygame.draw.circle(tela, (0,0,255), (x, y), 20)  #parametros(local de exibição=tela , (r,g,b), (posX, posY), radio)
        yellowLine= pygame.draw.line(tela, (255,255, 0), (0,250), (640, 250), 5)

        if blueCircle.colliderect(yellowLine):
                print('Colidiu!')
                              
        #pygame.draw.rect(tela, (230,0,0), (300, 195, 40, 50))
        
        pygame.display.update()

