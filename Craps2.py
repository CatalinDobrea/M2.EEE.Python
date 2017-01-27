import random
class Craps(object):

    def SimulateGame(amounts):
        A = []
        minimum = random.choice([0, 25, 50])
        for item in amounts:
            A.append(bool(item >=minimum))
        bets = [random.randint(2, 12) for i in amounts]
        dice = random.randint(1, 6) + random.randint(1, 6)
        rightbet = []
        for item in bets:
            rightbet.append(bool(item == dice))
        print(" Throwing the dice")
        print(" The sum of the upper faces  ", dice)
        if sum(rightbet) > 0:
            print(" There are ", sum(rightbet), " winner(s)")
        else:
            print("No player won")


        Probs = list([i / 36 for i in range(1, 6)]) + [6 / 36] + list(reversed([i / 36 for i in range(1, 6)]))
        Coeff = [0.9 / i for i in Probs]

        PlayerGains = [i * Coeff[k - 2] * j * l for i, k, j, l in zip(amounts, bets, A, rightbet)]
        CasinoGain = sum(amounts) - sum(PlayerGains)

        return [CasinoGain, PlayerGains]