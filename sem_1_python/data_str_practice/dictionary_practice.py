# Q1
d = {'x': 1, 'y': 2, 'z': 3}
# print(d.pop('y', 0))
# print(d)

# Q2
d = {'a':1, 'b':2}
d['b'] = d.get('c', 3)
# print(d)
output = {'a':1, 'b':3}

# Q3
output = {'x': 10, 'y': 30, 'z': 40}
d = {'x': 10, 'y': 20}
d.update({'y': 30, 'z': 40}) # update will first updating existing values 
# then if it doesnt exist add a new key pair
# print(d)

# Q4
d = {True: 'yes', False: 'no'}
# print(d[1]) # 1 is true 0 is false so ans will be yes

# Q5
d1 = {'a': [1, 2], 'b': 3, 'c':(4,5), 'd': {5:'x', 7:'y'}} 
d2 = d1.copy() # shallow copy: reflects on both d1, d2 but 
# on d2 everything gets changed while on d1 only lists, sets change 
# not tuples and integrs, strings since they are immutable
d2['a'].append(4)
d2['b'] = 5
d2['c'] = (7,8)
d2['d'][5] = 'z'
print(d1)
print(d2)

# from lecture 

nums = [1, 2, 1, 1, 2, 4, 6, 4, 1, 7]
d = {}
for i in nums:
    if i in d:
        d[i] += 1
    elif i not in d:
        d[i] = 1
print(d)

student = {
"rollno": "24274",
"name": "Jahanvi",
"sem1": [("m101", 4, 9), ("cs101", 4, 8), ("com101", 4, 10)],
"sem2": [("m102", 4, 8), ("cs102", 4, 9), ("ee102", 4, 8)],
"sem3": [("m202", 2, 10), ("cs201", 4, 8), ("elect1", 4, 10)],
}

def calc_sgpa(courses):
    total_weighted_points = 0
    total_credits = 0
    for course in courses:
        credits, grade_points = course[1], course[2]
        total_weighted_points += credits * grade_points
        total_credits += credits
    return round(total_weighted_points / total_credits, 2)

def calculate_all_sgpas(student):
    sgpas = {}
    for key in student:
        if key.startswith("sem"):
            sgpas[key] = calc_sgpa(student[key])
    return sgpas

sgpas = calculate_all_sgpas(student)

for semester, sgpa in sgpas.items():
    print(f"{semester}: SGPA = {sgpa}")

# WAP
# Q1
fruits = ['apple', 'banana', 'apricot', 'berry', 'blueberry', 'dragon fruit', 'mango', 'papaya']
sorted_fruits = {}
def sorting_fruits():
    for fruit in fruits:
        first_letter = fruit[0]
        if first_letter in sorted_fruits:
            sorted_fruits[first_letter].append(fruit)
            sorted_fruits[first_letter].sort()  # Sort the list of fruits
        else:
            sorted_fruits[first_letter] = [fruit]
sorting_fruits()
sorted_fruits = dict(sorted(sorted_fruits.items()))  # Sort the dictionary by keys
# print(sorted_fruits)


# Q2
dict1 = {'a': 5, 'b': [1, 2], 'c': 'hello', 'd': 42, 't' : (1,2)}
dict2 = {'a': 10, 'b': [3, 4], 'c': ' world', 'e': 'new_key', 't':(5,7)}
my_dict = {}
def the_stuff():
    my_dict['a'] = 0
    my_dict['b'] = []
    my_dict['c'] = ''
    my_dict['t'] = ()
    my_dict['d'] = 42
    my_dict['e'] = 'new_key' 
    my_dict['a'] = dict1.get('a') + dict2.get('a')
    my_dict['b'] = dict1.get('b') + dict2.get('b')
    my_dict['c'] = dict1.get('c') + dict2.get('c')
    my_dict['t'] = tuple(dict1.get('t')) + tuple(dict2.get('t'))
    return my_dict
# print(the_stuff())

# alternate and more versatile method

def merge_dicts(dict1, dict2):
    merged_dict = {}

    for key in dict1:
        if key in dict2:
            value1 = dict1[key]
            value2 = dict2[key]       
            if type(value1) == type(value2):
                if type(value1) == int or type(value1) == float:
                    merged_dict[key] = value1 + value2
                elif type(value1) == list:
                    merged_dict[key] = value1 + value2
                elif type(value1) == str:
                    merged_dict[key] = value1 + value2
                elif type(value1) == tuple:
                    merged_dict[key] = value1 + value2
                else:
                    print(f"Incompatible types for key '{key}': {type(value1)} and {type(value2)}")
            else:
                print(f"Incompatible types for key '{key}': {type(value1)} and {type(value2)}")
        else:
            merged_dict[key] = dict1[key]

    for key in dict2:
        if key not in dict1:
            merged_dict[key] = dict2[key]  
    return merged_dict

dict1 = {'a': 5, 'b': [1, 2], 'c': 'hello', 'd': 42, 't': (1, 2)}
dict2 = {'a': 10, 'b': [3, 4], 'c': ' world', 'e': 'new_key', 't': (5, 7)}

# result = merge_dicts(dict1, dict2)
# print(result)

# Q3
dic = {'a': [1, 2], 'b': [2, 3]}
def invert(dic):
    cid = {}
    for key in dic:
        for value in dic[key]:
            if value in cid:
                cid[value].append(key)
            else:
                cid[value] = [key]
    return cid
print(invert(dic))

# Q4
anagrams = {}
words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
def beeech():
    for word in words:
        sort_bee = ''.join(sorted(word))
        if sort_bee in anagrams:
            anagrams[sort_bee].append(word)
        else:
            anagrams[sort_bee] = [word]
    return anagrams
print(beeech())

# Q5
missing = {}
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2}
def missing_you():
    for key in dict1:
        if key not in dict2:
            missing[key] = dict1[key]
    return missing
print(missing_you())


# Q6
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6, 'e': 7}
unique = {}
def unique_you():
    for key1 in dict1:
        for key2 in dict2:
            if key1 not in dict2:
                unique[key1] = dict1[key1]
            if key2 not in dict1:
                unique[key2] = dict2[key2]
    return unique

def printing(unique):
    keys = unique.keys()
    values = unique.values()
    add = sum(values)
    return keys, add
unique_you()
keys, add = printing(unique)
print(f"Unique keys: {set(keys)}")
print(f"Sum of values of unique keys: {add}")



