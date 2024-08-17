import pygame

from Blocks import Single, Short_Line_H, Long_Line_H, Short_Line_V, Long_Line_V

test = pygame.transform.scale(pygame.image.load("Assets/light blue tile.png"), (32,32))

class Inventory(pygame.Surface):
    def __init__(self, size_x, blocks):
        self.size_x = size_x
        self.inv_tile_count = 5
        self.blocks = blocks
        self.scale_size = self.size_x/5/self.size_x*1.5
        self.tile_size = size_x/self.inv_tile_count
        self.image = pygame.transform.scale(pygame.image.load("Assets/InventorySlot.png"), (self.tile_size,self.tile_size))
        self.slots = []

        pygame.Surface.__init__(self, (size_x, self.tile_size) )

        for i in range(self.inv_tile_count):
            slot = InventorySlot(self, (i * self.tile_size, 0), self.tile_size)
            self.slots.append(slot)

    def render(self):
        for slot in self.slots:
            
            slot.render()

            '''if self.blocks[i] == 0:
                s = Single(self, 128, self.scale_size)
                s.renderInventory(i*216+89, 89)
            elif self.blocks[i] == 1:
                s = Short_Line_H(self, 128, self.scale_size)
                s.renderInventory(i*216+56, 89)
            elif self.blocks[i] == 2:
                s = Long_Line_H(self, 128, self.scale_size)
                s.renderInventory(i*216+13, 89)
            elif self.blocks[i] == 3:
                s = Short_Line_V(self, 128, self.scale_size)
                s.renderInventory(i*216+89, 56)
            elif self.blocks[i] == 4:
                s = Long_Line_V(self, 128, self.scale_size)
                s.renderInventory(i*216+89, 13)  '''         


class InventorySlot():
    def __init__(self, surface:pygame.Surface, coordinate:tuple[int,int], pixel_size:int):
        self.surface = surface
        self.coordinate = coordinate
        self.pixel_size = pixel_size
        self.image = pygame.transform.scale(pygame.image.load("Assets/InventorySlot.png"), (pixel_size,pixel_size))

    def render(self):
        self.image.blit(test, (10,10))

        self.surface.blit(self.image, self.coordinate) 