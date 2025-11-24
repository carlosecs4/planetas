#=======INICIALIZAÇÃO==========#

import pygame
import os
import math 
from constantes import *

pygame.init()

pasta_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(pasta_principal, 'animações')

#criando a tela do jogo
window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption("Planet System Simulator")

class Planeta(pygame.sprite.Sprite):
    def __init__(self, massa, raio, posicao, nome):
        #constantes do planeta
        self.massa = massa
        self.raio = raio
        self.volume = (4 / 3) * math.pi * self.raio ** 3
        self.densidade = self.massa / self.volume

        #adicionando animação - perceba que eu tenho apenas uma sprite sheet, o loop percorre essa imagem e pega cada uma imagem...
        #a partir do seu tamanho e posição com pixels.
        pygame.sprite.Sprite.__init__(self)
        self.sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, (nome + '.png'))).convert_alpha()

        #perceba que as imagens que são pegas no site podem ter larguras e alturas diferentes, por isso precisamos usar elas de
        #acordo com cada sprite sheet.
        largura_spritesheet = self.sprite_sheet.get_width()
        altura_spritesheet = self.sprite_sheet.get_height()
        self.lista_imagens = []
        for i in range(50):
            img = self.sprite_sheet.subsurface((altura_spritesheet * i, 0), (altura_spritesheet, altura_spritesheet))
            
            #aumenta a imagem
            img = pygame.transform.scale(img, (altura_spritesheet * 5, altura_spritesheet * 5))
            self.lista_imagens.append(img)
            
        self.index_lista = 0
        self.image = self.lista_imagens[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (posicao[0], posicao[1])

    def update(self):
        self.image = self.lista_imagens[int(self.index_lista)]
        self.index_lista += 0.25
        if self.index_lista == 49:
            self.index_lista = 0

    #def move():
        #precisamos considerar a interação de cada corpo com outro

terra = Planeta(1000, 30, (320, 360), 'Terra')
sol = Planeta(2000, 100, (960, 360), 'Sol')

pygame.sprite.Group.add

clock = pygame.time.Clock()
FPS = 30

#loop principal
game = True

while game:
    clock.tick(FPS)

    #verifica se o jogador apertou para fechar o jogo, se sim, o jogo fecha.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    #pinta o fundo com uma cor que sugere o universo
    window.fill((10, 10, 35))

    terra.update()
    sol.update()

    window.blit(terra.image, terra.rect)
    window.blit(sol.image, sol.rect)

    pygame.display.update()

pygame.quit()