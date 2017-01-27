import random
# random.seed(2)

nbRoulette = 10
nbCraps = 10
nbBarmen = 4
EmployeeWage = 200
CasionStartCash = 50000
nbCustomers = 100
prcReturning = 50
prcBachelor = 10
BachelorFree = 200


# The first step of the simulation is to create the casino iself, or more exactly the tables in that casino
# Bassically we generate a list of tables, which will store the information about those table (number, the type of game
# played on that particular table, and the minimum amount that can be betted on that particular table). The inputs of this
# function are the actual number of Roullette and Craps tables.

def TableWithPlayersGen(table, nrcustomer):
    listoftables = []
    for i in range(1,len(table)+1):
        tableplayers = []
        for j in range(nrcustomer):
            if Customers[j].table[0] == i:
                tableplayers.append(Customers[j])
        listoftables.append(tableplayers)
    return listoftables

# So we apply this function in order to get the list of objects sorted by table
TableWithPlayers = TableWithPlayersGen(CasinoTables, nbCustomers)


class Customer(object):
    def __init__(self, typeC, ID):
        self.typeC = typeC
        self.ID = ID
        self.table = random.choice(CasinoTables)
        if self.typeC == "Returning":
            self.budget = random.randint(100, 300)
            if self.budget >= self.table[2]:
                self.bet = self.table[2]
            elif self.budget < self.table[2]:
                self.bet = 0
            self.bet = self.table[2]
        elif self.typeC == "New":
            self.budget = random.randint(200, 300)
            self.bet = random.randint(0, int((self.budget) / 3))
        else:
            self.budget = random.randint(200, 500) + BachelorFree
            self.bet = random.randint(0, int(self.budget))
    def setBudget(self,budget):
        self.budget = self.budget + budget

# Te following step is to create the customers, and only information that we hold about them is their type, so basically
# we create a list with the number of all the 3 types of costumers, and then using the Customer object we will create a
# list of objects that will have the information about all the Customers

class Table(object):
    def __init__(self, number):
        self.number = number
        self.Players = TableWithPlayers[number-1]
        self.AmountsBetted = []
        self.type = type
        for i in range(len(self.Players)):
            self.AmountsBetted.append(self.Players[i].bet)


    def SimulateGame(self):

        if CasinoTables[self.number-1][1] == "roulette":
            MinimumBet = CasinoTables[self.number-1][2]
            Amounts = self.AmountsBetted
            Bets = [random.randint(0,36) for i in Amounts]

            def AboveMinimum(amts):
                output = []
                for item in amts:
                    output.append(bool(item >= MinimumBet))
                return output

            def SpinTheWheel(bts):
                winnumb = random.randint(0, 36)
                output = []
                for item in bts:
                    output.append(bool(item == winnumb))
                print(" Spinning the wheel...")
                print(" Ball lands on " + str(winnumb))
                if sum(output) > 0:
                    print(" There are " + str(sum(output)) + " correct bet(s)")
                else:
                    print("No winners this round")
                return (output)

            A=AboveMinimum(Amounts)
            S=SpinTheWheel(Bets)
            PlayerGains = [i * j * k * 30 for i, j, k in zip(Amounts, A, S)]
            CasinoGain = sum(Amounts) - sum(PlayerGains)
            if CasinoGain > 0:
                CasinoGain = CasinoGain * 0.95

            for i in range(len(self.Players)):
                self.Players[i].setbudget(PlayerGains[i] - Amounts[i])

            return [CasinoGain, PlayerGains,Amounts,Bets]


        elif CasinoTables[self.number-1][1] == "craps":
            MinimumBet = CasinoTables[self.number-1][2]
            Amounts = self.AmountsBetted
            Bets = [random.randint(2,12) for i in Amounts ]

            def AboveMinimum(amts):
                output = []
                for item in amts:
                    output.append(bool(item >= MinimumBet))
                return output

            def RollTheDice(bts):
                dice = random.randint(1, 6) + random.randint(1, 6)
                output = []
                for item in bts:
                    output.append(bool(item == dice))
                print(" Throwing the dice")
                print(" The sum of the upper faces  ", dice)
                if sum(output) > 0:
                    print(" There are ", sum(output), " winner(s)")
                else:
                    print("No player won")
                return output

            A = AboveMinimum(Amounts)
            R = RollTheDice(Bets)

            Probs = list([i / 36 for i in range(1, 6)]) + [6 / 36] + list(reversed([i / 36 for i in range(1, 6)]))
            Coeff = [0.9 / i for i in Probs]

            PlayerGains = [i * Coeff[k-2] * j * l for i, k, j, l in zip(Amounts, Bets, A, R)]
            CasinoGain = sum(Amounts) - sum(PlayerGains)
            for i in range(len(self.Players)):
                self.Players[i].setBudget(PlayerGains[i] - Amounts[i])
            return [CasinoGain, PlayerGains,Amounts,Bets]

def CustomerTypes(total, returning, bachelor):
        customers=[]
        ret = int(total * (returning / 100))
        bch = int(total * (bachelor / 100))
        new = total - (ret + bch)
        for i in range(ret):
            customers.append(Customer('Returning', i))
        for i in range(new):
            customers.append(Customer('New', i + ret))
        for i in range(bch):
            customers.append(Customer('Bachelor', i + new + ret))
        return customers

def CasinoTablesGen(nbR, nbC):
    tables = []
    for i in range(nbR):
        tables.append(Table(i+1))
    for i in range(nbC):
        tables.append(Table(i+nbR+1))
    return(tables)
print(CasinoTablesGen(nbRoulette, nbCraps))
# then we use that function to generate the tables
CasinoTables = CasinoTablesGen(nbRoulette,nbCraps)



# Then we actually make that list given the total number of costumers, the percentage of returning customers and the percentage
# of Bachelors
Customers = CustomerTypes(nbCustomers, prcReturning, prcBachelor)
initamounts = []
for i in range(len(Customers)):
    initamounts.append(Customers[i].budget)


# Then knowing that for the first round each customer has already defined the table at which he will play, we can create
# another list with with exact same information, but now sorted by table, so bassically the first term of that list will
# carry all the information about all the players that are at that particular moment at that particular table.








# for i in range(nbRoulette+nbCraps):
#     Table(i).SimulateGame()
#
# finamounts = []
# for i in range(len(Customers)):
#     finamounts.append(Customers[i].budget)

# print(zip(initamounts, finamounts))



# print(initamounts)
# print(finamounts)
#
