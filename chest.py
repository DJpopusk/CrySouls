from box import Box
from player import Player


class Chest(Box):
    def __init__(self, pos: list, group, chest_image="chest(not f).PNG", number_pos=None, transfer=None, number_room=0):
        super().__init__(pos, group, chest_image, number_pos, transfer, number_room)
        self.image_text = chest_image

    def update(self, collider_player: Player, speed: list, key: list):
        self._update(collider_player, speed, key)

    def open(self, *args):
        Box.open(self)
        self.animation()

    def animation(self):
        if self._open:
            ...
        else:
            ...
