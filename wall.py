import pygame
from player import Player


class Wall(pygame.sprite.Sprite):
    def __init__(self, pos: list, group, wall_image="wall(not f).PNG", number_pos=None, transfer=None, number_room=0):
        pygame.sprite.Sprite.__init__(self)
        self.image_text = wall_image
        self.image = pygame.image.load(f"textures\\{self.image_text}").convert_alpha()
        self.pos = pos
        self.rect = self.image.get_rect(center=pos if len(pos) == 2 else [pos[0] + pos[1], pos[2] + pos[3]])
        self.add(group)
        self.collide = True
        self.old_center = self.rect.center
        self.transfer = [0, 0] if transfer is None else transfer
        self.number_pos = [1, 1] if number_pos is None else number_pos
        self.number_room = number_room

    def update(self, collider_player: Player, speed: list, key: list):
        self._update(collider_player, speed, key)

    def resize(self, width, height, size_block):
        self.image = pygame.image.load(f"textures\\{self.image_text}").convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)

        k = width / height * size_block / 30
        self.image = pygame.transform.scale(self.image, (k * self.rect.width, k * self.rect.height))
        self.rect = self.image.get_rect(center=self.rect.center)

    def _update(self, collider_player, speed, key):
        if self.rect.colliderect(collider_player) and self.collide:
            collider_player.collide = True
            list_collide = [collider_player.rect.right - self.rect.left, self.rect.right - collider_player.rect.left,
                            collider_player.rect.bottom - self.rect.top, self.rect.bottom - collider_player.rect.top]

            if [list_collide[0] < i for i in list_collide[1:]].count(True) == 3:
                collider_player.rect.right = self.rect.left
            elif [list_collide[1] < i for i in list_collide[0:1] + list_collide[2:]].count(True) == 3:
                collider_player.rect.left = self.rect.right
            elif [list_collide[2] < i for i in list_collide[0:2] + list_collide[3:]].count(True) == 3:
                collider_player.rect.bottom = self.rect.top
            elif [list_collide[3] < i for i in list_collide[0:3]].count(True) == 3:
                collider_player.rect.top = self.rect.bottom

        if key[0]:
            self.rect.y += speed[1]
        if key[1]:
            self.rect.y -= speed[1]
        if key[2]:
            self.rect.x += speed[0]
        if key[3]:
            self.rect.x -= speed[0]
