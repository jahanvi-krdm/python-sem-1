# num = int(input())
# def number_to_binary(num): # learn it 
#     if num == 0:
#         return 0
#     binary_number = 0
#     place_value = 1
#     while num > 0:
#         remainder = num % 2
#         binary_number += remainder * place_value
#         num = num // 2
#         place_value *= 10
#     return binary_number
# print(number_to_binary(num))

# prime = int(input())
# def is_prime(num):
#     if num < 2 or (num > 2 and num % 2 == 0):
#         return False
#     for i in range(3, int(num**0.5) + 1, 2):
#         if num % i == 0:
#             return False
#     return True
# def get_prime_position(prime):
#     if not is_prime(prime):
#         return "Not a prime number"
#     prime_count = 0
#     num = 1
#     while True:
#         num += 1
#         if is_prime(num):
#             prime_count += 1
#             if num == prime:
#                 return prime_count
# print(get_prime_position(prime))

# def sum_of_proper_divisors(num):
#     divisor_sum = 0
#     for i in range(1, num // 2 + 1):
#         if num % i == 0:
#             divisor_sum += i
#     return divisor_sum
# def is_amicable(n):
#     m = sum_of_proper_divisors(n)
#     if m != n:  # Ensure they are not the same
#         if sum_of_proper_divisors(m) == n:
#             return True, m
#     return False, sum_of_proper_divisors(n)
# n = int(input("Enter a number: "))
# result, value = is_amicable(n)
# if result:
#     print(f"True {value}")
# else:
#     print(f"False {value}")

# a = int(input("enter a:"))
# b = int(input("enter b:"))
# def gcd(a,b):
#     while True: 
#         if b == 0:  
#             return a
#         a, b = b, a % b  
# print(gcd(a,b))

# pp = str(float(input()))
# def reverse_magic(pp):
#     if pp == pp[::-1]:
#         return True
#     else:
#         return False
# print(reverse_magic(pp))

# n = int(input("Enter a number: "))
# digits = [int(digit) for digit in str(n)]

# def adding_digits(digits):
#     total_sum = sum(digits)
#     while total_sum >= 10:
#         total_sum = sum(int(digit) for digit in str(total_sum))
#     return total_sum
# result = adding_digits(digits)
# print(result)

# x1, y1, x2, y2, x3, y3 = map(int, input().split())
# coord = (x1, y1, x2, y2, x3, y3)

# def cross_product(coord):
#     x1, y1, x2, y2, x3, y3 = coord
#     ans = ((x2 - x1)*(y3 - y1)) - ((y2 - y1)*(x3 - x1))
#     if ans < 0:
#         return "RIGHT"
#     elif ans > 0:
#         return "LEFT"
#     else:
#         return "ON THE LINE"
# print(cross_product(coord))

# import math
# n, x, y = map(int, input("commands, coord x, coord y: ").split())
# cmd = []
# for _ in range(n):
#     d, s = input().split()
#     cmd.append((d, int(s)))
# coord_x, coord_y = 0, 0
# distance = 0
# def dist_value():
#     global coord_x, coord_y, distance
#     for direction, steps in cmd:
#         if direction == "U":
#             coord_y += steps
#             distance += steps
#         elif direction == "D":
#             coord_y -= steps
#             distance += steps
#         elif direction == "L":
#             coord_x -= steps
#             distance += steps
#         elif direction == "R":
#             coord_x += steps
#             distance += steps
# def disp_value(coord_x, coord_y):
#     return math.sqrt((coord_x - x) ** 2 + (coord_y - y) ** 2)
# dist_value()
# displacement = disp_value(coord_x, coord_y)
# print(distance, round(displacement, 2))

# n = int(input("enter integer: "))
# def factorial(n):
#     if n == 0:
#         return 1
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# fact = factorial(n) # learn this
# digit_list = [int(digit) for digit in str(fact)] # learn this
# def trailing_zeros():
#     count = 0
#     new_lst = digit_list[::-1]
#     for i in new_lst:
#         if i == 0:
#             count += 1
#         else:
#             break
#     return count
# print(trailing_zeros())

# n, k = map(int, input("N, base: ").split())
# digits = []
# def convert_to_binary(num):
#     if num == 0:
#         return "0"  # Handle the case for 0
#     binary_number = ""
#     while num > 0:
#         remainder = num % 2
#         binary_number = str(remainder) + binary_number 
#         num = num // 2
#     return binary_number
# def is_palindrome(s):
#     return s == s[::-1]
# for num in range(n):
#     if is_palindrome(str(num)):
#         binary_num = convert_to_binary(num)
#         if is_palindrome(binary_num):
#             digits.append(num)
# total_sum = sum(digits)
# print("Sum of palindromic numbers in both bases:", total_sum)

# num = int(input())
# assert num > 0
# prime_factors = [2, 3, 5]
# def is_ugly(num):
#     for factor in prime_factors:
#         while num % factor == 0:
#             num //= factor
#     return num == 1
# print(is_ugly(num))

# def max_drunk_bottles(n, x):
#     total_drunk = n
#     empty_bottles = n

#     while empty_bottles >= x:
#         new_full_bottles = empty_bottles // x
#         total_drunk += new_full_bottles
#         empty_bottles = empty_bottles % x + new_full_bottles

#     return total_drunk
# n, x = map(int, input("Enter the number of full bottles and exchange rate (n x): ").split())
# result = max_drunk_bottles(n, x)
# print(result)  # Output: 13 for the input 9 3

# n, k = map(int, input().split())
# def kth_factor(n, k):
#     factors = []
#     for i in range(1, n + 1):
#         if n % i == 0:
#             factors.append(i)
#     if len(factors) < k:
#         return -1
#     else:
#         return factors[k - 1]
# print(kth_factor(n, k))

# n, k = input("Enter n and k: ").split()
# n = str(n)
# k = int(k) 

# def algorithm_burr(n, k):
#     op = int(n) 
#     for i in range(k):
#         if op % 10 == 0: # to check if last element is zero
#             op = op // 10
#         else:
#             op -= 1
#     return op
# print(algorithm_burr(n, k))
        