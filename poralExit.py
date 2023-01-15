import pygame


class PORTAL(pygame.sprite.Sprite):
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
            if self.Frame > 1:
                self.Frame -= 1
            Personnel = ['portal_0.png', 'portal_1.png']
            self.image = pygame.image.load('image/' + 'portalExit'
                                                      '' + '/' + Personnel[int(self.Frame)]).convert_alpha()


pygame.init()
width, height = 500, 500
sc = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
player = PORTAL(250, 250, 'image/right/main.png')

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
    clock.tick(5)
