from Model.TetrisModel import *
from View.TetrisView import *

class TetrisController:
    def __init__(self, model: TetrisModel, view: TetrisView):
        self.model = model
        self.view = view

    def get_user_input(self):
        while True:
            # Read user input from the command line
            action = input("Enter action (a=left, d=right, w=rotate, s=drop, space=fall): ").strip()
            # Validate user input
            if action in ['a', 'd', 'w', 's', '']:
                return action
            else:
                print("Invalid input, please try again.")

    def run_game(self):
        while True:
            self.view.display()
            action = self.get_user_input()
            if self.model.is_last_move_of_current_piece():
                print("No movement possible")
                break
            if not self.model.update(action):
                print("Invalid move, please try again.")
            if self.model.handle_end_of_game():
                break
        return False
