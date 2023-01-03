# import pygame
#
#
# class AnimatedSprite(pygame.sprite.Sprite):
#     def __init__(self, sheet, columns, rows, x, y):
#         super().__init__(all_sprites)
#         self.frames = []
#         self.cut_sheet(sheet, columns, rows)
#         self.cur_frame = 0
#         self.image = self.frames[self.cur_frame]
#         self.rect = self.rect.move(x, y)
#
#     def cut_sheet(self, sheet, columns, rows):
#         self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
#                                 sheet.get_height() // rows)
#         for j in range(rows):
#             for i in range(columns):
#                 frame_location = (self.rect.w * i, self.rect.h * j)
#                 self.frames.append(sheet.subsurface(pygame.Rect(
#                     frame_location, self.rect.size)))
#
#     def update(self):
#         self.cur_frame = (self.cur_frame + 1) % len(self.frames)
#         self.image = self.frames[self.cur_frame]
#         zlo = AnimatedSprite(load_image("ZLO.png"), 8, 2, 50, 50)
#
#
# size = WIDTH, HEIGHT = 900, 600
# screen = pygame.display.set_mode(size)
# clock = pygame.time.Clock()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#     screen.fill((0, 0, 0))
#     pygame.display.update()
# clock.tick(10)
# pygame.quit()


import pygame


class PLAYER(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = 0
        self.dy = 0
        self.Go = False
        self.Frame = 0

    def update(self, *args):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.Go:
            self.Frame += 0.2
            if self.Frame > 3:
                self.Frame -= 3
            Personnel = ['ZLO_0.png', 'ZLO_1.png', 'ZLO_2.png', 'ZLO_3.png']
            self.image = pygame.image.load('image/' + 'ZLO' + '/' + Personnel[int(self.Frame)]).convert_alpha()


pygame.init()
width, height = 500, 500
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
player = PLAYER(250, 250, 'image/right/main.png')

while True:
    sc.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYUP:
            player.Go = False
    key = pygame.key.get_pressed()
    player.Go = True
    player.update(height - player.rect.height)
    sc.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(15)
