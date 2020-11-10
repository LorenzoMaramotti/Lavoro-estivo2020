def pizza():
    import pygame
    from pygame import mixer
    from random import randint
    #Inizializzo pygame e pygame/mixer
    pygame.init()
    mixer.init()
    #creo lo schermo e il clock,
    larghezza_schermo=1080
    lunghezza_schermo=720
    pizzeria = pygame.display.set_mode((larghezza_schermo, lunghezza_schermo))
    pygame.display.set_caption('pizzeria')
    clock = pygame.time.Clock()
    FPS = 60 
    #Imposto la musica di sottofondo
    mixer.music.load(r'Song\pizzeria song.mp3') 
    mixer.music.set_volume(0.1) 
    mixer.music.play(-1) 
    #Imposto i colori
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    punteggio = 0
    vite = 3
    x_impasto = 458
    y_impasto = 570
    y_oggetto_increase = 15
    x_oggetto = randint (0,920)
    y_oggetto = 1

    ingrediente = randint (1,4)
    if ingrediente == 1:
        pmb = (r'image\mozzarella.png')
    elif ingrediente == 2:
        pmb = (r'image\pomodoro.png')
    elif ingrediente == 3:
        pmb = (r'image\basilico.png')
    elif ingrediente == 4:
        pmb = (r'image\petardo.png')

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
        
        #creo l'impasto
        ellipse_rect = pygame.Rect (x_impasto, y_impasto, 164, 60)
        ellipse = pygame.draw.ellipse (pizzeria, BLACK, ellipse_rect)
        image = pygame.image.load(r'image\pizza.png')
        image= pygame.transform.scale(image, (164,60))


        
        #Creo tutte le scritte
        font_inizio = pygame.font.Font('freesansbold.ttf', 80) 
        inizio = font_inizio.render("Pizzeria!", True, GREEN)

        font_istruzioni = pygame.font.Font('freesansbold.ttf', 20) 
        istruzioni = font_istruzioni.render("Per iniziare premi la barra spaziatrice ", True, GREEN)


        font_istruzioni2 = pygame.font.Font('freesansbold.ttf', 20) 
        istruzioni2 = font_istruzioni2.render("Per muoverti usa le freccette Dx Sx ", True, GREEN)

        font_istruzioni3 = pygame.font.Font ('freesansbold.ttf', 20)
        istruzioni3 = font_istruzioni3.render ("Raccogli gli ingredienti ed evita le bombe", True, GREEN)


        font_exit_ = pygame.font.Font('freesansbold.ttf', 20) 
        exit_= font_exit_.render("Premi esc per uscire", True, GREEN)


        #Creo lo sfondo
        sfondo=pygame.image.load(r'image\sfondo.jpg')
        sfondo=pygame.transform.scale(sfondo, (larghezza_schermo, lunghezza_schermo))
        sfondo_surface=pygame.Rect((0, 0), (larghezza_schermo, lunghezza_schermo))
        

        #Carico il tutto
        pizzeria.blit(sfondo, sfondo_surface)
        pizzeria.blit(image, ellipse)
        pizzeria.blit(inizio, (20, 200))
        pizzeria.blit(istruzioni, (20, 300))
        pizzeria.blit(istruzioni2, (20, 330))
        pizzeria.blit(istruzioni3, (20, 360))
        pizzeria.blit(exit_, (20, 390))

        pygame.display.update()

        
    while b:
        if ingrediente == 1:
            pmb = (r'image\mozzarella.png')
        elif ingrediente == 2:
            pmb = (r'image\pomodoro.png')
        elif ingrediente == 3:
            pmb = (r'image\basilico.png')
        elif ingrediente == 4:
            pmb = (r'image\petardo.png')

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
        
        ellipse_rect = pygame.Rect (x_impasto, y_impasto, 164, 60)
        ellipse = pygame.draw.ellipse (pizzeria, BLACK, ellipse_rect)
        image = pygame.image.load(r'image\pizza.png')
        image= pygame.transform.scale(image, (164,60))
        

        rect = pygame.Rect ((x_oggetto, y_oggetto), (160, 160))
        oggetto_image = pygame.image.load (pmb)
        oggetto_image = pygame.transform.scale (oggetto_image, (165, 165))

        y_oggetto += y_oggetto_increase

        if y_oggetto + 150 >= y_impasto and y_oggetto <= y_impasto + 60:
            if x_oggetto + 150 >= x_impasto and x_oggetto <= x_impasto+164:
                if ingrediente == 4:
                    vite -= 1
                elif ingrediente == 1 or ingrediente == 2 or ingrediente == 3:
                    punteggio += 1
                y_oggetto = 1
                x_oggetto = randint (0,920)
                ingrediente = randint (1,4)
                




        #Scritta punteggio
        punti2="Punteggio: {}".format(punteggio)
        font_punteggio = pygame.font.Font('freesansbold.ttf', 26) 
        punti = font_punteggio.render(punti2, True, GREEN)
        
        #Scritta vite
        vite2 = "Vite: {}".format (vite)
        font_vite = pygame.font.Font ('freesansbold.ttf', 26)
        lifs = font_vite.render(vite2, True, GREEN)

        
        #Movimenti piattaforma
        if keys[pygame.K_LEFT]: 
            if x_impasto>=2:
                x_impasto-=20
        if keys[pygame.K_RIGHT]:
            if x_impasto<=916:
                x_impasto+=20

        sfondo=pygame.image.load(r'image\sfondo1.jpg')
        sfondo=pygame.transform.scale(sfondo, (larghezza_schermo, lunghezza_schermo))
        sfondo_surface=pygame.Rect((0, 0), (larghezza_schermo, lunghezza_schermo))
        pizzeria.blit(sfondo, sfondo_surface)
        pizzeria.blit(punti, (0,0)) 
        pizzeria.blit(lifs, (1001,0))
        pizzeria.blit(image, ellipse)
        pizzeria.blit(oggetto_image, rect)

        #errore
        if y_oggetto >= lunghezza_schermo - 160:
            if ingrediente == 4 or ingrediente == 5:
                y_oggetto = 1
                ingrediente = randint (1,4)
                x_oggetto = randint (0,920)
            else:
                vite -= 1
                y_oggetto = 1
                ingrediente = randint (1,4)
                x_oggetto = randint (0,920)
        
        if vite == 0:
            while c:
                if pygame.event.get(pygame.QUIT):
                    a=False
                    b=False
                    c=False
                    pygame.mixer.music.pause()

                keys = pygame.key.get_pressed ()

                if keys [pygame.K_ESCAPE]:
                    a=False
                    b=False
                    c=False
                    pygame.mixer.music.pause()

                
                if keys[pygame.K_SPACE]:
                    vite = 3
                    punteggio = 0
                    x_impasto = 458
                    x_oggetto = randint (0,920)
                    ingrediente = randint (1,4)
                    if ingrediente == 1:
                        pmb = (r'image\mozzarella.png')
                    elif ingrediente == 2:
                        pmb = (r'image\pomodoro.png')
                    elif ingrediente == 3:
                        pmb = (r'image\basilico.png')
                    elif ingrediente == 4:
                        pmb = (r'image\petardo.png')
                    
                    break

                font_gameover = pygame.font.Font('freesansbold.ttf', 80) 
                gameover = font_gameover.render("GAMEOVER!!!", True, GREEN)

                font_restart = pygame.font.Font('freesansbold.ttf', 20) 
                restart = font_restart.render("Per riprovare premi la barra spaziatrice ", True, GREEN)

                font_exit_ = pygame.font.Font('freesansbold.ttf', 20) 
                exit_= font_exit_.render("Premi esc per uscire", True, GREEN)

                sfondo=pygame.image.load(r'image\sfondo.jpg')
                sfondo=pygame.transform.scale(sfondo, (larghezza_schermo, lunghezza_schermo))
                sfondo_surface=pygame.Rect((0, 0), (larghezza_schermo, lunghezza_schermo))
                pizzeria.blit(sfondo, sfondo_surface) 
                pizzeria.blit(gameover, (5, 200))
                pizzeria.blit(restart, (5,300))
                pizzeria.blit(exit_, (5, 330))

                pygame.display.update ()


        pygame.display.update()


def pizza_hard():
    import pygame
    from pygame import mixer
    from random import randint
    #Inizializzo pygame e pygame/mixer
    pygame.init()
    mixer.init()
    #creo lo schermo e il clock,
    larghezza_schermo=1080
    lunghezza_schermo=720
    pizzeria = pygame.display.set_mode((larghezza_schermo, lunghezza_schermo))
    pygame.display.set_caption('pizzeria')
    clock = pygame.time.Clock()
    FPS = 60 
    #Imposto la musica di sottofondo
    mixer.music.load(r'Song\pizzeria song.mp3') 
    mixer.music.set_volume(0.1) 
    mixer.music.play(-1) 
    #Imposto i colori
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    punteggio = 0
    vite = 3
    x_impasto = 458
    y_impasto = 570
    y_oggetto_increase = 15
    x_impasto_increase=20
    x_oggetto = randint (0,920)
    y_oggetto = 1

    ingrediente = randint (1,4)
    if ingrediente == 1:
        pmb = (r'image\mozzarella.png')
    elif ingrediente == 2:
        pmb = (r'image\pomodoro.png')
    elif ingrediente == 3:
        pmb = (r'image\basilico.png')
    elif ingrediente == 4:
        pmb = (r'image\petardo.png')

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
        
        #creo l'impasto
        ellipse_rect = pygame.Rect (x_impasto, y_impasto, 164, 60)
        ellipse = pygame.draw.ellipse (pizzeria, BLACK, ellipse_rect)
        image = pygame.image.load(r'image\pizza.png')
        image= pygame.transform.scale(image, (164,60))


        
        #Creo tutte le scritte
        font_inizio = pygame.font.Font('freesansbold.ttf', 80) 
        inizio = font_inizio.render("Pizzeria!", True, GREEN)
        inizio_textrect = inizio.get_rect()
    
        font_istruzioni = pygame.font.Font('freesansbold.ttf', 20) 
        istruzioni = font_istruzioni.render("Per iniziare premi la barra spaziatrice ", True, GREEN)

        font_istruzioni2 = pygame.font.Font('freesansbold.ttf', 20) 
        istruzioni2 = font_istruzioni2.render("Per muoverti usa le freccette Dx Sx ", True, GREEN)

        font_istruzioni3 = pygame.font.Font ('freesansbold.ttf', 20)
        istruzioni3 = font_istruzioni3.render ("Raccogli gli ingredienti ed evita le bombe", True, GREEN)

        font_istruzioni4 = pygame.font.Font ('freesansbold.ttf', 20)
        istruzioni4 = font_istruzioni4.render ("Ogni 5 punti la velocità aumenterà", True, GREEN)

        font_exit_ = pygame.font.Font('freesansbold.ttf', 20) 
        exit_= font_exit_.render("Premi esc per uscire", True, GREEN)

        #Creo lo sfondo
        sfondo=pygame.image.load(r'image\sfondo.jpg')
        sfondo=pygame.transform.scale(sfondo, (larghezza_schermo, lunghezza_schermo))
        sfondo_surface=pygame.Rect((0, 0), (larghezza_schermo, lunghezza_schermo))

        #randomizzo l'ingrediente
        ingrediente = randint (1,4)
        

        #Carico il tutto
        pizzeria.blit(sfondo, sfondo_surface)
        pizzeria.blit(image, ellipse)
        pizzeria.blit(inizio, (20, 200))
        pizzeria.blit(istruzioni, (20, 300))
        pizzeria.blit(istruzioni2, (20, 330))
        pizzeria.blit(istruzioni3, (20, 360))
        pizzeria.blit(istruzioni4, (20, 390))
        pizzeria.blit(exit_, (20, 420))

        pygame.display.update()

        
    while b:
        if ingrediente == 1:
            pmb = (r'image\mozzarella.png')
        elif ingrediente == 2:
            pmb = (r'image\pomodoro.png')
        elif ingrediente == 3:
            pmb = (r'image\basilico.png')
        elif ingrediente == 4:
            pmb = (r'image\petardo.png')


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
        
        ellipse_rect = pygame.Rect (x_impasto, y_impasto, 164, 60)
        ellipse = pygame.draw.ellipse (pizzeria, BLACK, ellipse_rect)
        image = pygame.image.load(r'image\pizza.png')
        image= pygame.transform.scale(image, (164,60))
        

        rect = pygame.Rect ((x_oggetto, y_oggetto), (160, 160))
        oggetto_image = pygame.image.load (pmb)
        oggetto_image = pygame.transform.scale (oggetto_image, (165, 165))

        y_oggetto += y_oggetto_increase

        if y_oggetto + 150 >= y_impasto and y_oggetto <= y_impasto + 60:
            if x_oggetto + 150 >= x_impasto and x_oggetto <= x_impasto+164:
                if ingrediente == 4:
                    vite -= 1
                elif ingrediente == 1 or ingrediente == 2 or ingrediente == 3:
                    punteggio += 1
                    if punteggio%5 == 0:
                        y_oggetto_increase+=5
                        x_impasto_increase+=4

                y_oggetto = 1
                x_oggetto = randint (0,920)
                ingrediente = randint (1,4)

                

    


        #Scritta punteggio
        punti2="Punteggio: {}".format(punteggio)
        font_punteggio = pygame.font.Font('freesansbold.ttf', 26) 
        punti = font_punteggio.render(punti2, True, GREEN)
        Punteggio_textrect = punti.get_rect()
        
        #Scritta vite
        vite2 = "Vite: {}".format (vite)
        font_vite = pygame.font.Font ('freesansbold.ttf', 26)
        lifs = font_vite.render(vite2, True, GREEN)
        
        #Movimenti piattaforma

        if keys[pygame.K_LEFT]: 
            if x_impasto>=2:
                x_impasto-=x_impasto_increase
        if keys[pygame.K_RIGHT]:
            if x_impasto<=916:
                x_impasto+=x_impasto_increase

        sfondo=pygame.image.load(r'image\sfondo1.jpg')
        sfondo=pygame.transform.scale(sfondo, (larghezza_schermo, lunghezza_schermo))
        sfondo_surface=pygame.Rect((0, 0), (larghezza_schermo, lunghezza_schermo))
        pizzeria.blit(sfondo, sfondo_surface)
        pizzeria.blit(punti, Punteggio_textrect) 
        pizzeria.blit(lifs, (1001,0))
        pizzeria.blit(image, ellipse)
        pizzeria.blit(oggetto_image, rect)


        #errore
        if y_oggetto >= lunghezza_schermo - 160:
            if ingrediente == 4 or ingrediente == 5:
                y_oggetto = 1
                ingrediente = randint (1,4)
                x_oggetto = randint (0,920)
            else:
                vite -= 1
                y_oggetto = 1
                ingrediente = randint (1,4)
                x_oggetto = randint (0,920)
        
        if vite == 0:
            while c:
                if pygame.event.get(pygame.QUIT):
                    a=False
                    b=False
                    c=False
                    pygame.mixer.music.pause()         

                keys = pygame.key.get_pressed ()

                if keys [pygame.K_ESCAPE]:
                    a=False
                    b=False
                    c=False
                    pygame.mixer.music.pause()

                
                if keys[pygame.K_SPACE]:
                    vite = 3
                    punteggio = 0
                    x_impasto_increase=15
                    y_oggetto_increase=10
                    x_impasto=458
                    x_oggetto = randint (0,920)
                    ingrediente = randint (1,4)
                    if ingrediente == 1:
                        pmb = (r'image\mozzarella.png')
                    elif ingrediente == 2:
                        pmb = (r'image\pomodoro.png')
                    elif ingrediente == 3:
                        pmb = (r'image\basilico.png')
                    elif ingrediente == 4:
                        pmb = (r'image\petardo.png')

                    break

                font_gameover = pygame.font.Font('freesansbold.ttf', 80) 
                gameover = font_gameover.render("GAMEOVER!!!", True, GREEN)

                font_restart = pygame.font.Font('freesansbold.ttf', 20) 
                restart = font_restart.render("Per riprovare premi la barra spaziatrice ", True, GREEN)

                font_exit_ = pygame.font.Font('freesansbold.ttf', 20) 
                exit_= font_exit_.render("Premi esc per uscire", True, GREEN)

                sfondo=pygame.image.load(r'image\sfondo.jpg')
                sfondo=pygame.transform.scale(sfondo, (larghezza_schermo, lunghezza_schermo))
                sfondo_surface=pygame.Rect((0, 0), (larghezza_schermo, lunghezza_schermo))
                pizzeria.blit(sfondo, sfondo_surface) 
                pizzeria.blit(gameover, (5, 200))
                pizzeria.blit(restart, (5,300))
                pizzeria.blit(exit_, (5, 330))

                pygame.display.update ()


        pygame.display.update()