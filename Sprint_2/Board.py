class Board:
    def __init__(self, size=3):
        self.size = size
        self.board = [["" for _ in range(size)] for _ in range(size)]

    def update_board(self, row, col, symbol):
        if self.board[row][col] == "":
            self.board[row][col] = symbol
            return True
        return False

    def reset_board(self):
        self.board = [["" for _ in range(self.size)] for _ in range(self.size)]

    def is_full(self):
        return all(cell != "" for row in self.board for cell in row)

    def display_board(self):
        # This method can be used for debugging purposes to print the board
        for row in self.board:
            print(row)
