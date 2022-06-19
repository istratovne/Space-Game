import pygame.font
from gun import Gun
from life import Life
from pygame.sprite import Group
import pygame.image


class Scores():
    """Вывод игровой информации"""

    def __init__(self, screen, stats):
        """инициализация подсчета очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (250, 250, 250)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_highscore()
        self.image_lives()

    def image_score(self):
        """приобразование текста счёта в графическое изображение"""
        self.score_img = self.font.render(str(self.stats.score),
                                          True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def image_highscore(self):
        """преобразование рекорда в графическое изображение"""
        self.highscore_img = self.font.render(str(self.stats.highscore),
                                              True, self.text_color, (0, 0, 0))
        self.highscore_rect = self.highscore_img.get_rect()
        self.highscore_rect.centerx = self.screen_rect.centerx
        self.highscore_rect.top = self.screen_rect.top + 20

    def image_lives(self):
        """количество жизней"""
        self.lives = Group()
        for life_number in range(self.stats.lives_left):
            life = Life(self.screen)
            life.rect.x = 15 + life_number * life.rect.width
            life.rect.y = 20
            self.lives.add(life)

    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.highscore_img, self.highscore_rect)
        self.lives.draw(self.screen)


