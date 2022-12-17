import pygame
from player import Player
from base import Base


class Drill(Base):
    def __init__(self, pos: list, group, drill_image="drill.PNG", number_pos=None, transfer=None, number_room=0):
        super().__init__(pos, group, drill_image, number_pos, transfer, number_room)
        self.collide = False

    def update(self, collider_player: Player, speed: list, key: list):
        self._update(collider_player, speed, key)
        self._animation()

    def _animation(self):
        ...
