from PyQt5 import QtCore
from pygame_project import GameWidget
from menu import MenuWidget


class Result(MenuWidget, GameWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400, 200, 800, 400)
        self.timer_while = QtCore.QTimer()
        self.timer_while.timeout.connect(self.__update)
        self.timer_while.start()
        self.HP = 100

    def __update(self):
        if self.pause_on:
            self.start, self.pause_on, self.score_on, self.game_timer_on = False, False, False, False
            self.play.setText("Продолжить игру")
            self.game_timer.stop()
            self.tabWidget.setCurrentIndex(0)
        elif self.start:
            self.progressBar.setValue(self.HP)

            if not self.game_timer_on:
                self.game_timer_on = True
                self.game_timer.start(5)

            if not self.progressBar.value():
                self.score = 0
                self.score_on, self.start = False, False
                self.play.setText("Играть")
                self.tabWidget.setCurrentIndex(0)

            if self.score != int(self.game_score.text()[self.game_score.text().index(':') + 1:]):
                self.game_score.setText(
                    f"{self.game_score.text()[:self.game_score.text().index(':') + 1]} {self.score}")


if __name__ == "__main__":
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    w = Result()
    w.show()
    sys.exit(app.exec_())
