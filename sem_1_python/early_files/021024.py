# Description: Global and Local Variables
# def f(x):
#     global y
#     y = 10
#     return (y+10)
# y = 0
# print(f(y), y)  

# x = 5
# def change_x():
#     global x
#     x = 10
# change_x()
# print(x)

# y = 3
# def f():
#     y = 7
#     return y
# print(f(), y)

# z = 8
# def modify():
#     global z
#     z += 2
#     return z
# print(modify(), z)

# a = 15
# def f1():
#     a = 10
#     def f2():
#         global a
#         a += 5
#     f2()
#     return a
# print(f1(), a)

# m = 20
# def modify_m():
#     global m
#     m = 30
# modify_m()
# def another_func():
#     m = 40
#     return m
# print(another_func(), m)

# x = 2
# def f(x):
#     y = x use x = 2
#     x = 5
#     return (y + x)
# def g():
#     global x
#     x = 7
#     return x
# print(f(x), g(), x)

# a = 3
# def f(a):
#     b = a
#     a = 10
#     return b + a
# def g():
#     global a
#     a += 2
#     return a
# b = 5
# print(f(b), g(), a)  #b is called so we take b = 5 and not a = 3

# m = 4
# def h():
#     global m
#     m += 3
#     return m
# def k():
#     m = 8
#     return m
# print(h(), k(), m)

# y = 9
# def outer():
#     y = 5
#     def inner():
#         global y
#         y += 1
#         return y
#     return inner() + y
# print(outer(), y)

# z = 12
# def func1():
#     z = 15
#     def func2():
#         global z
#         z = z - 3
#         return z
#     return func2() + z
# print(func1(), z)

# n = 11
# def change_n():
#     global n
#     n += 5
# def reset_n():
#     n = 20
#     return n
# change_n()
# print(reset_n(), n)

# p = 6
# def increment():
#     global p
#     p += 2
#     return p
# def reset():
#     p = 4
#     return p
# print(increment(), reset(), p)

# x = 10
# def modify_x():
#     global x
#     x = 15
#     return x
# def another(x):
#     return x + 3
# print(modify_x(), another(x), x)

# w = 14
# def first():
#     w = 10
#     return w + 2
# def second():
#     global w
#     w -= 4
#     return w
# print(first(), second(), w)

# v = 5
# def func_a():
#     v = 9
#     def func_b():
#         global v
#         v += 1
#         return v
#     return func_b() + v
# v = 7
# print(func_a(), v)

# x = 3
# def outer_func():
#     x = 6
#     def inner_func():
#         global x
#         x += 2
#         return x
#     return inner_func() + x
# x = 4
# print(outer_func(), x)

# y = 2
# def first_func():
#     y = 5
#     def second_func():
#         global y
#         y *= 3
#         return y
#     return second_func() + y
# y = 4
# print(first_func(), y)

# def count_prime(n):
#     prime = []
#     count = 0
#     for i in range(2, n):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             prime.append(i)
#             count += 1
#     print("The primes:", prime)
#     return count
# print("The number of primes:", count_prime(10))

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# print("The factorial of 5 is:", factorial(5))



                    
