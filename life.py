import pygame as pg
from pygame.sprite import Sprite

class Life(Sprite):

    def __init__(self, screen):
        super(Life, self).__init__()
        self.screen = screen
        self.image = pg.image.load('assets\heart.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

    def draw(self):
        self.screen.blit(self.image, self.rect)
