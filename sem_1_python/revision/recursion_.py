# Q1
# ques = "Which of the following correctly describes a characteristic of recursion?"
# a = "It always requires more memory than iteration."
# b = "It never uses the call stack."
# c = "Recursive solutions are always faster than iterative ones."
# d = "Recursive functions do not need a base case."
# ans = a


# Q2
# def mystery(n):
#     if n == 0:
#         return 0
#     else:
#         return n + mystery(n - 1)
# print(mystery(5))
# ans = "5"

# Q3
# def mystery(n):
#     if n == 0:
#         return 0
#     elif n % 2 == 0:
#         return n + mystery(n - 2)
#     else:
#         return mystery(n - 1)
# print(mystery(1))
# ans = "addition of even natural numbers"

# Q4
# def countdown(n):
#     if n == 0:
#         return
#     print(n, end=" ")
#     countdown(n - 1)
#     print(n, end=" ")
# countdown(3)

# Q5
# def zigzag(n):
#     if n == 0:
#         return
#     print(n, end=" ")
#     zigzag(n - 1)
#     print(n, end=" ")
#     zigzag(n - 1)
# zigzag(3)

# Q6
# def is_sorted(arr, index):
#     if index == len(arr) - 1:
#         return True
#     elif arr[index] > arr[index + 1]:
#         return False
#     else:
#         return is_sorted(arr, index + 1) 

# WAP
# Q1
# def sum_of_digits(inp):
#     inp = abs(inp)
#     inp_str = str(inp)
#     if len(str(inp)) == 1:
#         return inp
#     else:
#         return int(inp_str[0]) + sum_of_digits(int(inp_str[1:]))
# inp = int(input())
# print(sum_of_digits(inp))

# Q2
# inp = [3, 1, 4, 1, 5, 9, 2, 6, 5]
# def max_el(inp):
#     if len(inp) == 1:
#         return inp[0]
#     else:
#         el = max_el(inp[1:])
#         return max(inp[0], el)
# print(max_el(inp))

# Q3
# inp = "abc"
# def possible_pairs():
#     if len(inp) == 1:
#         return inp
#     else:

# Q4
# inp = str(input())
# char = str(input())
# def count_character(inp, char):
#     count = 0
#     if len(inp) == 1:
#         if inp == char:
#             count += 1
#         return count 
#     else:
#         return (1 if inp[0] == char else 0) + count_character(inp[1:], char)
# print(count_character(inp,char))


# Q5
# inp = str(input())
# def permutations(inp):
#     if len(inp) == 1:
#         return [inp]
#     else:
#         p = []
#         for i in range(len(inp)):
#             fix_char = inp[i]
#             rem = inp[:i] + inp[i+1:]
#             for perm in permutations(rem):
#                 p.append(fix_char + perm)
#         return p
# print(permutations(inp))

# Q6
# inp = {1, 2, 3}
# def power_set(inp):
#     if inp == {}:
#         return frozenset([{}]) 
#     else:
#         power = set()  
#         for i in inp:  
#             fix = i  
#             rem = inp - {fix}  
#             for f in power_set(rem):  
#                 power.add(frozenset([fix] | f))  
#         return power
# print(power_set(inp))

# Q7
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result
inp = [1, [2, 3], 4, [5, [6, 7]], 8, [[[1], 2, 3], 4], 5]
print(flatten(inp))