import pygame

from Blocks import Single, Short_Line_H, Long_Line_H, Short_Line_V, Long_Line_V

class Inventory(pygame.Surface):
    def __init__(self, size_x, size_y, blocks):
        pygame.Surface.__init__(self, (size_x, size_y) )

        self.size_x = size_x
        self.size_y = size_y
        self.block_count = 5
        self.blocks = blocks

        self.scale_size = self.size_x/5/self.size_x*1.5

        self.image = pygame.image.load("Assets/fullInvBackground.png")



        #how large the blocks will be in the inventory
    def render(self):
        self.fill("white")
        


        self.blit(self.image, (0, 0))

        for x in range(0, min(len(self.blocks), self.block_count)):
            if self.blocks[x] == 0:
                s = Single(self, 128, self.scale_size)
                s.renderInventory(x*216+89, 89)
            elif self.blocks[x] == 1:
                s = Short_Line_H(self, 128, self.scale_size)
                s.renderInventory(x*216+56, 89)
            elif self.blocks[x] == 2:
                s = Long_Line_H(self, 128, self.scale_size)
                s.renderInventory(x*216+13, 89)
            elif self.blocks[x] == 3:
                s = Short_Line_V(self, 128, self.scale_size)
                s.renderInventory(x*216+89, 56)
            elif self.blocks[x] == 4:
                s = Long_Line_V(self, 128, self.scale_size)
                s.renderInventory(x*216+89, 13)