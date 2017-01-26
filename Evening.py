import random
import Roulette
import Craps

class Customer(object):
    def __init__(self, typeC, ID):
        self.typeC = typeC
        self.ID = ID
        if self.typeC == "Returning" :
            self.bet = 10
            self.budget = random.randint(100,300)
        if self.typeC == "Onetime" :
            self.budget = random.randint(200,300)
            self.bet = random.randint(0,int((self.budget)/3))
        if self.typeC == "Bachelor":
            self.budget = random.randint(200,500)
            self.bet = random.randint(0,int(self.budget))


def CustomerType(returning, bachelor, total, startcash):
    customers = []
    ret = int(total * returning / 100)
    bch = int(total * bachelor / 100)
    onet = total - ret - bch
    for i in range(ret):
        customers.append(Customer('Returning',i))
    for i in range(onet):
        customers.append(Customer('Onetime', i+ret))
    for i in range(bch):
        customers.append(Customer('Bachelor', i+onet+ret))
    for i in range(100-bch, total):
        customers[i].budget += startcash
    return customers

customers = list(CustomerType(50, 10, 100, 200))
print(dir(customers))
#for i in customers:
#    print(i.ID)


# class Table(object):
#     def __init__(self, IDT, typeT, players):
#         self.typeT = typeT
#         self.players = players
#         self.IDT = IDT

print(len(customers))



# def repartition(tbnum):
#     tables = [[] for f in range(tbnum)]
#     aux = customers
#     for i in range(tbnum):
#         if aux != []:
#             tables[i] = random.sample(aux, random.randint(1, len(aux)))
#             aux = [x for x in aux if x not in tables[i]]
#     return tables
#
# print(repartition(20))
#
#
# for i in range(20):
#     print(len(repartition(20)[i]))