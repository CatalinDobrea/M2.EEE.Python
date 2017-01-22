import random

random.seed(3456)


class Roulette:
    def __init__(self, min):
        self.min = min

    def simulategame(self, bets, amount):

        def abovemin(amount):
            above = []
            for item in amount:
                above.append(bool(item >= self.min))
            return above

        def spinthewheel(bets):
            occ = random.randint(0, 36)
            print('Spinning the wheel...')
            print('The Ball lands on...', occ)
            correcte = []
            for item in bets:
                correcte.append(bool(item == occ))
            if correcte.count(True) == 0:
                print("No winners this round")
            else:
                print("There are", sum(correcte), "correct bets")
            return correcte

        y = abovemin(amount)
        z = spinthewheel(bets)
        playergains = [i*j*k for i, j, k in zip(amount, y, z)]
        casinogain = sum(amount) - sum(playergains)
        return [casinogain, [i*30 for i in playergains]]
