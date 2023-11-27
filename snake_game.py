import pygame
from pygame.locals import *
import random, button, main

def game(screen):

    pygame.init()

    screen2_width = 600
    screen2_height = 600

    screen2 = pygame.display.set_mode((screen2_width, screen2_height))
    pygame.display.set_caption('Snake')

    end_game_surface = pygame.image.load('assets/backgame.png').convert_alpha()
    end_game = button.Button(300,300, end_game_surface, 0.05)

    cell_size = 10
    direction = 1 # 1-up, 2-down, 3-right, 4-left
    update_snake = 0
    food = [0,0]
    new_food = True
    new_piece = [0,0]
    score = 0
    game_over = False
    clicked = False

    snake_pos = [[int(screen2_width/2),int(screen2_height/2)]]
    snake_pos.append([int(screen2_width/2),int(screen2_height/2) + cell_size])
    snake_pos.append([int(screen2_width/2),int(screen2_height/2) + cell_size*2])
    snake_pos.append([int(screen2_width/2),int(screen2_height/2) + cell_size*3])

    font = pygame.font.SysFont(None,40)

    bg = (255,200,150)
    body_inner = (50,175,25)
    body_outer = (100,100,200)
    food_col = (200,50,50)

    again_rect = Rect(screen2_width // 2 -80, screen2_height // 2, 160, 50)

    def draw_screen2():
        screen2.fill(bg)


    def draw_score():
        score_txt = 'Score:' + str(score)
        score_img = font.render(score_txt, True, (0,0,0))
        screen2.blit(score_img, (0,0))

    def check_game_over(game_over):
        head_count = 0
        for segment in snake_pos:
            if snake_pos[0] == segment and head_count>0:
                game_over = True
            head_count +=1

        if snake_pos[0][0] < 0 or snake_pos[0][0] >screen2_width or snake_pos[0][1]<0 or snake_pos[0][1]>screen2_height:
            game_over = True
        return game_over

    def draw_game_over():
        over_txt = 'Game Over'
        over_img = font.render(over_txt, True, (0,0,0))
        pygame.draw.rect(screen2, (170,74,68), (screen2_width // 2 - 80, screen2_height // 2 -60, 160, 50))
        screen2.blit(over_img, (screen2_width // 2 -80, screen2_height // 2 -50))


        again_text = 'Play Again'
        again_img = font.render(again_text, True, (0,0,0))
        pygame.draw.rect(screen2,(170,74,68), again_rect)
        screen2.blit(again_img, (screen2_width // 2 -80, screen2_height // 2 +10))

    run = True
    while run:
        if end_game.draw(screen) == True:
            pygame.quit()

        draw_screen2()
        draw_score()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 3:
                        direction = 1
                if event.key == pygame.K_RIGHT and direction != 4:
                    direction = 2
                if event.key == pygame.K_DOWN and direction != 1:
                    direction = 3
                if event.key == pygame.K_LEFT and direction != 2:
                    direction = 4

        if new_food == True:
            new_food = False
            food[0] = cell_size * random.randint(0, (screen2_width // cell_size) - 1)
            food[1] = cell_size * random.randint(0, (screen2_height // cell_size) - 1)

        pygame.draw.rect(screen2, food_col,(food[0], food[1], cell_size, cell_size))

        if snake_pos[0] == food:
            new_food = True
            new_piece = list(snake_pos[-1])
            if direction == 1:
                new_piece[1] += cell_size
            if direction == 3:
                new_piece[1] -= cell_size
            if direction == 2:
                new_piece[1] -= cell_size
            if direction == 4:
                new_piece[1] += cell_size

            snake_pos.append(new_piece)

            score +=1

        if game_over == False:
            if update_snake > 99:
                update_snake = 0
                snake_pos = snake_pos[-1:] + snake_pos[:-1]
                if direction == 1:
                    snake_pos[0][0] = snake_pos[1][0]
                    snake_pos[0][1] = snake_pos[1][1] - cell_size
                if direction == 3:
                    snake_pos[0][0] = snake_pos[1][0]
                    snake_pos[0][1] = snake_pos[1][1] + cell_size
                if direction == 2:
                    snake_pos[0][1] = snake_pos[1][1]
                    snake_pos[0][0] = snake_pos[1][0] + cell_size
                if direction == 4:
                    snake_pos[0][1] = snake_pos[1][1]
                    snake_pos[0][0] = snake_pos[1][0] - cell_size

                game_over = check_game_over(game_over)

        if game_over == True:
            draw_game_over()
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    direction = 1 # 1-up, 2-down, 3-right, 4-left
                    update_snake = 0
                    food = [0,0]
                    new_food = True
                    new_piece = [0,0]
                    score = 0
                    game_over = False


                    snake_pos = [[int(screen2_width/2),int(screen2_height/2)]]
                    snake_pos.append([int(screen2_width/2),int(screen2_height/2) + cell_size])
                    snake_pos.append([int(screen2_width/2),int(screen2_height/2) + cell_size*2])
                    snake_pos.append([int(screen2_width/2),int(screen2_height/2) + cell_size*3])

        head = 1
        for x in snake_pos:
            if head == 0:
                pygame.draw.rect(screen2,body_outer,(x[0],x[1],cell_size,cell_size))
                pygame.draw.rect(screen2,body_inner,(x[0]+1,x[1]+1,cell_size-2,cell_size-2))
            if head == 1:
                pygame.draw.rect(screen2,body_outer,(x[0],x[1],cell_size,cell_size))
                pygame.draw.rect(screen2,(170,74,68),(x[0]+1,x[1]+1,cell_size-2,cell_size-2))
                head = 0
        end_game.draw(screen)
        pygame.display.update()

        update_snake +=1

    pygame.quit()