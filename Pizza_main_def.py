import pygame
from pygame import mixer
from pizza_def import pizza, pizza_hard
def pizza_main():
    #Inizializzo pygame e pygame/mixer
    pygame.init() 
    mixer.init()
    #creo lo schermo e il clock
    x_pizza_main=300
    y_pizza_main=200

    clock = pygame.time.Clock()
    FPS = 60 
    #Imposto la musica di sottofondo


    def blit_button(pos_x, pos_y, dim_x, dim_y, color):
        button=pygame.Rect(pos_x, pos_y, dim_x, dim_y)
        image=pygame.Surface((dim_x, dim_y))
        image.fill(color)
        pizza_main.blit(image, button) 
        return button 

    def scritta(l_font, text, color, pos_text_x, pos_text_y):
        font = pygame.font.Font('freesansbold.ttf', l_font) 
        text_ = font.render(text, True, color)
        pizza_main.blit(text_, (pos_text_x, pos_text_y))

    def song(song_main):
        mixer.music.load(song_main) 
        mixer.music.set_volume(0.7)
        mixer.music.play(-1) 

    #Imposto i colori
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    a=True

    while a:
        pizza_main = pygame.display.set_mode((x_pizza_main, y_pizza_main))
        pygame.display.set_caption('Minigames')
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                a=False

            keys = pygame.key.get_pressed()
            if keys [pygame.K_ESCAPE]:
                a=False

        
        pizza_main.fill(WHITE)
        pizza_base=blit_button(30, 10, 200, 70, BLACK)
        piz_hard=blit_button(30, 100, 200, 70, BLACK)
        scritta(27, "Pizzeria Base", RED, 30, 30)
        scritta(28, "Pizzeria Hard", RED, 30, 120)

        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  


                if pizza_base.collidepoint(mouse_pos):
                    pizza()
                    song(r'Song/Song Main.mp3')


                if piz_hard.collidepoint(mouse_pos):
                    pizza_hard()
                    song(r'Song/Song Main.mp3')



        pygame.display.update()