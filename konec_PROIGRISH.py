import pygame


def draw(screen, width, height):
    screen.fill((0, 0, 0))
    font = pygame.font.Font(None, 100)
    text = font.render("Вы проиграли!", True, (255, 0, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))


if __name__ == '__main__':
    pygame.init()
    size = width, height = 800, 600
    screen = pygame.display.set_mode(size)
    draw(screen, width, height)
    pygame.display.flip()
    pygame.quit()
