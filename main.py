import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()
pygame.font.init()
pygame.font.get_fonts()

largura= 640
altura= 480
x= largura / 2
y= altura / 2
x1= randint(10, 630)
y1= randint(10, 470)
contador= 0
fonte= pygame.font.SysFont('inkfree', 30, True, False)
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo sem nome ainda')
relogio = pygame.time.Clock()

while True:
        relogio.tick(120) #framerate
        tela.fill((0,0,0)) #tela preta para nao registrar rastros dos objetos
        mensagem = f'Pontos= {contador}'
        texto_formato= fonte.render(mensagem, True, (255,255,255))
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
                x=x -3
        if pygame.key.get_pressed()[K_d]:
                x=x +3
        if pygame.key.get_pressed()[K_w]:
                y=y -3
        if pygame.key.get_pressed()[K_s]:
                y=y +3

        blueCircle= pygame.draw.circle(tela, (0,0,255), (x, y), 20)#parametros(local de exibição=tela , (r,g,b), (posX, posY), radio)
        ##redRect= pygame.draw.rect(tela, (230,0,0), (x1, y2, 40, 50))
        whiteCircle= pygame.draw.circle(tela, (0,255,0), (x1, y1), 5)
        ## yellowLine= pygame.draw.line(tela, (255,255, 0), (0,250), (640, 250), 5)

        if blueCircle.colliderect(whiteCircle):
                x1= randint(10, 630)
                y1= randint(10, 470)
                contador+= 1
        
        if contador == 25:
                pygame.quit()
        
        tela.blit(texto_formato, (450, 40))                   
        ## pygame.draw.rect(tela, (230,0,0), (300, 195, 40, 50))
        
        pygame.display.update()

