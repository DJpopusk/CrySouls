import pygame
from player import Player
from generation import Generation

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QImage, QPainter

player_group = pygame.sprite.Group()


def func_draw_field(screen):
    screen.fill((10, 30, 10))


class GameWidget(QWidget):
    def __init__(self):
        super().__init__()

        pygame.display.init()
        self.screen = pygame.display.set_mode((self.width(), self.height()), pygame.HIDDEN)

        self.player = Player((self.width() // 2, self.height() // 2), player_group)

        self.generation = Generation()
        self.size_block = 30
        self.generation.create_level(self.size_block)

        self.Exit = False
        self.paint = True
        self.FPS = 100
        self.MY_EVENT = pygame.USEREVENT + 1
        pygame.time.set_timer(self.MY_EVENT, 150)  # здесь можно менять скорость анимации
        self.clock = pygame.time.Clock()

        self.game_timer = QTimer()
        self.game_timer.timeout.connect(self.pygame_loop)
        self.score_on, self.start, self.pause_on, self.game_timer_on = False, False, False, False
        self.score = 0
        self.Go_always = [0, 0, 0, 0]
        self.Open = 0

        self.sum_list_collide_objects = []
        self.sum_list_collide_objects += [i for i in self.generation.sum_list_collide_objects]

        self.list_open_collide_objects = [j for i in self.generation.list_collide_objects[3:7] for j in i]

        self.groups = self.generation.groups

    def pygame_loop(self):
        """
        функция в которой происходят все действия основного цикла
        """
        for event in pygame.event.get():
            if event.type == self.MY_EVENT:
                self.player.animation = True

        func_draw_field(self.screen)

        if pygame.rect.Rect.collidelist(self.player.rect, self.sum_list_collide_objects) == -1:
            self.player.collide = False
        for i in self.groups[:7]:
            self.group_draw_update(i, (self.player, [self.player.player_speed_x, self.player.player_speed_y],
                                       self.Go_always))
        self.group_draw_update(self.groups[7], (self.player, [self.player.player_speed_x, self.player.player_speed_y],
                                                self.Go_always, self.generation.list_collide_objects[:7]))

        # pygame.draw.rect(self.screen, (255, 0, 0), self.player.region)  # эта строка отображает дальность
        # взаимодействия игрока

        self.group_draw_update(player_group, (self.width(), self.height(), self.sum_list_collide_objects,
                                              self.list_open_collide_objects, self.Open))
        self.Open = 0

        self.clock.tick(self.FPS)
        self.update(0, 0, self.width(), self.height())

    def group_draw_update(self, group, params):
        group.draw(self.screen)
        group.update(*params)

    def keyPressEvent(self, a0):
        self.key_on(a0, True)

    def keyReleaseEvent(self, a0):
        self.key_on(a0, False)

    def key_on(self, a0, on):
        """
        функция которая отслеживает нажатия в окне Qt
        """
        if not self.start:
            return

        match a0.text().lower():
            case "": self.pause_on = on
            case "w": self.Go_always[0] += 1 if on else -1
            case "ц": self.Go_always[0] += 1 if on else -1
            case "s": self.Go_always[1] += 1 if on else -1
            case "ы": self.Go_always[1] += 1 if on else -1
            case "a": self.Go_always[2] += 1 if on else -1
            case "ф": self.Go_always[2] += 1 if on else -1
            case "d": self.Go_always[3] += 1 if on else -1
            case "в": self.Go_always[3] += 1 if on else -1
            case "e": self.Open = 1 if on and not a0.isAutoRepeat() else 0
            case "у": self.Open = 1 if on and not a0.isAutoRepeat() else 0

        if self.Go_always[2] == self.Go_always[3]:
            self.player.Go_x = False
        else:
            self.player.Go_x = True
            self.player.direction[0], self.player.direction[1] = (False, True) if self.Go_always[3] else (True, False)

    def mousePressEvent(self, a0):
        """
         функция которая отлавливает нажатия мыши
        """
        ...

    def resizeEvent(self, a0):
        """
        функция которая меняет размер окна pygame рои изменении размеров окна Qt
        """
        self.screen = pygame.display.set_mode((self.width(), self.height()), pygame.HIDDEN)

        k = self.width() / self.height()
        size = self.size_block * k

        self.generation.update_level(size, k)

        for i in self.sum_list_collide_objects:
            i.resize(self.width(), self.height())

        rect = self.sum_list_collide_objects[0]
        self.player.rect.centerx -= rect.old_center[0] - rect.rect.centerx
        self.player.rect.centery -= rect.old_center[1] - rect.rect.centery

        self.player.resize(self.width(), self.height())

    def paintEvent(self, a):
        if self.paint:
            buf = self.screen.get_buffer()
            img = QImage(buf, self.width(), self.height(), QImage.Format_RGB32)
            p = QPainter(self)
            p.drawImage(0, 0, img)

    def closeEvent(self, a):
        # SQL

        QWidget.closeEvent(self, a)
        pygame.event.post(pygame.event.Event(pygame.QUIT))
