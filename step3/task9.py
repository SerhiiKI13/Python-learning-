def get_price(product):
        return product["price"]


def calculate_total(product, quantity):
    price = get_price(product)
    return price * quantity


def buy_product(product, quantity):
    total = calculate_total(product, quantity)
    return f"Total: {total}"


product = {
             "name": "Laptop",
             "price": 1000
                            }

quantity = 2

print(buy_product(product, quantity))