import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, group, player_image="main.PNG", player_speed=(20, 20)):
        pygame.sprite.Sprite.__init__(self)
        self.image_text = player_image
        self.image = pygame.image.load(f"image\\right\\{self.image_text}").convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.player_speed_x = player_speed[0]
        self.player_speed_y = player_speed[1]
        self.add(group)
        self.animation = False
        self.collide = False
        self.len_anim = 3
        self.animation_up = [True for _ in range(self.len_anim)]
        self.region = pygame.Rect(pos[0] - 80, pos[1] - 80, 160, 160)

        self.Go = False
        self.Frame = 0
        self.direction = [False, True, False, False]  # Left, Right, Up, Down

        path_png = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png']
        self.path = []
        for direction in ["left", "right", "up", "down"]:
            self.path.append([f"image\\{direction}\\{png}" for png in path_png])

        self.images = []
        for direction in self.path:
            self.images.append([pygame.image.load(i).convert_alpha() for i in direction])

        self.images_udar = []
        for direction, path_udar in zip(["left", "right", "up", "down"], [[j for j in range(i)] for i in [3, 3, 8, 8]]):
            self.images_udar.append([pygame.image.load(f"image/{direction}/udar{i}.png").convert_alpha() for i in
                                     [i for i in path_udar]])

        self.default_image = [pygame.image.load(f"image/{i}/main.png").convert_alpha()
                              for i in ["left", "right", "up", "down"]]

    def update(self, width, height, walls: list, collide: list, key_open, key_blows, size_block, level):
        self.update_region(width, height, key_open, key_blows, collide, level)
        self._animation(key_blows)
        self.resize(width, height, size_block)
        self._update_pos(width, height, walls)

    def update_region(self, width, height, key_open, key_blows, collide, level):
        """
        функция которая обновляет область вокруг персонажа

        :param width: ширена экрана
        :param height: высота экрана
        :param key_open: нажата ли клавиша открывающая что-то
        :param key_blows: нажата ли клавиша атаки
        :param collide: объекты с которыми можно взаимодействовать
        :param level: список всех объектов на карте
        """
        if self.region.left != width // 2 - 80 or self.region.top != height // 2 - 80:
            self.region = pygame.Rect(width // 2 - 80, height // 2 - 80, 160, 160)

        if key_open:
            for i in collide:
                if i.rect.colliderect(self.region):
                    i.open(width, height, level)

    def _update_pos(self, width, height, walls):
        """
        перемещение персонажа в центр если он не в центре

        :param width: ширена
        :param height: высота экрана
        :param walls: все объекты которые будут передвигаться
        """
        if (not [self.rect.y + self.rect.width // 2 != height // 2 + i for i in range(self.len_anim)].count(False) and
                not [self.rect.y + self.rect.width // 2 != height // 2 - i for i in range(self.len_anim)].count(False)):
            for i in walls:
                i.rect.y += height // 2 - self.rect.width // 2 - self.rect.y
            self.rect.y = height // 2 - self.rect.width // 2

        if self.rect.x + self.rect.width // 2 != width // 2:
            for i in walls:
                i.rect.x += width // 2 - self.rect.width // 2 - self.rect.x
            self.rect.x = width // 2 - self.rect.width // 2

    def resize(self, width, height, size_block):
        self.images = []
        for direction in self.path:
            self.images.append([pygame.image.load(i).convert_alpha() for i in direction])

        k = (width / height) * 0.5 * size_block / 30
        for ind, path_png in enumerate(self.images):
            for ind2, i in enumerate(path_png):
                rect = i.get_rect()
                self.images[ind][ind2] = pygame.transform.scale(i, (k * rect.width, k * rect.height))

    def _animation(self, key_udar):
        """
        функция которая совершает анимацию
        """
        if self.animation and not self.collide:
            if self.animation_up.count(True) and self.animation_up[0]:
                self.rect.y -= 1
                self.__update_animation_up(True)
            else:
                self.rect.y += 1
                self.__update_animation_up(False)
            self.animation = False

        if self.direction[0]:
            file = 0
        elif self.direction[1]:
            file = 1
        elif self.direction[2]:
            file = 2
        else:
            file = 3

        if not key_udar or self.Go:
            if self.Go:
                self.Frame += 0.2
                if self.Frame > 7:
                    self.Frame -= 7
                self.image = self.images[file][int(self.Frame)]
            else:
                self.image = self.default_image[file]
        else:
            if not self.Go:
                self.Frame += 0.2
                if self.Frame >= 3:
                    self.Frame = 0
                self.image = self.images_udar[file][int(self.Frame)]
            else:
                self.images = self.default_image[file]

    def __update_animation_up(self, up):
        for i in range(1, len(self.animation_up)):
            if self.animation_up[i] == up:
                self.animation_up[i] = not self.animation_up[i]
                if not up == self.animation_up[len(self.animation_up) - 2] and \
                        not up == self.animation_up[len(self.animation_up) - 1]:
                    self.animation_up[0] = not self.animation_up[0]
                return

    def get_pos(self):
        return self.rect.center
