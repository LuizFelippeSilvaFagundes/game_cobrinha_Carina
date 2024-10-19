import pygame
import time
import random

# Inicializa o Pygame
pygame.init()

# Definições de cores
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Configurações da tela
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Jogo da Cobrinha')  # Corrigido aqui

# Configurações da cobrinha
snake_block = 10
snake_speed = 15

# Fonte
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

# Função para mostrar a pontuação
def Your_score(score):
    value = score_font.render("Sua Pontuação: " + str(score), True, yellow)
    screen.blit(value, [0, 0])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

# Função de pausa
def pause_game():
    paused = True
    message("Jogo pausado. Pressione P para continuar", yellow)
    pygame.display.update()

    while paused:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:  # Despausar o jogo ao pressionar 'P'
                    paused = False
        time.sleep(0.1)  # Evita o uso excessivo de CPU enquanto o jogo está pausado

def gameLoop():
    game_over = False
    game_close = False

    x1 = width / 2
    y1 = height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    # Pontuação inicial
    score = 0

    # Criação das duas comidas
    foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    food2x = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
    food2y = round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close == True:
            screen.fill(blue)
            message("Perdeu! Pressione C para jogar novamente ou Q para sair", red)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:  # Movimento horizontal apenas se estiver se movendo verticalmente
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:  # Movimento horizontal apenas se estiver se movendo verticalmente
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:  # Movimento vertical apenas se estiver se movendo horizontalmente
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:  # Movimento vertical apenas se estiver se movendo horizontalmente
                    y1_change = snake_block
                    x1_change = 0
                elif event.key == pygame.K_p:  # Pausar o jogo ao pressionar 'P'
                    pause_game()

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        screen.fill(blue)
        
        # Desenhando as duas comidas
        pygame.draw.rect(screen, green, [foodx, foody, snake_block, snake_block])
        pygame.draw.rect(screen, red, [food2x, food2y, snake_block, snake_block])  # segunda comida

        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(score)  # Mostrar a pontuação na tela
        pygame.display.update()

        # Verifica se a cobra comeu a primeira comida (verde)
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
            score += 10  # Aumenta a pontuação

        # Verifica se a cobra comeu a segunda comida (vermelha) - game over
        if x1 == food2x and y1 == food2y:
            game_close = True  # Aciona o game over ao comer a comida vermelha

        pygame.time.Clock().tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
