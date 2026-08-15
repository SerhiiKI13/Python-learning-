def calculate_discount(price, discount):
        return price - price * discount / 100

def buy_product(name, price, discount):
    final_price = calculate_discount(price, discount)
    return f"{name}: {final_price}"

price = int(input("Enter price: "))
discount = int(input("Enter discount: "))

print(type(price))
print(buy_product("Laptop", price, discount))