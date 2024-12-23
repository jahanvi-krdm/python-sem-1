# LECTURE NOTES

# def factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return (n * factorial(n-1))

# def fib(n):
#     if n == 0 or n == 1:
#         return(n)
#     else:
#         return (fib(n-1) + fib(n-2))
    
# def f(n):
#     if n == 0:
#         return 1;
#     return  f(n-1) + g(n-1);
# def g(n):
#     if n == 0:
#         return 1;
#     return g(n-1) - f(n)
# print(f(2) == g(0))
# print(g(2) + f(2) == 0)
# print(g(2))

# lst, item = [1, 2, 4, 5, 32], 5
# start, end = 0, len(lst)-1
# found = 0
# while start <= end:
#     mid = (start + end) // 2
#     if lst[mid] == item:
#         print ('Item found at index:', mid)
#         found = 1
#         break
#     elif lst[mid] < item:
#         start = mid + 1
#     elif lst[mid] > item:
#         end = mid - 1
# if not found:
#     print('Item not found')

# def b_search(A, start, end, item):
#     if start > end:
#         return False
#     else:
#         mid = (start+end) // 2
#         if A[mid] == item:
#             return True
#         elif A[mid] < item:
#             start = mid + 1
#         else:
#            end = mid - 1
#     return b_search(A, start, end, item)

# PRACTICE SHEETS

# Q1
# def pascal_recursive(n):
#     if n == 0:
#         return [[1]]
#     else:
#         triangle = pascal_recursive(n - 1)
#         last_row = triangle[-1]
#         current_row = [1] + [last_row[i] + last_row[i + 1] for i in range(len(last_row) - 1)] + [1]
#         triangle.append(current_row)
#         return triangle

# rows = 6
# triangle = pascal_recursive(rows - 1)
# for row in triangle:
#     print(row)

# Q2
# def is_prime(n, i = 2):
#     if n <= 2:
#         return True if n == 2 else False
#     if n % i == 1:
#         return False
#     if (i * i > n):
#         return True
#     return is_prime(n, i + 1)
    
# n = int(input())
# if is_prime(n):
#     print('Yes')
# else:
#     print('No')

# Q3

# my_list, element = [-8, 3, 5, 7, 9, 11], 10
# low, high = 0, len(my_list) - 1
# def check_element(low, high):
#     if low > high:
#         return "-1, element not found"
#     mid = (low + high) // 2
#     if my_list[mid] == element:
#         return mid
#     elif my_list[mid] > element:
#         return check_element(low, mid - 1)
#     else:
#         return check_element(mid + 1, high)
# print(check_element(low, high))

# Q4
# def tower_of_hanoi(n, source, auxiliary, destination):
#     if n == 1:
#         print(f"Move disk 1 from {source} to {destination}")
#         return
#     tower_of_hanoi(n - 1, source, destination, auxiliary)
#     print(f"Move disk {n} from {source} to {destination}")
#     tower_of_hanoi(n - 1, auxiliary, source, destination)
# n = int(input("Enter the number of disks: "))
# source = 'A'
# auxiliary = 'B'
# destination = 'C'
# tower_of_hanoi(n, source, auxiliary, destination)

# LAB QUESTIONS
# MONDAY

# def findAllSequences(diff, out, start, end):
#     if abs(diff) > (end - start + 1) // 2:
#         return
#     if start > end:
#         if diff == 0:
#             print(''.join(out), end=" ")
#         return  
#     out[start] = '0'
#     out[end] = '1'
#     findAllSequences(diff - 1, out, start + 1, end - 1)

#     out[start] = out[end] = '1'
#     findAllSequences(diff, out, start + 1, end - 1)

#     out[start] = out[end] = '0'
#     findAllSequences(diff, out, start + 1, end - 1)

#     out[start] = '1'
#     out[end] = '0'
#     findAllSequences(diff + 1, out, start + 1, end - 1)
# n = int(input())
# out = [""] * (2 * n)
# print(findAllSequences(0, out, 0, 2 * n - 1))


# def gcd(a,b):
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a%b)   
# a, b = map(int, input().split())
# print(gcd(a, b))


