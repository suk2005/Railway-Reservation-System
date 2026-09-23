number = [10,20,10,30,20,40,30,50]

unique=[]

for num in number:
    if num not in unique:
        unique.append(num)

print("original list:", number)
print("unique list:", unique)
