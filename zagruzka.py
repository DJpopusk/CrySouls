import pygame


class ZAGRUZKA(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(-350, y))
        self.DX = 0
        self.dx = 0
        self.dy = 0
        self.Go = False
        self.Frame = 0
        self.FRAME = 0
        self.A = False
        self.D = False
        self.W = True
        self.S = True

    def update(self, *args):
        KARTINKA_surf = pygame.image.load('image/' + 'ZAGRUZKA' + '/' + '8.png')
        KARTINKA_rect = KARTINKA_surf.get_rect(
            bottomright=(650, 650))
        sc.blit(KARTINKA_surf, KARTINKA_rect)
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.Go:
            if self.Go:
                self.Frame += 0.2
                if self.Frame > 7:
                    self.Frame -= 7
                Personnel = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png']
                self.image = pygame.image.load('image/' + 'ZAGRUZKA' + '/' + Personnel[int(self.Frame)]).convert_alpha()
        if self.DX > 150:
            self.DX += 9.5
        else:
            self.DX += 2.5
        self.dx += 0.13
        self.dy = 0
        pygame.draw.rect(sc, 'black', (self.DX, 100, 1000, 1000), 0)
        # if self.DX > 800: когда человечек пробегает окно закрывается
        #     exit() когда человечек пробегает окно закрывается


pygame.init()
width, height = 800, 800
sc = pygame.display.set_mode((width, height))
sc.fill((100, 150, 200))

dog_surf = pygame.image.load('image/' + 'ZAGRUZKA' + '/' + '8.png')
dog_rect = dog_surf.get_rect(
    bottomright=(650, 650))
sc.blit(dog_surf, dog_rect)

clock = pygame.time.Clock()
player = ZAGRUZKA(250, 250, 'image/right/main.png')

while True:
    sc.fill(pygame.Color('black'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.Go = True
    player.W = True
    player.A = False
    player.update(height - player.rect.height)
    sc.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(50)
