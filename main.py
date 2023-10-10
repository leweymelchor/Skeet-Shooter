import pygame as pg, sys

pg.init()

clock = pg.time.Clock()

screen_width = 1920
screen_height = 1080

screen = pg.display.set_mode((screen_width, screen_height))
pg.display.set_caption('Name Here')


while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    screen.fill((0,0,0))
    pg.display.flip()
    clock.tick(60)
