import pygame
from typing import List

def display(map:List[List[int]]) -> None :
    pygame.init()

    while True:
        screen = pygame.display.set_mode((800,600))