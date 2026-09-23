num = []
for i in range(1,6):
    num.append(i)

print(num)

num1 = [i for i in range(1,6)]
print(num1)

sq = [i*i for i in range(1,11)]
print(sq)

even = [i for i in range(1,21) if i%2 == 0]
print(even)

list1 = ["Even" if i%2==0 else "Odd" for i in range(1,21)]
print(list1)

Word = input("Enter your name:")
list2 = [ch.upper() for ch in Word]
print(list2)

