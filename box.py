from wall import Wall
from player import Player


class Box(Wall):
    def __init__(self, pos: list, group, box_image="box(not f).PNG", number_pos=None, transfer=None, number_room=0):
        super().__init__(pos, group, box_image, number_pos, transfer, number_room)
        self.image_text = box_image

    def update(self, collider_player: Player, speed: list, key: list):
        self._update(collider_player, speed, key)

    def open(self, *args): ...
