numbers1 = [10, 20, 30, 40]
iterator = iter(numbers1)
try:
    while True:
        value = next(iterator)
        print(value)
except StopIteration:
    print("No more")