def snake():
    import pygame
    from pygame import mixer
    import time
    import random

    pygame.init()
    mixer.init()

    #colori
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    #dimensioni schermo
    x_snake = 720
    y_snake = 480
    #creo il display 
    snake = pygame.display.set_mode((x_snake, y_snake))
    pygame.display.set_caption('Snake Game')
    
    clock = pygame.time.Clock()

    #musica
    mixer.music.load(r'Song\snake song.mp3') 
    mixer.music.set_volume(0.3) 
    mixer.music.play(-1)

    #grandezza e velocità serpente
    snake_block = 10
    snake_speed = 10

    #scritte
    font_style = pygame.font.SysFont("freesansbold.ttf", 25)
    score_font = pygame.font.SysFont("freesansbold.ttf", 25)
    
    #punteggio
    def Your_score(score):
        value = score_font.render("Il tuo punteggio: " + str(score), True, yellow)
        snake.blit(value, [0, 0])
    
    
    #creo una classe che fa allungare il serpente  
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(snake, green, [x[0], x[1], snake_block, snake_block])
    
    
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        snake.blit(mesg, [x_snake / 6, y_snake / 3])


    #faccio il game loop con il cibo
    def gameLoop():
        game_over = False
        game_close = False
    
        x1 = x_snake / 2
        y1 = y_snake / 2
    
        x1_change = 0
        y1_change = 0
    
        snake_List = []
        Length_of_snake = 1
    
        foodx = round(random.randrange(0, x_snake - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, y_snake - snake_block) / 10.0) * 10.0
    
        while not game_over:
    
            while game_close == True:
                snake.fill(black)
                message("Hai perso! Premi C per giocare di nuovo oppure Q per uscire", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()
    
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        game_over = True
                        game_close = False
                    if event.type == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.K_ESCAPE:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
    
            if x1 >= x_snake or x1 < 0 or y1 >= y_snake or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            snake.fill(black)
            pygame.draw.rect(snake, blue, [foodx, foody, snake_block, snake_block])
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
            Your_score(Length_of_snake - 1)
    
            pygame.display.update()
    
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, x_snake - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, y_snake - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
    
            clock.tick(snake_speed)
    
        
        game_close=False
        

    gameLoop()
 
 
