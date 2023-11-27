

import pygame
import sys, os
from pygame import mixer
import button, rects, music_control, snake_game

def main_screen():
    pygame.init()

    width, height =  960 , 540
    screen = pygame.display.set_mode((960 , 540), pygame.RESIZABLE)
    pygame.display.set_caption('Virtual Villa')

    clock = pygame.time.Clock()

    WHITE_BUTTON = pygame.image.load("assets/start.png")
    songs = []

    for song in os.listdir(r"C:\Users\rashi\Desktop\cs project\main\audios"):
        if song.endswith('.mp3'):
            songs.append(song)

    
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(-1) 

    bg = pygame.image.load('assets/art2.jpg')
    bg = pygame.transform.scale(bg, (960 , 540))
    screen.blit(bg,(0,0))

    text_font = pygame.font.SysFont('Centaur',20,)
    timer_text = text_font.render("25:00", True, "white")
    timer_text_rect = timer_text.get_rect(center=(width/2, height/2))

    def draw_text(text,font,text_col,x,y):
        img = font.render(text,True,text_col)
        screen.blit(img,(x,y))

    mixer.init()

    play_surface = pygame.image.load('assets/play.png').convert_alpha()
    pause_surface = pygame.image.load('assets/pause.png').convert_alpha()
    next_surface = pygame.image.load('assets/next.png').convert_alpha()
    back_surface = pygame.image.load('assets/back.png').convert_alpha()

    play = button.Button(472,453, play_surface, 0.1)
    pause = button.Button(472,453, pause_surface, 0.05)
    next = button.Button(519, 453, next_surface, 0.05)
    back = button.Button(433, 453, back_surface, 0.05)

    game_start_surface = pygame.image.load('assets/gamestart.png').convert_alpha()
    game_start = button.Button(714, 447, game_start_surface, 0.1)



    start_surface = pygame.image.load('assets/start_game.png').convert_alpha()
    start_timer = button.Button(90,400, start_surface, 0.05)

    short_break_surface = pygame.image.load('assets/shortbreak.png').convert_alpha()
    long_break_surface = pygame.image.load('assets/longbreak.png').convert_alpha()

    short_break = button.Button(225,400, short_break_surface, 0.05)
    long_break = button.Button(50,400, long_break_surface, 0.08)

    pomodoro_surface = pygame.image.load('assets/pomodoro.jpg').convert_alpha()
    pomodoro = button.Button(150,400, pomodoro_surface, 0.08)

    pomodoro_length = 1500 # 1500 secs / 25 mins
    short_break_length = 300 # 300 secs / 5 mins
    long_break_length = 900 # 900 secs / 15 mins

    current_seconds = pomodoro_length
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    started = False
    played = False; pau = False
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT and started:
                    current_seconds -= 1
    
        if start_timer.draw(screen) == True:
            if started:
                started = False
            else:
                started = True
        if short_break.draw(screen) == True:
                current_seconds = short_break_length
                started = False
        if long_break.draw(screen) == True:
                current_seconds = long_break_length
                started = False
        if pomodoro.draw(screen):
                current_seconds = pomodoro_length
                started = False
        
        bg = pygame.image.load('assets/art2.jpg')
        bg = pygame.transform.scale(bg, (960 , 540))
        screen.blit(bg,(0,0))
        rects.rectangles(screen)

        '''if play.draw(screen) == True:
            music_control.play_song()
            pau = True
        if pau:
            if pause.draw(screen):
                music_control.pause_song()   '''
        if pause.draw(screen):
            music_control.pause_song()
            played = True   
        if played:
            pause = pause_surface = pygame.image.load('assets/play.png').convert_alpha()
            pause = button.Button(472,453, pause_surface, 0.08)
        else: 
            pause = pause_surface = pygame.image.load('assets/pause.png').convert_alpha()
            pause = button.Button(472,453, pause_surface, 0.05)
            if pause.draw(screen) == True:
                music_control.play_song()
            
        if game_start.draw(screen):
            snake_game.game(screen)


        '''if next.draw(screen) == True:
            music_control.mouse_clicks1(event)
    
        if back.draw(screen):
            music_control.mouse_clicks1(event)'''
        game_start.draw(screen)
        start_timer.draw(screen)
        short_break.draw(screen)
        long_break.draw(screen)
        pomodoro.draw(screen)

        if current_seconds >= 0:
            display_seconds = current_seconds % 60
            display_minutes = int(current_seconds / 60) % 60

        timer_text = text_font.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
        screen.blit( timer_text,timer_text_rect)
        draw_text('mini-game',text_font,(200,235,255),485,356)
        draw_text('music',text_font,(200,235,255),570,535)
        draw_text('timer',text_font,(200,235,255),27,356)

        pygame.display.update()

