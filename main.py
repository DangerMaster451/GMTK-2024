from Board import Board





import pygame

pygame.init()
screen = pygame.display.set_mode((1920, 1080), pygame.RESIZABLE | pygame.SCALED)
clock = pygame.time.Clock()
running = True

gameBoard = Board(1080, 3)



while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")

    # RENDER YOUR GAME HERE
    gameBoard.render()
    screen.blit(gameBoard, (420, 0))

    pygame.display.flip()

    clock.tick(60)
pygame.quit()