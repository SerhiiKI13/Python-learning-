from abc import ABC,abstractmethod

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woow")

class Cat(Animal):
    def make_sound(self):
        print("Meow")
        
animals = [Dog(), Cat(), Dog(), Cat()]
for a in animals:
    a.make_sound()      