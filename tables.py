import random

class customer(object):
    def __init__(self, custID):
        self.custID = custID
    def sitdown(self, tablelist):
        return random.choice(tablelist)

class returningcustomer(customer):
    def __init__(self, bet=0):
        self.budget = random.randint(100, 300)
        self.bet = bet
    def setbet(self, table):
        if self.budget >= table.minimumbet:
            self.bet = table.minimumbet
        else:
            self.bet=0

class onetimecustomer(customer):
    def __init__(self):
        self.budget = random.randint(200, 300)
        self.bet = random.randint(0, self.budget)

class bachelorcustomer(customer):
    def __init__(self):
        self.budget = random.randint(200, 500)
        self.bet = random.randint(0, self.budget / 3)
    def additionalcash(self, cash):
        self.budget += cash

class table(object, customer):
    def __init__(self, tableID):
        self.tableID = tableID




