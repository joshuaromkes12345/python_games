import pygame as pg
from random import randrange

pg.init()
WINDOW = 900
TILE_SIZE = 45
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)
get_random_position = lambda: [randrange(*RANGE), randrange(*RANGE)]
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()
lenght = 1
segment = [snake.copy()]
snake_dir =  (0, 0)
time = 0
time_step = 110
food = snake.copy()
food.center = get_random_position()
screen = pg.display.set_mode([WINDOW] * 2)
clock = pg.time.Clock()
dirs = {pg.K_w: 1,pg.K_a: 1,pg.K_s: 1,pg.K_d: 1,}
pg.display.set_caption('snake game in python')
score = 0
font = pg.font.Font('freesansbold.ttf', 32)
pygame_icon = pg.image.load("snake.png")
pg.display.set_icon(pygame_icon)
BG = pg.image.load("grass.png")

music = pg.mixer.music.load("music.wav")
pg.mixer.music.play(-1)
pg.mixer.music.set_volume(0.1)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:
                snake_dir = (0, - TILE_SIZE)
                dirs = {pg.K_w: 1,pg.K_a: 1,pg.K_s: 1,pg.K_d: 1,}
            if event.key == pg.K_s and dirs[pg.K_s]:
                snake_dir = (0, TILE_SIZE)
                dirs = {pg.K_w: 1,pg.K_a: 1,pg.K_s: 1,pg.K_d: 1,}
            if event.key == pg.K_a and dirs[pg.K_a]:
                snake_dir = (-TILE_SIZE, 0)
                dirs = {pg.K_w: 1,pg.K_a: 1,pg.K_s: 1,pg.K_d: 1,}
            if event.key == pg.K_d and dirs[pg.K_d]:
                snake_dir = (TILE_SIZE, 0)
                dirs = {pg.K_w: 1,pg.K_a: 1,pg.K_s: 1,pg.K_d: 1,}
    screen.blit(BG, (0,0))

    self_eating = pg.Rect.collidelist(snake, segment[:-1]) != -1
    if snake.left < 0 or snake.right > WINDOW or snake.top < 0 or snake.bottom > WINDOW or self_eating:
        snake.center, food.center = get_random_position(), get_random_position()
        lenght, snake_dir = 1, (0, 0)
        score = 0
        segment = [snake.copy()]
        
    if snake.center == food.center:
        food.center = get_random_position()
        lenght += 1
        score = score + 1

    text = font.render('Score: ' + str(score) ,True, 'white')
    screen.blit(text,(375, 20))
    pg.draw.rect(screen, 'red', food)
    [pg.draw.rect(screen, 'blue', segment) for segment in segment]

    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segment.append(snake.copy())
        segment = segment = segment[-lenght:]
    pg.display.flip()
    clock.tick(60)