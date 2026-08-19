import pandas as pd

df = pd.read_csv("users.csv")

df["Adult"] = df["Age"] >= 18
print(df)
