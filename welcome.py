import pygame
import sys
import rects
import button, main
pygame.init()
pygame.font.init()

width,height=700,500
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Virtual Villa')

screen.fill((134, 175, 240))

#texts to be displayed
heading_font = pygame.font.SysFont('timesnewroman',44,bold=True)
text_font=pygame.font.SysFont('timesnewroman',28)
welc_text=heading_font.render('Welcome to',True,(3, 15, 135))
welc_text2=heading_font.render('VIRTUAL VILLA',True,(1, 10, 89))
intro_text=text_font.render('Ready to start? Add your first task and',True,(3, 15, 135))
intro_text2=text_font.render('let the productivity journey begin!',True,(3, 15, 135))
ques_text=text_font.render('What do you want to focus on today?',True,(1, 10, 89))

#start button
start_surface=pygame.image.load('assets/start_task.png').convert_alpha()
start_task=button.Button(293,384,start_surface,0.25)

#text input box
user_ip = ''
text_box = pygame.Rect(280,308,100,50)
active = False
color = pygame.Color('black')
clock = pygame.time.Clock()

while True:
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if text_box.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_BACKSPACE:
                        user_ip = user_ip[:-1]
                    else:
                        user_ip += event.unicode

        if start_task.draw(screen):
                main.main_screen()
        
        if active:
            color = pygame.Color((3, 15, 135))
        else:
            color = pygame.Color('black')
        #print(pygame.font.get_fonts())
        rects.task(screen)

        pygame.draw.rect(screen,color, text_box,4)
        surf = text_font.render(user_ip,True,'black')
        screen.blit(surf, (text_box.x +5 , text_box.y +5))
        text_box.w = max(150, surf.get_width()+10)

        screen.blit(welc_text,(250,40))
        screen.blit(welc_text2,(190,94))
        screen.blit(intro_text,(145,156))
        screen.blit(intro_text2,(173,193))
        screen.blit(ques_text,(150,262))

        start_task.draw(screen)
        pygame.display.update()
        clock.tick(50)