# convert to binary
def convert_to_binary(num):
    if num == 0:
        return "0"  # Handle the case for 0
    binary_number = ""
    while num > 0:
        remainder = num % 2
        binary_number = str(remainder) + binary_number 
        num = num // 2
    return binary_number
print(convert_to_binary(8))

# gcd
def gcd(a,b):
    while True: 
        if b == 0:  
            return a
        a, b = b, a % b  
print(gcd(3, 4))

# factorial
def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
print(factorial(5))

# prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
print(is_prime(7))

# counts ditinct value
lst = [1, 2, 3, 3]
def count_distinct(lst):
    new_lst = []  
    for value in lst:
        if value not in new_lst:
            new_lst.append(value)  
    return len(new_lst)
print(count_distinct(lst))