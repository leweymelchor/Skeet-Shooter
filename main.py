import pygame as pg, sys
import random
from fire import Fire

# Sprites
class Crosshair(pg.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()

        self.gunshot1 = pg.mixer.Sound('sounds/gunshot1.mp3')
        self.gunshot2 = pg.mixer.Sound('sounds/gunshot2.mp3')
        self.gunshot3 = pg.mixer.Sound('sounds/gunshot3.mp3')
        self.gunshot4 = pg.mixer.Sound('sounds/gunshot4.mp3')
        self.gunshot5 = pg.mixer.Sound('sounds/gunshot5.mp3')
        self.gunshot6 = pg.mixer.Sound('sounds/gunshot6.mp3')

    def shoot(self):
        self.gunshots = [self.gunshot1, self.gunshot2, self.gunshot3,
                        self.gunshot4, self.gunshot5, self.gunshot6]
        gunshot = random.choice(self.gunshots)

        if gunshot == self.gunshot1:
            self.gunshot1.play()
        elif gunshot == self.gunshot2:
            self.gunshot2.play()
        elif gunshot == self.gunshot3:
            self.gunshot3.play()
        elif gunshot == self.gunshot4:
            self.gunshot4.play()
        elif gunshot == self.gunshot5:
            self.gunshot5.play()
        elif gunshot == self.gunshot6:
            self.gunshot6.play()

        if pg.sprite.spritecollide(crosshair, target_group, True):
            pg.time.delay(25)
            new_target.hit()
            fire_blast.draw(screen)
            fire_blast.update()

    def update(self):
        self.rect.center = pg.mouse.get_pos()

class Gun(pg.sprite.Sprite):
    def __init__(self, picture_path):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.topleft = pg.mouse.get_pos()

class Target(pg.sprite.Sprite):
    def __init__(self, picture_path, pos_x, pos_y):
        super().__init__()
        self.image = pg.image.load(picture_path)
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        self.hit1 = pg.mixer.Sound('sounds/hit1.wav')
        self.hit2 = pg.mixer.Sound('sounds/hit2.wav')
        self.hit3 = pg.mixer.Sound('sounds/hit3.wav')
        self.hit4 = pg.mixer.Sound('sounds/hit4.wav')
        self.hit5 = pg.mixer.Sound('sounds/hit5.wav')
        self.hit6 = pg.mixer.Sound('sounds/hit6.wav')

    def hit(self):
        self.hits = [self.hit1, self.hit2, self.hit3, self.hit4, self.hit5, self.hit6]
        hit_sound = random.choice(self.hits)

        if hit_sound == self.hit1:
            self.hit1.play()
        elif hit_sound == self.hit2:
            self.hit2.play()
        elif hit_sound == self.hit3:
            self.hit3.play()
        elif hit_sound == self.hit4:
            self.hit4.play()
        elif hit_sound == self.hit5:
            self.hit5.play()
        elif hit_sound == self.hit6:
            self.hit6.play()

class GameState():
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                crosshair.shoot()
                new_target.hit()
                self.state = 'main_game'

        pg.display.flip()

        for x in range(0, 1280, 230):
            for y in range(0, 720, 256):
                screen.blit(background, (x, y))
        screen.blit(ready, (screen_width // 2 - 115, screen_height // 2 - 33))

        crosshair_group.draw(screen)
        crosshair_group.update()
        gun_group.draw(screen)
        gun_group.update()

    def main_game(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                crosshair.shoot()

        for x in range(0, 1280, 230):
            for y in range(0, 720, 256):
                screen.blit(background, (x, y))

        target_group.draw(screen)
        print(target_group)
        crosshair_group.draw(screen)
        crosshair_group.update()
        gun_group.draw(screen)
        gun_group.update()

        if not target_group:
            self.state = 'intro'

        pg.display.flip()

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()


# Settings
pg.init()
clock = pg.time.Clock()
game_state = GameState()

# Screen
screen_width = 1280
screen_height = 720

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Skeet Shooter')

background = pg.image.load('sprites/bg.png')
ready = pg.image.load('images/ready.png')

pg.mouse.set_visible = False

# Crosshair
crosshair = Crosshair('sprites/crosshair.png')
crosshair_group = pg.sprite.Group()
crosshair_group.add(crosshair)

# Gun
gun = Gun('sprites/rifle.png')
gun_group = pg.sprite.Group()
gun_group.add(gun)

# Targets
target_group = pg.sprite.Group()
for target in range(20):
    new_target = Target('sprites/target_1.png', random.randrange(0, screen_width),
                        random.randrange(0, screen_height))
    target_group.add(new_target)

fire_blast = pg.sprite.Group()
fire = Fire((screen_width // 2) + 50, (screen_height // 2) - 50)
fire_blast.add(fire)

while True:
    game_state.state_manager()
    clock.tick(60)
