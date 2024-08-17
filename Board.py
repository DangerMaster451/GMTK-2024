import pygame

class Board(pygame.Surface):
    def __init__(self, pixel_size:int, grid_size:int) -> None:
        pygame.Surface.__init__(self, (pixel_size, pixel_size))

        self.grid_size = grid_size
        self.tiles = []

        # calculate pixel size of tiles
        tile_pixel_size = pixel_size/grid_size

        # create a list of Tile objects each with an x and y value
        for y in range(0, grid_size):
            for x in range(0, grid_size):
                t = Tile(self, (x,y), tile_pixel_size)
                self.tiles.append(t)

    def render(self):
        self.fill("blue")
        for tile in self.tiles:
            tile.render()


class Tile():
    def __init__(self, surface:pygame.Surface, coordinate:tuple[int,int], pixel_size:int):
        self.surface = surface
        self.coordinate = coordinate
        self.pixel_size = pixel_size
        self.image = pygame.transform.scale(pygame.image.load("Assets/Tile.png"), (pixel_size,pixel_size))

    def render(self):
        x = self.coordinate[0] * self.pixel_size
        y = self.coordinate[1] * self.pixel_size
        self.surface.blit(self.image, (x,y))