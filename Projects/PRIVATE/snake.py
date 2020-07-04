import pygame as pg
from random import randrange

RES = 800
SIZE = 20

x, y = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
dirs = {'W': True, 'A': True, 'S': True, 'D': True}

lenght = 1
snake = [(x, y)]
dx, dy = 0, 0
score = 0
fps = 10

pg.init()
screen = pg.display.set_mode([RES, RES])
clock = pg.time.Clock()
font_score = pg.font.SysFont('Arial', 26, bold=True)
font_end = pg.font.SysFont('Arial', 66, bold=True)

while True:
    screen.fill(pg.Color('black'))
    [(pg.draw.rect(screen, pg.Color('green'), (i, j, SIZE - 2, SIZE - 2))) for i, j in snake]
    pg.draw.rect(screen, pg.Color('red'), (*apple, SIZE, SIZE))

    render_score = font_score.render(f'SCORE: {score}', 1, pg.Color('orange'))
    screen.blit(render_score, (5, 5))

    x += dx * SIZE
    y += dy * SIZE
    snake.append((x, y))
    snake = snake[-lenght:]

    if snake[-1] == apple:
        apple = randrange(0, RES, SIZE), randrange(0, RES, SIZE)
        lenght += 1
        score += 1
        fps += 0.1

    if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
        while True:
            render_end = font_end.render('GAME OVER', 1, pg.Color('orange'))
            screen.blit(render_end, (RES // 2 - 200, RES // 3))
            pg.display.flip()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()

    pg.display.flip()
    clock.tick(fps)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()

    key = pg.key.get_pressed()
    if key[pg.K_w] and dirs['W']:
        dx, dy = 0, -1
        dirs = {'W': True, 'A': True, 'S': False, 'D': True}
    if key[pg.K_a] and dirs['A']:
        dx, dy = -1, 0
        dirs = {'W': True, 'A': True, 'S': True, 'D': False}
    if key[pg.K_s] and dirs['S']:
        dx, dy = 0, 1
        dirs = {'W': False, 'A': True, 'S': True, 'D': True}
    if key[pg.K_d] and dirs['D']:
        dx, dy = 1, 0
        dirs = {'W': True, 'A': False, 'S': True, 'D': True}
