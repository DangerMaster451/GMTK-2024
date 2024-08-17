from Board import Board
from Inventory import Inventory
from Blocks import *

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE | pygame.SCALED)
clock = pygame.time.Clock()
running = True

gameBoard = Board(720, 3)
s = Long_Line_H(screen, 128)

blocks = [0,1,2,3,4]
inventory = Inventory (1080, 216, blocks)

inventory.render()


while running:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        else:
            click = False

    screen.fill("black")
    gameBoard.render()


    screen.blit(gameBoard, (420, 0))
    screen.blit(inventory, (0, 0))
    
    s.render(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    screen.blit(gameBoard, ((1920 - gameBoard.pixel_size)/2, 64))
    s.update(click)
    pygame.display.flip()
    clock.tick(120)
pygame.quit()