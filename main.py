#Game: LCR
#Authors: Ollie, Nini, Ahmed
#Date: 10/03/2022
#Version: 3.0
#Comment: Most bugs regarding the chips properly looping around the players have been fixed. 
# The game now runs smoothly and is ready for the final version.


import random
import time

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

class Dice:
    def __init__(self):
        self.sides = 6

    def roll(self, num_dice):
        rolls = []
        for i in range(num_dice):
            rolls.append(random.randint(1, self.sides))
        return rolls

def main():
    print("Welcome to LCR")
    num_players = int(input("How many players? "))
    players = []
    for i in range(num_players):
        name = input(f"Player {i + 1} name: ")
        players.append(Player(name))
    game = Game(players)
    game.play()
    print(f"{game.winner.name} wins!")

if __name__ == "__main__":
    main()

