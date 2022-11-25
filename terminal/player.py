import time
from game import Game
class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 3


    def take_turn(self, game):
        
        print(f"{self.name}'s turn")
        print(f"{self.name} has {self.chips} chips")
        print(f"There are {game.pot} chips in the pot")
        print("Rolling dice...")
        time.sleep(1)
        # Prof input below #
        numdice = self.chips
        if numdice > 3:
            numdice = 3
        rolls = game.dice.roll(numdice)
        #-------------------------------#
        
        print(rolls)
        for roll in rolls:
            if roll == 4:
                print(f"{self.name} rolled an L")
                self.give_chip(game.players[game.turn - 1])
            elif roll == 5:
                print(f"{self.name} rolled a C")
                self.put_in_pot(game)
            elif roll == 6:
                print(f"{self.name} rolled an R")
                if game.turn == len(game.players) - 1:
                    self.give_chip(game.players[0])
                else:
                    self.give_chip(game.players[game.turn + 1])
            else:
                print(f"{self.name} rolled a dot")
        print(f"{self.name} has {self.chips} chips")
        print(f"There are {game.pot} chips in the pot")
        for player in game.players:
            print(f"{player.name} has {player.chips} chips, ", end=" ")
        print("Press enter to continue")
        input()
    def give_chip(self, player):
        self.chips -= 1
        player.chips += 1

        

    def put_in_pot(self, game):
        self.chips -= 1
        game.pot += 1
