import pygame as pg

class Bullet(pg.sprite.Sprite):

    def __init__(self, screen, gun):
        """создание пули в позиции пушки"""
        super(Bullet, self).__init__()
        self.screen = screen
        self.rect = pg.Rect(0, 0, 2, 12)
        self.color = 255, 203, 14
        self.speed = 4.5
        self.rect.centerx = gun.rect.centerx
        self.rect.top = gun.rect.top
        self.y = float(self.rect.y)

    def update(self):
        """перемещение пули вверх"""
        self.y -= self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """отрисовка на экране"""
        pg.draw.rect(self.screen, (255, 203, 14), self.rect)
