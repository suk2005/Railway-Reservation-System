import numpy as np 

numbers = np.array([10, 20, 30, 40])

print(numbers)

print()

import numpy as np
number = np.array([10, 20, 30, 40, 50])
print(number * 2)

print()

a= np.zeros(5)
print(a)

print()

a= np.ones(5)
print(a)

print()

a = np.arange(1,6)
print(a)

print()

a= np.linspace(1, 10, 5)
print(a)

print()

a = np.array([10, 20, 30, 40, 50, 60])
b=a.reshape(2,3)
print(b)

print()

a = np.array([[10, 20, 30],
              [40, 50, 60]])
b=a.flatten()
print(b)

print()

a = np.array([[10, 20, 30],
              [40, 50, 60]])
b=a.ravel()
print(b)

print()

a = np.array([10, 20, 30])
b = np.array([40, 50, 60])

c=np.concatenate((a,b))
print(c)

print()

a = np.array([10, 20, 30, 40, 50, 60])
b= np.split(a, 3)
print(b)

print()

a= np.array([[10,20,30],
             [40,50,60]])

b=a.copy()
b[0]= 100
print(b)

print()

a= np.array([[10,20,30],
             [40,50,60]])

b=a.view()
b[0]= 100
print(a)
print(b)

print()

a=np.array([[1,2],
            [4,5]])
b=np.array([[1,2],
            [4,5]])
c=a.dot(b)
print(c)

print()

a=np.random.randint(1, 10, (2,3))
print(a)


