import pandas as pd
import numpy as np

'''s=pd.Series([10,20,30], index=['a','b','c'])
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

print()

data = pd.DataFrame({
    "Name": ["Rahul", "Amit", "Priya", "Neha", "Rohan"],
    "Age": [22, 25, 23, 24, 26],
    "Marks": [85, 78, 92, 88, 75]
})
print(data.describe())
print(data["Age"].value_counts())
print(data["Age"].value_counts(normalize=True))

print()

import pandas as pd

data = pd.DataFrame({
    "Name": [
        "Rahul", "Amit", "Priya", "Neha", "Rohan",
        "Sneha", "Vikas", "Pooja", "Akash", "Kiran",
        "Sahil", "Anita", "Ravi", "Meena", "Arjun"
    ],

    "Age": [
        22, 25, 23, 24, 26,
        28, 27, 23, 30, 29,
        25, 26, 24, 27, 31
    ],

    "Department": [
        "IT", "HR", "IT", "Sales", "HR",
        "IT", "Finance", "Sales", "IT", "HR",
        "Finance", "IT", "Sales", "Finance", "IT"
    ],

    "City": [
        "Mumbai", "Pune", "Mumbai", "Delhi", "Pune",
        "Mumbai", "Nashik", "Delhi", "Mumbai", "Pune",
        "Nashik", "Mumbai", "Delhi", "Nashik", "Pune"
    ],

    "Salary": [
        30000, 35000, 32000, 28000, 40000,
        45000, 38000, 30000, 50000, 42000,
        36000, 48000, 31000, 39000, 55000
    ],

    "Status": [
        "Active", "Active", "Inactive", "Active", "Active",
        "Active", "Inactive", "Active", "Active", "Active",
        "Inactive", "Active", "Active", "Inactive", "Active"
    ]
})

print(data)

print(data.shape)
print(data.columns)
print(data.dtypes)
print(data.head(5))
print(data.tail(5))
print(data.value_counts("Status"))
print(data["Name"])
print(data.iloc[3])
print(data[data["Salary"]>40000])
print(data.sort_values("Salary", ascending=False))
print(data.drop_duplicates())
total_sal=data.groupby("Department")["Salary"].sum()
print(total_sal)
s=data.merge(data, on="Department")
print(s)
print(data.loc[0:4, ["Name", "Salary"]])

print()

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Rahul", "Amit", "Priya", "Neha"],
    "Age": [22, np.nan, 24, 25],
    "Salary": [30000, 35000, np.nan, 40000]
})

print(df)

print(df.isnull())
print(df.isnull().sum())
df["Age"]=df["Age"].fillna(df["Age"].mean())
print(df)
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print(df)

print()

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Sales"],
    "Salary": [30000, np.nan, 40000, np.nan]
})

print(df["Salary"].dropna())

print()

data = pd.DataFrame({
    "Name": ["Rahul", "Amit", "Priya", "Neha", "Rohan"],
    "Age": [22, 25, 23, 24, 26],
    "Marks": [85, 78, 92, 88, 75]
})
print(data.describe())
print(data["Age"].value_counts())
print(data["Age"].value_counts(normalize=True))

print()'''

import pandas as pd

data = pd.DataFrame({
    "Name": [
        "Rahul", "Amit", "Priya", "Neha", "Rohan",
        "Sneha", "Vikas", "Pooja", "Akash", "Kiran",
        "Sahil", "Anita", "Ravi", "Meena", "Arjun"
    ],

    "Age": [
        22, 25, 23, 24, 26,
        28, 27, 23, 30, 29,
        25, 26, 24, 27, 31
    ],

    "Department": [
        "IT", "HR", "IT", "Sales", "HR",
        "IT", "Finance", "Sales", "IT", "HR",
        "Finance", "IT", "Sales", "Finance", "IT"
    ],

    "City": [
        "Mumbai", "Pune", "Mumbai", "Delhi", "Pune",
        "Mumbai", "Nashik", "Delhi", "Mumbai", "Pune",
        "Nashik", "Mumbai", "Delhi", "Nashik", "Pune"
    ],

    "Salary": [
        30000, 35000, 32000, 28000, 40000,
        45000, 38000, 30000, 50000, 42000,
        36000, 48000, 31000, 39000, 55000
    ],

    "Status": [
        "Active", "Active", "Inactive", "Active", "Active",
        "Active", "Inactive", "Active", "Active", "Active",
        "Inactive", "Active", "Active", "Inactive", "Active"
    ]
})

print()

print(data.groupby("Department")["Salary"].sum())

print()

output = data.groupby("Department").agg({
    "Salary":["min", "max", "mean", "sum"],
    "Age": ["max", "mean", "min"]
})

print(output)

print()

data["Dept_Avg_Salary"] = (data.groupby("Department")["Salary"].transform("mean"))

print(data[["Name", "Department", "Salary", "Dept_Avg_Salary"]])

print()

data["Salary_Level"] = data["Salary"].apply(
    lambda x: "High" if x > 40000 else "Low"
)

print(data[["Name", "Salary_Level"]])
