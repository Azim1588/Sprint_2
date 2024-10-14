from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout, QHBoxLayout, QMessageBox, QComboBox, QFrame
from PyQt5.QtCore import Qt
from Game import Game  # Import the Game class

class View(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Tic-Tac-Toe')
        self.setStyleSheet("background-color: #20c997;")
        
        # Create the main layout
        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Board Size and Game Mode Layout
        board_game_mode_layout = QHBoxLayout()
        
        # Board Size selection
        board_size_label = QLabel("Choose board size:", self)
        board_size_label.setStyleSheet("font-size: 20px;")
        self.board_size_combo = QComboBox(self)
        self.board_size_combo.addItems(["3", "4", "8", "10"])
        self.board_size_combo.setStyleSheet("font-size: 20px;")

        # Game Mode selection
        game_mode_label = QLabel("Choose game mode:", self)
        game_mode_label.setStyleSheet("font-size: 20px;")
        self.game_mode_combo = QComboBox(self)
        self.game_mode_combo.addItems(["Simple Game", "General Game"])
        self.game_mode_combo.setStyleSheet("font-size: 20px;")

        # Connect dropdown changes to game reset
        self.board_size_combo.currentIndexChanged.connect(self.start_new_game_with_settings)
        self.game_mode_combo.currentIndexChanged.connect(self.start_new_game_with_settings)

        # Add board size and game mode widgets to layout
        board_game_mode_layout.addWidget(board_size_label)
        board_game_mode_layout.addWidget(self.board_size_combo)
        board_game_mode_layout.addWidget(game_mode_label)
        board_game_mode_layout.addWidget(self.game_mode_combo)
        board_game_mode_layout.setAlignment(Qt.AlignCenter)

        # Add the layout to the main layout
        main_layout.addLayout(board_game_mode_layout)

        # Create a horizontal layout for player selections
        player_layout = QHBoxLayout()

        # Player 1 Selection on the left
        player1_layout = QVBoxLayout()
        player1_label = QLabel("Player 1", self)
        player1_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        player1_symbol_label = QLabel("Choose symbol (X or O):", self)
        player1_symbol_label.setStyleSheet("font-size: 16px;")
        self.player1_symbol_combo = QComboBox(self)  # Initialize this combo box for Player 1 symbols
        self.player1_symbol_combo.addItems(["X", "O"])
        self.player1_symbol_combo.setStyleSheet("font-size: 16px;")

        player1_color_label = QLabel("Choose color (Blue or Red):", self)
        player1_color_label.setStyleSheet("font-size: 16px;")
        self.player1_color_combo = QComboBox(self)  # Initialize this combo box for Player 1 colors
        self.player1_color_combo.addItems(["Blue", "Red"])
        self.player1_color_combo.setStyleSheet("font-size: 16px;")

        player1_layout.addWidget(player1_label)
        player1_layout.addWidget(player1_symbol_label)
        player1_layout.addWidget(self.player1_symbol_combo)
        player1_layout.addWidget(player1_color_label)
        player1_layout.addWidget(self.player1_color_combo)
        player1_layout.setAlignment(Qt.AlignLeft)

        # Player 2 Selection on the right
        player2_layout = QVBoxLayout()
        player2_label = QLabel("Player 2", self)
        player2_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        player2_symbol_label = QLabel("Choose symbol (X or O):", self)
        player2_symbol_label.setStyleSheet("font-size: 16px;")
        self.player2_symbol_combo = QComboBox(self)  # Initialize this combo box for Player 2 symbols
        self.player2_symbol_combo.addItems(["X", "O"])
        self.player2_symbol_combo.setStyleSheet("font-size: 16px;")

        player2_color_label = QLabel("Choose color (Red or Blue):", self)
        player2_color_label.setStyleSheet("font-size: 16px;")
        self.player2_color_combo = QComboBox(self)  # Initialize this combo box for Player 2 colors
        self.player2_color_combo.addItems(["Red", "Blue"])
        self.player2_color_combo.setStyleSheet("font-size: 16px;")

        player2_layout.addWidget(player2_label)
        player2_layout.addWidget(player2_symbol_label)
        player2_layout.addWidget(self.player2_symbol_combo)
        player2_layout.addWidget(player2_color_label)
        player2_layout.addWidget(self.player2_color_combo)
        player2_layout.setAlignment(Qt.AlignRight)

        # Add both player layouts to the main horizontal layout
        player_layout.addLayout(player1_layout)
        player_layout.addStretch()
        player_layout.addLayout(player2_layout)

        # Add player layout to the main layout
        main_layout.addLayout(player_layout)

        # Game board layout (Grid for buttons)
        self.grid_layout = QGridLayout()
        main_layout.addLayout(self.grid_layout)

        # Status Label at the bottom
        self.status_label = QLabel('Start a new game to begin', self)
        self.status_label.setStyleSheet("color: white; font-size: 20px;")
        self.status_label.setAlignment(Qt.AlignCenter)
        main_layout.addWidget(self.status_label)

        # New Game Button
        self.new_game_button = QPushButton('New Game', self)
        self.new_game_button.clicked.connect(self.start_new_game_with_settings)
        main_layout.addWidget(self.new_game_button, alignment=Qt.AlignCenter)

    def start_new_game_with_settings(self):
        # Get the selected board size and game mode from the dropdowns
        size = int(self.board_size_combo.currentText())
        game_mode = self.game_mode_combo.currentText()

        # Get selected symbols and colors for both players
        player1_symbol = self.player1_symbol_combo.currentText()
        player1_color = self.player1_color_combo.currentText().lower()  # Convert color to lowercase for consistency
        player2_symbol = self.player2_symbol_combo.currentText()
        player2_color = self.player2_color_combo.currentText().lower()

        # Set up the game with the selected options
        self.controller.restart_game(size, player1_symbol, player1_color, player2_symbol, player2_color, game_mode)
        self.reset_board(size)
        self.update_display()

    def reset_board(self, size):
        # Reset the grid layout for the new board size
        for i in reversed(range(self.grid_layout.count())):
            self.grid_layout.itemAt(i).widget().setParent(None)

        self.buttons = [[QPushButton() for _ in range(size)] for _ in range(size)]

        for i in range(size):
            for j in range(size):
                self.buttons[i][j].setFixedSize(140, 140)
                self.buttons[i][j].setStyleSheet("font-size: 30px;")
                self.buttons[i][j].clicked.connect(lambda _, row=i, col=j: self.on_click(row, col))
                self.grid_layout.addWidget(self.buttons[i][j], i, j)

    def on_click(self, row, col):
        result = self.controller.play_turn(row, col)
        current_player = self.controller.players[self.controller.current_player_index]
        symbol = current_player.symbol

        # Update the button text and color based on the symbol
        if symbol == "X":
            self.buttons[row][col].setStyleSheet("color: blue; font-size: 40px;")
        elif symbol == "O":
            self.buttons[row][col].setStyleSheet("color: red; font-size: 40px;")
        
        self.buttons[row][col].setText(symbol)
        self.buttons[row][col].setEnabled(False)  # Disable the button after it's clicked

        if "wins" in result or "draw" in result:
            QMessageBox.information(self, 'Game Over', result)
            self.reset_board(self.controller.board.size)
        self.update_display()

    def update_display(self):
        current_player = self.controller.players[self.controller.current_player_index]
        self.status_label.setText(f"{current_player.name}'s turn")
