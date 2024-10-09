import os
import pygame

object_sprites = []

path = os.path.join('assets', 'sprites', 'object')
for file in os.listdir(path):
    object_sprites.append(pygame.image.load(os.path.join(path, file)))

hero_sprite = pygame.image.load(
    os.path.join('assets', 'sprites', 'hero.png')
)

background_sprite = pygame.image.load(
    os.path.join('assets', 'sprites', 'background.png')
)

heart_sprite = pygame.image.load(
    os.path.join('assets', 'sprites', 'heart.gif')
)
