from PyQt5 import QtCore, QtWidgets
from PyQt5.QtMultimedia import QMediaPlayer, QMediaPlaylist, QMediaContent
from Project_PyQt5_1 import *


class MenuWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.r, self.g, self.b = 1, 1, 1
        self.replace_color_text_on, self.complexity_on, self.timer_go = False, 0, False
        self.music_on, self.sound_on = True, True

        self.setObjectName("GameGL")
        self.setAutoFillBackground(True)

        self.lobby_layout = QtWidgets.QVBoxLayout(self)
        self.lobby_layout.setObjectName("lobby_layout")

        self.tabWidget = QtWidgets.QTabWidget(self)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet(self.set_style_tabWidget())
        self.tabWidget.setDocumentMode(False)
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setMovable(False)
        self.tabWidget.setTabBarAutoHide(True)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")

        self.settings = QtWidgets.QPushButton(self.tab)
        self.settings.setMinimumSize(QtCore.QSize(0, 20))
        self.settings.setFont(set_font(12, True, 75))
        self.settings.setObjectName("settings")
        self.gridLayout.addWidget(self.settings, 2, 1, 1, 1)

        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 1, 1, 1)

        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 0, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 0, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 0, 1, 1, 1)

        self.play = QtWidgets.QPushButton(self.tab)
        self.play.setMinimumSize(QtCore.QSize(140, 20))
        self.play.setFont(set_font(12, True, 75))
        self.play.setObjectName("play")
        self.gridLayout.addWidget(self.play, 1, 1, 1, 1)

        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)

        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 2, 2, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)

        self.tabWidget.addTab(self.tab, "")

        self.tab2 = QtWidgets.QWidget()
        self.tab2.setObjectName("tab2")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab2)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setVerticalSpacing(43)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.sound = QtWidgets.QPushButton(self.tab2)
        self.sound.setFont(set_font(11, True, 75))
        self.sound.setObjectName("sound")
        self.gridLayout_2.addWidget(self.sound, 3, 0, 1, 1)

        self.info = QtWidgets.QPushButton(self.tab2)
        self.info.setFont(set_font(11, True, 75))
        self.info.setObjectName("info")
        self.gridLayout_2.addWidget(self.info, 4, 1, 1, 1)

        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 0, 1, 1, 1)

        self.complexity = QtWidgets.QPushButton(self.tab2)
        self.complexity.setFont(set_font(11, True, 75))
        self.complexity.setObjectName("complexity")
        self.gridLayout_2.addWidget(self.complexity, 4, 0, 1, 1)

        self.replace_color_text = QtWidgets.QPushButton(self.tab2)
        self.replace_color_text.setFont(set_font(11, True, 75))
        self.replace_color_text.setObjectName("replace_color_text")
        self.gridLayout_2.addWidget(self.replace_color_text, 2, 1, 1, 1)

        self.select_player = QtWidgets.QPushButton(self.tab2)
        self.select_player.setFont(set_font(11, True, 75))
        self.select_player.setObjectName("select_player")
        self.gridLayout_2.addWidget(self.select_player, 3, 1, 1, 1)

        self.music = QtWidgets.QPushButton(self.tab2)
        self.music.setFont(set_font(11, True, 75))
        self.music.setObjectName("music")
        self.gridLayout_2.addWidget(self.music, 2, 0, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.back_1 = QtWidgets.QPushButton(self.tab2)
        self.back_1.setFont(set_font(11, True, 75))
        self.back_1.setObjectName("back")
        self.horizontalLayout_2.addWidget(self.back_1)
        self.back_1.setMaximumWidth(100)

        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")

        self.red_dial = QtWidgets.QDial(self.tab2)
        self.red_dial.setObjectName("red_dial")
        self.gridLayout_5.addWidget(self.red_dial, 0, 0, 1, 1)

        self.green_dial = QtWidgets.QDial(self.tab2)
        self.green_dial.setObjectName("green_dial")
        self.gridLayout_5.addWidget(self.green_dial, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_5, 1, 0, 1, 1)

        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.blue_dial = QtWidgets.QDial(self.tab2)
        self.blue_dial.setObjectName("blue_dial")
        self.gridLayout_6.addWidget(self.blue_dial, 0, 0, 1, 1)

        self.red_dial.setMinimum(1)
        self.green_dial.setMinimum(1)
        self.blue_dial.setMinimum(1)
        self.red_dial.setMaximum(255)
        self.green_dial.setMaximum(255)
        self.blue_dial.setMaximum(255)

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        self.replace_color_default = QtWidgets.QPushButton(self.tab2)
        self.replace_color_default.setFont(set_font(11, True, 75))
        self.replace_color_default.setStyleSheet(self.set_style_btn(padding_x=10))
        self.replace_color_default.setObjectName("replace_color_default")
        self.verticalLayout.addWidget(self.replace_color_default)

        self.replace_color = QtWidgets.QPushButton(self.tab2)
        self.replace_color.setFont(set_font(11, True, 75))
        self.replace_color.setStyleSheet(self.set_style_btn(padding_x=10))
        self.replace_color.setObjectName("replace_color")
        self.verticalLayout.addWidget(self.replace_color)

        self.replace_colorSQL = QtWidgets.QPushButton(self.tab2)
        self.replace_colorSQL.setFont(set_font(11, True, 75))
        self.replace_colorSQL.setStyleSheet(self.set_style_btn(padding_x=10))
        self.replace_colorSQL.setObjectName("replace_colorSQL")
        self.verticalLayout.addWidget(self.replace_colorSQL)
        self.gridLayout_6.addLayout(self.verticalLayout, 0, 1, 1, 1)

        self.gridLayout_2.addLayout(self.gridLayout_6, 1, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab2, "")
        self.lobby_layout.addWidget(self.tabWidget, 0)

        self.tab3 = QtWidgets.QWidget()
        self.tab3.setObjectName("tab3")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.back_2 = QtWidgets.QPushButton(self.tab2)
        self.back_2.setFont(set_font(11, True, 75))
        self.back_2.setObjectName("back")
        self.verticalLayout_2.addWidget(self.back_2)
        self.back_2.setMaximumWidth(100)

        self.information_1 = QtWidgets.QLabel(self.tab3)
        self.information_1.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.information_1.setObjectName("information_1")
        self.verticalLayout_2.addWidget(self.information_1)

        self.information_2 = QtWidgets.QLabel(self.tab3)
        self.information_2.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignCenter | QtCore.Qt.AlignTop)
        self.information_2.setObjectName("information_2")
        self.verticalLayout_2.addWidget(self.information_2)

        self.information_3 = QtWidgets.QLabel(self.tab3)
        self.information_3.setAlignment(QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeading | QtCore.Qt.AlignRight)
        self.information_3.setObjectName("information_3")
        self.verticalLayout_2.addWidget(self.information_3)

        self.tabWidget.addTab(self.tab3, "")

        self.tab4 = QtWidgets.QWidget()
        self.tab4.setObjectName("tab4")

        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab4)
        self.gridLayout_3.setObjectName("gridLayout_3")

        self.game_score = QtWidgets.QLabel(self.tab4)
        self.game_score.setFont(set_font(12, True, 75))
        self.game_score.setObjectName("game_score")
        self.gridLayout_3.addWidget(self.game_score, 0, 1, 1, 1)

        self.HP = 100
        self.progressBar = QtWidgets.QProgressBar(self.tab4)
        self.progressBar.setProperty("value", self.HP)
        self.progressBar.setTextVisible(False)
        self.progressBar.setMaximumSize(340, 16777215)
        self.progressBar.setStyleSheet("""QProgressBar{    
    border: 2px solid rgb(64, 198, 255);
    border-radius: 10px;
    background-color: rgb(202, 255, 255);
}
QProgressBar::chunk {
    background-color: rgb(26, 200, 10);
    width: 15px;
    margin: 2px;
}""")
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_3.addWidget(self.progressBar, 0, 3, 1, 1)

        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem8, 1, 0, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem9, 0, 2, 1, 1)

        self.tabWidget.addTab(self.tab4, "")

        self.media_player = QMediaPlayer(self)
        self.media_play_list = QMediaPlaylist(self.media_player)

        self.media_player.setPlaylist(self.media_play_list)
        self.media_URL = QMediaContent(QtCore.QUrl.fromLocalFile("evolution.mp3"))
        self.media_player.setMedia(self.media_URL)
        self.media_player.setVolume(100)
        self.media_play_list.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)

        self.sound_player = QMediaPlayer(self)
        self.sound_play_list = QMediaPlaylist(self.sound_player)

        self.sound_player.setPlaylist(self.sound_play_list)
        self.sound_player.setMedia(QMediaContent(QtCore.QUrl.fromLocalFile("")))
        self.sound_play_list.setPlaybackMode(QMediaPlaylist.CurrentItemOnce)

        self.music_timer = QtCore.QTimer()
        self.music_timer.timeout.connect(self.__music_timer)

        with connect("pygame_YL.db") as con:
            cur = con.cursor()
            self.r, self.g, self.b = [j for i, j in
                                      enumerate(*cur.execute("""SELECT red_btn, green_btn, blue_btn FROM colors"""))]
            if [*cur.execute("""SELECT music_on FROM musics""")] != [(1,)]:
                self.music_on = set_music_or_sounds(self.music, self.music_on, self.media_play_list.media
                                                    (self.media_play_list.currentIndex()))
            if [*cur.execute("""SELECT sound_on FROM musics""")] != [(1,)]:
                self.sound_on = set_music_or_sounds(self.sound, self.sound_on, self.sound_play_list.media
                                                    (self.sound_play_list.currentIndex()))
            if (i := [*cur.execute("""SELECT complexity_game FROM complexity""")]) != [(0,)]:
                self.complexity_on = i = i[0][0]
                self.complexity.setText("Уровень Сложности: Средний") if i == 1 else \
                    self.complexity.setText("Уровень Сложности: Сложный")

        if self.music_on:
            self.media_player.play()
            self.music_timer.start(170000)

        if self.sound_on:
            self.sound_player.play()

        self.all_btn = [self.play, self.settings, self.back_1, self.music, self.sound, self.complexity,
                        self.replace_color_text, self.back_2, self.replace_color, self.select_player, self.info,
                        self.replace_colorSQL, self.replace_color_default]
        self.music.setStyleSheet(self.set_style_btn(padding_x=100))
        self.sound.setStyleSheet(self.set_style_btn(padding_x=100))
        self.complexity.setStyleSheet(self.set_style_btn(padding_x=100))

        for i in [self.information_1, self.information_2, self.information_3]:
            i.setFont(set_font(12, True, 75))
        self.set_style_all_btn(self.all_btn[:3] + self.all_btn[6:])

        _translate = QtCore.QCoreApplication.translate
        if not self.music.text():
            self.music.setText(_translate("GameGL", "Музыка: вкл"))
        if not self.sound.text():
            self.sound.setText(_translate("GameGL", "Звуки: вкл"))
        if not self.complexity.text():
            self.complexity.setText(_translate("GameGL", "Уровень Сложности: Лёгкий"))

        self.setWindowTitle(_translate("GameGL", "Game"))
        self.play.setText(_translate("GameGL", "Играть"))
        self.settings.setText(_translate("GameGL", "Настройки"))
        self.select_player.setText(_translate("GameGL", "Выберите персонажа: мальчик"))
        self.info.setText(_translate("GameGL", "Информация"))
        self.back_1.setText(_translate("GameGL", "←"))
        self.back_2.setText(_translate("GameGL", "←"))
        self.replace_color_text.setText(_translate("GameGL", """применить, выбранный цвет на текст
(используйте кнопки выше для БД)"""))
        self.replace_color.setText(_translate("GameGL", "применить"))
        self.replace_colorSQL.setText(_translate("GameGL", "применить на всегда"))
        self.replace_color_default.setText(_translate("GameGL", "автоприменение"))
        BETA_text = """Добро пожаловать в BETA-версию
В BETA-версии временно можно подключать и использовать только простые шейдеры."""
        self.information_1.setText(_translate("GameGL", BETA_text))
        self.information_2.setText(_translate("GameGL", "Text ..."))
        self.information_3.setText(_translate("GameGL", "Музыка была взята с сайта Bensound.com"))
        self.game_score.setText(_translate("GameGL", "scpre: 0"))

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self)

        self.__click_button()

    def __music_timer(self):
        if self.music_on:
            self.media_player.play()
        else:
            self.music_timer.stop()

    def __click_button(self):
        self.back_1.clicked.connect(lambda: self.tabWidget.setCurrentIndex(0))
        self.back_2.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.settings.clicked.connect(lambda: self.tabWidget.setCurrentIndex(1))
        self.info.clicked.connect(lambda: self.tabWidget.setCurrentIndex(2))
        self.play.clicked.connect(self.__play)
        self.replace_color.clicked.connect(self.__replace_color)
        self.replace_colorSQL.clicked.connect(self.__replace_colorSQL)
        self.replace_color_default.clicked.connect(self.__replace_color_default)
        self.music.clicked.connect(self.__music)
        self.sound.clicked.connect(self.__sound)
        self.replace_color_text.clicked.connect(self.__replace_color_text)
        self.select_player.clicked.connect(self.__select_player)
        self.complexity.clicked.connect(self.__complexity)

    def __complexity(self):
        def help_complexity(str_1, str_2, number):
            self.complexity_on = number
            self.complexity.setText(self.complexity.text().replace(str_1, str_2))
            UPDATE_BD("complexity", f"complexity_game = {self.complexity_on}")

        if self.complexity_on == 0:
            help_complexity("Лёгкий", "Средний", 1)
        elif self.complexity_on == 1:
            help_complexity("Средний", "Сложный", 2)
        else:
            help_complexity("Сложный", "Лёгкий", 0)

    def __select_player(self):
        ...

    def __replace_color_text(self, update=False, SQL=False):
        if update is False:
            self.replace_color_text_on = not self.replace_color_text_on
        else:
            for i in [self.information_1, self.information_2, self.information_3]:
                my_string = f"color: rgb({self.red_dial.value()}, {self.green_dial.value()}, {self.blue_dial.value()});"
                i.setStyleSheet(my_string)
            if SQL:
                UPDATE_BD("color", f"red_text = {self.red_dial.value()}, "
                                   f"green_text = {self.green_dial.value()}, blue_text = {self.blue_dial.value()}")

    def __music(self):
        self.music_on = set_music_or_sounds(self.music, self.music_on, self.media_player, self.music_timer)
        if self.music_on:
            UPDATE_BD("musics", "music_on = 1")
        else:
            UPDATE_BD("musics", "music_on = 0")

    def __sound(self):
        self.sound_on = set_music_or_sounds(self.sound, self.sound_on, self.sound_player)
        if self.sound_on:
            UPDATE_BD("musics", "sound_on = 1")
        else:
            UPDATE_BD("musics", "sound_on = 0")

    def __play(self):
        self.tabWidget.setCurrentIndex(3)
        self.start, self.score_on = True, True
        self.progressBar.setValue(self.HP)

    def __replace_color(self):
        if self.replace_color_text_on:
            self.__replace_color_text(True)
        self.r = self.red_dial.value()
        self.g = self.green_dial.value()
        self.b = self.blue_dial.value()
        self.set_style_all_btn(self.all_btn, True)

    def __replace_colorSQL(self):
        if self.replace_color_text_on:
            self.__replace_color_text(True, True)
        self.__replace_color()
        UPDATE_BD("colors", f"red_btn = {self.r}, green_btn = {self.g}, blue_btn = {self.b}")

    def __replace_color_default(self):
        if not self.timer_go:
            if self.replace_color_text_on:
                self.__replace_color_text(True)
            self.color_timer = QtCore.QTimer()
            self.color_timer.timeout.connect(self.__replace_color)
            self.color_timer.start(60)
            self.timer_go = True
        else:
            self.timer_go = False
            self.color_timer.stop()

    def set_style_all_btn(self, arr, new_color=False, param=None):
        for i in arr:
            if new_color:
                i.setStyleSheet(self.set_style_btn(self.r, self.g, self.b))
            else:
                i.setStyleSheet(self.set_style_btn()) if param is None else i.setStyleSheet(self.set_style_btn(param))

    def set_style_btn(self, r=82, g=70, b=56, a=255, padding_x=60):
        return f"""QPushButton {'{'
    f"padding: 20px {padding_x}px;"
    "border-radius: 30px;"
    "border-left: 1px solid rgb(170, 170, 170);"
    "border-top: 1px solid rgb(170, 170, 170);"
    "border-right: 2px solid rgb(170, 170, 170);"
    "border-bottom: 2px solid rgb(170, 170, 170);"
'}'}

QPushButton:enabled {'{'
    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
    f"rgba{r, g, b, a}, stop:1 rgba{255 * self.r / 255, 255 * self.g / 255, 255 * self.b / 255, a});"
    "color: white;"
    '}'}

QPushButton:pressed {'{'
    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
    f"rgba{r - 8, g - 21, b - 7, a}, stop:1 "
    f"rgba{255 * self.r / 255, 255 * self.g / 255, 255 * self.b / 255, a});"
    "color: white;"
    "border-right: 1px solid rgb(170, 170, 170);"
    "border-bottom: 1px solid rgb(170, 170, 170);"
    "border-left: 2px solid rgb(170, 170, 170);"
    "border-top: 2px solid rgb(170, 170, 170);"
'}'}

QPushButton:hover:!pressed {'{'
    "background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 "
    f"rgba{r, g + 4, b + 25, a}, stop:1 "
    f"rgba{255 * self.r / 255, 255 * self.b / 255, 255 * self.b / 255, a});"
    "color: white;"
'}'}"""

    @staticmethod
    def set_style_tabWidget():
        return f"""QTabWidget::pane {'{'
    "margin-top: -10px;"
    "border: 0px;"
    "background-repeat: no repeat;"
    "margin: 0px;"
    "padding: 0px;"
'}'}

QTabBar::tab {'{'
    "margin: 0px;"
    "padding: 0px;"
'}'}"""


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ui = MenuWidget()
    ui.show()
    sys.exit(app.exec_())
