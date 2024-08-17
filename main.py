from Board import Board
from Inventory import Inventory
from Blocks import *

import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE | pygame.SCALED)
clock = pygame.time.Clock()
running = True

gameBoard = Board(720, 3)

blocks = [0,1,2,3,4]
inventory = Inventory (720, blocks)

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
    inventory.render()

    screen.blit(gameBoard, ((1920 - gameBoard.pixel_size)/2, 64))
    screen.blit(inventory, ((1920 - inventory.size_x)/2, 820))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()