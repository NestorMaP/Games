import pygame

import sys
sys.path.append("C:\\Users\\nesxr\\Documents\\GitHub\\Games\\flappy_bird")

import assets
import configs

class Background(pygame.sprite.Sprite):
    def __init__(self, index, *groups):

        super().__init__(*groups)

        self.image = assets.get_sprite("background")
        self.rect = self.image.get_rect(topleft=(configs.SCREEN_WIDTH*index,0))

    def update(self):
        self.rect.x -= 2

        if self.rect.right <= 0:
            self.rect.x = configs.SCREEN_WIDTH