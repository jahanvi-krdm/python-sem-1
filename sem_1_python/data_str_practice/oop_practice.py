# Object orientated programming in Python
# a = "hello"
# print(type(a))

# class babe:
#     def string(self):
#         return 'string'    
# b = babe()
# print(type(b))

# METHOD 1
# class babe:
#     def __init__(self, name):
#         self.name = name
#         print(name)  
# b = babe('Jahanvi')
# print(b)

# METHOD 2
# class babe:
#     def __init__(self, name):
#         self.name = name 
# b = babe('Jahanvi')
# print(b.name) 

# METHOD 3
# class babe:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
#     def get_name(self):
#         return self.name
#     def get_age(self):
#         return self.age 
#     def set_age(self, age):
#         self.age = age
# b = babe('Jahanvi', 18)
# print(b.get_name())
# b.set_age(20)
# print(b.get_age()) 

# class student:
#     def __init__(self, name, age, grade):
#         self.name = name
#         self.age = age
#         self.grade = grade
#     def get_grade(self):
#         return self.grade    
# class course:
#     def __init__(self, name, max_students):
#         self.name = name
#         self.max_students = max_students
#         self.students = []
#     def add_student(self, student):
#         if len(self.students) < self.max_students:
#             self.students.append(student)
#             return True
#         return False   
#     def get_average_grade(self):
#         value = 0
#         for student in self.students:
#             value += student.get_grade()
#         return value / len(self.students)
# s1 = student('Jahanvi', 18, 75)
# s2 = student('Nikhil', 19, 85)
# s3 = student('Max', 18, 80)
# course = course("MTH100", 2)
# course.add_student(s1)
# course.add_student(s2)
# print(course.get_average_grade())

# class complex:
#     real = 0
#     img = 0
# c = complex()
# print(c.real)
# print(c.img)

# class  complex:
#     def __init__(self, x, y):
#         self.real = x
#         self.img = y
#     def printcomplex(self):
#         print(f'{self.real} + {self.img}i')
# c1 = complex(6, 7)
# c1.printcomplex()

# class queue:
#     def __init__(self):
#         self.qdata = []
#         self.front = 0
#         self.end = 0

#     def add(self, obj):
#         self.qdata.append(obj)
#         self.end += 1
    
#     def remove(self):
#         if self.isempty():
#             return None
#         else:
#             obj = self.qdata[self.front]
#             self.front += 1
#         return obj
    
#     def isempty(self):
#         if self.front == self.end:
#             return True
#         else:
#             return False
# waitroom = queue()
# while True:
#     op = input("1: add, 2: remove, -1: exit: ")
#     op = int(op)
#     if op == 1:
#         roll_no = input("Give roll no: ")
#         waitroom.add(roll_no)
#     elif op == 2:
#         obj = waitroom.remove()
#         if obj == None:
#             print("No student waiting")
#         else:
#             print(f'Next student: {roll_no}')
#     elif op == -1:
#         break
#     else:
#         print("Incorrect command, try again")

# class StrangerThings:
#     def __init__(self, power):
#         self.power = power
#     @property
#     def ten_power(self):
#         return (self.power)*10
#     @ten_power.setter
#     def ten_power(self,new_value):
#         self.power = (new_value)/2
# a = StrangerThings(100)
# print(a.ten_power)
# a.ten_power=int(input())
# print(a.ten_power)

# class Employee:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id
#     def showDetails(self):
#         print(f"The name of the employee: {self.id} is {self.name}")
# class Programmer(Employee):
#     def showLanguage(self):
#         print("The default language is Python")
# e1 = Employee("Rohan Das", 400)
# e1.showDetails()
# e2 = Programmer("Jahanvi", 274)
# e2.showDetails()
# e2.showLanguage()

# Debugging

# class Inventory:
#     def __init__(self):
#         self.items = {}

#     def add_item(self, item, quantity):
#         if item in self.items:
#             self.items[item] += int(quantity)
#         else:
#             self.items[item] = int(quantity)

#     def remove_item(self, item, quantity):
#         if item not in self.items or self.items[item] < int(quantity):
#             print("NOT ENOUGH STOCK")
#         else:
#             self.items[item] -= int(quantity)
#             if self.items[item] == 0:
#                 del self.items[item]

#     def display_inventory(self):
#         for item, quantity in self.items.items():
#             print(f"{item}: {quantity}")

# inventory = Inventory()
# q = int(input())
# for _ in range(q):
#     opt, fruit, quantity = input().split()
#     if opt == "1":
#         inventory.add_item(fruit, quantity)
#     elif opt == "2":
#         inventory.remove_item(fruit, quantity)
        
# inventory.display_inventory()

# class BankAccount:
#     def __init__(self, initial_balance):
#         self.balance = initial_balance

#     def deposit(self, amount):
#         self.balance += int(amount)

#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Insufficient funds")
#         else:
#             self.balance -= amount

#     def display_balance(self):
#         print(f"Current balance: {self.balance}")

# account = BankAccount(100)
# n = int(input())
# for _ in range(n):
#     operation, amount = input().split()
#     if operation == "D":
#         account.deposit(amount)
#     elif operation == "W":
#         account.withdraw(int(amount))

# account.display_balance()

# import math
# class Fraction:
#     def __init__(self, n, d):
#         if d == 0:
#             raise ValueError("Denominator cannot be zero.")
#         g = math.gcd(n, d)
#         self.n, self.d = n // g, d // g
#         if self.d < 0:
#             self.n, self.d = -self.n, -self.d
#     def __str__(self):
#         return str(self.n) if self.d == 1 else f"{self.n}/{self.d}"
#     def __add__(self, other):
#         return Fraction(self.n * other.d + self.d * other.n, self.d * other.d)
#     def __mul__(self, other):
#         return Fraction(self.n * other.n, self.d * other.d)
# a, b, c, d = map(int, input().split())
# op = int(input())
# f1, f2 = Fraction(a, b), Fraction(c, d)
# result = f1 + f2 if op == 1 else f1 * f2
# print(result)

# import math
# def simplify_fraction(n, d):
#     if d == 0:
#         raise ValueError("Denominator cannot be zero.")
#     g = math.gcd(n, d)
#     n, d = n // g, d // g
#     if d < 0:
#         n, d = -n, -d
#     return n, d
# def add_fractions(a, b, c, d):
#     numerator = a * d + b * c
#     denominator = b * d
#     return simplify_fraction(numerator, denominator)
# def multiply_fractions(a, b, c, d):
#     numerator = a * c
#     denominator = b * d
#     return simplify_fraction(numerator, denominator)
# def format_fraction(n, d):
#     return str(n) if d == 1 else f"{n}/{d}"
# a, b, c, d = map(int, input().split())
# op = int(input())
# if op == 1:
#     num, den = add_fractions(a, b, c, d)
# else:
#     num, den = multiply_fractions(a, b, c, d)
# print(format_fraction(num, den))

# class queue:
# 	def __init__(self):
# 		self.arr = []
# 	def enqueue(self , val):
# 		self.arr.append(val)
# 	def dequeue(self):
# 		if not self.is_empty():
# 			return self.arr.pop(0)
# 		return None
# 	def is_empty(self):
# 		return len(self.arr) == 0
# 	def front(self):
# 		if not self.is_empty():
# 			return self.arr[0]
# que1 = queue()
# s = input().strip()
# for x in s :
# 	que1.enqueue(x)
# revstr = ''
# while not que1.is_empty():
# 	charval = que1.dequeue()
# 	revstr += charval
# if s == revstr[::-1]:
#     print("YES")
# else:
#     print("NO")

# class Mystery:
#     def __init__(self, value=0):
#         self.value = value
#     def increment(self):
#         self.value += 1
#         return self.value
# e1 = Mystery()
# e2 = e1
# print(e1.increment(), e2.increment(), e1.value)

# class MyClass:
#     def __init__(self, name):
#         self.name = name
#     def change_name(self, name):
#         name = name
# obj = MyClass("OldName")
# obj.change_name("NewName")
# print(obj.name)
	
# class MyClass:
#     def __init__(self):
#         pass
#     def display(self):
#         print("Hello")
# obj = MyClass()
# obj.display(5)
# "error due to obj.display(5)"

# class Stack:
#     def __init__(self):
#         self.data = []
#     def push(self, item):
#         self.data.append(item)
#     def pop(self):
#         return self.data.pop()
# s = Stack()
# s.pop()
# error due to s.pop()

# Q5
# "B initializes the objetc's attributes."

# Q6
# class MyClass:
#     def __init__(self, value):
#         self.value = value
#     def __str__(self):
#         return self.value
# obj = MyClass(10)
# print(obj)
# "TypeError: str() should return a string"

# Q7
# class Test:
#     def __init__(self, value):
#         self.value = value
#     def __eq__(self, other):
#         return self.value == other.value
# obj1 = Test(5)
# obj2 = Test(5)
# print(obj1 == obj2)
# "True"

# Q8
# class Car:
#     def __init__(self, brand):
#         self.brand = brand
#     def __eq__(self, other):
#         return self.brand == other.brand
# car1 = Car("Toyota")
# car2 = Car("Honda")
# print(car1 == "Honda")

class Counter:
    def __init__(self, value=0):
        self.value = value
    def increment(self):
        self.value += 1
    def __str__(self):
        return str(self.value)
counter1 = Counter()
counter1.increment()
counter2 = counter1
counter2.increment()
print(counter1)


