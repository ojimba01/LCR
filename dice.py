import random
class Dice:
    def __init__(self):
        self.sides = 6

    def roll(self, num_dice):
        rolls = []
        for i in range(num_dice):
            rolls.append(random.randint(1, self.sides))
        return rolls