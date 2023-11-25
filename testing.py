import pygame
import sys, os
from pygame import mixer
import button
import rects
import game_window
pygame.init()

screen = pygame.display.set_mode((800,500))
pygame.display.set_caption('Virtual Villa')

bg = pygame.image.load('art.jpg')
bg = pygame.transform.scale(bg, (800,500))
screen.blit(bg,(0,0))

text_font = pygame.font.SysFont('Centaur',20,)

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

mixer.init()

songs = []

for song in os.listdir(r"C:\Users\rashi\Desktop\cs project\audios"):
    if song.endswith('.mp3'):
        songs.append(song)

#def imgs_load():



play_surface = pygame.image.load('play.png').convert_alpha()
pause_surface = pygame.image.load('pause.png').convert_alpha()
next_surface = pygame.image.load('next.png').convert_alpha()
game_surface = pygame.image.load('start_game.png').convert_alpha()

play = button.Button(70, 200, play_surface, 0.1)
pause = button.Button(20, 200, pause_surface, 0.05)
next = button.Button(120, 200, next_surface, 0.05)
game_start = button.Button(600,400, game_surface, 0.08)

def play_song():
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play()   

def pause_song():
    pygame.mixer.music.pause()

# to register number of clicks
MouseClicks = 1
def mouse_clicks():
     global MouseClicks
     if MouseClicks:
            if event.button == 1:
                print(MouseClicks)
                # to move to next song in queue
                next_song = MouseClicks
                if next_song == len(songs):
                    next_song = 0
                pygame.mixer.music.load(songs[next_song])
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play()
                MouseClicks+=1


while True:

    rects.rectangles(screen)
    draw_text('mini-game',text_font,(200,235,255),600,250)
    draw_text('music',text_font,(200,235,255),62,153)
    draw_text('timer',text_font,(200,235,255),27,356)
   
    if pause.draw(screen) == True:
        pause_song()
    if play.draw(screen) == True:
        play_song()
    if next.draw(screen) == True:
        mouse_clicks()
    if game_start.draw(screen) == True:
        game_window.game(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()