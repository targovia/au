class Area:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def calculate_area(self):
        return self.a * self.b

myvar = Area(5, 4)
print(myvar.calculate_area())
