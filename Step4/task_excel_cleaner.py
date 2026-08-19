import pandas as pd

df = pd.read_excel("ExelFolder/dirty_users.xlsx")
d = df.isna().sum()
print(d)
df["Age"] = pd.to_numeric(df["Age"],errors="coerce")
print(df)
df.dropna(subset=["Name","Age","City"],inplace=True)
print(df)
df.to_excel("clean_users_pandas.xlsx",index=False)