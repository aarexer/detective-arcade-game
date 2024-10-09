import pygame
import config
import assets
import random


class CollideObject(pygame.sprite.Sprite):
    def __init__(self, cords=None):
        pygame.sprite.Sprite.__init__(self)
        self.collided = False

        if cords is not None:
            self.x_pos = cords[0]
            self.y_pos = cords[1]

        self.image = assets.object_sprites[
            random.randint(
                0, len(assets.object_sprites) - 1
            )
        ].convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)

        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        self.rect.left -= config.OBJECT_PACE

        if self.rect.right <= 0:
            self.rect.left = config.WIDTH + random.randint(80, 500)
            self.image = assets.object_sprites[
                random.randint(
                    0, len(assets.object_sprites) - 1
                )
            ].convert_alpha()
            self.collided = False
