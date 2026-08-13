product_name = input("Введите название товара: ")
product_price = float(input("Введите цену товара: "))
product_quantity = int(input("Введите количество товара: "))
customer_age = int(input("Введите ваш возраст: "))
answer = input("Do you have discount card? ")
discount = answer == "yes"
total_price = product_price * product_quantity

print("Название товара: " + product_name)
print("Цена: " , product_price)
print("Количество: ", product_quantity)
print("Adult: ", customer_age > 18)
print("Карта магазина: ", discount)
print(customer_age > 18 and discount)
print("Вы должны заплатить: ", total_price)