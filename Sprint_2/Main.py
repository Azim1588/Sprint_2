from PyQt5.QtWidgets import QApplication
import sys
from Game import Game
from View import View

if __name__ == "__main__":
    # Ensure the game starts with no terminal input
    app = QApplication(sys.argv)
    game = Game()  # Initialize the game with a default size; size can change via GUI.
    view = View(game)
    view.show()
    
    # Start the event loop
    sys.exit(app.exec_())


