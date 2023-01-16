import pygame


class PortalV(pygame.sprite.Sprite):
    def __init__(self, x, y, file):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(file).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.Frame = 0
        path = ['portal_0.png', 'portal_1.png']
        self.images = [pygame.image.load(f"image/portalV/{i}").convert_alpha() for i in path]

    def update(self, *args):
        self.animation()
        self.teleport()

    def teleport(self): ...

    def animation(self):
        self.Frame += 0.2
        if self.Frame > 1:
            self.Frame -= 1
        self.image = self.images[int(self.Frame)]
