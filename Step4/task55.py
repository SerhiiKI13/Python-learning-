import pandas as pd
users = [
    ["Serhii", 24, "Torun"],
    ["Alex", 30, "Bydgoszcz"],
    ["John", 18, "Warszawa"],
    ["Mike", 27, "Gdansk"],
]

df = pd.DataFrame(users,columns=["Username", "Age", "City"])
print(df)