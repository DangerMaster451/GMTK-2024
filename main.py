from Board import Board
from Blocks import *

import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE | pygame.SCALED)
clock = pygame.time.Clock()
running = True

gameBoard = Board(720, 5)
s = Test(screen, 128)

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

    screen.blit(gameBoard, ((1920 - gameBoard.pixel_size)/2, 64))
    s.update(click)
    pygame.display.flip()
    clock.tick(120)
pygame.quit()