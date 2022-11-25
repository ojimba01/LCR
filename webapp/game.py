from dice import Dice
class Game:
    def __init__(self, players):
        self.players = players
        self.dice = Dice()
        self.pot = 0
        
        self.turn = 0
        self.player = self.players[self.turn]
        self.winner = None
        self.game_over = False

    def play(self):
        while not self.game_over:
            self.player = self.players[self.turn]
            self.player.take_turn(self)
            self.turn += 1
            if self.turn == len(self.players):
                self.turn = 0
        
            if len([player for player in self.players if player.chips > 0]) == 1:
                self.game_over = True
                self.winner = [player for player in self.players if player.chips > 0][0]
                print(f"{self.winner.name} wins!")

            if len(self.players) == 1:
                self.winner = self.players[0]
                self.game_over = True

        if self.player.chips <= 0:
            self.player.chips = 0
            self.turn += 1
                