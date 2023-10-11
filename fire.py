# Player Class
import pygame as pg

class Fire(pg.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.sprites = []
        self.is_animating = False
        self.sprites.append(pg.image.load('sprites/shot1.png'))
        self.sprites.append(pg.image.load('sprites/shot2.png'))

        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]

        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

    def animate(self):
        self.is_animating = True


    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.2

            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False

            self.image = self.sprites[int(self.current_sprite)]
