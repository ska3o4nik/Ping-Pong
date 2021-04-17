import pygame
from player import Player
from ball import Ball

pygame.init()

#Ну типа цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Ну типо окно
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong")

playerA = Player(WHITE, 10, 100)
playerA.rect.x = 20
playerA.rect.y = 200

playerB = Player(WHITE, 10, 100)
playerB.rect.x = 670
playerB.rect.y = 200

ball = Ball(WHITE, 10, 10)
ball.rect.x = 345
ball.rect.y = 195


all_sprites_list = pygame.sprite.Group()


all_sprites_list.add(playerA)
all_sprites_list.add(playerB)
all_sprites_list.add(ball)

carryOn = True

clock = pygame.time.Clock()

#Ну типо счет
scoreA = 0
scoreB = 0

#Ну а типа мне дальше лень писать
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            carryOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                carryOn = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        playerA.moveUp(5)
    if keys[pygame.K_s]:
        playerA.moveDown(5)
    if keys[pygame.K_UP]:
        playerB.moveUp(5)
    if keys[pygame.K_DOWN]:
        playerB.moveDown(5)


    all_sprites_list.update()


    if ball.rect.x >= 690:
        scoreA += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        scoreB += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y > 490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]


    if pygame.sprite.collide_mask(ball, playerA) or pygame.sprite.collide_mask(ball, playerB):
        ball.bounce()

    screen.fill(BLACK)
    pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)


    all_sprites_list.draw(screen)


    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250, 10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420, 10))


    pygame.display.flip()


    clock.tick(60)

pygame.quit()
#Делал Арсен но некоторые места посмотрел на ютубе ;DD