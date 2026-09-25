import pygame
import sys

SIZE = 500
GRID_SIZE = 50

pygame.init()
pygame.font.init()
font = pygame.font.SysFont("FreeSans", 36)
screen = pygame.display.set_mode((SIZE, SIZE))
clock = pygame.time.Clock()
pygame.display.set_caption("Super coole TD game")
# timestep = 500

red = (255,0,0)

class enemy:
    def __init__(self, start_point, path_cords):
        self.health = 3
        self.speed = 2
        self.path_tracker = path_cords
        self.pos = self.path_tracker.index(start_point)

    def move(self):
        self.pos += self.speed
        self.pos = min(self.pos, len(self.path_tracker) - 1)

    def draw(self, screen):
        gx, gy = self.path_tracker[self.pos]
        pygame.draw.circle(screen, (255, 0, 0),
                           (gx * GRID_SIZE + GRID_SIZE // 2,
                            gy * GRID_SIZE + GRID_SIZE // 2), 20)

    def take_damage(self):
        self.health -= 1
class player:
    def __init__(self):
        self.money = 100
        self.health = 10


dt = 0
running = True

path_cords = [
    (0, 5), (1, 5), (2, 5), (3, 5), 
    (3, 4), (3, 3), (4, 3), (5, 3), 
    (5, 4), (5, 5), (6, 5), (7, 5),
    (8,5), (9,5)
]

tower = []
enemys = [(0,5) for _ in range(5) ] 
enemy_objs = [enemy(start, path_cords) for start in enemys]

def redraw_window():

    #tekenen
    screen.fill("green")


    # teken grid lines
    for x in range(0, SIZE, GRID_SIZE):
        for y in range(0, SIZE, GRID_SIZE):
            rect = pygame.Rect(x, y, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, (0,0,0), rect, 1)

    #teken path
    for p in path_cords:
        rect = pygame.Rect(p[0] * GRID_SIZE, p[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, "gray", rect)
    #teken tower
    for t in tower:
        rect = pygame.Rect(t[0] * GRID_SIZE, t[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(screen, "blue", rect)

    for e in enemy_objs:
        e.draw(screen)
        e.move()
        
        


while running:

    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #pixelcords van de click
            pixel_x, pixel_y = pygame.mouse.get_pos()
            #maak gridcords van de pixels
            grid_x = pixel_x // GRID_SIZE
            grid_y = pixel_y // GRID_SIZE

            clicked_pos = (grid_x, grid_y)


            if clicked_pos not in path_cords and clicked_pos not in tower:
                tower.append(clicked_pos)

    redraw_window()
    pygame.display.flip()


    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()