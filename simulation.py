import Roulette
import random
import Craps
"""amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [10, 24, 36, 0, 11, 24]
table1 = Roulette.Roulette(100)
print(table1.simulategame(bets1, amounts1))
print(table1.simulategame(bets1, amounts1))"""

"""Coeff = [42.65, 35.54, 28.43, 21.32, 14.21, 7.11, 14.21, 21.23, 28.43, 35.54, 42.65]
probas = [0.0278, 0.0556, 0.0833, 0.1111, 0.1389, 0.1667, 0.1389, 0.1111, 0.0833, 0.0556, 0.0278]
altCoeff = [30.490974729241877, 14.216216216216218, 8.804321728691477, 6.100810081008101, 4.484149855907781,
            3.4021608643457384, 4.484149855907781, 6.100810081008101, 8.804321728691477, 14.216216216216218,
            30.490974729241877]
z = [i * j for i, j in zip(Coeff, probas)]
w = [i * j for i, j in zip(altCoeff, probas)]
x = [(0.9 - j)/j for j in probas]
print(x)
print(altCoeff)"""



out = [0,0]
MinBet = [0, 25, 50]

casinogain = 0
playedsum = 0
for i in range(10000):

    players = random.randint(0,6)
    MinBetX = random.choice(MinBet)
    amount = random.sample(range(MinBetX,100),players)
    k = sum(amount)
    bet = random.sample(range(2,13),players)
    table1 = Craps.Craps(MinBetX)
    casinogain += table1.SimulateGame(bet, amount)[0]
    playedsum +=k
print(casinogain)
print(playedsum)
print(casinogain/playedsum)
casinogain = 0


