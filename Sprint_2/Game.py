
from Board import Board
from Player import Player

class Game:
    def __init__(self, board_size=3):
        self.board = Board(board_size)
        self.players = []
        self.current_player_index = 0
        self.game_mode = "Simple Game"  # Default game mode

    def restart_game(self, size, player1_symbol, player1_color, player2_symbol, player2_color, game_mode="Simple Game"):
        self.board = Board(size)
        self.game_mode = game_mode  # Store the game mode choice
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

        # Different win condition check logic based on game mode
        if self.game_mode == "Simple Game":
            return self.simple_game_check_win(board, size)
        elif self.game_mode == "General Game":
            return self.general_game_check_win(board, size)

        return False

    def simple_game_check_win(self, board, size):
        # Check win conditions for the simple game mode (default rules)
        for i in range(size):
            if all(board[i][j] == board[i][0] and board[i][0] != "" for j in range(size)):
                return True
            if all(board[j][i] == board[0][i] and board[0][i] != "" for j in range(size)):
                return True
        if all(board[i][i] == board[0][0] and board[0][0] != "" for i in range(size)):
            return True
        if all(board[i][size - i - 1] == board[0][size - 1] and board[0][size - 1] != "" for i in range(size)):
            return True
        return False

    def general_game_check_win(self, board, size):
        # Implement different rules for general game mode (this can be customized further)
        # This placeholder could implement a more complex rule set
        return self.simple_game_check_win(board, size)  # Currently reusing the same logic

    def next_turn(self):
        self.current_player_index = (self.current_player_index + 1) % 2
