import pygame
from typing import List
import sys

ICON_SIZE = 34
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800
WHITE = (255,255,255)
BLACK = (0,0,0)


def display(map:List[List[int]]) -> None :

    pygame.init()
    # create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # title caption and icon 
    pygame.display.set_caption("maze")
    icon = pygame.image.load('image/icon.png')
    icon = pygame.transform.scale(icon, (ICON_SIZE, ICON_SIZE))
    pygame.display.set_icon(icon)

    # menu
    menu = True

    # draw text
    def draw_text(text, text_rect, surface, x, y):
        text_rect.topleft = (x,y)
        surface.blit(text, text_rect)

   # show title 
    def draw_menu():

        t = pygame.image.load('image/title.jpg')
        t.set_colorkey(WHITE)
        x = (SCREEN_WIDTH - t.get_width()) // 2
        y = (SCREEN_HEIGHT - t.get_height()) // 4
        
        font = pygame.font.SysFont(None, 50)
    
        text_1 = font.render('small maze', 1, BLACK) 
        text_1_rect = text_1.get_rect()
        x_1= (SCREEN_WIDTH - text_1_rect.width) // 2
        y_1= (SCREEN_HEIGHT) // 1.5
        draw_text(text_1, text_1_rect, screen, x_1, y_1)

        text_2 = font.render('medium maze', 1, BLACK)
        text_2_rect = text_2.get_rect() 
        x_2 = (SCREEN_WIDTH - text_2_rect.width) // 2
        y_2 = y_1 + text_1_rect.height * 2
        draw_text(text_2, text_2_rect, screen, x_2, y_2)

        text_3 = font.render('large maze', 1, BLACK)
        text_3_rect = text_3.get_rect() 
        x_3 = (SCREEN_WIDTH - text_3_rect.width) // 2
        y_3 = y_2 + text_2_rect.height * 2
        draw_text(text_3, text_3_rect, screen, x_3, y_3)
        screen.blit(t, (x,y))

    while True:

        # if on menu screen
        if menu:
            # load screen color 
            screen.fill((234,225,176))
            # add title
            draw_menu()
        # detect event
        for event in pygame.event.get():

            # if quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()