import os
import pygame

sprites = {}

def load_sprites():
    path = "C:\\Users\\nesxr\\Documents\\GitHub\\Games\\flappy_bird\\assets\\sprites"
    for file in os.listdir(path):
        sprites[file.split('.')[0]] = pygame.image.load(os.path.join(path, file))

def get_sprite(name):
    return sprites[name]