import random
import Roulette
import Craps



print(random.choice([50,100,200]))

# class Customer(object):
#     def __init__(self, typeC, ID):
#         self.typeC = typeC
#         self.ID = ID
#         if self.typeC == "Returning" :
#             self.bet = 10
#             self.budget = random.randint(100,300)
#         if self.typeC == "Onetime" :
#             self.budget = random.randint(200,300)
#             self.bet = random.randint(0,int((self.budget)/3))
#         if self.typeC == "Bachelor":
#             self.budget = random.randint(200,500)
#             self.bet = random.randint(0,int(self.budget))
#         self.table = random.randint(1,10)
#
#
# def CustomerType(returning, bachelor, total, startcash):
#     customers = []
#     ret = int(total * returning / 100)
#     bch = int(total * bachelor / 100)
#     onet = total - ret - bch
#     for i in range(ret):
#         customers.append(Customer('Returning',i ))
#     for i in range(onet):
#         customers.append(Customer('Onetime', i+ret))
#     for i in range(bch):
#         customers.append(Customer('Bachelor', i+onet+ret))
#     for i in range(100-bch, total):
#         customers[i].budget += startcash
#     return customers
#
# customers = CustomerType(50, 10, 100, 200)
#
#
# for i in range(len(customers)):
#     print (customers.ID)








# tableplayers  = [[] for i in range(10)]
# for i in range(10):
#     for y in range(len(customers)):
#         if customers[y].table==i:
#             tableplayers[i].append(customers[y])
# print(tableplayers)
#
# def(nbtables):
#











#for i in customers:
#    print(i.ID)


# class Table(object):
#     def __init__(self, IDT, typeT, players):
#         self.typeT = typeT
#         self.players = players
#         self.IDT = IDT




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