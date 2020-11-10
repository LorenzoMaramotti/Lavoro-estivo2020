def blackjack_main():
    global punti1, punti2, carte_2, carte_3, carte_4, carte_5, carte_6, carte_7, carte_8, carte_9, carte_10, carte_jack, carte_donna, carte_re, carte_asso, carte, controllo1, controllo2, carte_iniziali, game_over1, win, pareggio1, game, x_player, x_dealer, due, tre, quattro, cinque, sei, sette, otto, nove, dieci, jack, donna, asso, mazzo
    import pygame, sys
    from pygame import mixer
    import random

    due=[r'Image\Blackjack\2C.png', r'Image\Blackjack\2D.png', r'Image\Blackjack\2H.png', r'Image\Blackjack\2S.png']
    tre=[r'Image\Blackjack\3C.png', r'Image\Blackjack\3D.png', r'Image\Blackjack\3H.png', r'Image\Blackjack\3S.png']
    quattro=[r'Image\Blackjack\4C.png', r'Image\Blackjack\4D.png', r'Image\Blackjack\4H.png', r'Image\Blackjack\4S.png']
    cinque=[r'Image\Blackjack\5C.png', r'Image\Blackjack\5D.png', r'Image\Blackjack\5H.png', r'Image\Blackjack\5S.png']
    sei=[r'Image\Blackjack\6C.png', r'Image\Blackjack\6D.png', r'Image\Blackjack\6H.png', r'Image\Blackjack\6S.png']
    sette=[r'Image\Blackjack\7C.png', r'Image\Blackjack\7D.png', r'Image\Blackjack\7H.png', r'Image\Blackjack\7S.png']
    otto=[r'Image\Blackjack\8C.png', r'Image\Blackjack\8D.png', r'Image\Blackjack\8H.png', r'Image\Blackjack\8S.png']
    nove=[r'Image\Blackjack\9C.png', r'Image\Blackjack\9D.png', r'Image\Blackjack\9H.png', r'Image\Blackjack\9S.png']
    dieci=[r'Image\Blackjack\10C.png', r'Image\Blackjack\10D.png', r'Image\Blackjack\10H.png', r'Image\Blackjack\10S.png']
    jack=[r'Image\Blackjack\JC.png', r'Image\Blackjack\JD.png', r'Image\Blackjack\JH.png', r'Image\Blackjack\JS.png']
    donna=[r'Image\Blackjack\QC.png', r'Image\Blackjack\QD.png', r'Image\Blackjack\QH.png', r'Image\Blackjack\QS.png']
    re=[r'Image\Blackjack\KC.png', r'Image\Blackjack\KD.png', r'Image\Blackjack\KH.png', r'Image\Blackjack\KS.png']
    asso=[r'Image\Blackjack\AC.png', r'Image\Blackjack\AD.png', r'Image\Blackjack\AH.png', r'Image\Blackjack\AS.png']
    mazzo=[due, tre,quattro, cinque, sei, sette, otto, nove, dieci, jack, donna, re, asso]


    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    COLORE1=(150, 0, 24)

    pygame.init()
    mixer.init()
    pygame.display.set_caption('BlackJack ')

    x_screen=1080
    y_screen=720
    x_player=800
    x_dealer=200

    main = pygame.display.set_mode((x_screen, y_screen))
    pygame.key.set_repeat(0)
    sfondo=pygame.image.load(r'image\Blackjack\blackjack back.jpg')
    sfondo=pygame.transform.scale(sfondo, (x_screen, y_screen))
    sfondo_surface=pygame.Rect((0, 0), (x_screen, y_screen))
    main.blit(sfondo, sfondo_surface)

    clock = pygame.time.Clock()

    FPS = 2

    carte=0
    punti1=0
    punti2=0
    controllo1=1
    controllo2=0
    carte_iniziali=0

    carte_2=0
    carte_3=0
    carte_4=0
    carte_5=0
    carte_6=0
    carte_7=0
    carte_8=0
    carte_9=0
    carte_10=0
    carte_jack=0
    carte_donna=0
    carte_re=0
    carte_asso=0
    game_over1=True
    win=True
    pareggio1=True
    game=True

    def blit_background(background, dim_gen_x, dim_gen_y, name_screen):
        sfondo=pygame.image.load(background)
        sfondo=pygame.transform.scale(sfondo, (dim_gen_x, dim_gen_y))
        sfondo_surface=pygame.Rect((0, 0), (dim_gen_x, dim_gen_y))
        name_screen.blit(sfondo, sfondo_surface)

    def song(song_main):
        mixer.music.load(song_main) 
        mixer.music.set_volume(2)
        mixer.music.play(1) 

    def blit_button(pos_x, pos_y, dim_x, dim_y,image_def):
        button=pygame.Rect(pos_x, pos_y, dim_x, dim_y)
        image = pygame.image.load(image_def)
        image= pygame.transform.scale(image, (dim_x,dim_y)) 
        main.blit(image, button)
        return button 

    def scritta(l_font, text, color, pos_text_x, pos_text_y):
        font = pygame.font.Font('freesansbold.ttf', l_font) 
        text_ = font.render(text, True, color)
        main.blit(text_, (pos_text_x, pos_text_y))

    def carta_pescata_1():
        global punti1, carte_2, carte_3, carte_4, carte_5, carte_6, carte_7, carte_8, carte_9, carte_10, carte_jack, carte_donna, carte_re, carte_asso
        carta=random.randint(0, (len(mazzo)-1))
        pescata=mazzo[carta]
        if pescata==due:
            if carte_2<=3:
                punti1+=2
                carte_2+=1
        elif pescata == tre:
            if carte_3<=3:
                punti1+=3
                carte_3+=1
        elif pescata == quattro:
            if carte_4<=3:
                punti1+=4
                carte_4+=1
        elif pescata == cinque:
            if carte_5<=3:
                punti1+=5
                carte_5+=1
        elif pescata == sei:
            if carte_6<=3:
                punti1+=6
                carte_6+=1
        elif pescata == sette:
            if carte_7<=3:
                punti1+=7
                carte_7+=1
        elif pescata ==otto:
            if carte_8<=3:
                punti1+=8
                carte_8+=1
        elif pescata == nove:
            if carte_9<=3:
                punti1+= 9
                carte_9+=1
        elif pescata == dieci:
                if carte_10<=3:
                    punti1+=10
                    carte_10+=1
        elif pescata == jack:
            if carte_jack<=3:
                punti1+=10
                carte_jack+=1
        elif pescata == donna:
            if carte_donna<=3:
                punti1+=10
                carte_donna+=1
        elif pescata == re:
            if carte_re<=3:
                punti1+=10
                carte_re+=1
        elif pescata == asso:
            if carte_asso<=3:
                if punti1 <= 10:
                    punti1+=11
                else:
                    punti1+=1
        carta_2=random.randint(0, (len(pescata)-1))
        pescata=pescata.pop(carta_2)
        return pescata


    def carta_pescata_2():
        global punti2, carte_2, carte_3, carte_4, carte_5, carte_6, carte_7, carte_8, carte_9, carte_10, carte_jack, carte_donna, carte_re, carte_asso
        carta=random.randint(0, (len(mazzo)-1))
        pescata=mazzo[carta]
        if pescata==due:
            if carte_2<=3:
                punti2+=2
                carte_2+=1
        elif pescata == tre:
            if carte_3<=3:
                punti2+=3
                carte_3+=1
        elif pescata == quattro:
            if carte_4<=3:
                punti2+=4
                carte_4+=1
        elif pescata == cinque:
            if carte_5<=3:
                punti2+=5
                carte_5+=1
        elif pescata == sei:
            if carte_6<=3:
                punti2+=6
                carte_6+=1
        elif pescata == sette:
            if carte_7<=3:
                punti2+=7
                carte_7+=1
        elif pescata ==otto:
            if carte_8<=3:
                punti2+=8
                carte_8+=1
        elif pescata == nove:
            if carte_9<=3:
                punti2+= 9
                carte_9+=1
        elif pescata == dieci:
                if carte_10<=3:
                    punti2+=10
                    carte_10+=1
        elif pescata == jack:
            if carte_jack<=3:
                punti2+=10
                carte_jack+=1
        elif pescata == donna:
            if carte_donna<=3:
                punti2+=10
                carte_donna+=1
        elif pescata == re:
            if carte_re<=3:
                punti2+=10
                carte_re+=1
        elif pescata == asso:
            if carte_asso<=3:
                if punti2 <= 10:
                    punti2+=11
                else:
                    punti2+=1
        carta_2=random.randint(0, (len(pescata)-1))
        pescata=pescata.pop(carta_2)
        return pescata


    def reset():
        global due, tre, quattro, cinque, sei, sette, otto, nove, dieci, jack, donna, re, asso, mazzo, x_player, x_dealer, carte, punti1, punti2, controllo1, controllo2, carte_iniziali, carte_2, carte_3, carte_4, carte_5, carte_6, carte_7, carte_8, carte_9, carte_10, carte_jack, carte_donna, carte_re, carte_asso 
        due=[r'Image\Blackjack\2C.png', r'Image\Blackjack\2D.png', r'Image\Blackjack\2H.png', r'Image\Blackjack\2S.png']
        tre=[r'Image\Blackjack\3C.png', r'Image\Blackjack\3D.png', r'Image\Blackjack\3H.png', r'Image\Blackjack\3S.png']
        quattro=[r'Image\Blackjack\4C.png', r'Image\Blackjack\4D.png', r'Image\Blackjack\4H.png', r'Image\Blackjack\4S.png']
        cinque=[r'Image\Blackjack\5C.png', r'Image\Blackjack\5D.png', r'Image\Blackjack\5H.png', r'Image\Blackjack\5S.png']
        sei=[r'Image\Blackjack\6C.png', r'Image\Blackjack\6D.png', r'Image\Blackjack\6H.png', r'Image\Blackjack\6S.png']
        sette=[r'Image\Blackjack\7C.png', r'Image\Blackjack\7D.png', r'Image\Blackjack\7H.png', r'Image\Blackjack\7S.png']
        otto=[r'Image\Blackjack\8C.png', r'Image\Blackjack\8D.png', r'Image\Blackjack\8H.png', r'Image\Blackjack\8S.png']
        nove=[r'Image\Blackjack\9C.png', r'Image\Blackjack\9D.png', r'Image\Blackjack\9H.png', r'Image\Blackjack\9S.png']
        dieci=[r'Image\Blackjack\10C.png', r'Image\Blackjack\10D.png', r'Image\Blackjack\10H.png', r'Image\Blackjack\10S.png']
        jack=[r'Image\Blackjack\JC.png', r'Image\Blackjack\JD.png', r'Image\Blackjack\JH.png', r'Image\Blackjack\JS.png']
        donna=[r'Image\Blackjack\QC.png', r'Image\Blackjack\QD.png', r'Image\Blackjack\QH.png', r'Image\Blackjack\QS.png']
        re=[r'Image\Blackjack\KC.png', r'Image\Blackjack\KD.png', r'Image\Blackjack\KH.png', r'Image\Blackjack\KS.png']
        asso=[r'Image\Blackjack\AC.png', r'Image\Blackjack\AD.png', r'Image\Blackjack\AH.png', r'Image\Blackjack\AS.png']
        mazzo=[due, tre,quattro, cinque, sei, sette, otto, nove, dieci, jack, donna, re, asso]
        x_player=800
        x_dealer=200
        carte=0
        punti1=0
        punti2=0
        controllo1=1
        controllo2=0
        carte_iniziali=0
        carte_2=0
        carte_3=0
        carte_4=0
        carte_5=0
        carte_6=0
        carte_7=0
        carte_8=0
        carte_9=0
        carte_10=0
        carte_jack=0
        carte_donna=0
        carte_re=0
        carte_asso=0

    def gameover_player(text, pos_text):
        global game_over1, win, pareggio1, game
        scritta(150, "HAI PERSO", BLACK, 100, 250)
        scritta(40, text, BLACK, pos_text, 390)
        scritta(40, "Premi invio per restartare", BLACK, 250, 430)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over1=False
                win=False
                pareggio1=False
                game=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over1=False
                    win=False
                    pareggio1=False
                    game=False
                if event.key == pygame.K_RETURN:
                    reset()
                    blit_background(r'image\Blackjack\blackjack back.jpg', x_screen, y_screen, main)
                    game_over1=False
                    break

    def win_player(text, pos_text):
        global win, game, game_over1, pareggio1
        scritta(150, "HAI VINTO", BLACK, 100, 250)
        scritta(40, text, BLACK, pos_text, 390)
        scritta(40, "Premi invio per restartare", BLACK, 250, 430)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over1=False
                win=False
                pareggio1=False
                game=False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over1=False
                    win=False
                    pareggio1=False
                    game=False
                if event.key == pygame.K_RETURN:
                    reset()
                    blit_background(r'image\Blackjack\blackjack back.jpg', x_screen, y_screen, main)
                    win=False
                    break

    def pareggio():
        global pareggio1, game_over1, win, game
        scritta(150, "PAREGGIO", BLACK, 100, 250)
        scritta(40, "Premi invio per restartare", BLACK, 250, 390)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over1=False
                win=False
                pareggio1=False
                game=False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over1=False
                    win=False
                    pareggio1=False
                    game=False
                if event.key == pygame.K_RETURN:
                    reset()
                    blit_background(r'image\Blackjack\blackjack back.jpg', x_screen, y_screen, main)
                    pareggio1=False
                    break





    while game:
        clock.tick(FPS)
        

        if punti1>=22:
            game_over1=True
            while game_over1:
                gameover_player("Il tuo punteggio ha superato 21", 220)
                pygame.display.update()

        if punti2>=22:
            win=True
            while win:
                win_player("Il banco ha superato 21", 250)
                pygame.display.update()
        
        if punti2>16 and controllo1==2 and controllo2==3:
            if punti1==punti2:
                pareggio1=True
                while pareggio1:
                    pareggio()
                    pygame.display.update()
            elif punti1>punti2:
                win=True
                while win:
                    win_player("Hai battutto il banco", 250)
                    pygame.display.update()
            elif punti1<punti2:
                game_over1=True
                while game_over1:
                    gameover_player("Il banco ti ha battuto", 300)
                    pygame.display.update()



        sfondo1=pygame.image.load(r'image\Blackjack\alto.blackjack.jpg')
        sfondo1=pygame.transform.scale(sfondo1, (241, 68))
        sfondo_surface1=pygame.Rect((0, 0), (241, 68))
        main.blit(sfondo1, sfondo_surface1)

        sfondo2=pygame.image.load(r'image\Blackjack\basso.blackjack.jpg')
        sfondo2=pygame.transform.scale(sfondo2, (241, 68))
        sfondo_surface2=pygame.Rect((839, 652), (241, 68))
        main.blit(sfondo2, sfondo_surface2)

        

        
        if carte_iniziali <=4:
            clock.tick(FPS)
            if carte_iniziali==0:
                pescata_giocatore=carta_pescata_1()
                song(r'Song\Carta sound.wav')
                blit_button(900, 500, 98, 150, pescata_giocatore)
            elif carte_iniziali==1:
                pescata_dealer=carta_pescata_2()
                song(r'Song\Carta sound.wav')
                blit_button(100, 70, 98, 150, pescata_dealer)
            elif carte_iniziali==2:
                pescata_giocatore=carta_pescata_1()
                song(r'Song\Carta sound.wav')
                blit_button(850, 500, 98, 150, pescata_giocatore)
            elif carte_iniziali==3:
                pescata_dealer=carta_pescata_2()
                song(r'Song\Carta sound.wav')
                blit_button(150, 70, 98, 150, pescata_dealer)
            carte_iniziali+=1
            pygame.display.update()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over1=False
                win=False
                pareggio1=False
                game=False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over1=False
                    win=False
                    pareggio1=False
                    game=False
                if carte<=8 and controllo1==1:
                    if event.key == pygame.K_SPACE:
                        pescata_giocatore=carta_pescata_1()
                        carte+=1
                        blit_button(x_player, 500, 98, 150, pescata_giocatore)
                        song(r'Song\Carta sound.wav')
                        x_player-=50

                        
                if event.key == pygame.K_RETURN:
                    controllo2=3
                    controllo1=2
            if controllo2==3:
                if punti2<=16:
                    clock.tick(FPS)
                    pescata_dealer=carta_pescata_2()
                    blit_button(x_dealer, 70, 98, 150, pescata_dealer)
                    song(r'Song\Carta sound.wav')
                    x_dealer+=50
                    pygame.display.update()

        punti1_blit="I tuoi punti: {}" .format(punti1)
        punti2_blit="Punti Dealer: {}" .format (punti2)

        scritta(25, punti2_blit, BLACK, 0, 10)
        scritta(25, punti1_blit, BLACK, 900, 690)
        scritta(20, "Premi spazio per prendere un altra carta", COLORE1, 300, 670)
        scritta(20, "premi inivio per stare", COLORE1, 300, 690)
        
        pygame.display.update()