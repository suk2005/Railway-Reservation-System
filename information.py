import pandas as pd
import numpy as np

s=pd.Series([10,20,30], index=['a','b','c'])
print(s)

print()

df = pd.DataFrame({
    'name':['ABC', 'DEF', 'XYZ'],
    'age': [22,23,24],
    'city': ['Mumbai', 'Pune', 'Delhi']
})
print(df)

print()

df.index=['r1', 'r2', 'r3']
print(df.index)

print()

score = [99, 97, 98]
s= pd.Series(score, index=['Science', 'Math', 'English'])
print(s)

print()

s=pd.Series([1, 2, 3])
print(s[0])
print(s[1])

print()

data = {"Pen":90,
        "Pencil":98
        }
s= pd.Series(data)
print(s["Pen"])

print()

s= pd.Series([10, 20, 30, 40, 50])
print(s)

print()

s = pd.Series(["Science", "Math", "English"], index=[99, 96, 98])
print(s)

print()

s = pd.Series({"Science":99,
               "Math": 96,
               "English": 98})
print(s["Science"])

