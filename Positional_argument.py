def calculate_average(*args):
    average = sum(args) / len(args)
    print(average)

calculate_average(10, 20, 30)

print()

def even_num(*args):
    num=0
    for num in args:
        if num % 2==0:
            print(num)

even_num(1,2,3,4,5,6,7,8)

print()

def high(*args):
    largest = 0
    for num in args:
        if num > largest:
            largest = num
    print(largest)

high(1,2,3,4,5)

print()

def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_details(name="Sam", age=21, city="Mumbai", course="Data Science")


