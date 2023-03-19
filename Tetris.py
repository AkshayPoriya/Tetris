from Model.TetrisModel import *
from View.TetrisView import *
from Controller.TetrisController import *

class Tetris:
    def __init__(self):
        self.model = TetrisModel()
        self.view = TetrisView(self.model)
        self.controller = TetrisController(self.model, self.view)

    def play(self):
        self.controller.run_game()

if __name__ == '__main__':
    game = Tetris()
    game.play()
