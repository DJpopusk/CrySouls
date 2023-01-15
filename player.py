import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple, group, player_image="main.PNG", player_speed=(5, 5)):
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
        self.path = "image\\right\\main.png"

    def update(self, width, height, walls: list, collide: list, key_open, key_blows, size_block):
        self.update_region(width, height, key_open, key_blows, collide)
        self._animation(key_blows)
        self.resize(width, height, size_block)
        self._update_pos(width, height, walls)

    def update_region(self, width, height, key_open, key_blows, collide):
        """
        функция которая обновляет область вокруг персонажа

        :param width: ширена экрана
        :param height: высота экрана
        :param key_open: нажата ли клавиша открывающая что-то
        :param key_blows: нажата ли клавиша атаки
        :param collide: объекты с которыми можно взаимодействовать
        """
        if self.region.left != width // 2 - 80 or self.region.top != height // 2 - 80:
            self.region = pygame.Rect(width // 2 - 80, height // 2 - 80, 160, 160)

        if key_open:
            for i in collide:
                if i.rect.colliderect(self.region):
                    i.open(width, height)

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
        self.image = pygame.image.load(self.path).convert_alpha()
        self.rect = self.image.get_rect(center=self.rect.center)

        k = (width / height) * 0.5 * size_block / 30
        self.image = pygame.transform.scale(self.image, (k * self.rect.width, k * self.rect.height))
        self.rect = self.image.get_rect(center=self.rect.center)

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
            file = 'left'
        elif self.direction[1]:
            file = 'right'
        elif self.direction[2]:
            file = 'up'
        elif self.direction[3]:
            file = 'down'

        if not key_udar or self.Go:
            if self.Go:
                self.Frame += 0.2
                if self.Frame > 7:
                    self.Frame -= 7
                Personnel = ['0.png', '1.png', '2.png', '3.png', '4.png', '5.png', '6.png', '7.png']
                self.path = f"image/{file}/{Personnel[int(self.Frame)]}"
                self.image = pygame.image.load(self.path).convert_alpha()
            else:
                self.path = f"image/{file}/main.png"
                self.image = pygame.image.load(self.path).convert_alpha()
        else:
            if not self.Go:
                self.Frame += 0.3
                if self.Frame >= 3:
                    self.Frame = 0
                Personnel = ['udar0.png', 'udar1.png', 'udar2.png']
                self.path = f"image/{file}/{Personnel[int(self.Frame)]}"
                self.image = pygame.image.load(self.path).convert_alpha()
            else:
                self.path = f"image/{file}/main.png"
                self.image = pygame.image.load(self.path).convert_alpha()

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