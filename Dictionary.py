dict1 = {
    "ID":100,
    "Name":"Manoj",
    "Salary":120000
    }

print(dict1)

print()

print(dict1["Name"])

print()

print("Name:",["Name"])

print()

print(dict1.get("Exp"))

print()

#new element
dict1["Exp"]="18 Year"
print(dict1)

print()

#update
dict1["Salary"]=1400000
print(dict1)

print()

#pop
dict1.pop("Exp")
print(dict1)

print()

#popitem
dict1.popitem()
print(dict1)

print()

#del
del dict1["Name"]
print(dict1)

print()

#len
print(len(dict1))

print()

#in

if "Exp" in dict1:
    print("Exp present in dict1")

print()

#not in

if "Dept" not in dict1:
    print("Dept not present in dict1")

print()

#method of dict
print(dict1.keys())
print(dict1.values())
print(dict1.items())

print()

#key, value in items
for key, value in dict1.items():
    print(f"key is: {key} value is {value}")

print()

#update dict1
dict1.update({"Salary": 150000})
print(dict1)

print()

#nested if
student = {
    "student1" :{
        "roll no.":1,
        "mark": 90
        },
    "student2" : {
        "roll no":2,
        "mark": 95
        },
    "student3" : {
        "roll no":3,
        "mark": 92
        }
}

print(student)
print(student["student2"])
print(student["student2"]["mark"])






