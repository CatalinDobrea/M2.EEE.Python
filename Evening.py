import random
random.seed(3456)

# EXCERCISE 5
class Customer(object):
    def __init__(self, typeC):
        self.typeC = typeC
        if self.typeC == "Returning":
            self.bet = 10
            self.budget = random.randint(100,300)
        if self.typeC == "Onetime":
            self.budget = random.randint(200,300)
            self.bet = random.randint(0,int((self.budget)/3))
        if self.typeC == "Bachelor":
            self.budget = random.randint(200,500)
            self.bet = random.randint(0,int(self.budget))



def CustomerType(returning, bachelor, total):
    customers = []
    ret = int(total * returning / 100)
    bch = int(total * bachelor / 100)
    onet = total - ret -bch
    for i in range(ret):
        customers.append(Customer('Returning'))
    for i in range(bch):
        customers.append(Customer('Bachelor'))
    for i in range(onet):
        customers.append(Customer('Onetime'))
    return customers

cost = CustomerType(50, 10, 100)
print(cost[2].budget)






# for i in range(100):
#     customers.append(Customer('Returning'))
# for obj in customers:
#     print(obj.budget)
















'''    def averagegrade(self):
        sum = 0
        for student in self.studentslist:
            sum += student.grade
        return float(sum/len(self.studentslist))

    def givegrades(self):
        return False

class Workshop(Class):

    def givegrades(self):

        for student in self.studentslist:
            student.gradeStudent(self.teacher)

        for index, student in enumerate(self.studentslist):
            if index %2 ==0:
                if index+1 < len(self.studentslist):
                    student.grade = (student.grade + self.studentslist[index+1].grade)/2
            else:
                student.grade = self.studentslist[index-1].grade

class Lecture(Class):

    def givegrades(self):

        for student in self.studentslist:
            student.gradeStudent(self.teacher)

from random import randint

class Teacher(object):


    def __init__(self, strictness):
        self.strictness = strictness


class Student(object):
    def __init__(self, intelect):
        self.intelect = intelect
    def gradeStudent(self, teacher):
        self.grade  = self.intelect * (1-teacher.strictness) * float(randint(5,10)/10.0)

class ErasmusStudent(Student):
    def gradeStudent(self, teacher):
           self.grade  = self.intelect * (1-teacher.strictness*0.8) * float(randint(5,10)/10.0) '''