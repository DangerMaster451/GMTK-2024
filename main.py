from Board import Board
from Blocks import Single

import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE | pygame.SCALED)
clock = pygame.time.Clock()
running = True

gameBoard = Board(1080, 8)
s = Single(screen, 128)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    # RENDER YOUR GAME HERE

    gameBoard.render()

    screen.blit(gameBoard, (420, 0))
    s.render(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1])
    pygame.display.flip()
    clock.tick(60)
pygame.quit()