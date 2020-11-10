import pygame
from pygame import mixer
from Pizza_main_def import pizza_main
from Snake_def import snake
from pingpong_main_def import pingpong_main
from blackjack_def import blackjack_main

#Imposto i colori
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#Inizializzo pygame 
pygame.init() 
mixer.init()
#creo lo schermo e il clock
x_main=480
y_main=533

clock = pygame.time.Clock()
FPS = 60 

def song(song_main):
    mixer.music.load(song_main) 
    mixer.music.set_volume(0.7)
    mixer.music.play(-1) 

def blit_button(pos_x, pos_y, dim_x, dim_y, color,image_def):
    button=pygame.Rect(pos_x, pos_y, dim_x, dim_y)
    image = pygame.image.load(image_def)
    image= pygame.transform.scale(image, (dim_x,dim_y)) 
    main.blit(image, button)
    return button 

song(r'Song/Song Main.mp3')

while True:
    main = pygame.display.set_mode((x_main, y_main))
    main.fill(WHITE)

    pingpong_solo=blit_button(0, 0, 230, 278, RED, (r'Image\pingpong_image.png'))
    piz_base=blit_button(230, 0, 250, 145, RED, (r'Image\pizza.png'))
    snake_button=blit_button(-1, 270, 481, 263, RED, (r'Image\snake_main.jpg'))
    blackjack_button=blit_button(230, 146, 257, 125, RED, (r'Image\blackjack\blackjack main.jpg'))


    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos  


            if pingpong_solo.collidepoint(mouse_pos):
                pingpong_main()

            if piz_base.collidepoint(mouse_pos):
                pizza_main()

            if snake_button.collidepoint(mouse_pos):
                snake()
                song(r'Song\Song Main.mp3')

            if blackjack_button.collidepoint(mouse_pos):
                blackjack_main()
                song(r'Song\Song Main.mp3')

    pygame.display.set_caption('Minigames')

    pygame.display.update()