class Car:
    def __init__(self,brand,year,color):
        self.brand = brand
        self.year = year
        self.color = color
    def show_info(self):
        print(f"{self.brand}-{self.year}-{self.color}")
    def get_age(self):
        return 2026 - self.year

car1 = Car("Bmw",2005,"white")
car2 = Car("Mersedec",2010,"orange")
car3 = Car("Audi",2012,"black")
car1.show_info()
car2.show_info()
car3.show_info()
print(car1.get_age())