import random
# This is used to fixethe random generator so we can test the output
random.seed(3456)


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

        Coeff = [42.65, 35.54, 28.43, 21.32, 14.21, 7.11, 14.21, 21.23, 28.43, 35.54, 42.65]
        a = AboveMinimum(amount)
        r = RollTheDice(bet)
        qualify = [i * j for i, j in zip(a, r)]
        if sum(qualify) == 0:
            playergains = [0 for i in amount]
            casinogain = sum(amount)
        else:
            playergains = [i * Coeff[k-2] * j for i, k, j in zip(amount, bet, qualify)]
            casinogain = sum(amount) - sum(playergains)
        return [casinogain, playergains]