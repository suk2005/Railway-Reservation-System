student = {
    "ABC": 99,
    "DEF": 98,
    "PQR": 97,
    "XYZ": 95,
    "STU": 96
}
print(student)

print()

student["city"]="Mumbai"
print(student)

print()

student["XYZ"]=94
print(student)

print()

student.pop("XYZ")
print(student)

print()

data =str(input("Enter key:"))
if data in student:
    print("key exist")
else:
    print("not exist")

print()

print(student.keys())
print(student.values())

print()

student = {
    "ABC": 99,
    "DEF": 98,
    "PQR": 97,
    "XYZ": 95,
    "STU": 96
}

total= sum(student.values())
print(total)

print()

high = max(student, key=student.get)
print(student[high])
print(high)

print()

text = "Data"

frequency = {}

for char in text:
    if char in frequency:
        frequency[char] = frequency[char] + 1
    else:
        frequency[char]= 1

print(frequency)

print()

student = {
    "ABC": 99,
    "DEF": 98,
    "PQR": 97,
    "XYZ": 95,
    "STU": 96
}

std = {
    "ABC": 99,
    "DEF": 98,
    "PQR": 97,
    "XYZ": 95,
    "STU": 96
}

s = {
    "student": student,
    "std": std
}

print(s)


