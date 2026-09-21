#List
list1 = [10, 20, 3.14, "Amit", "Raj", "Manoj"]
print(list1)

#Accessing List Element
print(list1[0])
print(list1[4])

#Accessing Last Element from List
print(list1[-1])
print(list1[-2])

#Changing List Element
list1[2] = 5.4
print(list1)

#List Function
#Append() - add element at the end
list1.append(100)
print(list1)

#Insert() - add element at specific location
list1.insert(2, "Data")
print(list1)

#Extend() - add multiple element
list1.extend([2,3,4])
print(list1)

#Remove - remove specific value
num=[10, 20, 30, 40, 50, 60, 70]
print(num)
num.remove(20)
print(num)

#pop() - remove value using indexing
num.pop(2)
print(num)

#del() - delete value using index
del num[3]
print(num)

#clear() - remove all value from list
num.clear()
print(num)

#len() - find out number of value present in the list
print(len(num))

#slicing - list[start:end]
print(list1)
print(list1[2:6])
print(list1[2:])
print(list1[:6])

#traversing
print("traversing using for loop")
num2 = [5,5,8,1,3,5,3,9]
for i in num2:
    print(i)

print("traversing using range()")
for i in range(len(num2)):
    print(num2[i])


