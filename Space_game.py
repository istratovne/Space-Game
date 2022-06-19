import pygame as pg
from gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats
from scores import Scores

FPS = 120
clock = pg.time.Clock()


def run():
    pg.init()
    screen = pg.display.set_mode((700, 800))
    pg.display.set_caption('Space defenders')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    aliens = Group()
    lives = Group()
    controls.create_army(screen, aliens)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update(bg_color, screen, stats, sc, gun, lives, aliens, bullets)
            controls.update_bullets(screen, stats, sc, lives, aliens, bullets)
            controls.update_aliens(stats, screen, sc, gun, lives, aliens, bullets)
            clock.tick(FPS)


run()
