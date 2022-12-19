import pygame
from wall import Wall
from player import Player


class Enemy(Wall):
    def __init__(self, pos: list, group, enemy_image="door(close).PNG", number_pos=None, transfer=None, number_room=0):
        super().__init__(pos, group, enemy_image, number_pos, transfer, number_room)
        self.image_text = enemy_image
        self.collide = False
        self.region = pygame.Rect(pos[0] - 160, pos[1] - 160, 320, 320)

    def update_region(self):
        """функция которая обновляет область вокруг врага"""
        if self.region.left != self.rect.centerx - 160 or self.region.top != self.rect.centery - 160:
            self.region = pygame.Rect(self.rect.centerx - 160, self.rect.centery - 160, 320, 320)

    def resize(self, width, height, size_block):
        self.image = pygame.image.load(f"textures\\{self.image_text}").convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)

        k = width / height / 5 * size_block / 30
        self.image = pygame.transform.scale(self.image, (k * self.rect.width, k * self.rect.height))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, collider_player: Player, speed: list, key: list, walls):
        self.update_region()
        self._update(collider_player, speed, key)
        self._go(collider_player)
        self._update_pos(walls)

    def _go(self, collider_player):
        # надо проаисать логику подойти ударить отойти
        if self.region.colliderect(collider_player.rect):
            if collider_player.rect.centerx - 100 > self.rect.centerx:
                self.rect.centerx += 1
            elif collider_player.rect.centerx + 100 < self.rect.centerx:
                self.rect.centerx -= 1
            if collider_player.rect.centery - 100 > self.rect.centery:
                self.rect.centery += 1
            elif collider_player.rect.centery + 100 < self.rect.centery:
                self.rect.centery -= 1
        ...

    def _update_pos(self, walls):
        # for j in walls:
        #     for i in j:
        #         if self.rect.colliderect(i):
        #             код выше определяет что враг столкнулся со стеной и проходом
        #             объект i это стена или предемет с которым столкнулся враг
        ...
