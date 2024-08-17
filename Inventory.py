import pygame
import math

from Blocks import *

class Inventory(pygame.Surface):
    def __init__(self, size_x, blocks):
        self.size_x = size_x
        self.blocks = blocks
        self.inv_tile_count = len(self.blocks)
        self.scale_size = self.size_x/5/self.size_x*1.5
        self.tile_size = size_x/self.inv_tile_count
        
        self.slots = []

        pygame.Surface.__init__(self, (size_x, self.tile_size) )

        for i in range(self.inv_tile_count):
            slot = InventorySlot(self, (i * self.tile_size, 0), self.tile_size, i, self.blocks[i], size_x)
            self.slots.append(slot)

    def render(self, click):
        for slot in self.slots: slot.render(click)

class InventorySlot():
    def __init__(self, surface:pygame.Surface, coordinate:tuple[int,int], pixel_size:int, index:int, block:int, inventory_length:int):
        self.surface = surface
        self.coordinate = coordinate
        self.real_point = ((1920 - inventory_length)/2 + self.coordinate[0] + pixel_size/2, 820 + pixel_size/2)
        self.pixel_size = pixel_size
        self.default_image = pygame.transform.scale(pygame.image.load("Assets/InventorySlot.png"), (self.pixel_size,self.pixel_size))
        self.hovered_image = pygame.transform.scale(pygame.image.load("Assets/HoverInvSlot.png"), (self.pixel_size,self.pixel_size))
        self.index = index
        self.block = block
        self.scale_size = 0.25

    def render(self,click):
        if self.isHovered():
            image = self.hovered_image
        else:
            image = self.default_image

        if self.block == 0:
            pass
        elif self.block == 1:
            s = Single(image, 128, self.scale_size)
            s.renderInventory((self.pixel_size - s.pixel_size)/2, (self.pixel_size - s.pixel_size)/2)
        elif self.block == 2:
            s = Short_Line_H(image, 128, self.scale_size)
            s.renderInventory((self.pixel_size - s.pixel_size)/2, (self.pixel_size - s.pixel_size)/2)
        elif self.block == 3:
            s = Long_Line_H(image, 128, self.scale_size)
            s.renderInventory((self.pixel_size - s.pixel_size)/2, (self.pixel_size - s.pixel_size)/2)
        elif self.block == 4:
            s = Short_Line_V(image, 128, self.scale_size)
            s.renderInventory((self.pixel_size - s.pixel_size)/2, (self.pixel_size - s.pixel_size)/2)
        elif self.block == 5:
            s = Long_Line_V(image, 128, self.scale_size)
            s.renderInventory((self.pixel_size - s.pixel_size)/2, (self.pixel_size - s.pixel_size)/2)
    
        self.surface.blit(image, self.coordinate)

        if self.isClicked(click):
            self.surface.slots[self.index] = InventorySlot(self.surface, (self.index * self.surface.tile_size, 0), self.surface.tile_size, self.index, 0, self.surface.size_x)


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
