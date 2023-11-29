import pygame

def rectangles(screen):
    villa_color_pink = (76,84,129)
    music_menu = pygame.draw.rect(screen,villa_color_pink,(414,410,150,100), width = 0, border_radius = 15)
    pomodoro_timer = pygame.draw.rect(screen,villa_color_pink,(20,390,300,130), width = 0, border_radius = 15)
    return music_menu,pomodoro_timer

def task(screen):
    task_box=pygame.draw.rect(screen,(255,255,255),(135,43,420,400),width = 0,border_bottom_right_radius=75,border_top_left_radius=50)
    return task_box