import pygame
import config
from hero import Hero
from collide_object import CollideObject
import assets
import os

pygame.init()

font = pygame.font.Font(os.path.join('assets', 'fonts', 'prstartk.ttf'), 15)
font_collide = pygame.font.Font(
    os.path.join(
        'assets',
        'fonts',
        'prstartk.ttf'
    ),
    50
)

screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
clock = pygame.time.Clock()

score = 0
score_surface = font.render(f'Score: {score}', True, 'White')

back = assets.background_sprite.convert()
text_collide = font_collide.render('Collide', False, 'Red')
heart = assets.heart_sprite.convert_alpha()

pygame.display.set_caption('Simple Arcade Game')

hero = Hero((75, config.HEIGHT / 2))
collision_objects = [
    CollideObject((config.WIDTH + 100, 200)),
    CollideObject((config.WIDTH + 200, 345)),
    CollideObject((config.WIDTH + 400, 70))
]

time_delay = 1000
SCORE_INCREMENT_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(SCORE_INCREMENT_EVENT, time_delay)

COLLIDE_INFO_EVENT = pygame.USEREVENT + 2

is_game = True
while is_game:
    screen.blit(back, (0, 0))
    screen.blit(hero.image, hero.rect)
    screen.blit(score_surface, (350, 10))

    heart_font = font.render(f'{hero.health}', True, 'White')
    screen.blit(heart_font, (750, 18))
    screen.blit(heart, (770, 15))

    if hero.health <= 0:
        screen.blit(font_collide.render('GAMEOVER!', False, 'Red'), (200, 165))
        is_game = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_game = False
            pygame.quit()

        if event.type == SCORE_INCREMENT_EVENT:
            score += 1
            score_surface = font.render(f'Score: {score}', True, 'White')

        if event.type == COLLIDE_INFO_EVENT and hero.health > 0:
            screen.blit(text_collide, (200, 165))

        hero.handle_event(event)

    for col_obj in collision_objects:
        screen.blit(col_obj.image, col_obj.rect)
        col_obj.update()

    if hero.has_collisions(collision_objects):
        pygame.time.set_timer(COLLIDE_INFO_EVENT, 1, 500)
        heart_font = font.render(f'{hero.health}', True, 'White')

    pygame.display.update()

    clock.tick(config.FPS)

pygame.time.delay(1000)
pygame.quit()
