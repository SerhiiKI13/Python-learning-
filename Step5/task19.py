numbers = [10, 20, 30]
iterator = iter(numbers)


while True:
    try:
        value = next(iterator)
        print(value)
    except StopIteration:
        break            