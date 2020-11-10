def pingpong():
    import pygame
    from pygame import mixer
    #Inizializzo pygame e pygame/mixer
    pygame.init() 
    mixer.init()
    #creo lo schermo e il clock
    x_pingpong=480
    y_pingpong=720
    pingpong = pygame.display.set_mode((x_pingpong, y_pingpong))
    pygame.display.set_caption('pingpong')
    clock = pygame.time.Clock()
    FPS = 60 
    #Imposto la musica di sottofondo
    mixer.music.load(r'Song\song pingpong.mp3') 
    mixer.music.set_volume(0.7) 
    mixer.music.play(-1) 
    #Imposto i colori
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


    punti=0

    #Creo le cordinate degli item
    x=208
    y=670
    x_ball = 100
    x_increase = 5
    y_ball = 100
    y_increase = 5


    a=True
    b=True
    c=True


    while a:
        #Imposto le funzioni dei tasti della tastiera
        if pygame.event.get(pygame.QUIT):
            a=False
            b=False
            c=False
            pygame.mixer.music.pause()

        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
            a=False
            b=False
            c=False
            pygame.mixer.music.pause()

        if keys[pygame.K_SPACE]: 
            break
        #Creo il rettangolo
        rect = pygame.Rect((x, y), (64, 15))
        image = pygame.image.load('Image\wood.jpg')
        image= pygame.transform.scale(image, (64,15)) 
        #Creo tutte le scritte
        font_inizio = pygame.font.Font('freesansbold.ttf', 80) 
        inizio = font_inizio.render("Ping Pong!!!", True, RED)
        inizio_textrect = inizio.get_rect()

        font_istruzioni = pygame.font.Font('freesansbold.ttf', 20) 
        istruzioni = font_istruzioni.render("\nPer iniziare premi la barra spaziatrice ", True, RED)
        istruzioni_textrect2 = istruzioni.get_rect()

        font_istruzioni2 = pygame.font.Font('freesansbold.ttf', 20) 
        istruzioni2 = font_istruzioni2.render("\nPer muoverti usa le freccette Dx Sx ", True, RED)
        istruzioni_textrect2 = istruzioni2.get_rect()

        font_exit_ = pygame.font.Font('freesansbold.ttf', 20) 
        exit_= font_exit_.render("\nPremi esc per uscire", True, RED)
        exit_textrect = exit_.get_rect()

        
        #Creo lo sfondo
        sfondo=pygame.image.load(r'Image\sky.png')
        sfondo=pygame.transform.scale(sfondo, (x_pingpong, y_pingpong))
        sfondo_surface=pygame.Rect((0, 0), (x_pingpong, y_pingpong))
        #Creo la palla
        circle=pygame.draw.circle(pingpong, BLACK, (x_ball,y_ball), 15)
        ball=pygame.image.load(r'Image\ball.png')
        ball=pygame.transform.scale(ball, (30,30)) 
        #Carico il tutto
        pingpong.blit(sfondo, sfondo_surface) 
        pingpong.blit(image, rect)
        pingpong.blit(ball, circle)
        pingpong.blit(inizio, (20, 200))
        pingpong.blit(istruzioni, (20, 300))
        pingpong.blit(istruzioni2, (20, 330))
        pingpong.blit(exit_, (20, 360))

        pygame.display.update()




    while b:
        clock.tick(FPS)

        if pygame.event.get(pygame.QUIT):
            a=False
            b=False
            c=False
            pygame.mixer.music.pause()
        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
            a=False
            b=False
            c=False
            pygame.mixer.music.pause()



        rect = pygame.Rect((x, y), (64, 15))
        image = pygame.image.load(r'Image\wood.jpg')
        image= pygame.transform.scale(image, (64,15)) 

        #Scritta punteggio
        punti2="Punteggio: {}".format(punti)
        font_punteggio = pygame.font.Font('freesansbold.ttf', 26) 
        punteggio = font_punteggio.render(punti2, True, GREEN)
        Punteggio_textrect = punteggio.get_rect()


        #Movimenti piattaforma

        if keys[pygame.K_LEFT]: 
            if x>=2:
                x-=5
        if keys[pygame.K_RIGHT]:
            if x<=416:
                x+=5


        


        #Movimenti palla e collisioni
        x_ball += x_increase
        if x_ball >= (x_pingpong-10) or x_ball <= 10:
            x_increase *= -1
        y_ball += y_increase
        if y_ball <= 10:
            y_increase *= -1


        if y_ball+10==y:
            if x_ball >=x and x_ball<=x+64:
                y_increase *= -1
                punti+=1

        if x_ball+10<=x+10 and x_ball+10>=x-10:
            if y_ball+10>=y and y_ball-10<=y:
                y_increase *= -1
                x_increase *= -1
                punti+=1

        if x_ball-74<=x+10 and x_ball-74>=x-10:
            if y_ball+10>=y and y_ball-10<=y:
                y_increase *= -1
                x_increase *= -1
                punti+=1

        sfondo=pygame.image.load(r'Image\sky.png')
        sfondo=pygame.transform.scale(sfondo, (x_pingpong, y_pingpong))
        sfondo_surface=pygame.Rect((0, 0), (x_pingpong, y_pingpong))
        circle=pygame.draw.circle(pingpong, BLACK, (x_ball,y_ball), 15)
        ball=pygame.image.load(r'Image\ball.png')
        ball=pygame.transform.scale(ball, (30,30)) 
        pingpong.blit(sfondo, sfondo_surface)
        pingpong.blit(punteggio, Punteggio_textrect) 
        pingpong.blit(image, rect)
        pingpong.blit(ball, circle)
        
        #ciclo while quando il player perde
        if y_ball>=y_pingpong-5:
            x_ball=100
            y_ball=100
            x=208
            y=670
            punti=0
            while c:
                if pygame.event.get(pygame.QUIT):
                    a=False
                    b=False
                    c=False
                    pygame.mixer.music.pause()

                keys = pygame.key.get_pressed()
                if keys [pygame.K_ESCAPE]:
                    a=False
                    b=False
                    c=False
                    pygame.mixer.music.pause()

                
                if keys[pygame.K_SPACE]: 
                    break


                #Scritte
                font_gameover = pygame.font.Font('freesansbold.ttf', 80) 
                gameover = font_gameover.render("GAMEOVER!!!", True, RED)
                gameover_textrect = gameover.get_rect()

                font_restart = pygame.font.Font('freesansbold.ttf', 20) 
                restart = font_restart.render("\nPer riprovare premi la barra spaziatrice ", True, RED)
                restart_textrect = inizio.get_rect()

                font_exit_ = pygame.font.Font('freesansbold.ttf', 20) 
                exit_= font_exit_.render("\nPremi esc per uscire", True, RED)
                exit_textrect = exit_.get_rect()

            


                sfondo=pygame.image.load(r'Image\sky.png')
                sfondo=pygame.transform.scale(sfondo, (x_pingpong, y_pingpong))
                sfondo_surface=pygame.Rect((0, 0), (x_pingpong, y_pingpong))
                pingpong.blit(sfondo, sfondo_surface) 
                pingpong.blit(gameover, (5, 200))
                pingpong.blit(restart, (5,300))
                pingpong.blit(exit_, (5, 330))



                pygame.display.update()


        
        

        pygame.display.update()





def pingpongduo():
    import pygame
    from pygame import mixer
    pygame.init() 

    x_pingpong=480
    y_pingpong=720
    pingpong = pygame.display.set_mode((x_pingpong, y_pingpong))
    pygame.display.set_caption('pingpong')
    mixer.music.load(r'Song\song pingpong.mp3') 
    mixer.music.set_volume(0.7) 
    mixer.music.play(-1) 
    clock = pygame.time.Clock()
    FPS = 60  # Frames per second.

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)


    punti=0
    punti1=0





    x_rect=208
    y_rect=670
    x_rect2=208
    y_rect2=50
    x_ball=240
    x_increase = 5
    y_ball=360
    y_increase = 5


    a=True
    b=True
    c=True
    d=True


    while a:
        
        if pygame.event.get(pygame.QUIT):
            a=False
            b=False
            c=False
            d=False
            pygame.mixer.music.pause()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]: 
            break

        if keys [pygame.K_ESCAPE]:
            a=False
            b=False
            c=False
            d=False
            pygame.mixer.music.pause()

        rect = pygame.Rect((x_rect, y_rect), (64, 15))
        image = pygame.image.load(r'Image\wood.jpg')
        image= pygame.transform.scale(image, (64,15)) 

        rect2 = pygame.Rect((x_rect2, y_rect2), (64, 15))
        image2 = pygame.image.load(r'Image\wood.jpg')
        image2= pygame.transform.scale(image, (64,15))

        font_inizio = pygame.font.Font('freesansbold.ttf', 80) 
        inizio = font_inizio.render("Ping Pong!!!", True, RED)
        inizio_textrect = inizio.get_rect()

        font_istruzioni = pygame.font.Font('freesansbold.ttf', 20) 
        istruzioni = font_istruzioni.render("\nPer iniziare premi la barra spaziatrice ", True, RED)
        istruzioni_textrect2 = istruzioni.get_rect()

        font_istruzioni2 = pygame.font.Font('freesansbold.ttf', 20) 
        istruzioni2 = font_istruzioni2.render("\nPer muovere il player1 usa A & D ", True, RED)
        istruzioni_textrect2 = istruzioni2.get_rect()

        font_istruzioni3 = pygame.font.Font('freesansbold.ttf', 20) 
        istruzioni3 = font_istruzioni3.render("\nPer muovere il player2 usa le freccette Dx Sx ", True, RED)
        istruzioni_textrect3 = istruzioni3.get_rect()

        font_exit_ = pygame.font.Font('freesansbold.ttf', 20) 
        exit_= font_exit_.render("\nPremi esc per uscire", True, RED)
        exit_textrect = exit_.get_rect()

        

        sfondo=pygame.image.load(r'Image\sky.png')
        sfondo=pygame.transform.scale(sfondo, (x_pingpong, y_pingpong))
        sfondo_surface=pygame.Rect((0, 0), (x_pingpong, y_pingpong)) 
        pingpong.blit(sfondo, sfondo_surface) 
        pingpong.blit(image, rect)
        pingpong.blit(image2, rect2)
        pingpong.blit(inizio, (20, 200))
        pingpong.blit(istruzioni, (20, 300))
        pingpong.blit(istruzioni2, (20, 330))
        pingpong.blit(istruzioni3, (20, 360))
        pingpong.blit(exit_, (20, 390))

        pygame.display.update()




    while b:
        punti2="{}-{}".format(punti, punti1)
        clock.tick(FPS)

        if pygame.event.get(pygame.QUIT):
            for event in pygame.event.get():
                a=False
                b=False
                c=False
                d=False
                pygame.mixer.music.pause()



        rect = pygame.Rect((x_rect, y_rect), (65, 15))
        image = pygame.image.load(r'Image\wood.jpg')
        image= pygame.transform.scale(image, (65,15)) 


        rect2 = pygame.Rect((x_rect2, y_rect2), (65, 15))
        image2 = pygame.image.load(r'Image\wood.jpg')
        image2= pygame.transform.scale(image, (65,15))

        x_ball += x_increase
        if x_ball >= (x_pingpong-10) or x_ball <= 10:
            x_increase *= -1


        y_ball += y_increase

        if y_ball+10==y_rect:
            if x_ball >=x_rect and x_ball<=x_rect+64:
                y_increase *= -1

        if x_rect<=x_ball+10 and x_rect+65>=x_ball-10:
            if y_rect+1<=y_ball+10 and y_rect+14>=y_ball-10:
                x_increase*=-1
                y_increase*=-1

    
        if y_ball-10==y_rect2+15:
            if x_ball >=x_rect2 and x_ball<=x_rect2+64:
                y_increase *= -1

        if x_rect2<=x_ball+10 and x_rect2+65>=x_ball-10:
            if y_rect2+14>=y_ball-10 and y_rect2+1<=y_ball+10:
                x_increase*=-1
                y_increase*=-1



        font_punteggio = pygame.font.Font('freesansbold.ttf', 70) 
        punteggio = font_punteggio.render(punti2, True, GREEN)
        Punteggio_textrect = punteggio.get_rect()



        keys = pygame.key.get_pressed()
        if keys [pygame.K_ESCAPE]:
            a=False
            b=False
            c=False
            d=False
            pygame.mixer.music.pause()

        if keys[pygame.K_LEFT]: 
            if x_rect>=2:
                x_rect-=7
        if keys[pygame.K_RIGHT]:
            if x_rect<=416:
                x_rect+=7

        if keys[pygame.K_a]: 
            if x_rect2>=2:
                x_rect2-=7
        if keys[pygame.K_d]:
            if x_rect2<=416:
                x_rect2+=7

            

        sfondo=pygame.image.load(r'Image\sky.png')
        sfondo=pygame.transform.scale(sfondo, (x_pingpong, y_pingpong))
        sfondo_surface=pygame.Rect((0, 0), (x_pingpong, y_pingpong))
        circle=pygame.draw.circle(pingpong, BLACK, (x_ball,y_ball), 15)
        ball=pygame.image.load(r'Image\ball.png')
        ball=pygame.transform.scale(ball, (30,30)) 
        pingpong.blit(sfondo, sfondo_surface)
        pingpong.blit(punteggio, (200, 290)) 
        pingpong.blit(image, rect)
        pingpong.blit(image2, rect2)
        pingpong.blit(ball, circle)

        if y_ball>=y_pingpong-5 or y_ball<=5:
            if y_ball>=y_pingpong-5:
                punti+=1
            if y_ball<=5:
                punti1+=1
            x_ball=240
            y_ball=360
            x_rect=208
            y_rect=670
            x_rect2=208
            y_rect2=50
            y_increase*=-1
            while c:
                if punti==3 or punti1==3:
                    while d:
                        if pygame.event.get(pygame.QUIT):
                            a=False
                            b=False
                            c=False
                            d=False
                            pygame.mixer.music.pause()
                        keys = pygame.key.get_pressed()
                        if keys[pygame.K_SPACE]:
                            punti=0
                            punti1=0 
                            break

                        if keys [pygame.K_ESCAPE]:
                            a=False
                            b=False
                            c=False
                            d=False
                            pygame.mixer.music.pause()

                        font_istruzioni3 = pygame.font.Font('freesansbold.ttf', 20) 
                        istruzioni3 = font_istruzioni3.render("\nPer riiniziare premi la barra spaziatrice ", True, RED)
                        istruzioni3_textrect = istruzioni3.get_rect()

                        font_exit_ = pygame.font.Font('freesansbold.ttf', 20) 
                        exit_= font_exit_.render("\nPremi esc per uscire", True, RED)
                        exit_textrect = exit_.get_rect()

                        win=pygame.image.load(r'Image\win.jpg')
                        win=pygame.transform.scale(win, (x_pingpong, y_pingpong))
                        win_surface=pygame.Rect((0, 0), (x_pingpong, y_pingpong))
                        pingpong.blit(win, win_surface)
                        pingpong.blit(exit_, (15, 620))
                        pingpong.blit(istruzioni3, (15, 650))
                        if punti==3:
                            font_player1 = pygame.font.Font('freesansbold.ttf', 70) 
                            player1 = font_player1.render("Player 1 wins", True, RED)
                            player1_textrect = player1.get_rect()
                            pingpong.blit(player1, (5, 50))
                        elif punti1==3:
                            font_player2 = pygame.font.Font('freesansbold.ttf', 70) 
                            player2 = font_player2.render("Player 2 wins", True, RED)
                            player2_textrect = player2.get_rect()
                            pingpong.blit(player2, (5, 50))

                        pygame.display.update()

                
                if pygame.event.get(pygame.QUIT):
                    a=False
                    b=False
                    c=False
                    d=False
                    pygame.mixer.music.pause()

                keys = pygame.key.get_pressed()
                if keys [pygame.K_ESCAPE]:
                    a=False
                    b=False
                    c=False
                    d=False
                    pygame.mixer.music.pause()

                if keys[pygame.K_SPACE]: 
                    break


                punti2="{}-{}".format(punti, punti1)
                font_punteggio = pygame.font.Font('freesansbold.ttf', 70) 
                punteggio = font_punteggio.render(punti2, True, GREEN)
                Punteggio_textrect = punteggio.get_rect()

                font_restart = pygame.font.Font('freesansbold.ttf', 20) 
                restart = font_restart.render("\nPer continuare premi la barra spaziatrice", True, RED)
                restart_textrect = restart.get_rect()
            
                font_restart2 = pygame.font.Font('freesansbold.ttf', 20) 
                restart2 = font_restart.render("\nIl primo che arriva a 3 vince ", True, RED)
                restart2_textrect = restart2.get_rect()

                font_exit_ = pygame.font.Font('freesansbold.ttf', 20) 
                exit_= font_exit_.render("\nPremi esc per uscire", True, RED)
                exit_textrect = exit_.get_rect()


                sfondo=pygame.image.load(r'Image\sky.png')
                sfondo=pygame.transform.scale(sfondo, (x_pingpong, y_pingpong))
                sfondo_surface=pygame.Rect((0, 0), (x_pingpong, y_pingpong))
                pingpong.blit(sfondo, sfondo_surface)
                pingpong.blit(punteggio, (200, 200))  
                pingpong.blit(restart, (5,300))
                pingpong.blit(restart2, (5, 330))
                pingpong.blit(exit_, (5,360))



                pygame.display.update()






        


        pygame.display.update()