import pygame
from wall import Wall
from player import Player


class Enemy(Wall):
    def __init__(self, pos: list, group, enemy_image="door(close).PNG", number_pos=None, transfer=None, number_room=0):
        super().__init__(pos, group, enemy_image, number_pos, transfer, number_room)
        self.image_text = enemy_image
        self.collide = False

    def resize(self, width, height):
        self.image = pygame.image.load(f"textures\\{self.image_text}").convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)

        k = width / height / 5
        self.image = pygame.transform.scale(self.image, (k * self.rect.width, k * self.rect.height))
        self.rect = self.image.get_rect(center=self.rect.center)

    def update(self, collider_player: Player, speed: list, key: list, walls):
        self._update(collider_player, speed, key)
        self._update_pos(walls)

    def _update_pos(self, walls):
        # for j in walls:
        #     for i in j:
        #         if self.rect.colliderect(i):
        #             код выше определяет что враг столкнулся со стеной
        #             объект i это стена или предемет с которым столкнулся враг
        ...
