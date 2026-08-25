class Car:
    def __init__(self,brand,year,color):
            self.brand = brand
            self.year = year
            self.color = color
    def __str__(self):
                return f"{self.brand}-{self.year}-{self.color}"
    def __repr__(self):
                return f"Car('{self.brand}', {self.year}, '{self.color}')"
    def __eq__(self, other):
            return self.brand == other.brand and self.year == other.year and self.color == other.color

car = Car("BMW", 2005, "Black")
print(car)
print(repr(car))
car1 = Car("BMW", 2005, "Black")
car2 = Car("BMW", 2005, "Black")
car3 = Car("BMW", 2005, "White")

print(car1 == car2)
print(car1 == car3)