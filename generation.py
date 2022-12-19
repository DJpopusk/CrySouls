import pygame
from wall import Wall
from chest import Chest
from box import Box
from door import Door
from bed import Bed
from base import Base
from drill import Drill
from enemy import Enemy
import random

enemy_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
chest_group = pygame.sprite.Group()
box_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
bed_group = pygame.sprite.Group()
base_group = pygame.sprite.Group()
drill_group = pygame.sprite.Group()


class Generation:
    def __init__(self):
        self.bases, self.walls, self.drills, self.chests, self.boxes, self.doors, self.beds, self.enemies \
            = [], [], [], [], [], [], [], []

        self.list_collide_objects = [self.bases, self.walls, self.drills, self.chests, self.boxes, self.doors,
                                     self.beds, self.enemies]
        self.sum_list_collide_objects = [*self.bases, *self.walls, *self.drills, *self.chests, *self.boxes, *self.doors,
                                         *self.beds, *self.enemies]

        self.base_image = "base.PNG"
        self.wall_image = "wall(f).PNG"
        self.drill_image = "drill.PNG"
        self.chest_image = "chest(f).PNG"
        self.box_image = "box(f).PNG"
        self.door_image = "door(close).PNG"
        self.bed_image = "bed.PNG"
        self.enemy_image = "enemy_golem.PNG"
        self.images = [self.base_image, self.wall_image, self.drill_image, self.chest_image, self.box_image,
                       self.door_image, self.bed_image, self.enemy_image]

        self.classes = [Base, Wall, Drill, Chest, Box, Door, Bed, Enemy]
        self.groups = [base_group, wall_group, drill_group, chest_group, box_group, door_group, bed_group, enemy_group]

    def create_level(self, size_object, width=10, height=10, count_room=(6, 10), count_enemy=(3, 10)):
        def block_select(block, a, over):
            if over:
                if block < a:
                    block = a
            else:
                if block > a:
                    block = a
            return block

        generations = [self.generation_enemy_room for _ in range(3)] + [self.generation_chest_room]
        count_room = random.randint(count_room[0], count_room[1])
        transform = [0, 0]
        next_horizontal_on = [random.choice([0, 1]), random.choice([0, 1])]
        next_random_x = [random.choice([1, -1]), random.choice([1, -1])]
        next_random_y = [random.choice([1, -1]), random.choice([1, -1])]

        blocks = [0, 0]
        for j in range(count_room):
            past_horizontal_on = next_horizontal_on[0]
            past_random_x = next_random_x[0]
            past_random_y = next_random_y[0]

            next_horizontal_on[0], next_horizontal_on[1] = next_horizontal_on[1], random.choice([0, 1])
            horizontal_on = next_horizontal_on[0]

            next_random_x[0], next_random_x[1] = next_random_x[1], random.choice([1, -1])
            next_random_y[0], next_random_y[1] = next_random_y[1], random.choice([1, -1])

            left_or_right = next_random_x[0]
            up_or_down = next_random_y[0]

            if past_horizontal_on != horizontal_on != next_horizontal_on[1]:
                if past_random_x != next_random_x[1] and not horizontal_on:
                    left_or_right = -left_or_right
                if past_random_y != next_random_y[1] and horizontal_on:
                    up_or_down = -up_or_down

            for i in self.sum_list_collide_objects:
                if i.number_room == j - 1:
                    blocks[0] = block_select(blocks[0], i.rect.centerx, True) if left_or_right == 1 else \
                        block_select(blocks[0], i.rect.centerx - width * size_object, False)
                    blocks[1] = block_select(blocks[1], i.rect.centery, True) if up_or_down == 1 else \
                        block_select(blocks[1], i.rect.centery - height * size_object, False)

            if horizontal_on and next_random_x[0] != next_random_x[1]:
                next_random_x[1] = next_random_x[0]
            elif not horizontal_on and next_random_y[0] != next_random_y[1]:
                next_random_y[1] = next_random_y[0]

            if horizontal_on:
                transform[0] = blocks[0] + size_object if blocks[0] > 0 else blocks[0]
            else:
                transform[1] = blocks[1] if blocks[1] > 0 else blocks[1] - size_object

            direction = [0, 0, 0, 0]
            if (next_horizontal_on[1] and next_random_x[1] == -1 and j + 1 != count_room) \
                    or (left_or_right == 1 and horizontal_on and j != 0):
                direction[0] = 1
            if (next_horizontal_on[1] and next_random_x[1] == 1 and j + 1 != count_room) \
                    or (left_or_right == -1 and horizontal_on and j != 0):
                direction[1] = 1
            if (not next_horizontal_on[1] and next_random_y[1] == -1 and j + 1 != count_room) \
                    or (up_or_down == 1 and not horizontal_on and j != 0):
                direction[3] = 1
            if (not next_horizontal_on[1] and next_random_y[1] == 1 and j + 1 != count_room) \
                    or (up_or_down == -1 and not horizontal_on and j != 0):
                direction[2] = 1

            gnr = generations[random.randint(0, len(generations) - 1)] if j > 0 else self.generation_house_room
            if gnr == self.generation_enemy_room:
                self.draw_room(gnr(width, height, direction, [count_enemy[0], count_enemy[1]]), size_object, transform,
                               j)
            else:
                self.draw_room(gnr(width, height, direction), size_object, transform, j)

            if j != count_room - 1:
                transform[0] = transform[0] + width * size_object * next_random_x[1] if next_horizontal_on[1]\
                    else transform[0]
                transform[1] = transform[1] + height * size_object * next_random_y[1] if not next_horizontal_on[1]\
                    else transform[1]

                self.draw_room(self.generation_corridor(height, width, not next_horizontal_on[1]), size_object,
                               [transform[0], transform[1]], j)

    def draw_room(self, generation, size_object, transfer=(0, 0), number_room=0):
        for a, b in enumerate(generation):
            for c, j in enumerate(b):
                c = len(b) - c
                if j:
                    index = self.images.index(j)
                    if j == "bed.PNG":
                        my_object = self.classes[index]([a * size_object + transfer[0], c * size_object + transfer[1] +
                                                         size_object / 2],
                                                        self.groups[index], self.images[index], [a, c],
                                                        [transfer[0], transfer[1] + size_object / 2], number_room)
                    else:
                        my_object = self.classes[index]([a * size_object + transfer[0], c * size_object + transfer[1]],
                                                        self.groups[index], self.images[index], [a, c],
                                                        [transfer[0], transfer[1]], number_room)

                    self.sum_list_collide_objects.append(my_object)
                    self.list_collide_objects[index].append(my_object)

        return self.sum_list_collide_objects

    def update_level(self, size_object, r):
        for k in self.sum_list_collide_objects:
            k.old_center = k.rect.center

            k.rect.centerx = k.number_pos[0] * size_object + k.transfer[0] * r
            k.rect.centery = k.number_pos[1] * size_object + k.transfer[1] * r

    def exit_room(self, my_room, direction):
        def exit_room(my_room, up=0, h=True):
            for k in range(2, len(my_room) - 2):
                if h:
                    my_room[up][k] = self.base_image
                else:
                    my_room[k][up] = self.base_image

        if direction[0]:
            exit_room(my_room)
        if direction[1]:
            exit_room(my_room, -1)
        if direction[2]:
            exit_room(my_room, 0, False)
        if direction[3]:
            exit_room(my_room, -1, False)

        return my_room

    def generation_house_room(self, len_room_h, len_room_w, direction=None):
        direction = [0, 0, 0, 0] if direction is None else direction

        my_room = self.create_room(len_room_h, len_room_w)
        my_room[1][1] = self.box_image
        my_room[len_room_h-3][1] = self.bed_image
        my_room = self.exit_room(my_room, direction)
        if direction[2] == 1:
            my_room[len_room_h-3][0] = self.wall_image
            my_room[len_room_h-4][0] = self.wall_image

        return my_room

    def generation_enemy_room(self, len_room_h, len_room_w, direction=None, count_enemy=None):
        direction = [0, 0, 0, 0] if direction is None else direction
        count_enemy = [3, 10] if count_enemy is None else count_enemy

        my_room = self.create_room(len_room_h, len_room_w)
        my_room = self.exit_room(my_room, direction)

        count_enemy = random.randint(count_enemy[0], count_enemy[1])
        for _ in range(count_enemy):
            Exit = False
            while not Exit:
                a = random.randint(3, len_room_h - 3)
                b = random.randint(3, len_room_w - 3)
                if not my_room[a][b]:
                    my_room[a][b] = self.enemy_image
                    Exit = True

        return my_room

    def generation_chest_room(self, len_room_h, len_room_w, direction=None):
        direction = [0, 0, 0, 0] if direction is None else direction

        my_room = self.create_room(len_room_w, len_room_h)
        my_room[len_room_h // 2 - 1][len_room_w // 2 - 1] = self.chest_image
        my_room = self.exit_room(my_room, direction)
        return my_room

    def generation_corridor(self, len_room_h, len_room_w, h=True):
        my_room = self.create_room(len_room_h, len_room_w)

        for k in range(1, len(my_room) - 1):
            if h:
                my_room[k][0] = self.base_image
                my_room[k][-1] = self.base_image
            else:
                my_room[0][k] = self.base_image
                my_room[-1][k] = self.base_image

        return my_room

    def create_room(self, len_room_h, len_room_w):
        my_list = [[] for _ in range(len_room_h)]
        my_list[0] = [f"{self.wall_image}" for _ in range(len_room_w)]
        my_list[-1] = [f"{self.wall_image}" for _ in range(len_room_w)]

        for index in range(1, len(my_list) - 1):
            my_list[index] = [f"{self.wall_image}"] + ["" for _ in range(1, len_room_w - 1)] + [f"{self.wall_image}"]

        return my_list


if __name__ == "__main__":
    pygame.init()
    size = we, he = 1000, 650
    screen = pygame.display.set_mode(size)
    g = Generation()
    g.create_level(30)
    [i.resize(we, he, 30) for i in g.list_collide_objects[7]]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                exit()

        screen.fill((0, 0, 0))
        for i in g.groups:
            i.draw(screen)

        pygame.display.update()
