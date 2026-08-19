import numpy as np
import pandas as pd

df = pd.read_csv("users.csv")
df["AgeGroup"] = np.where(df["Age"] >= 18,"Adult","Child")
g = df.groupby("City")
print(g.size())
m = g["Age"].mean()
print(m)

