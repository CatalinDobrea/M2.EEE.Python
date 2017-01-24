import random
# This is used to fixethe random generator so we can test the output

class Craps:
    def __init__(self, min):
        self.min = min

    def SimulateGame(self, bet, amount):

        def AboveMinimum(amount):
            output = []
            for item in amount:
                output.append(bool(item >= self.min))
            return output

        def RollTheDice(bet):
            Dices = random.randint(1, 6) + random.randint(1, 6)
            output = []
            for item in bet:
                output.append(bool(item == Dices))
            print(" Throwing the dice")
            print(" The sum of the upper faces  ", Dices)
            if sum(output) > 0:
                print(" There are ", sum(output), " winner(s)")
            else:
                print("No player won")
            return output

        probas = [0.0278, 0.0556, 0.0833, 0.1111, 0.1389, 0.1667, 0.1389, 0.1111, 0.0833, 0.0556, 0.0278]
        Coeff = [0.9 /j for j in probas]

        a = AboveMinimum(amount)
        r = RollTheDice(bet)
        qualify = [i * j for i, j in zip(a, r)]
        playergains = [i * Coeff[k-2] * j for i, k, j in zip(amount, bet, qualify)]
        casinogain = sum(amount) - sum(playergains)
        return [casinogain, playergains]