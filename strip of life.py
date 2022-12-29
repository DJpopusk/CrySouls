import pygame


def draw_square(screen):
    pygame.draw.rect(screen, (255, 255, 255),
                     (400, 20, 301, 35), 2)
    x = 402
    for i in range(5):
        pygame.draw.rect(screen, 'green',
                         (x, 22, 59, 33))
        x += 60

if __name__ == '__main__':
    # инициализация Pygame:
    pygame.init()
    # размеры окна:
    size = width, height = 800, 800
    # screen — холст, на котором нужно рисовать:
    screen = pygame.display.set_mode(size)
    # формирование кадра:
    # команды рисования на холсте
    # ...
    # ...
    # смена (отрисовка) кадра:
    draw_square(screen)
    pygame.display.flip()

    while pygame.event.wait().type != pygame.QUIT:
        pass
    # завершение работы:
    pygame.quit()
