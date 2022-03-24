import pygame, os, random

class Tile(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, ):
        super().__init__()

        self.name = filename.split('.')[0]

        self.original_image = pygame.transform.smoothscale(pygame.image.load('pics/cards/' + filename), (64, 64))

        self.back_image = pygame.transform.smoothscale(pygame.image.load('pics/cards/' + filename), (64, 64))
        pygame.draw.rect(self.back_image, (255, 255, 255), self.back_image.get_rect())

        self.image = self.back_image
        self.rect = self.image.get_rect(topleft = (x, y))
        self.shown = False

    def update(self):
        self.image = self.original_image if self.shown else self.back_image

    def show(self):
        self.shown = True
        
    def hide(self):
        self.shown = False