import pygame
from wall import Wall
from player import Player
from random import randint


class Enemy(Wall):
    def __init__(self, pos: list, group, enemy_image="enemy_golem.PNG", number_pos=None, transfer=None,
                 number_room=0):
        super().__init__(pos, group, enemy_image, number_pos, transfer, number_room)
        self.image_text = enemy_image
        self.collide = False
        self.region = pygame.Rect(pos[0] - 160, pos[1] - 160, 320, 320)
        self.__resize = 1
        self.Go, self.Frame = False, 0
        self.attacking = True
        self.damage = 2
        path = ['ZLO_0.png', 'ZLO_1.png', 'ZLO_2.png', 'ZLO_3.png']
        self.images = [pygame.image.load(f"image/ZLO/{i}").convert_alpha() for i in path]
        self.default_image = self.image
        self.last_mowed = ["x", 2]
        self.a = 0
    def update_region(self):
        """функция которая обновляет область вокруг врага"""
        if self.region.left != self.rect.centerx - 160 or self.region.top != self.rect.centery - 160:
            self.region = pygame.Rect(self.rect.centerx - 160, self.rect.centery - 160, 320, 320)

    def resize(self, width, height, size_block):
        path = ['ZLO_0.png', 'ZLO_1.png', 'ZLO_2.png', 'ZLO_3.png']
        self.images = [pygame.image.load(f"image/ZLO/{i}").convert_alpha() for i in path]

        k = width / height / 5 * size_block / 30
        self.__resize = k
        self.rect = self.image.get_rect(center=self.rect.center)

        rect = self.default_image.get_rect()
        self.default_image = pygame.transform.scale(self.default_image, (k * rect.width, k * rect.height))

        for i in self.images:
            ind = self.images.index(i)
            rect = i.get_rect()
            self.images[ind] = pygame.transform.scale(i, (k * rect.width * 2, k * rect.height * 2))

    def update(self, collider_player: Player, speed: list, key: list, walls, hp=None):
        self.update_region()
        self.animation()
        self._update(collider_player, speed, key)
        self._go(collider_player, walls, hp)
        self._update_pos(walls)

    def _go(self, collider_player: Player, walls, hp):
        # надо прописать логику подойти ударить отойти

        if self.attacking and self.region.colliderect(collider_player.rect):  # двигается на игрока
            if collider_player.rect.centerx - 25 > self.rect.centerx:
                self.rect.centerx += 2
                self.last_mowed = ("x", 2)
            elif collider_player.rect.centerx + 25 < self.rect.centerx:
                self.rect.centerx -= 2
                self.last_mowed = ("x", -2)
            if collider_player.rect.centery - 25 > self.rect.centery:
                self.rect.centery += 2
                self.last_mowed = ("y", 2)
            elif collider_player.rect.centery + 25 < self.rect.centery:
                self.rect.centery -= 2
                self.last_mowed = ("y", -2)
            else:
                self.hit(hp)
                self.attacking = False
        else:  # двигается от игрока
            pos = collider_player.get_pos()  # +_+ 38 62 160
            # a = randint(0, 4)
            # if a == 0:
            #     if self.region.colliderect(collider_player.rect) and any(
            #             [any([not self.rect.colliderect(i) for i in j]) for j
            #              in walls]):
            #         self.rect.centery += 2
            #     else:
            #         self.attacking = True
            # elif a == 1:
            #     if self.region.colliderect(collider_player.rect) and any(
            #             [any([not self.rect.colliderect(i) for i in j]) for j
            #              in walls]):
            #         self.rect.centerx += 2
            #     else:
            #         self.attacking = True
            # elif a == 2:
            #     if self.region.colliderect(collider_player.rect) and any(
            #             [any([not self.rect.colliderect(i) for i in j]) for j
            #              in walls]):
            #         self.rect.centery -= 2
            #     else:
            #         self.attacking = True
            # elif a == 3:
            #     if self.region.colliderect(collider_player.rect) and any(
            #             [any([not self.rect.colliderect(i) for i in j]) for j
            #              in walls]):
            #         self.rect.centerx -= 2
            #     else:
            #         self.attacking = True
            # if self.region.colliderect(collider_player.rect) and any(
            #         [any([not self.rect.colliderect(i) for i in j]) for j
            #          in walls]) and self.attacking == False:
            #         if self.last_mowed[0] == "x":
            #             self.rect.centerx += self.last_mowed[1]
            #         else:
            #             self.rect.centery += self.last_mowed[1]
            # else:
            #     self.attacking == True
            if self.a <= 20:
                if self.last_mowed[0] == "x":
                    if randint(1,2) == 1:
                        self.rect.centerx += self.last_mowed[1]
                    else:
                        self.rect.centerx += self.last_mowed[1]
                else:
                    if randint(1, 2) == 1:
                        self.rect.centery += self.last_mowed[1]
                    else:
                        self.rect.centery -= self.last_mowed[1]
                self.a += 1
            else:
                self.attacking = True
                self.a = 0

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
        self.Frame += 0.2
        if self.Frame > 3:
            self.Frame -= 3
        self.image_text = f"../{self.images[int(self.Frame)]}"
        self.image = self.images[int(self.Frame)]

    def hit(self, hp):
        hp(self.damage)

    def player_coord(self, player: Player):
        return player.get_pos()
