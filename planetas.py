#=======INICIALIZAÇÃO==========

import pygame
import os

pygame.init()

pasta_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(pasta_principal, 'animações')

#criando a tela do jogo
ALTURA = 1280
LARGURA = 720

window = pygame.display.set_mode((ALTURA, LARGURA))
pygame.display.set_caption("Planet System Simulator")

sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, 'sprite da Terra.png')).convert_alpha()

class Planeta(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.lista_imagens = []
        for i in range(50):
            img = sprite_sheet.subsurface((30 * i, 0), (30, 30))
            img = pygame.transform.scale(img, (30 * 5, 30 * 5))
            self.lista_imagens.append(img)

        self.index_lista = 0
        self.image = self.lista_imagens[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (640, 360)

    def update(self):
        self.image = self.lista_imagens[int(self.index_lista)]
        self.index_lista += 0.25
        if self.index_lista == 49:
            self.index_lista = 0

planeta = Planeta()

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

    planeta.update()

    window.blit(planeta.image, planeta.rect)

    pygame.display.update()

pygame.quit()