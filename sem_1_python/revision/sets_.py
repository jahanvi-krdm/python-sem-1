# Q1
sq = {x**2 for x in range(5)}
# print(sq)

# Q2
c = "a frozen set can be used as key in a dict"

# Q3
A = {1, 2, 3}
B = {1, 2}
# print(B.issubset(A))

# Q4
A = {1, 2, 3}
B = {4, 5}
A.add(4)
# print(A)

# Q5
# def custom_frozenset(lst):
#     return tuple(sorted(set(lst)))
# def check_element_in_sets(element, sets):
#     for s in sets:
#         if element in s:
#             return True
#     return False
# even_numbers = custom_frozenset([0, 2, 4, 6, 8])
# odd_numbers = custom_frozenset([1, 3, 5, 7, 9])
# prime_numbers = custom_frozenset([2, 3, 5, 7])
# all_sets = [even_numbers, odd_numbers, prime_numbers]
# element_to_check = 3
# found = check_element_in_sets(element_to_check, all_sets)
# if found:
#     print(f"{element_to_check} is present in one of the sets.")
# else:
#     print(f"{element_to_check} is not present in any of the sets.")

# A = {1, 2, 3}
# B = {3, 4, 5}
# C = A + B


