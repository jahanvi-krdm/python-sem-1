
# Q1
# d = {'x':1, 'y':2, 'z':3}
# print(d.pop('y', 0))
# print(d)
# ans = "2, {'x':1, 'z':3}"

# Q2
# d = {'a': 1, 'b': 2}
# d['b'] = d.get('c', 3)
# print(d)
# ans = "{'a': 1, 'b': 3}"

# Q3
# d = {'x': 10, 'y': 20}
# d.update({'y': 30, 'z': 40})
# print(d)
# ans = "{'x':10, 'y':30, 'z':40}"

# Q4
# d = {True: 'yes', False: 'no'}
# print(d[1])
# its taking as binary

# Q5
# d1 = {'a': [1, 2], 'b': 3, 'c':(4,5), 'd': {5:'x', 7:'y'}}
# d2 = d1.copy()
# d2['a'].append(4)
# d2['b'] = 5
# d2['c'] = (7,8)
# d2['d'][5] = 'z'
# print(d1)
# print(d2)
# ans = '''
# {'a': [1, 2, 4], 'b': 3, 'c': (4, 5), 'd': {5: 'z', 7: 'y'}}
# {'a': [1, 2, 4], 'b': 5, 'c': (7, 8), 'd': {5: 'z', 7: 'y'}}
# '''

# WAP
# Q1
# inp = ['apple', 'banana', 'apricot', 'berry', 'blueberry']
# out = {}
# for fruit in inp:
#     if fruit[0] not in out:
#         out[fruit[0]] = [fruit]
#     else:
#         out[fruit[0]].append(fruit)
# print(out)

# Q2
# dict1 = {'a': 5, 'b': [1, 2], 'c': 'hello', 'd': 42, 't' : (1,2)}
# dict2 = {'a': 10, 'b': [3, 4], 'c': ' world', 'e': 'new_key', 't': (5,7)}
# def merge_dicts(dict1, dict2):
#     merged_dict = {}
#     for key in dict1:
#         if key in dict2:
#             value1 = dict1[key]
#             value2 = dict2[key]       
#             if type(value1) == type(value2):
#                 if type(value1) == int or type(value1) == float:
#                     merged_dict[key] = value1 + value2
#                 elif type(value1) == list:
#                     merged_dict[key] = value1 + value2
#                 elif type(value1) == str:
#                     merged_dict[key] = value1 + value2
#                 elif type(value1) == tuple:
#                     merged_dict[key] = value1 + value2
#                 else:
#                     print(f"Incompatible types for key '{key}': {type(value1)} and {type(value2)}")
#             else:
#                 print(f"Incompatible types for key '{key}': {type(value1)} and {type(value2)}")
#         else:
#             merged_dict[key] = dict1[key]
#     for key in dict2:
#         if key not in dict1:
#             merged_dict[key] = dict2[key]  
#     return merged_dict
# print(merge_dicts(dict1, dict2))

# Q3
# inp = {'a':[1,2], 'b':[2,3]}
# out = {}
# for key in inp:
#     for value in inp[key]:
#         if value not in out:
#             out[value] = [key]
#         else:
#             out[value].append(key)
# print(out)

# Q4
# inp = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
# def sorting(inp):
#     unique = set()
#     for word in inp:
#         sorted_word = ''.join(sorted(word))
#         unique.add(sorted_word)
#     return list(unique)
# def dict_making():
#     unique = sorting(inp)
#     out = {}
#     for word in inp:
#         sorted_word = ''.join(sorted(word))
#         for key in unique:
#             if sorted_word == key:
#                 if key in out:
#                     out[key].append(word)
#                 else:
#                     out[key] = [word]
#     return out
# print(dict_making())

# Q5
# maki = {'a': 1, 'b': 2, 'c': 3} 
# yuta = {'a': 1, 'b': 2}
# b = {}
# for key in maki:
#     if key not in yuta:
#         b[key] = maki[key]
# print(b)

# Q6
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6, 'e': 7}
# unique = {}
# def unique_you():
#     for key1 in dict1:
#         for key2 in dict2:
#             if key1 not in dict2:
#                 unique[key1] = dict1[key1]
#             if key2 not in dict1:
#                 unique[key2] = dict2[key2]
#     return unique
# print(unique_you())

# Q7
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6, 'e': 7}
# uni = {}
# unique_keys = set()
# sum_values = 0
# for key1 in dict1:
#     for key2 in dict2:
#         if key1 not in dict2:
#             uni[key1] = dict1[key1]
#         if key2 not in dict1:
#             uni[key2] = dict2[key2]
# for key, value in uni.items():
#     unique_keys.add(key)
#     sum_values += value
# print("Unique keys:", unique_keys)
# print("Sum of values of unique keys:", sum_values)

