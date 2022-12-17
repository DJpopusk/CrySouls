from wall import Wall
from player import Player


class Bed(Wall):
    def __init__(self, pos: list, group, bed_image="bed.PNG", number_pos=None, transfer=None, number_room=0):
        super().__init__(pos, group, bed_image, number_pos, transfer, number_room)
        self.image_text = bed_image
        self.sleep = False

    def update(self, collider_player: Player, speed: list, key: list):
        self._update(collider_player, speed, key)

    def open(self, *args):
        self.sleep = not self.sleep

        if self.sleep:
            self.collide = False
            print("спокойной ночи")
        else:
            self.collide = True
