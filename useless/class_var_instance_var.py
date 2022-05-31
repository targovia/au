class Rate:
    masterinterest = 4
    def __init__(self, name, loan):
        self.name = name
        self.loan = loan



    def calculate_interest(self):
       print ("Total interest", + self.loan * self.masterinterest)

p1 = Rate("Milen", 4000)
p1.masterinterest = 9
p1.calculate_interest()

class Child(Rate):
    pass

p5 = Child("Dete", 999999999)
p5.calculate_interest()

class Masive:
    def masive1(self):
        pass
    def masive2(self):
        pass
    def masive3(self):
        pass

class NewAll(Masive, Child, Rate):
    pass
n = NewAll()

n.masive2()
n.loan