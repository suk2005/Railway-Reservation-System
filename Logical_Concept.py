n = int(input("Enter Number:"))
f=1
for i in range(1, n+1):
    f=f*i

print(f" factorial of {n} is {f}")


num1 = 0
num2 = 1

print("\n")

n = int(input("Enter Number:"))

num1=0
num2=1

print(num1)
print(num2)

i=1
while i<=n-2:
    num3 = num1+num2
    print(num3)
    num1 = num2
    num2 = num3
    i=i+1

n=int(input("Enter Number:"))
sum = 0
while n>0:
    digit = n % 10
    sum= sum + digit
    n=n//10

print(sum)
