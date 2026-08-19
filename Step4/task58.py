import pandas as pd
users = [
    [1, "Serhii"],
    [2, "Alex"],
    [3, "John"],
]

orders = [
    [1, "Laptop"],
    [2, "Phone"],
    [4, "Keyboard"],
]


df = pd.DataFrame(users,columns=["Index","Username"])
df1 = pd.DataFrame(orders,columns=["Index","ProductName"])
print(df)
print(df1)
m = pd.merge(df,df1,how="right",on="Index")
print(m)