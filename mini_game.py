import random
import pygame

spisok_voprosov = [['5x + 1 = 16', '3'], ['x - 25 = 75', '100'], ['12 + x = 23', '11'],
                   ['88 - 3x = 22', '22'], ['7x - 14 = 0', '2'], ['5x = 125', '25'], ['17 + x = 21', '4'],
                   ['x + 18 = 87', '69'], ['5x + 7 = 67', '12'], ['8x - 88 = 0' '11'], ['44 + 2x = 44', '0'],
                   ['12x - 4 = 44', '4']]
number = random.randint(0, len(spisok_voprosov) - 1)
vopros = (spisok_voprosov[number])[0]
otvet = (spisok_voprosov[number])[-1]

KOMANDA_VIJGRISHA_ILI_NET = ''

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode([800, 400])
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(400 - 35, 300 - 35, 70, 35)
color_active = pygame.Color(0, 255, 0)
color_passive = pygame.Color(0, 255, 0)
color = color_passive

active = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
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
    font = pygame.font.Font(None, 50)
    text = font.render(f'Решите уровнение: {vopros}', True, (0, 255, 0))
    text_x = 800 // 2 - text.get_width() // 2
    text_y = 600 // 2 - text.get_height() // 2 - 125
    text_w = text.get_width()
    text_h = text.get_height()
    screen.blit(text, (text_x, text_y))
    pygame.draw.rect(screen, (255, 0, 255), (text_x - 10, text_y - 10,
                                             text_w + 20, text_h + 20), 1)
    pygame.draw.rect(screen, color, input_rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))

    screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
    if len(user_text) == len(otvet):
        if user_text == otvet:
            KOMANDA_VIJGRISHA_ILI_NET = 'True'
        else:
            KOMANDA_VIJGRISHA_ILI_NET = 'False'
        print(KOMANDA_VIJGRISHA_ILI_NET)
        exit()
    pygame.display.flip()

    clock.tick(10)

# Если KOMANDA_VIJGRISHA_ILI_NET = True, то ответ верный, если False, то нет
