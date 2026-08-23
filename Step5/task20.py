def count_numbers():
    yield 1
    yield 2
    yield 3 
    yield 4
    yield 5
    
numbers = count_numbers()
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))
print(next(numbers))