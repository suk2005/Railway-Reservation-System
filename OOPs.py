
'''class class_name:
    attributes
    method

object_creation
object_name = class_name()'''

#class with only data member

class student:
    roll = 1

s = student()
print(s.roll)

print()

#class with attributes and method

class student:
    roll = 1
    def data(self):
        print("Roll Number:", self.roll)

s = student()
s.data()

print()

class data:
    def display(self):
        print("Welcome")

d = data()
d.display()

print()

class area:
    r = int(input("Enter redius:"))
    def circle(self):
        self.area_circle = 3.14*self.r*self.r
        print("Area of Circle Is:", self.area_circle)

a = area()
a.circle()

print()

class Car:
    def show_details(self):
        print("Name:", self.name)
        print("Color:", self.color)
        print("Speed:", self.speed)

c = Car()

c.name="BMW"
c.color="Blue"
c.speed="280km/h"

c.show_details()

#Encapsulation

class car:
    speed = 120
    def car_speed(self):
        print("Speed of car is:", self.speed)

c=car()
c.car_speed()

#Abstraction

class detail:

    def car_detail(self):
        print("Blue car")

d=detail()
d.car_detail()

#Inheritant

class Car:

    def data(self):
        print("Car is driving")

class BMW(Car):
    pass

b=BMW()
b.data()

#Polymorphisom

class car:
    def car1(self):
        print("car")

class bike:
    def bike1(self):
        print("bike")

c=car()
b=bike()

c.car1()
b.bike1()

        
        
