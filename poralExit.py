import pygame
from wall import Wall
from player import Player


class PortalE(Wall):
    def __init__(self, pos: list, group, portal_image="../image/portalExit/portal_0.PNG", numbers=None, transfer=None,
                 number_room=0):
        super().__init__(pos, group, portal_image, numbers, transfer, number_room)
        self.image_text = portal_image
        self.collide = False

        self.Frame = 0
        path = ['portal_0.png', 'portal_1.png']
        self.images = [pygame.image.load(f"image/portalExit/{i}").convert_alpha() for i in path]

    def open(self, *args):
        self.teleport(args[2])

    def update(self, collider_player: Player, speed: list, key: list):
        self._update(collider_player, speed, key)
        self.animation()

    def teleport(self, level):
        for i in level:
            i.kill()
        while level:
            level.pop(-1)

    def animation(self):
        self.Frame += 0.2
        if self.Frame > 1:
            self.Frame -= 1
        self.image = self.images[int(self.Frame)]
