import pygame
import math

class Board(pygame.Surface):
    def __init__(self, pixel_size:int, grid_size:int) -> None:
        pygame.Surface.__init__(self, (pixel_size, pixel_size))

        self.grid_size = grid_size
        self.tiles = []
        self.pixel_size = pixel_size

        # calculate pixel size of tiles
        self.tile_pixel_size = pixel_size/grid_size

        # create a list of Tile objects each with an x and y value
        for y in range(0, grid_size):
            for x in range(0, grid_size):
                t = Tile(self, (x,y), self.tile_pixel_size)
                self.tiles.append(t)

    def render(self):
        for tile in self.tiles:
            tile.render()

class Tile():
    def __init__(self, surface:pygame.Surface, coordinate:tuple[int,int], pixel_size:int):
        self.surface = surface
        self.coordinate = coordinate
        self.pixel_size = pixel_size
        self.default_image = pygame.transform.scale(pygame.image.load("Assets/InventorySlot.png"), (pixel_size,pixel_size))
        self.hovered_image = pygame.transform.scale(pygame.image.load("Assets/HoverInvSlot.png"), (pixel_size,pixel_size))
        self.real_point = ((1920 - self.surface.pixel_size)/2 + self.coordinate[0] * self.surface.tile_pixel_size + self.surface.tile_pixel_size/2,
                           (1080 - self.surface.pixel_size)/2 + self.coordinate[1] * self.surface.tile_pixel_size)

    def render(self):
        if self.isHovered():
            image = self.hovered_image
        else:
            image = self.default_image


        x = self.coordinate[0] * self.pixel_size
        y = self.coordinate[1] * self.pixel_size
        self.surface.blit(image, (x,y))

    def isHovered(self) -> bool:
        if math.sqrt((self.real_point[0] - pygame.mouse.get_pos()[0])**2 + (self.real_point[1] - pygame.mouse.get_pos()[1])**2) < self.pixel_size/2:
            return True
        else:
            return False
        
    def isClicked(self, click:bool) -> bool:
        if self.isHovered() and click:
            return True
        else:
            return False