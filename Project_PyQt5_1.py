from PyQt5.QtGui import QFont
from sqlite3 import connect


def set_font(size, bold, weight):
    font = QFont()
    font.setPointSize(size)
    font.setBold(bold)
    font.setWeight(weight)
    return font


def set_music_or_sounds(music_or_sounds, on, media_player, timer=None):
    on = not on
    if on:
        media_player.play()
        if timer is not None:
            timer.start(170000)
        music_or_sounds.setText(music_or_sounds.text().replace("выкл", "вкл"))
    else:
        if timer is not None:
            timer.stop()
        music_or_sounds.setText(music_or_sounds.text().replace("вкл", "выкл"))
        try:
            media_player.pause()
        except AttributeError:
            music_or_sounds.setText("Музыка: выкл")
    return on


def UPDATE_BD(table: str, update):
    with connect("pygame_YL.db") as con:
        cur = con.cursor()
        my_str = f"""UPDATE {table} set {update}"""
        cur.execute(my_str)


def replace_image(image, text_1, text_2):
    if image == text_1:
        image = text_2
    else:
        image = text_1

    return image
