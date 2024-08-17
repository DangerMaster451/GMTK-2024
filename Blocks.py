import pygame

single = pygame.image.load("Assets/Single.png")

class Block():
    def __init__(self, surface:pygame.Surface, image:pygame.Surface, structure:list[tuple[int,int]]) -> None:
        self.surface = surface
        self.image = pygame.transform.scale(image, (self.pixel_size,self.pixel_size))
        self.structure = structure
        self.pixel_size = surface.tile_pixel_size

    def render(self, rel_x, rel_y) -> None:
        for coord in self.structure:
            self.surface.blit(self.image, (coord[0] * self.pixel_size + rel_x, coord[1] * self.pixel_size + rel_y))
            

class Single(Block):
    def __init__(self, surface) -> None:
        super().__init__(surface, single, [(0,0)])