import pygame as pg

class Alien(pg.sprite.Sprite):
    """класс одного пришельца"""

    def __init__(self, screen):
        """инициализация и задание начальной позиции"""
        super(Alien, self).__init__()
        self.screen = screen
        self.image = pg.image.load('assets/alien.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def draw(self):
        """вывод пришельца на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещение пришельцев"""
        self.y += 0.1
        self.rect.y = self.y

        
