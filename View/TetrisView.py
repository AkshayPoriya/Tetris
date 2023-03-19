from Model.TetrisModel import *

class TetrisView:
    def __init__(self, model: TetrisModel):
        self.model = model

    def __draw_board(self):
        """Draws the game board."""
        board = self.model.board
        for row in board:
            print('|', end=' ')
            for cell in row:
                print(cell, end=' ')
            print('|')
        print('-' * 26)

    def __draw_piece(self, piece, board_row, board_col):
        """Draws a piece on the game board."""
        for i, row in enumerate(piece):
            for j, char in enumerate(row):
                if char == '*':
                    self.model.board[board_row+i][board_col+j] = char
        
        self.__draw_board()

    def __clear_piece(self, piece, row, col):
        """Clears a piece from the game board."""
        for i, row in enumerate(piece):
            for j, char in enumerate(row):
                if char == '*':
                    self.model.board[row+i][col+j] = ' '

    def display(self):
        """Displays the game state."""
        #self.draw_board()
        self.__draw_piece(self.model.current_piece, self.model.current_row, self.model.current_col)
