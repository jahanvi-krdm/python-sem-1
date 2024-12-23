# f = open("/Users/jahanvikardam/Desktop/ip quiz 2 material/file_handling/data.txt", "w")
# f.write("Line1\n")
# f.write("Line 2")
# f.close()
# ans = 2 new lines

# f = open("/Users/jahanvikardam/Desktop/ip quiz 2 material/file_handling/data.txt", "r")
# print(f.read(12))
# f.seek(0)
# print(f.readline())
# f.close()
# ans = ''' Good morning
# Good morning, Everybody!'''

# Q4
# with open("data.txt", "r") as f:
#     for _ in range(5):
#         print(f.readline().strip())
# blank lines are printed

# Q5
# f = open("example.txt", "w")
# f.write("Writing to a file.") # adds this to the file
# f.close()
# f.write("Attempting to write again.") # assertion error

# Q6
# with open("numbers.txt", "r") as f:
#     for line in f:
#         number = int(line) # ValueError

# WRITE A PROGRAM FOR GIVEN PROBLEMS
# with open("meow.txt", "r") as f:
#     my_dict = {}
#     count = 0
#     for line in f:
#         words = line.split()
#         for word in words:
#             if word in my_dict:
#                 my_dict[word] += 1
#             else:
#                 my_dict[word] = 1
# for word, count in sorted(my_dict.items(), key=lambda x: (-x[1], x[0])):
#     print(f"{word}: {count}")

# Q2
# with open("bark.txt", "r") as f:
#     my_list = []
#     for line in f:
#         words = line.split()
#         for word in words:
#             for char in word:
#                 if char not in my_list:
#                     letter = ord(char)
#                     my_list.append((char, letter))
#     print(sorted(tuple(set(my_list))))

# Q3
# with open("/Users/jahanvikardam/Desktop/ip/file_handling/meow.txt", "r") as f:
#     string = f.read()
#     words = string.split()
#     single_string = ''.join(words)
#     print(len(single_string) + 1)

#     unique = set([word.lower() for word in words])
#     word_dict = {}
#     for word in words:
#         if word in word_dict:
#             word_dict[word] += 1
#         else:
#             word_dict[word] = 1
#     print(f"Word dictionary: {word_dict}")
#     print(f"Unique words: {unique}")




    








