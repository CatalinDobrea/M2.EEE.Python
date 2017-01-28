import random

nbroulettetables = 10
nbcrapstables =10
nbbarmen = 4
employeewage = 200
startingcash = 50000
nbcustomers =100
sharereturningcustomers = 0.5
sharebachelorcustomers = 0.1
freestartbudget = 200

class customer(object):
    def __init__(self, custID, table=0, bet =0, budget=0):
        self.custID = custID
        self.table = table
        self.bet = bet
        self.budget = budget


class returningcustomer(customer):
    def __init__(self, custID, bet=0, table=0, budget=0):
        super(returningcustomer, self).__init__(custID)
        super(returningcustomer, self).__init__(table)
        super(returningcustomer, self).__init__(budget)
        super(returningcustomer, self).__init__(bet)
        self.budget = random.randint(100, 300)
    def setbet(self):
        if self.budget >= self.table.minimumbet:
            self.bet = self.table.minimumbet
        else:
            self.bet=0
    def sitdown(self, tablelist):
        self.table = random.choice(tablelist)
    def standup(self, table=0):
        self.table = table
    def updatewealth(self,update):
        self.budget += update -self.bet
class onetimecustomer(customer):

    def __init__(self, custID, table=0, bet=0, budget=0):
        super(onetimecustomer, self).__init__(custID)
        super(onetimecustomer, self).__init__(table)
        super(onetimecustomer, self).__init__(budget)
        super(onetimecustomer, self).__init__(bet)
        self.budget = random.randint(200, 300)
        self.bet = random.randint(0, self.budget)
    def sitdown(self, tablelist):
        self.table = random.choice(tablelist)
    def standup(self, table=0):
        self.table = table
    def updatewealth(self,update):
        self.budget += update -self.bet
    def setbet(self):
        return False
class bachelorcustomer(customer):
    def __init__(self, custID, table=0, budget=0, bet=0):
        super(bachelorcustomer, self).__init__(custID)
        super(bachelorcustomer, self).__init__(table)
        super(bachelorcustomer, self).__init__(budget)
        super(bachelorcustomer, self).__init__(bet)
        self.budget = random.randint(200, 500) + freestartbudget
        self.bet = random.randint(0, self.budget // 3)
    def sitdown(self, tablelist):
        self.table = random.choice(tablelist)
    def standup(self, table=0):
        self.table = table
    def updatewealth(self,update):
        self.budget += update -self.bet
    def setbet(self):
        return False

#Create the customers
# loscostumers = []
# for i in range(int(sharereturningcustomers * nbcustomers)):
#     loscostumers.append(returningcustomer(i+1))
# for i in range(int(sharereturningcustomers * nbcustomers +1), int(sharereturningcustomers * nbcustomers + sharebachelorcustomers * nbcustomers)):
#     loscostumers.append((bachelorcustomer(i+1)))
# for i in range(int(sharereturningcustomers * nbcustomers + sharebachelorcustomers * nbcustomers +1), int(nbcustomers)):
#     loscostumers.append((onetimecustomer(i+1)))

#print(range(int(sharereturningcustomers * nbcustomers)))
#print(range(int(sharereturningcustomers * nbcustomers +1), int(sharereturningcustomers * nbcustomers + sharebachelorcustomers * nbcustomers)))

####### Here should the function for one round start
#Sitdown players for a round
# for i in range(0, len(loscostumers)):
#     loscostumers[i].sitdown(lostables)

# print(range(0,len([1,2,3,4,5])))

# #Create a list with lists of players for each table
#
# jugadores = [[] for item in lostables]
# for z in range(0, len(jugadores)-1):
#     for item in range(0, len(loscostumers)-1):
#         if loscostumers[item].table == lostables[z]:
#             jugadores[z].append(loscostumers[item])

print(range(len([1,2])))