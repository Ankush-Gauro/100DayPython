import pygame

import random

import math



# Initialize Pygame

pygame.init()



# Screen setup

WIDTH, HEIGHT = 800, 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Invaders")



# Load images

player_img = pygame.image.load("player.png")  # spaceship

enemy_img = pygame.image.load("enemy.png")

bullet_img = pygame.image.load("bullet.png")



# Player

player_x = 370

player_y = 480

player_speed = 5



# Enemy

enemy_x = []

enemy_y = []

enemy_speed = []

enemy_count = 6



for _ in range(enemy_count):

    enemy_x.append(random.randint(0, 735))

    enemy_y.append(random.randint(50, 150))

    enemy_speed.append([3, 40])  # x-speed and drop distance



# Bullet

bullet_x = 0

bullet_y = player_y

bullet_speed = 10

bullet_state = "ready"  # "ready" = can fire, "fire" = in motion



# Score

score = 0

font = pygame.font.Font(None, 36)



# Collision detection

def is_collision(x1, y1, x2, y2):

    return math.hypot(x2 - x1, y2 - y1) < 27



# Game loop

running = True

while running:

    screen.fill((0, 0, 30))  # Dark background



    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False



    # Movement

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x > 0:

        player_x -= player_speed

    if keys[pygame.K_RIGHT] and player_x < WIDTH - 64:

        player_x += player_speed

    if keys[pygame.K_SPACE] and bullet_state == "ready":

        bullet_x = player_x + 16

        bullet_state = "fire"



    # Bullet movement

    if bullet_state == "fire":

        screen.blit(bullet_img, (bullet_x, bullet_y))

        bullet_y -= bullet_speed

        if bullet_y <= 0:

            bullet_y = player_y

            bullet_state = "ready"



    # Enemy movement

    for i in range(enemy_count):

        enemy_x[i] += enemy_speed[i][0]

        if enemy_x[i] <= 0 or enemy_x[i] >= WIDTH - 64:

            enemy_speed[i][0] *= -1

            enemy_y[i] += enemy_speed[i][1]



        # Collision

        if is_collision(enemy_x[i], enemy_y[i], bullet_x, bullet_y):

            bullet_y = player_y

            bullet_state = "ready"

            score += 1

            enemy_x[i] = random.randint(0, 735)

            enemy_y[i] = random.randint(50, 150)



        screen.blit(enemy_img, (enemy_x[i], enemy_y[i]))



    # Draw player

    screen.blit(player_img, (player_x, player_y))



    # Score

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))

    screen.blit(score_text, (10, 10))



    pygame.display.update()

