import pygame, os
songs = []

for song in os.listdir(r"C:\Users\rashi\Desktop\cs project\main\audios"):
    if song.endswith('.mp3'):
        songs.append(song)

 
def play_song():
    pygame.mixer.music.unpause() 

def pause_song():
    pygame.mixer.music.pause()

# to register number of clicks
MouseClicks = 1
def mouse_clicks1(event):
     global MouseClicks
     if MouseClicks:
            if event.button == 1:
                print(MouseClicks)
                # to move to next song in queue
                next_song = MouseClicks
                if next_song == len(songs):
                    next_song = 0
                    next_song+=1
                pygame.mixer.music.load(songs[next_song])
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play()
                MouseClicks+=1
     else:
           if event.button == 1:
                print(MouseClicks)
                # to move to prev song in queue
                prev_song = MouseClicks-1
                if prev_song == len(songs):
                    prev_song = 0
                    
                    
                pygame.mixer.music.load(songs[prev_song])
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play()
                prev_song-=1
                MouseClicks-=1
          

