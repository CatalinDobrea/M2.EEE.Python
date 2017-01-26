import random


class Customer:
    def __init__(self):

        def drinks(self):
            if self.wealth > 60:
                self.drink = random.randint(1, 2) * 20
                self.tips = random.randint(0, 20)
                self.wealth -= self.drink + self.tips
                return True
            else:
                self.drink = 0
                self.tips = 0
                return False

        def playat(self, tbnum, rounds):
            self.tblplay = [random.randint(1,tbnum) for i in range(rounds)]



class Returning(Customer):
    def rich(self):
        self.wealth = random.randint(100, 300)
        self.bet = 0
        return False


class OneTime(Customer):
    def rich(self):
        self.wealth = random.randint(200, 300)
        self.bet = random.randint(0, (self.wealth / 3))
        return False


class Bachelor(Customer):
    def rich(self):
        self.wealth = random.randint(200, 500) + 0
        self.bet = random.randint(0, self.wealth)
        return False

customers = []
for i in range(1,20):
    customers.append(Returning())
print(customers)
