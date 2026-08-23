from dataclasses import dataclass
@dataclass
class Product:
    name: str
    price: float
    category: str="Other"
    
product1 = Product("Laptop",3500,"Electronics")
product2 = Product("Mouse",100)
print(product1)
print(product2)