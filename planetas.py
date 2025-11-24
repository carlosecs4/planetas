#=======INICIALIZAÇÃO==========

import pygame

pygame.init()

game = True

ALTURA = 1280
LARGURA = 720

#criando a tela do jogo
window = pygame.display.set_mode((ALTURA, LARGURA))

#loop principal
while game:
    #verifica se o jogador apertou para fechar o jogo, se sim, o jogo fecha.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
    
    #pinta o fundo com uma cor que sugere o universo
    window.fill((10, 10, 35))
    
    pygame.display.update()

pygame.quit()