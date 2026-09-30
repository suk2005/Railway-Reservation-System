import pandas as pd

df = pd.read_csv("Employee.csv")

print(df.head())

print(df.groupby("Department")["Salary"].mean())

print(df.groupby("Department")["Employee"].count())
