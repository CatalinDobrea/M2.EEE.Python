#test code for the roulette functioning and random gains
import Roulette
import random
import Craps
"""amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [10, 24, 36, 0, 11, 24]
table1 = Roulette.Roulette(100)
print(table1.simulategame(bets1, amounts1))
print(table1.simulategame(bets1, amounts1))"""

MinBet = [0, 25, 50]

casinogain = 0
playedsum = 0
for i in range(50000):
    players = random.randint(0,6)
    MinBetX = random.choice(MinBet)
    amount = random.sample(range(MinBetX,100),players)
    k = sum(amount)
    bet = random.sample(range(2,13),players)
    table1 = Craps.Craps(MinBetX)
    casinogain += table1.SimulateGame(bet, amount)[0]
    playedsum +=k
casinoprofitshare = casinogain / playedsum
print(casinoprofitshare)
