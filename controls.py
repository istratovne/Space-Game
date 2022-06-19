import pygame as pg
import sys
from bullet import Bullet
from alien import Alien
import time


def events(screen, gun, bullets):
    """"обработка событий"""
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_d:
                gun.mright = True
            elif event.key == pg.K_a:
                gun.mleft = True
            elif event.key == pg.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pg.KEYUP:
            if event.key == pg.K_d:
                gun.mright = False
            elif event.key == pg.K_a:
                gun.mleft = False


def update(bg_color, screen, stats, sc, gun, lives, alien, bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    alien.draw(screen)
    pg.display.flip()


def update_bullets(screen, stats, sc, lives, aliens, bullets):
    """обновление позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pg.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += 10 * len(aliens)
        sc.image_score()
        check_highscore(stats, sc)
        sc.image_lives()
    if len(aliens) == 0:
        bullets.empty()
        create_army(screen, aliens)
        time.sleep(1)


def gun_kill(stats, screen, sc, gun, lives, aliens, bullets):
    """столкновение армии с пушкой"""
    if stats.lives_left > 1:
        stats.lives_left -= 1
        sc.image_lives()
        aliens.empty()
        bullets.empty()
        create_army(screen, aliens)
        gun.create_gun()
        time.sleep(1)
    else:
        stats.run_game = False
        gameover()


def update_aliens(stats, screen, sc, gun, lives, aliens, bullets):
    """обновление позиции пришельцев"""
    aliens.update()
    if pg.sprite.spritecollideany(gun, aliens):
        gun_kill(stats, screen, sc, gun, lives, aliens, bullets)
    aliens_check(stats, screen, sc, gun, lives, aliens, bullets)


def aliens_check(stats, screen, sc, gun, lives, aliens, bullets):
    """проверка края экрана"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, sc, gun, lives, aliens, bullets)
            break


def create_army(screen, aliens):
    """создание арммии пришельцев"""
    alien = Alien(screen)
    alien_width = alien.rect.width
    number_alien_x = int((700 - 2 * alien_width) / alien_width)
    alien_height = alien.rect.height
    number_alien_y = int((800 - 100 - 2 * alien_height) / alien_height)

    for row_number in range(number_alien_y - 3):
        for alien_number in range(number_alien_x):
            alien = Alien(screen)
            alien.x = alien_width + (alien_width * alien_number)
            alien.y = alien_height + (alien_height * row_number)
            alien.rect.x = alien.x
            alien.rect.y = alien.rect.height + (alien.rect.height * row_number)
            aliens.add(alien)


def check_highscore(stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.highscore:
        stats.highscore = stats.score
        sc.image_highscore()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.highscore))


def gameover():
    screen = pg.display.set_mode((700, 800))
    screen.fill((0, 0, 0))
    f1 = pg.font.Font(None, 150)
    text1 = f1.render('GAME OVER', 1, (250, 0, 0))
    screen.blit(text1, (35, 400))
    pg.display.update()
