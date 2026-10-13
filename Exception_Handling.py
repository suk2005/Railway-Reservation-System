try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    c=a/b
except ZeroDivisionError:
    print("Number can't divide by zero")
else:
    print("output:", c)
finally:
    print("Program execution sucessful")

