import pygame
import random


HEIGHT = 720
WIDTH = 1280


# pygame setup
pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
game_over = False
running = True
dt = 0
pygame.display.set_caption("Goudzoeker")
font1 = pygame.font.SysFont('freesanbold.ttf', 50)


class Player:
    def __init__(self):
        self.pos = pygame.Vector2(
            WIDTH / 2,
            HEIGHT / 2
        )
        self.gold = 0
        self.vel = 700
        self.health = 3

    def draw(self):
        self.move()
        pygame.draw.circle(screen, "blue", self.pos, 40)

    def move(self):
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2(0, 0)

        if keys[pygame.K_w] or keys[pygame.K_UP]: direction.y -= 1
        if keys[pygame.K_s] or keys[pygame.K_DOWN]: direction.y += 1
        if keys[pygame.K_a] or keys[pygame.K_LEFT]: direction.x -= 1
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]: direction.x += 1

        if direction.length():
            direction = direction.normalize()

        self.pos += direction * self.vel * dt

        self.pos.x = max(40, min(WIDTH - 40, self.pos.x))
        self.pos.y = max(40, min(HEIGHT - 40, self.pos.y))
    

class Enemy:
    def __init__(self, player_pos):
        self.pos = pygame.Vector2(0, 0)
        self.strenght = 1
        self.respawn(player_pos)

    def respawn(self, player_pos):
        while True:
            new_pos = pygame.Vector2(
                random.randint(45, WIDTH - 45),
                random.randint(45, HEIGHT - 45)
            )
            if new_pos.distance_to(player_pos) > 150:
                self.pos = new_pos
                break

    def draw(self):
        pygame.draw.circle(screen, "red", self.pos, 45)

class Gold:
    def __init__(self):
        self.pos = pygame.Vector2(0, 0)
        self.respawn()
        self.value = 1

    def respawn(self):
        self.pos = pygame.Vector2(
            random.randint(45, WIDTH - 45),
            random.randint(45, HEIGHT - 45)
        )

    def draw(self):
        pygame.draw.circle(screen, "yellow", self.pos, 30)



player = Player()

enemies = [Enemy(player.pos) for _ in range(3)]
gold_coin = Gold()

def redraw_screen():
    global game_over
    screen.fill("black")

    if game_over == True:
        lose = font1.render("Je hebt verloren!", True, (255, 255, 255))
        textRect3 = lose.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        screen.blit(lose, textRect3)
        return

    player.draw()
    gold_coin.draw()

    for enemy in enemies:
        enemy.draw()
        if player.pos.distance_to(enemy.pos) < 85:
            player.health -= enemy.strenght
            enemy.respawn(player.pos)

    if player.pos.distance_to(gold_coin.pos) < 70:
        player.gold += gold_coin.value
        gold_coin.respawn()


    if player.health <= 0:
        game_over = True
        

    text1 = font1.render(f"Goud: {player.gold}", True, (255, 255, 255))
    textRect1 = text1.get_rect()
    textRect1.center = (100, 50)
    
    text2 = font1.render(f"Levens: {player.health}", True, (255, 255, 255))
    textRect2 = text2.get_rect()
    textRect2.center = (110, 100)

    screen.blit(text1, textRect1)
    screen.blit(text2, textRect2)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    redraw_screen()

    pygame.display.flip()

    dt = clock.tick(60) / 1000

pygame.quit()