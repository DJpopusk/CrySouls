from Project_PyQt5_1 import *
from wall import Wall
from player import Player
import pygame


class Door(Wall):
    def __init__(self, pos: list, group, door_image="door(close).PNG", numbers=None, transfer=None, number_room=0):
        super().__init__(pos, group, door_image, numbers, transfer, number_room)
        self.image_text = door_image

    def update(self, collider_player: Player, speed: list, key: list):
        self._update(collider_player, speed, key)

    def open(self, *args):
        self.image_text = replace_image(self.image_text, "door(close).PNG", "door(open).PNG")

        self.resize(args[0], args[1])

        self.collide = False if self.image_text == "door(open).PNG" else True
