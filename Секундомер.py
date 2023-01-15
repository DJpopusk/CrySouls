import pygame
import sys
t = 0  # сек
m = 0  # мин
t1 = '0'
t2 = '.0'
x = 110  # x
y = 85
z = 145
n = 600
v = 0  # Всего времени для игры
pygame.init()
size = width, height = 800, 400
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

pygame.time.set_timer(pygame.USEREVENT, 1000)
font = pygame.font.SysFont('IBM 3270', 100)
font1 = pygame.font.SysFont('IBM 3270', 70)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           sys.exit()
        if event.type == pygame.USEREVENT:
            if v == n:
                x -= 40
                y -= 30
                z += 30
                n *= 10

            v += 1
            t += 1

            if t == 60:
                t = 0
                m += 1

            t1 = str(m)
            t2 = '.' + str(t)

    else:
        screen.fill((255, 255, 255))
        pygame.draw.rect(screen, (0, 0, 0), (y, 25, z, 75))
        pygame.draw.rect(screen, (64, 128, 255), (y, 25, z, 75), 4)
        screen.blit(font.render(t1, True, (198, 9, 9)), (x, 30))
        screen.blit(font1.render(t2, True, (198, 9, 9)), (150, 45))
        pygame.display.flip()
        clock.tick(60)
        continue

    pygame.display.flip()
pygame.quit()