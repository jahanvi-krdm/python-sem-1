# str1 = input("")
# remove all vowels from str 1
# vowels = ('a', 'e', 'i', 'o', 'u')
# for i in vowels:
#     str1 = str1.replace(i, '')
# print(str1)

# list_input = list(map(int, input().split()))
# def sort_list(list_input):
#     count_0 = 0
#     count_1 = 0 
#     count_2 = 0
#     for i in list_input:
#         if i == 0:
#             count_0 += 1
#         elif i == 1:
#             count_1 += 1
#         elif i == 2:
#             count_2 += 1
#     return [0]*count_0 + [1]*count_1 + [2]*count_2
# print(*sort_list(list_input))

# str = input("")
# duplicate_char = []
# def duplicate_characters(str):
#     for i in range(len(str)):
#         count = 0 
#         for j in range(len(str)):
#             if str[i] == str[j]:
#                 count += 1
#         if count > 1 and str[i] not in duplicate_char:
#             duplicate_char.append(str[i])
#     return duplicate_char
# print(*duplicate_characters(str))

# string = input("")
# if string == string[::-1]:
#     print("true")
# else:
#     print("false")

# N = 10
# num = 0
# for i in range(N):
#     for j in range(i):
#         num = num + 1
# print(num)

# for i in range(1,9,2):
#     print(i)

# string = input("")
# def string_frequency(string):
#     frequency = []
#     for i in range(len(string)):
#         count = 0
#         for j in range(len(string)):
#             if string[i] == string[j]:
#                 count += 1
#         if count > 1 and string[i] not in frequency:
#             frequency.append(string[i])
#     return frequency
# print(*string_frequency(string))

# string = input("")
# def string_frequency(string):
#     if not string:
#         return ""
#     frequency = []
#     count = 1
#     for i in range(1, len(string)):
#         if string[i] == string[i - 1]:
#             count += 1
#         else:
#             frequency.append(string[i - 1])
#             if count > 1:
#                 frequency.append(str(count))
#             count = 1 
#     frequency.append(string[-1])
#     if count > 1:
#         frequency.append(str(count))
#     return ''.join(frequency)
# print(string_frequency(string))

# test_str = 'geekforgeeks'
# def odd_occurence(test_str):
#     str = []
#     count = 0
#     for i in range(len(test_str)):
#         count = 0 
#         for j in range (len(test_str)):
#             if test_str[i] == test_str[j]:
#                 count += 1
#                 if count % 2 != 0 and test_str[i] not in str:
#                     str.append(test_str[i])
#                 elif count % 2 == 0 and test_str[i] in str:
#                     str.remove(test_str[i])
#     return str
# print(odd_occurence(test_str))

# s1 = "aabbcsddaa"
# s2 = "absbeaddawew"
# def most_common_alphabet(s1, s2):
#     count1 = 0
#     count2 = 0 
#     list1 = []
#     list2 = []
#     for i in range(len(s1)):
#         count1 = 0
#         for j in range(len(s1)):
#             if s1[i] == s1[j]:
#                 count1 += 1
#                 list1.append(s1[i])
#     for i in range(len(s2)):
#         count2 = 0
#         for j in range(len(s2)):
#             if s2[i] == s2[j]:
#                 count2 += 1
#                 list2.append(s2[i])
#     if count1 > count2 and count1 < count2:
#         return None
#     elif count1 == count2:
#         return max(count1[i], count2[i])
#     else:
#         return max(count1, count2)
# print(most_common_alphabet(s1, s2))   

# def integrate(x1, x2, d):
#     x = x1
#     sum = 0
#     while x < x2:
#         sum += f(x) * d
#         x += d
#     return sum
# def f(x):    
#     return x*x
# print(integrate(0, 1, 0.01))   

# import math

# def cost1(r):
#     return r**3
# def cost1(r):
#     return r**2


# num = int(input())
# a = num
# reverse = 0
# while num > 0:
#     reverse = reverse*10 + num%10
#     num = num//10

#     # if num == 0:
#     #     break
# if reverse == a:
#     print("true")
# else:                                     
#     print("false")
# print(reverse)

# string = input("")
# # if string == string[::-1]:
# #     print("true")
# # else:
# #     print("false")

# reverse = int(string[::-1])
# print(reverse)

# s = "the cat in the hat"
# print(s.count("the"))   


# def student_bmi(wt, ht):
#     students = []
#     for i in range(len(wt)):
#         students.append(wt[i] / (ht[i] ** 2))
#     return students

# wt = list(map(float, input("Enter weight in kg (separated by space): ").split()))
# ht = list(map(float, input("Enter height in meters (separated by space): ").split()))
# print(student_bmi(wt, ht))

# def funct1(s):
#     return s[::-1]
# list = ['python', 'java', 'c++', 'html']

# for i in range(len(list)):
#     list[i] = funct1(list[i])

# for i in range(2, len(list)):
#     print(str(i-1) + ". "+list[i])

# l = [1, 'banana', 12, "MIDSEM"]
# l[1].replace('a','z')
# l[1] = l[1].replace('n', 'q')
# l[1] = l[1].split("q")
# print(l[1])

# string = "Hello"
# for i in range(len(string)-1):
#     a = string[i]
#     print(a)

# names = [ 'john', 'jane', 'pajamas', 'joe']
# j_names = []
# for name in names:
#     if name[0] == 'j':
#         j_names.append(name)
# print(j_names)

# names = [ 'john', 'jane', 'pajamas', 'joe']
# j_names = []
# for name in names:
#     if 'j' in name:
#         j_names.append(name)
# print(j_names)

# name = ['john', 'jane', 'pajamas', 'joe' , 'english']
# j_names = [name for name in name if 'j' in name]
# print(j_names)

# def check_prime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# print(check_prime(9))

# inc = 350000
# tax = 0
# if inc < 100000:
#     tax = 0 
# if inc > 100000:
#      tax += (inc - 100000) * 0.1
# elif inc > 200000:
#      tax += (inc - 200000) * 0.2
# elif inc > 300000:
#      tax += (inc - 300000) * 0.3

# print(tax)

# x = 'hello all'
# for i in range(len(x)):
#     print(x[i])

# def compute_pi(n_terms):
#     pi_approx = 0
#     sign = 1

#     for i in range(n_terms):
#         pi_approx += sign / (2 * i + 1)
#         sign *= -1  # alternate sign

#     return pi_approx * 4
# n = 4  
# pi_value = compute_pi(n)
# print(f"Approximation of π using {n} terms: {pi_value}")


# n=4
# ans =0
# sign = 1
# for i in range(n+1):
#     ans += sign/(2*i+1)
#     sign=-1**i
# print(ans)


# sum = 0
# N = 10 
# for i in range(1, N+1):
#     if i % 2 == 0 and i % 3 == 0:
#         sum -= 2
#     elif i % 2 == 0 :
#         sum += 1
#     elif i % 3 == 0:
#         sum -= 1
#     elif i % 2 == 0 and i % 3 == 0:
#         sum -= 2
#     else: 
#         sum += 2
# print(sum)


# num =0 
# sum =0 
# for num in range(1,11):
#     if num%2==0 and num%3!=0:
#        num+=1
#        sum+=num
#     elif num%3==0 and num%2!=0:
#         num-=1
#         sum+=num
#     elif num%2==0 and num%3==0:
#         num-=2
#         sum+=num
#     else:   
#         num+=2
#         sum+=num
# print(sum) 

c = -9
while c != 0:
    if c > 0:
       continue
    print(c)
    c = c + 2
    if c > 5:
        break
print("Finished")

# Infinite loop
# c = -9
# while c != 0:
#     if c > 5 :
#         break
#     if c > 0 :
#         continue
#     print(c)
#     c = c + 2
# print("Finished")