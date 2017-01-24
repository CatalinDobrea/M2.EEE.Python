import random

# These are the winning coefficients for every sum of the two dice face. The coefficinets are inversely proportional
# with probabilities and are computed in such a way that on average the casino gets 10% profit

probas = [0.0278, 0.0556, 0.0833, 0.1111, 0.1389, 0.1667, 0.1389, 0.1111, 0.0833, 0.0556, 0.0278]
Coeff = [0.9 / j for j in probas]


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
            dice = random.randint(1, 6) + random.randint(1, 6)
            output = []
            for item in bet:
                output.append(bool(item == dice))
            print(" Throwing the dice")
            print(" The sum of the upper faces  ", dice)
            if sum(output) > 0:
                print(" There are ", sum(output), " winner(s)")
            else:
                print("No player won")
            return output

        a = AboveMinimum(amount)
        r = RollTheDice(bet)
        qualify = [i * j for i, j in zip(a, r)]
        playergains = [i * Coeff[k-2] * j for i, k, j in zip(amount, bet, qualify)]
        casinogain = sum(amount) - sum(playergains)
        return [casinogain, playergains]
