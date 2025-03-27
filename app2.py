import pygame
import random

# Pygameの初期化
pygame.init()

# 画面のサイズ
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Breaker")

# 色の定義
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# ボールの初期設定
ball_radius = 10
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = 3
ball_dy = -3

# パドルの設定
paddle_width = 100
paddle_height = 15
paddle_x = (WIDTH - paddle_width) // 2
paddle_y = HEIGHT - paddle_height - 10
paddle_speed = 5

# ブロックの設定
block_width = 60
block_height = 20
blocks = []
for row in range(5):
    for col in range(WIDTH // block_width):
        block_x = col * block_width
        block_y = row * block_height + 50
        blocks.append(pygame.Rect(block_x, block_y, block_width, block_height))

# ゲームループ
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # キー入力の処理
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_x > 0:
        paddle_x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle_x < WIDTH - paddle_width:
        paddle_x += paddle_speed

    # 画面のクリア
    screen.fill(WHITE)

    # ボールの移動
    ball_x += ball_dx
    ball_y += ball_dy

    # 壁との衝突判定
    if ball_x < ball_radius or ball_x > WIDTH - ball_radius:
        ball_dx = -ball_dx
    if ball_y < ball_radius:
        ball_dy = -ball_dy
    if ball_y > HEIGHT:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = 3
        ball_dy = -3

    # パドルとの衝突判定
    paddle_rect = pygame.Rect(paddle_x, paddle_y, paddle_width, paddle_height)
    ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)
    if ball_rect.colliderect(paddle_rect):
        ball_dy = -ball_dy

    # ブロックとの衝突判定
    for block in blocks[:]:
        if ball_rect.colliderect(block):
            blocks.remove(block)
            ball_dy = -ball_dy

    # ボールの描画
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # パドルの描画
    pygame.draw.rect(screen, BLACK, paddle_rect)

    # ブロックの描画
    for block in blocks:
        pygame.draw.rect(screen, BLACK, block)

    # 画面の更新
    pygame.display.flip()

# Pygameの終了
pygame.quit()