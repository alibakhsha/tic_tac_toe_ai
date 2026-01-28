import copy

HUMAN = 'X'
AI = 'O'
EMPTY = None

class TicTacToe:
    def __init__(self):
        self.board = [[EMPTY]*3 for _ in range(3)]

    def available_moves(self):
        return [(r, c) for r in range(3) for c in range(3) if self.board[r][c] is EMPTY]

    def make_move(self, row, col, player):
        if self.board[row][col] is EMPTY:
            self.board[row][col] = player
            return True
        return False

    def undo_move(self, row, col):
        self.board[row][col] = EMPTY

    def is_winner(self, player):
        for i in range(3):
            if all(self.board[i][j] == player for j in range(3)):
                return True
            if all(self.board[j][i] == player for j in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True

        return False

    def is_draw(self):
        return all(self.board[r][c] is not EMPTY for r in range(3) for c in range(3))

    def is_terminal(self):
        return self.is_winner(HUMAN) or self.is_winner(AI) or self.is_draw()

    def evaluate(self):
        if self.is_winner(AI):
            return 1
        if self.is_winner(HUMAN):
            return -1
        return 0
