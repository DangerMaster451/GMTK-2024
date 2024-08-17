from Board import Board
from Inventory import Inventory
from Blocks import *

import pygame
import time

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE | pygame.SCALED)
clock = pygame.time.Clock()
running = True

gameBoard = Board(1080, 8)
s = Long_Line_H(screen, 128, 0.2)

blocks = [0,1,2,3,4]
inventory = Inventory (1080, 216, blocks)

inventory.render()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    screen.fill("black")

    # RENDER YOUR GAME HERE

    gameBoard.render()


    screen.blit(gameBoard, (420, 0))
    screen.blit(inventory, (0, 0))
    
    s.render(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()