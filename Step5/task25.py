from functools import wraps
def log_call(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
       print(f"Function: {func.__name__}")
       print(f"Args: {*args,}")
       result = func(*args,**kwargs)
       print(f"Result: {result}")
       return result
    return wrapper
@log_call
def multiply(a, b):
    return a * b
result = multiply(4, 5)
print(result)
