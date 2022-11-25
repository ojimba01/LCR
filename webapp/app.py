from game import Game
from player import Player

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