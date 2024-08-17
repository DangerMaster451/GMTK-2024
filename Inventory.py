import pygame

from Blocks import Single, Short_Line_H, Long_Line_H, Short_Line_V, Long_Line_V

test = pygame.transform.scale(pygame.image.load("Assets/light blue tile.png"), (32,32))

class Inventory(pygame.Surface):
    def __init__(self, size_x, blocks):
        self.size_x = size_x
        self.blocks = blocks
        self.inv_tile_count = len(self.blocks)
        self.scale_size = self.size_x/5/self.size_x*1.5
        self.tile_size = size_x/self.inv_tile_count
        self.image = pygame.transform.scale(pygame.image.load("Assets/InventorySlot.png"), (self.tile_size,self.tile_size))
        self.slots = []

        pygame.Surface.__init__(self, (size_x, self.tile_size) )

        for i in range(self.inv_tile_count):
            slot = InventorySlot(self, (i * self.tile_size, 0), self.tile_size, i, self.blocks[i])
            self.slots.append(slot)

    def render(self):
        for slot in self.slots: slot.render()

class InventorySlot():
    def __init__(self, surface:pygame.Surface, coordinate:tuple[int,int], pixel_size:int, index:int, block:int):
        self.surface = surface
        self.coordinate = coordinate
        self.pixel_size = pixel_size
        self.image = pygame.transform.scale(pygame.image.load("Assets/InventorySlot.png"), (pixel_size,pixel_size))
        self.index = index
        self.block = block
        self.scale_size = 0.25

    def render(self):
        if self.block == 0:
            s = Single(self.image, 128, self.scale_size)
        elif self.block == 1:
            s = Short_Line_H(self.image, 128, self.scale_size)
        elif self.block == 2:
            s = Long_Line_H(self.image, 128, self.scale_size)
        elif self.block == 3:
            s = Short_Line_V(self.image, 128, self.scale_size)
        elif self.block == 4:
            s = Long_Line_V(self.image, 128, self.scale_size)

        s.renderInventory((self.pixel_size - s.pixel_size)/2, (self.pixel_size - s.pixel_size)/2)
    
        self.surface.blit(self.image, self.coordinate)