users = ["Alex", "Serhii", "Alex", "John", "Serhii", "Mike", "John"]
print(users)
unique = set(users)
print(unique)
list_users = list(unique)
print(list_users)
product = {
        "name": "Laptop",
            "price": 3000,
                "quantity": 5,
                    "available": True
                    }

for key in product.keys():
    print(key)

    for value in product.values():
        print(value)

        for key,value in product.items():
            print(f"{key}: {value}")