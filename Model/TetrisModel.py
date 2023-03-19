import random
from copy import deepcopy

class TetrisModel:
    _PIECES = [
        [['*', '*', '*', '*']],
        [['*', ' '], ['*', ' '], ['*', '*']],
        [[' ', '*'], [' ', '*'], ['*', '*']],
        [[' ', '*'], ['*', '*'], ['*', ' ']],
        [['*', '*'], ['*', '*']]
    ]

    def __init__(self):
        self.board_width = 12
        self.board = [[' ' for _ in range(self.board_width)] for _ in range(self.board_width)]
        self.settled_board = [[' ' for _ in range(self.board_width)] for _ in range(self.board_width)]
        self.current_piece = self.__get_random_piece()
        self.next_piece = self.__get_random_piece()
        self.current_row = 0
        self.current_col = random.randint(0, self.board_width-len(self.current_piece[0])-1)

    def __get_random_piece(self):
        return random.choice(self._PIECES)

    def __rotate_piece(self, piece, clockwise=True):
        if clockwise:
            return [[piece[y][x] for y in range(len(piece))] for x in range(len(piece[0]) - 1, -1, -1)]
        else:
            return [[piece[y][x] for y in range(len(piece) - 1, -1, -1)] for x in range(len(piece[0]))]

    def __is_valid_move(self, new_row, new_col, piece):
        for x in range(len(piece)):
            for y in range(len(piece[x])):
                if piece[x][y] == '*':
                    if new_row + x >= len(self.board) or new_col + y < 0 or new_col + y >= len(self.board[0]):
                        return False
                    elif self.settled_board[new_row + x][new_col + y] != ' ':
                        return False
        return True

    def __update_board(self):
        # Place current piece on board
        current_board =  deepcopy(self.settled_board)
        for x in range(len(self.current_piece)):
            for y in range(len(self.current_piece[x])):
                if self.current_piece[x][y] == '*':
                    current_board[self.current_row + x][self.current_col + y] = '*'

        # Check for full rows and remove them
        full_rows = []
        for row in range(len(current_board)):
            if ' ' not in current_board[row]:
                full_rows.append(row)

        if full_rows:
            for row in full_rows:
                current_board.pop(row)
                current_board.insert(0, [' ' for _ in range(12)])
        
        

        if self.is_last_move_of_current_piece():
            self.settled_board = deepcopy(current_board)
            print("Current Piece Settled!")
            # Update current piece and next piece
            self.current_piece = self.next_piece
            self.next_piece = self.__get_random_piece()
            self.current_row = 0
            self.current_col = random.randint(0, self.board_width-len(self.current_piece[0])-1)
        
        self.board = current_board

    def is_last_move_of_current_piece(self):
        cur_last_row = self.current_row + len(self.current_piece)
        if cur_last_row == len(self.settled_board):
            return True
        for y in range(len(self.current_piece[0])):
            col = self.current_col+y
            if (self.settled_board[cur_last_row][col]=='*' and self.current_piece[len(self.current_piece)-1][y]=='*'):
                return True
        return False

    def update(self, action):
        if action == 'a':
            new_row = self.current_row + 1
            new_col = self.current_col - 1
        elif action == 'd':
            new_row = self.current_row + 1
            new_col = self.current_col + 1
        elif action == 'w':
            new_piece = self.__rotate_piece(self.current_piece)
            if self.__is_valid_move(self.current_row + 1, self.current_col, new_piece):
                self.current_piece = new_piece
                new_row = self.current_row + 1
                new_col = self.current_col
            else:
                return False
        elif action == 's':
            new_piece = self.__rotate_piece(self.current_piece, clockwise=False)
            if self.__is_valid_move(self.current_row + 1, self.current_col, new_piece):
                self.current_piece = new_piece
                new_row = self.current_row + 1
                new_col = self.current_col
            else:
                return False
        elif action == '':
            new_row = self.current_row + 1
            new_col = self.current_col
        else:
            return False

        if self.__is_valid_move(new_row, new_col, self.current_piece):
            self.current_row = new_row
            self.current_col = new_col
            self.__update_board()
            return True
        else:
            return False

    def handle_end_of_game(self):
        if not self.__is_valid_move(self.current_row, self.current_col, self.current_piece):
            print("Game Over!")
            return True
            # do something else here if desired

