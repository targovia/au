class Worker:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address

    def psuva(self):
        print("Zleee pari vika -->" + self.email)

empl1 = Worker("Milen", "milen@abv.bg", "Lozenez, barod 2")
empl2 = Worker("Vanya", "Van@abv.bg", "Selo")

print(empl1.name)
print(empl2.psuva())