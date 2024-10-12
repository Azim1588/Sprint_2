import unittest
from Game import Game
from Board import Board
from Player import Player

class TestTicTacToe(unittest.TestCase):

    # Test board initialization
    def test_board_initialization(self):
        board = Board(3)  # Create a 3x3 board
        self.assertEqual(len(board.board), 3)  # Test if the board size is correct
        for row in board.board:
            self.assertEqual(len(row), 3)  # Test if each row has the correct number of columns
            self.assertTrue(all(cell == "" for cell in row))  # Test if all cells are empty

    # Test board update
    def test_board_update(self):
        board = Board(3)
        result = board.update_board(0, 0, "X")  # Test if placing an X works
        self.assertTrue(result)  # Should return True for valid move
        self.assertEqual(board.board[0][0], "X")  # Test if the cell is updated

        # Test an invalid move (placing in the same spot)
        result = board.update_board(0, 0, "O")
        self.assertFalse(result)  # Should return False for invalid move

    # Test resetting the board
    def test_reset_board(self):
        board = Board(3)
        board.update_board(0, 0, "X")
        board.reset_board()
        for row in board.board:
            self.assertTrue(all(cell == "" for cell in row))  # All cells should be reset to empty

    # Test player initialization
    def test_player_initialization(self):
        player = Player("Player 1", "X", "blue")
        self.assertEqual(player.name, "Player 1")
        self.assertEqual(player.symbol, "X")
        self.assertEqual(player.color, "blue")

    # Test game initialization
    def test_game_initialization(self):
        game = Game(3)
        game.restart_game(3, "X", "blue", "O", "red")
        self.assertEqual(game.board.size, 3)  # Test board size
        self.assertEqual(game.players[0].symbol, "X")  # Test if Player 1 symbol is X
        self.assertEqual(game.players[1].symbol, "O")  # Test if Player 2 symbol is O

    # Test a valid move
    def test_valid_move(self):
        game = Game(3)
        game.restart_game(3, "X", "blue", "O", "red")
        result = game.play_turn(0, 0)
        self.assertEqual(game.board.board[0][0], "X")  # Test if X is placed correctly
        self.assertIn("Player 2's turn", result)  # Next player's turn

    # Test invalid move
    def test_invalid_move(self):
        game = Game(3)
        game.restart_game(3, "X", "blue", "O", "red")
        game.play_turn(0, 0)  # Valid move
        result = game.play_turn(0, 0)  # Invalid move
        self.assertEqual(result, "Invalid move")  # Should return invalid move message

    # Test win condition (horizontal win)
    def test_horizontal_win(self):
        game = Game(3)
        game.restart_game(3, "X", "blue", "O", "red")
        game.play_turn(0, 0)  # X
        game.play_turn(1, 0)  # O
        game.play_turn(0, 1)  # X
        game.play_turn(1, 1)  # O
        result = game.play_turn(0, 2)  # X wins horizontally
        self.assertIn("Player 1 wins!", result)

    # Test win condition (vertical win)
    def test_vertical_win(self):
        game = Game(3)
        game.restart_game(3, "X", "blue", "O", "red")
        game.play_turn(0, 0)  # X
        game.play_turn(0, 1)  # O
        game.play_turn(1, 0)  # X
        game.play_turn(1, 1)  # O
        result = game.play_turn(2, 0)  # X wins vertically
        self.assertIn("Player 1 wins!", result)

    # Test draw condition
    def test_draw_condition(self):
        game = Game(3)
        game.restart_game(3, "X", "blue", "O", "red")
        game.play_turn(0, 0)  # X
        game.play_turn(0, 1)  # O
        game.play_turn(0, 2)  # X
        game.play_turn(1, 1)  # O
        game.play_turn(1, 0)  # X
        game.play_turn(1, 2)  # O
        game.play_turn(2, 1)  # X
        game.play_turn(2, 0)  # O
        result = game.play_turn(2, 2)  # Draw
        self.assertIn("It's a draw!", result)

    # Test game reset after a win
    def test_game_reset_after_win(self):
        game = Game(3)
        game.restart_game(3, "X", "blue", "O", "red")
        game.play_turn(0, 0)  # X
        game.play_turn(0, 1)  # O
        game.play_turn(1, 0)  # X
        game.play_turn(1, 1)  # O
        game.play_turn(2, 0)  # X wins
        self.assertIn("Player 1 wins!", game.play_turn(2, 0))
        game.restart_game(3, "X", "blue", "O", "red")
        self.assertTrue(all(cell == "" for row in game.board.board for cell in row))  # Board should be reset

if __name__ == '__main__':
    unittest.main()
