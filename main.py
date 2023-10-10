import pygame as pg, sys
import random

# Sprites
class Crosshair(pg.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()


        self.gunshot1 = pg.mixer.Sound('sounds/gunshot_1.mp3')
        self.gunshot2 = pg.mixer.Sound('sounds/gunshot_2.mp3')

    def shoot(self):
        self.gunshots = [self.gunshot1, self.gunshot2]
        gunshot = random.choice(self.gunshots)

        if gunshot == self.gunshot1:
            self.gunshot1.play()
        else:
            self.gunshot2.play()

        pg.sprite.spritecollide(crosshair, target_group, True)

    def update(self):
        self.rect.center = pg.mouse.get_pos()


class Target(pg.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

# Settings
pg.init()
clock = pg.time.Clock()

# Screen
screen_width = 1280
screen_height = 720

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Skeet Shooter')

background = pg.image.load('sprites/bg.png')

pg.mouse.set_visible = False

# Crosshair
crosshair = Crosshair('sprites/crosshair.png')
crosshair_group = pg.sprite.Group()
crosshair_group.add(crosshair)

# Targets
target_group = pg.sprite.Group()
for target in range(20):
    new_target = Target('sprites/target_1.png', random.randrange(0, screen_width), random.randrange(0, screen_height))
    target_group.add(new_target)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN:
            crosshair.shoot()

    pg.display.flip()

    for x in range(0, 1280, 230):
        for y in range(0, 720, 256):
            screen.blit(background, (x, y))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()
    clock.tick(60)
