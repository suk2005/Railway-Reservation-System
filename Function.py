# function defination
'''def greet():
    print("Hello")

greet()
# function calling

print()

def greet(name):
    print("Hello", name)

greet("ABC")

print()

def greet1(n):
    print("Hello", n)

n=input("Enter name:")
greet1(n)

print()

#Addition with using funtion
def add(x,y):
    z=x+y
    print("Output:", z)

a=int(input("Enter first value:"))
b=int(input("Enter second value:"))
add(a,b)

print()

def add(x,y):
    z=x+y
    return z

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
output = add(a,b)
print(output)'''

print()

#default argument
def add(a, b=10, c=10):
    print(a+b+c)

add(5)
add(5,1)
add(5)

print()

def square(x):
    return x*x

print(square(5))

print()

#using lambda

square = lambda x : x*x
print(square(5))
