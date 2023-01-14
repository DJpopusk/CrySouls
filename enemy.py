import pygame
from wall import Wall
from player import Player


class Enemy(Wall):
    def __init__(self, pos: list, group, enemy_image="enemy_golem.PNG", number_pos=None, transfer=None,
                 number_room=0):
        super().__init__(pos, group, enemy_image, number_pos, transfer, number_room)
        self.image_text = enemy_image
        self.collide = False
        self.region = pygame.Rect(pos[0] - 160, pos[1] - 160, 320, 320)
        self.__resize = 1
        self.Go, self.Frame = False, 0

    def update_region(self):
        """функция которая обновляет область вокруг врага"""
        if self.region.left != self.rect.centerx - 160 or self.region.top != self.rect.centery - 160:
            self.region = pygame.Rect(self.rect.centerx - 160, self.rect.centery - 160, 320, 320)

    def resize(self, width, height, size_block):
        self.image = pygame.image.load(f"textures\\{self.image_text}").convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)

        k = width / height / 5 * size_block / 30
        self.__resize = k
        self.image = pygame.transform.scale(self.image, (k * self.rect.width, k * self.rect.height))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, collider_player: Player, speed: list, key: list, walls):
        self.update_region()
        self.animation()
        self._update(collider_player, speed, key)
        self._go(collider_player)
        self._update_pos(walls)

    def _go(self, collider_player):
        # надо прописать логику подойти ударить отойти
        if self.region.colliderect(collider_player.rect):
            self.Go = True
            if collider_player.rect.centerx - 100 > self.rect.centerx:
                self.rect.centerx += 2
            elif collider_player.rect.centerx + 100 < self.rect.centerx:
                self.rect.centerx -= 2
            if collider_player.rect.centery - 100 > self.rect.centery:
                self.rect.centery += 2
            elif collider_player.rect.centery + 100 < self.rect.centery:
                self.rect.centery -= 2
        else:
            self.Go = False

    def _update_pos(self, walls):
        for j in walls:
            for i in j:
                if self.rect.colliderect(i):
                    x_1, x_2 = self.rect.centerx - i.rect.right, i.rect.left - self.rect.centerx
                    y_1, y_2 = self.rect.centery - i.rect.bottom, i.rect.top - self.rect.centery
                    y = y_1 - y_2 if y_1 < y_2 else y_2 - y_1
                    x = x_1 - x_2 if x_1 < x_2 else x_2 - x_1

                    if x < y:
                        if x_1 < x_2:
                            self.rect.right = i.rect.left
                        else:
                            self.rect.left = i.rect.right
                    else:
                        if y_1 < y_2:
                            self.rect.bottom = i.rect.top
                        else:
                            self.rect.top = i.rect.bottom

    def animation(self):
        if self.Go:
            self.Frame += 0.2
            if self.Frame > 3:
                self.Frame -= 3
            Personnel = ['ZLO_0.png', 'ZLO_1.png', 'ZLO_2.png', 'ZLO_3.png']
            self.image_text = f"../image/ZLO/{Personnel[int(self.Frame)]}"
            self.image = pygame.image.load(f"image/ZLO/{Personnel[int(self.Frame)]}").convert_alpha()
            self.rect = self.image.get_rect(center=self.rect.center)
            self.image = pygame.transform.scale(self.image, (self.__resize * 2.5 * self.rect.width,
                                                             self.__resize * 2.5 * self.rect.height))
        else:
            self.image = pygame.image.load("textures/enemy_golem.png").convert_alpha()
            self.rect = self.image.get_rect(center=self.rect.center)
            self.image = pygame.transform.scale(self.image, (self.__resize * self.rect.width,
                                                             self.__resize * self.rect.height))
        self.rect = self.image.get_rect(center=self.rect.center)
