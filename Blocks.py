import pygame

red_tile = pygame.image.load("Assets/red tile.png")
blue_tile = pygame.image.load("Assets/blue tile.png")
yellow_tile = pygame.image.load("Assets/yellow tile.png")
light_blue_tile = pygame.image.load("Assets/light blue tile.png")
orange_tile = pygame.image.load("Assets/orange tile.png")

class Block():
    def __init__(self, surface:pygame.Surface, image:pygame.Surface, pixel_size:int, structure:list[tuple[int,int]]) -> None:
        self.surface = surface
        self.structure = structure
        self.pixel_size = pixel_size
        self.image = pygame.transform.scale(image, (self.pixel_size,self.pixel_size))
        self.center = self.calculate_center()

    def render(self, rel_x, rel_y) -> None:
        self.calculate_center()
        for coord in self.structure:
            self.surface.blit(self.image, (coord[0] * self.pixel_size + rel_x - self.center[0], coord[1] * self.pixel_size + rel_y - self.center[1]))
        #pygame.draw.circle(self.surface, "green", (self.center[0] + rel_x , self.center[1] + rel_y), 12)
            
    def calculate_center(self) -> tuple[int,int]:
        smallest_x = self.structure[0][0]
        largest_x = self.structure[-1][0]
        smallest_y = self.structure[0][1]
        largest_y = self.structure[-1][1]

        for tile in self.structure:
            if tile[0] < smallest_x:
                smallest_x = tile[0]
            if tile[0] > largest_x:
                largest_x = tile[0]
            if tile[1] > smallest_y:
                smallest_y = tile[1]
            if tile[1] < largest_y:
                largest_y = tile[0]

        center = ((largest_x * self.pixel_size - smallest_x * self.pixel_size)/2 + self.pixel_size/2, (smallest_y * self.pixel_size - largest_y * self.pixel_size)/2 + self.pixel_size/2)
        return center

class Single(Block):
    def __init__(self, surface, pixel_size) -> None:
        super().__init__(surface, red_tile, pixel_size, [(0,0)])

class Short_Line_H(Block):
    def __init__(self, surface, pixel_size) -> None:
        super().__init__(surface, yellow_tile, pixel_size, [(0,0),(1,0),(2,0)])

class Long_Line_H(Block):
    def __init__(self, surface, pixel_size) -> None:
        super().__init__(surface, blue_tile, pixel_size, [(0,0),(1,0),(2,0),(3,0),(4,0)])

class Short_Line_V(Block):
    def __init__(self, surface, pixel_size) -> None:
        super().__init__(surface, orange_tile, pixel_size, [(0,0),(0,1),(0,2)])

class Long_Line_V(Block):
    def __init__(self, surface, pixel_size) -> None:
        super().__init__(surface, light_blue_tile, pixel_size, [(0,0),(0,1),(0,2),(0,3),(0,4)])

