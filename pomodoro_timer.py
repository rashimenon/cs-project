import pygame
import sys
import button

pygame.init()

width,height = 900, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pomodoro Timer")

clock = pygame.time.Clock()

WHITE_BUTTON = pygame.image.load("start.png")

text_font = pygame.font.SysFont('Centaur',20,)
timer_text = text_font.render("25:00", True, "white")
timer_text_rect = timer_text.get_rect(center=(width/2, height/2-25))


start_surface = pygame.image.load('start_game.png').convert_alpha()
start_timer = button.Button(100,400, start_surface, 0.05)

short_break_surface = pygame.image.load('shortbreak.png').convert_alpha()
long_break_surface = pygame.image.load('longbreak.png').convert_alpha()

short_break = button.Button(100,200, short_break_surface, 0.08)
long_break = button.Button(300,200, long_break_surface, 0.08)


pomodoro_length = 1500 # 1500 secs / 25 mins
short_break_length = 300 # 300 secs / 5 mins
long_break_length = 900 # 900 secs / 15 mins

current_seconds = pomodoro_length
pygame.time.set_timer(pygame.USEREVENT, 1000)
started = False

def draw_text(text,font,text_col,x,y):
    img = font.render(text,True,text_col)
    screen.blit(img,(x,y))

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


    screen.fill("#ba4949")

    start_timer.draw(screen)
    short_break.draw(screen)
    long_break.draw(screen)

    if current_seconds >= 0:
        display_seconds = current_seconds % 60
        display_minutes = int(current_seconds / 60) % 60
    timer_text = text_font.render(f"{display_minutes:02}:{display_seconds:02}", True, "white")
    screen.blit(timer_text, timer_text_rect)
    draw_text('mini-game',text_font,(200,235,255),600,250)


    pygame.display.update()