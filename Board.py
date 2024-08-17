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

    def render(self):
        size = self.pixel_size
        rect = pygame.Rect(self.coordinate[0]*size-0+5, self.coordinate[1]*size+5, size-5, size-5)
        pygame.draw.rect(self.surface, "red", rect)

