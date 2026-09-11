mark = int(input("Enter your mark:"))
attendance = float(input("Enter your attendance:"))

if mark >= 50 and attendance >= 75:
    print("pass")
else:
    print("fail")
    

year = int(input("Enter year:"))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Yaer")
else:
    print("Not Laep Yaer")


num = int(input("Enter Number:"))

if num > 0 and num % 5 == 0:
    print("Number is positie and divisible by 5")
else:
    print("Number is positie and not divisible by 5")


age = int(input("Enter age:"))

if age >= 18 and age < 60:
    print("Perseon is allow for deriving license")
else:
    print("Perseon is not allow for deriving license")

Character = str(input("Enter Character:"))

if Character == a or Character == e or Character == i or Character == o or Character == u:
    print("Enter character is vowel")
else:
    print("Enter character is not vowel")

