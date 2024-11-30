
import pygame
pygame.init()
clock = pygame.time.Clock()

display = pygame.display.set_mode((650, 721))
pygame.display.set_caption("Okurmen_Team_GAME!")
icon = pygame.image.load("game/icon2.png")
pygame.display.set_icon(icon)

# фон
background = pygame.image.load('game/game fon 1.jpg')

# игрок
walk = [
    pygame.image.load('game/Pac_Man.1.png').convert_alpha()
]




player_anim_count = 0

# передвижение игрока
player_speed = 5
player_x = 45
player_y = 20

# музыка
bg_sound = pygame.mixer.Sound("game/music12.mp3")
bg_sound.play()





running = True
while running:
    display.blit(background, (0, 0))
    display.blit(walk[player_anim_count], (player_x, player_y))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and player_x - player_speed > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x + player_speed < 650 - walk[0].get_width():
        player_x += player_speed
    if keys[pygame.K_UP] and player_y - player_speed > 0:
        player_y -= player_speed
    if keys[pygame.K_DOWN] and player_y + player_speed < 721 - walk[0].get_height():
        player_y += player_speed
   


    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    clock.tick(20)

pygame.quit()




