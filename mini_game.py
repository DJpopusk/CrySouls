import random
import pygame
from konec_VIJGRAL import draw
from konec_PROIGRISH import draw as draw2

spisok_voprosov = [['5x + 1 = 16', '3'], ['x - 25 = 75', '100'], ['12 + x = 23', '11'],
                   ['88 - 3x = 22', '22'], ['7x - 14 = 0', '2'], ['5x = 125', '25'], ['17 + x = 21', '4'],
                   ['x + 18 = 87', '69'], ['5x + 7 = 67', '12'], ['8x - 88 = ' '11'], ['44 + 2x = 44', '0'],
                   ['12x - 4 = 44', '4']]


number = random.randint(0, len(spisok_voprosov) - 1)
vopros = (spisok_voprosov[number])[0]
otvet = (spisok_voprosov[number])[-1]

KOMANDA_VIJGRISHA_ILI_NET = ''

pygame.init()

clock = pygame.time.Clock()

base_font = pygame.font.Font(None, 32)
user_text = ''
color_active = pygame.Color(0, 255, 0)
color_passive = pygame.Color(0, 255, 0)
color = color_passive

active = False


def main(screen, update, width, height):
    global active, user_text, color, color_active, color_passive, KOMANDA_VIJGRISHA_ILI_NET
    input_rect = pygame.Rect(width // 2 - width // 20, height // 2, width // 8, height // 8)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = True
                else:
                    active = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

        screen.fill((0, 0, 0))
        if active:
            color = color_active
        else:
            color = color_passive

        screen.fill((0, 0, 0))
        font = pygame.font.Font(None, width // 15)
        text = font.render(f'Решите уровнение: {vopros}', True, (0, 255, 0))
        text_x = width // 2 - text.get_width() // 2
        text_y = height // 2 - text.get_height() // 2 - height // 5
        text_w = text.get_width()
        text_h = text.get_height()
        screen.blit(text, (text_x, text_y))
        pygame.draw.rect(screen, (255, 0, 255), (text_x - width // 40, text_y - height // 80,
                                                 text_w + width // 20, text_h + height // 40), 4)
        pygame.draw.rect(screen, color, input_rect)

        text_surface = base_font.render(user_text, True, (255, 255, 255))

        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        if len(user_text) == len(otvet):
            if user_text == otvet:
                KOMANDA_VIJGRISHA_ILI_NET = 'True'
                draw(screen, width, height)
            else:
                KOMANDA_VIJGRISHA_ILI_NET = 'False'
                draw2(screen, width, height)

            pygame.display.update()
            update()
            pygame.time.wait(2000)
            return KOMANDA_VIJGRISHA_ILI_NET

        pygame.display.update()
        update()
        clock.tick(10)


if __name__ == "__main__":
    size = main_width, main_height = 800, 400
    main_screen = pygame.display.set_mode(size)
    main(main_screen, lambda: ..., main_width, main_height)
