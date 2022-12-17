import pygame


class PLAYER(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.dx = 0
        self.dy = 0
        self.onGround = False
        self.Go = False
        self.Frame = 0

        self.direction = [False, True, False]  # Left, Right, Jump

    def update(self, *args):
        # self.rect.x += self.dx
        # if not self.onGround:
        #     self.dy += 1

        self.rect.y += self.dy
        self.onGround = False

        if self.rect.y > args[0]:
            self.rect.y = args[0]
            self.dy = 0
            self.onGround = True
            self.direction[2] = False

        file = "right" if self.direction[1] else "left" if self.direction[0] else ...

        if not self.direction[2]:
            if self.Go:
                self.Frame += 0.2
                if self.Frame > 7:
                    self.Frame -= 7
                Personnel = ["0.png", "1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png"]
                self.image = pygame.image.load(f"image/{file}/{Personnel[int(self.Frame)]}").convert_alpha()
            else:
                self.image = pygame.image.load(f"image/{file}/main.png").convert_alpha()
        else:
            self.image = pygame.image.load(f"image/{file}/jump.png").convert_alpha()
        self.dx = 0


pygame.init()
size = width, height = 500, 500
sc = pygame.display.set_mode(size)
clock = pygame.time.Clock()
player = PLAYER(100, 400, 'image/right/main.png')

while True:
    sc.fill(pygame.Color('white'))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYUP:
            player.Go = False
    key = pygame.key.get_pressed()
    if key[pygame.K_d]:
        player.dx = 5
        player.Go, player.direction[0], player.direction[1] = True, False, True
    elif key[pygame.K_a]:
        player.dx = -5
        player.Go, player.direction[0], player.direction[1] = True, True, False
    if key[pygame.K_SPACE]:
        if player.onGround:
            player.dy = -20
            player.onGround, player.direction[2] = False, True

    player.update(height - player.rect.height)
    sc.blit(player.image, player.rect)
    pygame.display.update()
    clock.tick(50)
