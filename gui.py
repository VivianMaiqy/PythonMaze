import pygame
from typing import List
import sys

ICON_SIZE = 34
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800



def display(map:List[List[int]]) -> None :

    pygame.init()
    # create screen
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    # title caption and icon 
    pygame.display.set_caption("maze")
    icon = pygame.image.load('image/icon.png')
    icon = pygame.transform.scale(icon, (ICON_SIZE, ICON_SIZE))
    pygame.display.set_icon(icon)

    # manu
    manu = True

   # show title 
    def title():

        t = pygame.image.load('image/title.jpg')
        t.set_colorkey((255,255,255))
        x = (SCREEN_WIDTH - t.get_width()) // 2
        y = (SCREEN_HEIGHT - t.get_height()) // 4
        screen.blit(t, (x,y))
    while True:

        # if on manu screen
        if manu:
            # load screen color 
            screen.fill((234,225,176))
            # add title
            title()

        # detect event
        for event in pygame.event.get():

            # if quit
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        pygame.display.update()