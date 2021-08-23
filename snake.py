import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

# parametros para tamanho da tela
largura = 600
altura = 600

# variaveis para snake
x_snake = 300
y_snake = 300

x_controle = 20
y_controle = 0
velocidade = 8

lista_cobra = []
comprimento_inicial = 5

# variaveis para apple
apple_x = randint(20, 560)
apple_y = randint(20, 560)

# variaveis para o jogo
screen = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()

morreu = False
play = False
pause = False

# variaveis de texto
comicsans_Bold = pygame.font.SysFont('comicsans', 30, True, False)
comicsans_Normal = pygame.font.SysFont('comicsans', 30, False, False)
pontos = 0

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(screen, (0, 255, 0), (XeY[0], XeY[1], 20, 20))


def restart():
    global pontos, comprimento_inicial, x_snake, y_snake, lista_cobra, lista_cabeca, apple_x, apple_y, morreu, play
    pontos = 0
    comprimento_inicial = 5
    x_snake = 300
    y_snake = 300
    lista_cobra = []
    lista_cabeca = []
    apple_x = randint(20, 560)
    apple_y = randint(20, 560)
    morreu = False


while not play:
    screen.fill((119,136,153))
    mensagem = 'Pressione [ENTER] para jogar'
    gameMenu = comicsans_Bold.render(mensagem, True, (0, 0, 0))
    ret_gameMenu = gameMenu.get_rect()
    ret_gameMenu.center = (largura // 2, altura // 2)
    screen.blit(gameMenu, ret_gameMenu)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                play = True

    pygame.display.update()


while play:
    clock.tick(20)
    screen.fill((25, 25, 112))
    mensagem = f'Pontos {pontos}'
    pontuacao = comicsans_Bold.render(mensagem, True, (0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pause = True

            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == -velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    y_controle = -velocidade
                    x_controle = 0
            if event.key == K_s:
                if y_controle == -velocidade:
                    pass
                else:
                    y_controle = velocidade
                    x_controle = 0
    while pause:
        screen.fill((205, 133, 63))

        mensagem = 'JOGO PAUSADO! Presione [ESC] para continuar'
        gamePause = comicsans_Normal.render(mensagem, True, (0, 0, 0))
        ret_gamePause = gamePause.get_rect()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = False
                    play = True

        ret_gamePause.center = (largura // 2, altura // 2)
        screen.blit(gamePause, ret_gamePause)
        pygame.display.update()


    x_snake = x_snake + x_controle
    y_snake = y_snake + y_controle

    wall_L = pygame.draw.rect(screen, (139, 69, 19), (0, 0, 20, altura))
    wall_R = pygame.draw.rect(screen, (139, 69, 19), (largura - 20, 0, 20, altura))
    wall_U = pygame.draw.rect(screen, (139, 69, 19), (0, altura - 20, largura, 20))
    wall_D = pygame.draw.rect(screen, (139, 69, 19), (0, 0, largura, 20))

    snake = pygame.draw.rect(screen, (0, 255, 0), (x_snake, y_snake, 20, 20))
    apple = pygame. draw.rect(screen, (255, 0, 0), (apple_x, apple_y, 20, 20))

    if snake.colliderect(wall_L):
        morreu = True

    if snake.colliderect(wall_R):
        morreu = True

    if snake.colliderect(wall_U):
        morreu = True

    if snake.colliderect(wall_D):
        morreu = True

    if snake.colliderect(apple):
        apple_x = randint(20, 560)
        apple_y = randint(20, 560)
        pontos += 1
        comprimento_inicial += 1

    lista_cabeca = []
    lista_cabeca.append(x_snake)
    lista_cabeca.append(y_snake)

    lista_cobra.append(lista_cabeca)

    if lista_cobra.count(lista_cabeca) > 1:
        morreu = True

    while morreu:
        screen.fill((255, 69, 0))
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    restart()

        mensagem = 'GAME OVER! Presione [R] para jogar novamente'
        mensagem2 = f'sua pontuação foi {pontos}'
        gameOver = comicsans_Normal.render(mensagem, True, (0, 0, 0))
        mensagem2 = comicsans_Normal.render(mensagem2, True, (0, 0, 0))
        ret_gameOver = gameOver.get_rect()
        ret_mensagem2 = mensagem2.get_rect()

        ret_mensagem2.center = (largura // 2, (altura // 2) + 50)
        ret_gameOver.center = (largura // 2, altura // 2)
        screen.blit(mensagem2, ret_mensagem2)
        screen.blit(gameOver, ret_gameOver)
        pygame.display.update()

    if len(lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    screen.blit(pontuacao, (450, 30))
    pygame.display.update()
