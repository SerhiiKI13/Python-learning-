from projectF.utils import users
from functools import wraps
from dataclasses import dataclass
users = [
        {"name": "Serhii", "age": 24, "city": "Torun"},
        {"name": "Alex", "age": 30, "city": "Bydgoszcz"},
        {"name": "John", "age": 18, "city": "Warszawa"},
        {"name": "Mike", "age": 27, "city": "Gdansk"},
        {"name": "Anna", "age": 32, "city": "Torun"},
]
adult_names = {u["name"] for u in users if u["age"] >= 25}
print(adult_names)

for i,u in enumerate(users,start=1):
        print(i,u["name"])
        
cities = ["Torun", "Bydgoszcz", "Warszawa", "Gdansk", "Torun"]
for u,city in zip(users,cities):
        print(u["name"],city)
        
sorted_users = sorted(users,key=lambda x: x["age"],reverse=True)
print(sorted_users)
print("####")
for u in adult_users(users):
        print(u)
print("Decorator")
def log_call(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
           print(f"Calling function: {func.__name__}")
           result= func(*args,**kwargs)
           print(f"Function finished: {func.__name__}")  
           return result
        return wrapper
@log_call

def adult_users(users):
        for u in users:
          if u["age"] >= 25:
                yield u
for u in adult_users(users):
      print(u)

print("Dataclass")
@dataclass
class User:
        name: str
        age: int
        city: str
user = User(users[1]["name"],users[1]["age"],users[1]["city"])
print(user)