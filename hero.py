import pygame
from collide_object import CollideObject
import config
import assets


class Hero(pygame.sprite.Sprite):
    health = 5

    def __init__(self, cords=None):
        pygame.sprite.Sprite.__init__(self)

        if cords is not None:
            self.x_pos = cords[0]
            self.y_pos = cords[1]

        self.image = assets.hero_sprite.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def handle_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and self.rect.top > 0:
            self.rect.top -= config.HERO_STEP

        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and self.rect.bottom < config.HEIGHT:
            self.rect.top += config.HERO_STEP

    def has_collisions(self, collision_objects: list[CollideObject]):
        for obj in collision_objects:
            if not obj.collided and self.mask.overlap(obj.mask, (self.rect.x - obj.rect.x, self.rect.y - obj.rect.y)):
                obj.collided = True
                self.health -= 1

                return True

        return False
