def get_name(user):
  return user["name"]

user = {
        "age": 23,
        "city": "Torun"
                }

name = get_name(user)

print(name)