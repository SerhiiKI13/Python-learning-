from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        print("Start")
        result = func(*args,**kwargs)
        print("End")
        return result
    return wrapper

@my_decorator
def add(a, b):
    return a + b

result = add(5, 3)
print(result) 
print(add.__name__)