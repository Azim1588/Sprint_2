class Player:
    def __init__(self, name="", symbol="", color=""):
        self.name = name
        self.symbol = symbol
        self.color = color

    def choose_symbol(self, symbol):
        self.symbol = symbol

    def choose_color(self, color):
        self.color = color
