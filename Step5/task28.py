from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: int
    category: str
    def discount(self,percent):
        result = self.price * (percent / 100)
        self.price = self.price - result
    
product1 = Product("Laptop",3500,"Electronics")
product1.price = 3000
product1.category = "Computers"
product1.discount(15)
print(product1)
