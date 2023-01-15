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
        self.A = False
        self.D = False
        self.W = True
        self.S = True
        self.UDAR = False

    def update(self, *args):
        self.rect.x += self.dx
        self.rect.y += self.dy
        if self.D:
            file = 'right'
        elif self.A:
            file = 'left'
        elif self.S:
            file = 'down'
        elif self.W:
            file = 'up'
        elif self.right:
            file = 'right'
        if not (self.UDAR):
            if self.Go:
                self.Frame += 0.2
                if self.Frame > 7:
                    self.Frame -= 7
                Personnel = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png']
                self.image = pygame.image.load('image/' + file + '/' + Personnel[int(self.Frame)]).convert_alpha()
            else:
                self.image = pygame.image.load('image/' + file + '/main.png').convert_alpha()
        else:
            if self.Go:
                self.Frame += 0.3
                if self.Frame > 3:
                    self.Frame -= 3
                Personnel = ['udar0.png', 'udar1.png', 'udar2.png']
                self.image = pygame.image.load('image/' + file + '/' + Personnel[int(self.Frame)]).convert_alpha()
            else:
                self.image = pygame.image.load('image/' + file + '/main.png').convert_alpha()
        self.dx = 0
        self.dy = 0

    def get_pos(self):
        return self.rect.center


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
    if key[pygame.K_d]:
        player.Go = True
        player.A = False
        player.D = True
        player.UDAR = False
    elif key[pygame.K_a]:
        player.Go = True
        player.A = True
        player.D = False
        player.UDAR = False
    elif key[pygame.K_w]:
        player.Go = True
        player.W = True
        player.S = False
        player.A = False
        player.D = False
        player.UDAR = False
    elif key[pygame.K_s]:
        player.Go = True
        player.W = False
        player.S = True
        player.A = False
        player.D = False
        player.UDAR = False
    elif key[pygame.K_k]:
        player.Go = True
        player.UDAR = True
    player.update(height - player.rect.height)
    sc.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(60)
