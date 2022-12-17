import pygame
from player import Player
from wall import Wall


class Base(Wall):
    def __init__(self, pos: list, group, base_image="base.PNG", number_pos=None, transfer=None, number_room=0):
        super().__init__(pos, group, base_image, number_pos, transfer, number_room)
        self.collide = False

    def update(self, collider_player: Player, speed: list, key: list):
        self._update(collider_player, speed, key)
