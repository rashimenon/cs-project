import pygame
import pygame_gui
import sys

pygame.init()

# Set up Pygame window

width, height = 1600,900
window = pygame.display.set_mode((1600,900))
pygame.display.set_caption('To-Do List')

# Set up pygame_gui manager
manager = pygame_gui.UIManager((1600,900))

# Create a to-do list
todo_list = []

# Create a Pygame clock to control the frame rate
clock = pygame.time.Clock()

# Create Pygame fonts
font = pygame.font.Font(None, 36)

# Main loop
running = True
while running:
    time_delta = clock.tick(60) / 1000.0  # Control frame rate

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle button click event
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame.MOUSEBUTTONDOWN:
                task_text = event.get_rect(center=(width/2, height/2))
                todo_list.append(task_text)

        # Update pygame_gui manager
        manager.process_events(event)

    # Draw the background
    window.fill((255, 255, 255))

    # Draw the to-do list
    y_position = 50
    for task in todo_list:
        task_surface = font.render(task, True, (0, 0, 0))
        window.blit(task_surface, (50, y_position))
        y_position += 40

    # Draw the input box and button
    text_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((350, 275), (900, 50)), manager=manager,
                                               object_id='#main_text_entry')

    add_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((260, 220), (80, 30)),
        text='Add',
        manager=manager)
    

    # Update pygame_gui manager
    manager.update(time_delta)

    # Draw pygame_gui elements
    manager.draw_ui(window)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()