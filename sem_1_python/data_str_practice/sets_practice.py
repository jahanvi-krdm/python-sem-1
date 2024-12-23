# https://classroom.google.com/c/NzAzNjQwMzYwNTgz/p/NzE0OTA2MjMyMTk3/details
# Q1
# squares = {x**2 for x in range(5)}
# print(squares)

# Q2
# frozen are like sets but are immutable - i.e. cannot be changed
# Can convert a set (or a list, tuple) into a frozenset by
# frozenset(s)
# Can perform all set operations, except add, delete, ...
# With frozensets, you can define a set of frozensets (but cannot have a set of sets)
# Wherever immutable objects are required, frozensets can be used, but not sets.

# Q3
# A = {1, 2, 3}
# B = {1, 2}
# print(B.issubset(A))

# Q4
# A = {1, 2, 3}
# B = {4, 5}
# A = A.union(B)

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

# output = 3 is present in one of the sets

# Q6
# A = {1, 2, 3}
# B = {3, 4 ,5}
# C = A.union(B)
# print(C)

# Write code for the given problems
# Q1
# s = {23, 45, 67 , 8 , 99, 100}
# s = frozenset(s)
# r = {3, 36, 78}
# s.add(r)
# print(s)

# Q2
elements = list(map(str, input().split()))
big_string = ''.join(elements)
big_string = big_string.lower() 
set_alpha = list(big_string)
def checking_conditions(set_alpha):
    if len(set(set_alpha)) == len(set_alpha):
        return 'Yes'
    elif len(set(set_alpha)) < len(set_alpha):
        return 'No'
print(checking_conditions(set_alpha))

# scenario based questions
# villager_memories = [["fly", "hex", "bake", "brew potion"],
#                      ["brew potion", "hex", "fly", "cook"],
#                      ["hex", "bake", "brew potion", "fly"]]
# forbidden_memories = {"hex", "brew potion"}
# def extract_memories():
#     A = set(villager_memories[0])
#     B = set(villager_memories[1])
#     C = set(villager_memories[2])
#     common_memories = A & B & C
#     valid_memories = common_memories - forbidden_memories
#     return valid_memories
# print(extract_memories())

# target_letters = {'h', 't', 'g', 'a'}
# sentences = [
#     "The ancient tree had strange powers",
#     "Agnes gave the pendant to Agatha",
#     "A tall glass of apple juice was on the table"
# ]
# b = " ".join(sentences)
# word_list = b.split(" ")
# valid_words = []
# for word in word_list:
#     wording = word.lower()
#     for letter in wording:
#         if letter in target_letters:
#             valid_words.append(word)
#             break
# valid_words = sorted(valid_words)
# print(valid_words)

# activities = ["bewitchcraft", "prebake", "clean", "enchantpre", "hexcraft"]
# forbidden_parts = {"pre", "craft"}
# letter =[]
# def remove_forbidden_parts():
#     for activity in activities:
#         for letters in forbidden_parts:
#             if letters in activity:
#                 a = activity.replace(letters,"")
#         letter.append(a)
# remove_forbidden_parts()
# print(letter)

scrambled_names = ["adnWa", "shVi", "aiAgtha", "oVnsi", "agnThaa"]
villagers = ["Wanda", "Vision", "Agatha"]
def check_anagram():
    op = set()      
    for names in scrambled_names:
        sorted_names = ''.join(sorted(names.lower())) 
        for real_names in villagers:
            sorted_real_names = ''.join(sorted(real_names.lower()))  
            if sorted_real_names in sorted_names:
                op.add(real_names)                 
    return op
print(check_anagram())





                