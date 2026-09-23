num = [i for i in range(5, 101, 5)]
print(num)

print()

numbers = [-5, 3, -2, 8, -1, 6, 0, 10]
positive = [i for i in numbers if i > 0]
print(positive)

print()

words = ["python", "java", "sql", "power bi"]
upper = [word.upper() for word in words]
print(upper)

print()

words = ["Python", "SQL", "Excel", "Tableau"]
length = [word for word in words if word.split()]
print(len(length))

print()

numbers = [10, -5, 8, -2, 15, -7]
replace = [0 if num < 0 else num for num in numbers]
print(replace)

print()

divisible = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]
print(divisible)

print()

cube = {i:i**3 for i in range(1,11)}
print(cube)

print()

word = ["Python", "SQL"]
dict = {i: len(i) for i in word}
print(dict)

print()

celsius = [0, 10, 20, 30, 40]
temp = {i: (i * 9/5) + 32 for i in celsius}
print(temp)

print()

data = {i: "even" if i%2==0 else "odd" for i in range(1,21)}
print(data)
