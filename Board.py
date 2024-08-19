import pygame
import math

from Inventory import Inventory
from Blocks import *

class Board(pygame.Surface):
    def __init__(self, pixel_size:int, grid_size:int, inventory:Inventory) -> None:
        pygame.Surface.__init__(self, (pixel_size, pixel_size))

        self.grid_size = grid_size
        self.tiles = []
        self.pixel_size = pixel_size
        self.inventory = inventory
        self.select_structure = []

        # calculate pixel size of tiles
        self.tile_pixel_size = pixel_size/grid_size

        # create a list of Tile objects each with an x and y value
        for y in range(0, grid_size):
            for x in range(0, grid_size):
                t = Tile(self, (x,y), self.tile_pixel_size)
                self.tiles.append(t)

    def render(self,click):
        for tile in self.tiles:
            tile.render(click)

class Tile():
    def __init__(self, surface:pygame.Surface, coordinate:tuple[int,int], pixel_size:int):
        self.surface = surface
        self.coordinate = coordinate
        self.pixel_size = pixel_size
        self.default_image = pygame.transform.scale(pygame.image.load("Assets/InventorySlot.png"), (pixel_size,pixel_size))
        self.hovered_image = pygame.transform.scale(pygame.image.load("Assets/HoverInvSlot.png"), (pixel_size,pixel_size))
        self.real_point = ((1920 - self.surface.pixel_size)/2 + self.coordinate[0] * self.surface.tile_pixel_size + self.surface.tile_pixel_size/2,
                           (1080 - self.surface.pixel_size)/2 + self.coordinate[1] * self.surface.tile_pixel_size)
        self.state = 0 # blank

    def render(self, click):
        if self.isHovered():
            selected_item = self.surface.inventory.selected_tile
            if selected_item != None:
                block_type_index = self.surface.inventory.slots[selected_item].block

                self.surface.select_structure = []
                if block_type_index == 1:
                    for block in Single.structure: 
                        self.surface.select_structure.append([block[0] + self.coordinate[0], block[1] + self.coordinate[1]])
                        image = pygame.transform.scale(Single.image,(self.pixel_size,self.pixel_size))
                elif block_type_index == 2:
                    for block in Short_Line_H.structure: 
                        self.surface.select_structure.append([block[0] + self.coordinate[0], block[1] + self.coordinate[1]])
                        image = pygame.transform.scale(Short_Line_H.image,(self.pixel_size,self.pixel_size))
                elif block_type_index == 3:
                    for block in Long_Line_H.structure: 
                        self.surface.select_structure.append([block[0] + self.coordinate[0], block[1] + self.coordinate[1]])
                        image = pygame.transform.scale(Long_Line_H.image,(self.pixel_size,self.pixel_size))
                elif block_type_index == 4:
                    for block in Short_Line_V.structure: 
                        self.surface.select_structure.append([block[0] + self.coordinate[0], block[1] + self.coordinate[1]])
                        image = pygame.transform.scale(Short_Line_V.image,(self.pixel_size,self.pixel_size))
                elif block_type_index == 5:
                    for block in Long_Line_V.structure: 
                        self.surface.select_structure.append([block[0] + self.coordinate[0], block[1] + self.coordinate[1]])
                        image = pygame.transform.scale(Long_Line_V.image,(self.pixel_size,self.pixel_size))
            else:
                image = self.hovered_image

            if click and self.state == 0:
                self.state = block_type_index
                    
        elif [self.coordinate[0], self.coordinate[1]] in self.surface.select_structure or self.state != 0:
            selected_item = self.surface.inventory.selected_tile
            if self.state != 0:
                block_type_index = self.state
            else:
                block_type_index = self.surface.inventory.slots[selected_item].block

            if block_type_index == 1:
                image = pygame.transform.scale(Single.image,(self.pixel_size,self.pixel_size))
            elif block_type_index == 2:
                image = pygame.transform.scale(Short_Line_H.image,(self.pixel_size,self.pixel_size))
            elif block_type_index == 3:
                image = pygame.transform.scale(Long_Line_H.image,(self.pixel_size,self.pixel_size))
            elif block_type_index == 4:
                image = pygame.transform.scale(Short_Line_V.image,(self.pixel_size,self.pixel_size))
            elif block_type_index == 5:
                image = pygame.transform.scale(Long_Line_V.image,(self.pixel_size,self.pixel_size))

            if click and self.state == 0:
                self.state = block_type_index
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