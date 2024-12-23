# Tuesday
# Lab 4 Week 4
# def binary_number(n):
#     if n == 0:
#         return 0 
#     else:
#         return n % 2 + 10 * binary_number(n // 2)
# print(binary_number(21))

# n = 5
# for x in range(n):
#     for y in range(n):
#         print('*', end = ' ')
#     print()

# n = 5
# for x in range(n):
#     for y in range(x,n):
#         print(' ', end = ' ')
#     for y in range(x+1):
#         print('*', end = ' ')
#     print()

# n = 5
# for x in range(n):
#     for y in range(x+1):
#         print(' ', end = ' ')
#     for y in range(x,n):
#         print('*', end = ' ')
#     print()

# n = 5
# for x in range(n):
#     for y in range(x,n):
#         print(' ', end = ' ')
#     for y in range(x):
#         print('*', end = ' ')
#     for y in range(x+1):
#         print('*', end = ' ')
#     print()

# n = 5
# for x in range(n):
#     for y in range(x+1):
#         print(' ', end = ' ')
#     for y in range(x,n):
#         print('*', end = ' ')
#     for y in range(x,n-1):
#         print('*', end = ' ')
#     print()

# Binary number is a number made up of only 0s and 1s (i.e., 1010101 → binary; 10121234 → not a binary).

# Write a program to compute 1’s complement of a binary number, i.e., change 1 → 0 and 0 → 1.

# 1010101 ⇒ 0101010

def ones_complement(binary_number):
    complement = ''
    for bit in binary_number:
        if bit == '0':
            complement += '1'
        else:
            complement += '0'
    return complement

binary_number = input("Enter a binary number: ")
complement = ones_complement(binary_number)
print(complement)

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

a, b = map(int, input("Enter two numbers: ").split())
result = gcd(a, b)
print(result)
