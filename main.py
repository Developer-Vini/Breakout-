import pygame
import sys 

pygame.font.init()
pygame.init()

size_screen = (800, 600)

finished_game = False
game_won = False
score = 0
moviment_ball = [7, -7]

colors = {
    "white": (255,255,255),
    "black": (0,0,0),
    "yellow": (255,255,0),
    "blue": (0,0,255),
    "green": (0,255,0)
}

game_font = pygame.font.SysFont("Arial", 24)
title_font = pygame.font.SysFont("Arial", 50, bold = True)

screen = pygame.display.set_mode(size_screen)
pygame.display.set_caption("Breakout")

ball_size = 15
player_size = 100

line_block = 5
block_line = 8

player_speed = 10

all_bloc = block_line * line_block

ball = pygame.Rect(100, 500, ball_size, ball_size)
player = pygame.Rect(350, 550, player_size, 15)


def draw_text(text, font, color, x, y, center = False):
    text_sufarce = font.render(text, True, color)
    text_rect = text_sufarce.get_rect()

    if center: 
        text_rect.center = (x ,y)
    else:
        text_rect.topleft = (x,y)
    screen.blit(text_sufarce, text_rect)

def create_blocks(block_line, line_block):

    blocks_list = []

    distance = 5

    screen_h = size_screen[1]
    screen_w = size_screen[0]

    distance_per_blocks = 5

    w_block = (size_screen[0] - (block_line + 1) * distance) / block_line
    h_block = 15
    distance_per_blocks = h_block + 10

    for j in range(line_block):
        for i in range(block_line):
            x = distance + i * (w_block + distance)
            y = distance + j * (h_block + distance)
            block = pygame.Rect(x, y, w_block, h_block)

            blocks_list.append(block)
    return blocks_list


blocks = create_blocks(block_line, line_block)
def draw_game():
    screen.fill(colors["black"])
    pygame.draw.rect(screen, colors["green"], player)
    pygame.draw.rect(screen, colors["yellow"], ball)
    for block in blocks:
        pygame.draw.rect(screen, colors["blue"], block)

    draw_text(f"Score: {score}", game_font, colors["white"], 15, 15)

    if game_won:
        draw_text(f"WIN GAME", title_font, colors["green"], 400, 250, center = True)
        draw_text(f"Final Score: {score}", game_font, colors["white"], 400, 320, center = True)
clock = pygame.time.Clock()

while not finished_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished_game = True

    if not game_won:

        keys = pygame.key.get_pressed()
        if(keys[pygame.K_LEFT] or keys[pygame.K_a]) and player.left > 0:
            player.x -= player_speed
        if(keys[pygame.K_RIGHT] or keys[pygame.K_d]) and player.right < size_screen[0]:
            player.x += player_speed

        ball.x += moviment_ball[0]
        ball.y += moviment_ball[1]

        if ball.left <= 0 or ball.right >= size_screen[0]:
            moviment_ball[0] = -moviment_ball[0]

        if ball.top <= 0:
            moviment_ball[1] = -moviment_ball[1]

        if ball.bottom >= size_screen[1]:
            ball.x = 400
            ball.y = 400
            moviment_ball = [7, -7]


        if ball.colliderect(player):
            moviment_ball[1] = -moviment_ball[1]
            ball.bottom = player.top

        for block in blocks: 
            if ball.colliderect(block):
                blocks.remove(block)
                moviment_ball[1] = -moviment_ball[1]
                score += 10
                break
        if len(blocks) == 0:
            game_won = True

    draw_game()
    clock.tick(60)
    pygame.display.flip()

pygame.quit()
sys.exit()