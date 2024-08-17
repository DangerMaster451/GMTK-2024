import pygame

red_tile = pygame.image.load("Assets/red tile.png")
blue_tile = pygame.image.load("Assets/blue tile.png")
yellow_tile = pygame.image.load("Assets/yellow tile.png")
light_blue_tile = pygame.image.load("Assets/light blue tile.png")
orange_tile = pygame.image.load("Assets/orange tile.png")

class Block():
    def __init__(self, surface:pygame.Surface, image:pygame.Surface, pixel_size:int, structure:list[tuple[int,int]], scale_factor:float=1) -> None:
        self.surface = surface
        self.structure = structure
        self.pixel_size = pixel_size
        self.scale_factor = scale_factor
        self.image = pygame.transform.scale(image, (self.pixel_size*self.scale_factor,self.pixel_size*self.scale_factor))
        self.center = self.calculate_center()
        self.state = "rest"
        self.position = (0,0)

    def update(self, clicked):
        m_pos = pygame.mouse.get_pos()

        if self.state == "drag":
            self.position = m_pos
            if clicked and pygame.mouse.get_rel()[0] == 0 and pygame.mouse.get_rel()[1] == 0:
                self.state = "rest"

        elif self.state == "rest":
            if clicked and abs(m_pos[0] - self.position[0]) < 100 and abs(m_pos[1] - self.position[1]) < 100:
                self.state = "drag"

        self.render()

    def render(self) -> None:
        self.calculate_center()
        for coord in self.structure:
            self.surface.blit(self.image, (self.scale_factor * coord[0] * self.pixel_size + self.position[0] - self.center[0], self.scale_factor * coord[1] * self.pixel_size + self.position[1] - self.center[1]))
        
    def renderInventory(self, rel_x:float, rel_y:float) -> None:
        offset = 1
        previous_x = 0
        for coord in self.structure:
            x = self.scale_factor * coord[0] * self.pixel_size + rel_x
            y = self.scale_factor * coord[1] * self.pixel_size + rel_y
            if(offset != 1):
                if(x == previous_x):
                    y -= offset
                else:
                    x -= offset
            self.surface.blit(self.image, (x, y))
            if(offset == 1):
                previous_x = x
            offset +=1

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
    def __init__(self, surface, pixel_size, scale_factor=1) -> None:
        super().__init__(surface, red_tile, pixel_size, [(0,0)], scale_factor)

class Short_Line_H(Block):
    def __init__(self, surface, pixel_size, scale_factor=1) -> None:
        super().__init__(surface, yellow_tile, pixel_size, [(0,0),(1,0),(2,0)], scale_factor)

class Long_Line_H(Block):
    def __init__(self, surface, pixel_size, scale_factor=1) -> None:
        super().__init__(surface, blue_tile, pixel_size, [(0,0),(1,0),(2,0),(3,0),(4,0)], scale_factor)

class Short_Line_V(Block):
    def __init__(self, surface, pixel_size, scale_factor=1) -> None:
        super().__init__(surface, orange_tile, pixel_size, [(0,0),(0,1),(0,2)], scale_factor)

class Long_Line_V(Block):
    def __init__(self, surface, pixel_size, scale_factor=1) -> None:
        super().__init__(surface, light_blue_tile, pixel_size, [(0,0),(0,1),(0,2),(0,3),(0,4)], scale_factor)

class Test(Block):
    def __init__(self, surface, pixel_size) -> None:
        super().__init__(surface, orange_tile, pixel_size, [(0,0), (1,0),(0,1)])