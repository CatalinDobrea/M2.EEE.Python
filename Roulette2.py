import random
class Roulette(object):

    def SimulateGame(amounts):
        minimum = random.choice([50, 100, 200])
        A=[]
        bets = [random.randint(0,36) for i in amounts]
        for item in amounts:
            A.append(bool(item >= minimum))
        winnumb = random.randint(0, 36)
        rightnumber= []
        for item in bets:
            rightnumber.append(bool(item == winnumb))
        print(" Spinning the wheel...")
        print(" Ball lands on " + str(winnumb))
        if sum(rightnumber) > 0:
            print(" There are " + str(sum(rightnumber)) + " correct bet(s)")
        else:
            print("No winners this round")

        PlayerGains = [i * j * k * 30 for i, j, k in zip(amounts, A, rightnumber)]
        CasinoGain = sum(amounts) - sum(PlayerGains)
        return [CasinoGain, PlayerGains]