




import pygame
import time

pygame.init()

# Экран
SCREEN_WIDTH, SCREEN_HEIGHT = 1150, 650
display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man Game")

# цвет
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (244, 6, 21)

try:
    bg_sound = pygame.mixer.Sound("music12.mp3")  
    bg_sound.play(-1)  
except pygame.error:
    print() 

# Таймер
player_lives =1  
start_time = time.time()
game_time_limit = 105 # секунд

# карта 
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

TILE_SIZE = 45
player_x, player_y = TILE_SIZE + 5, TILE_SIZE + 5
player_speed = 9

# Сары смайлик
player_image = pygame.image.load("Pac_Man.1.png")
player_image = pygame.transform.scale(player_image, (30, 30))
player_left = pygame.transform.flip(player_image, True, False)
player_right = player_image
player_up = pygame.transform.rotate(player_image, 90)
player_down = pygame.transform.rotate(player_image, -90)


current_player_image = player_right

# стена
walls = []
dots = []
dot_radius = 5

for row_index, row in enumerate(maze):
    for col_index, tile in enumerate(row):
        x, y = col_index * TILE_SIZE, row_index * TILE_SIZE
        if tile == 1:
            walls.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
        elif tile == 0:
            dots.append(pygame.Rect(x + TILE_SIZE // 3, y + TILE_SIZE // 3, dot_radius * 2, dot_radius * 2))

running = True
while running:
    pygame.time.delay(40)
    current_time = time.time()
    elapsed_time = current_time - start_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    next_x, next_y = player_x, player_y

    if keys[pygame.K_LEFT]:
        next_x -= player_speed
        current_player_image = player_left  # Солго карайт
    if keys[pygame.K_RIGHT]:
        next_x += player_speed
        current_player_image = player_right  # Оңго карайт
    if keys[pygame.K_UP]:
        next_y -= player_speed
        current_player_image = player_up  # ойдо
    if keys[pygame.K_DOWN]:
        next_y += player_speed
        current_player_image = player_down  # ылдый

    
    player_rect = pygame.Rect(next_x, next_y, 30, 30)
    collision = False
    for wall in walls:
        if player_rect.colliderect(wall):
            collision = True
            break

    if not collision:
        player_x, player_y = next_x, next_y

    # Тоголокторду жеегендегиси
    player_rect = pygame.Rect(player_x, player_y, 30, 30)
    dots = [dot for dot in dots if not player_rect.colliderect(dot)]

    if len(dots) == 0:
        print("Жеңиш ихуууу!")
        running = False
        continue

    if elapsed_time > game_time_limit:
        player_lives -= 1
        if player_lives > 0:
            start_time = time.time() 
        else:
            print("Утулдуңуз!")
            running = False
            continue

    # Экран
    display.fill(BLACK)
    for wall in walls:
        pygame.draw.rect(display, BLUE, wall)

    # Тоголокторду тартуу
    for dot in dots:
        pygame.draw.ellipse(display, RED, dot)

    # игрок
    display.blit(current_player_image, (player_x, player_y))  # Жашты экранга чыгаруу
    font = pygame.font.SysFont(None, 36)
    lives_text = font.render 

    lives_text = font.render(f"Жаны: {player_lives}", True, (255, 255, 255))
    display.blit(lives_text, (10, 10))
    

    time_left = max(0, game_time_limit - int(elapsed_time))  # Калган убакыт
    timer_text = font.render(f"Убакыт: {time_left} сек", True, (255, 255, 255))
    display.blit(timer_text, (10, 50))


    pygame.display.update()

pygame.quit()