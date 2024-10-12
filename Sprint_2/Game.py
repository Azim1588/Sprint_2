
from Board import Board
from Player import Player

class Game:
    def __init__(self, board_size=3):
        self.board = Board(board_size)
        self.players = []
        self.current_player_index = 0

    def restart_game(self, size, player1_symbol, player1_color, player2_symbol, player2_color):
        self.board = Board(size)
        # Initialize players with the chosen symbol and color
        self.players = [
            Player("Player 1", player1_symbol, player1_color),
            Player("Player 2", player2_symbol, player2_color)
        ]
        self.current_player_index = 0

    def play_turn(self, row, col):
        current_player = self.players[self.current_player_index]
        if self.board.update_board(row, col, current_player.symbol):
            if self.check_win():
                return f"{current_player.name} wins!"
            elif self.board.is_full():
                return "It's a draw!"
            self.next_turn()
            return f"{self.players[self.current_player_index].name}'s turn"
        return "Invalid move"

    def check_win(self):
        board = self.board.board
        size = self.board.size

        # Check rows and columns
        for i in range(size):
            if all(board[i][j] == board[i][0] and board[i][0] != "" for j in range(size)):
                return True
            if all(board[j][i] == board[0][i] and board[0][i] != "" for j in range(size)):
                return True

        # Check diagonals
        if all(board[i][i] == board[0][0] and board[0][0] != "" for i in range(size)):
            return True
        if all(board[i][size - i - 1] == board[0][size - 1] and board[0][size - 1] != "" for i in range(size)):
            return True

        return False

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % 2
