#variable length argument - *args, *kwargs

def add(*args):
    total = 0
    for i in args:
        total = total + i
    print(total)

add(5, 3, 2)
add(5, 1)
add(1, 2, 3, 4)

print()

def display(**kwargs):
    print(kwargs)

display(Roll_no = 1, Name = "ABC", Mark = 98)
display(Roll_no = 2, Mark = 97)

print()

#maximum argument without using function

def show(*args):
    highest = args[0]
    for i in args:
        if i > highest:
            highest = i
    print(i)

show(1, 2, 3)

#using max directly to find maximum argument

print()

def maximum(*args):
    print(max(args))

maximum(7,2,9,0,4)

print()

def maximum(**kwargs):
    large = 0
    for num in kwargs.values():
        if num > large:
            large=num
    print(large)

maximum(Excel=90, SQL=95, PBI=89, Python=70)

print()

def maximum(**kwargs):
    print(max(kwargs.values()))

maximum(Excel=90, SQL=95, PBI=89, Python=70)




            
