import logging

logging.basicConfig(level=logging.INFO)


class AgeError(Exception):
    pass


def check_age(age):
    if age < 18:
        raise AgeError("You must be 18 or older")
    return "Access granted"


def calculate_total(price, quantity):
    return price * quantity


def find_product(products, name):
    for product in products:
        if product["name"] == name:
            return product
    return None


products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone", "price": 500},
    {"name": "Mouse", "cost": 50}
]

try:
    logging.info("Program started")

    age = int(input("Enter your age: "))
    print(check_age(age))

    name = input("Enter product name: ")
    product = find_product(products, name)

    quantity = int(input("Enter quantity: "))

    total = calculate_total(product['price'], quantity)

    print("Total:", total)

except ValueError:
    logging.error("Invalid number")

except AgeError as error:
    logging.error(error)

except KeyError as error:
    logging.error("Missing key: %s", error)