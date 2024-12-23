# https://classroom.google.com/c/NzAzNjQwMzYwNTgz/p/NzE0OTA2MjMyMTk3/details
# Q1
output = (1,2, [5, 4])

# Q2
tup = (1, 2, 3)
tup += (4, 5)
# print(tup)
tup = (1, 2, 3, 4, 5)

# Q3
tup1 = (1,2,3)
tup2 = tup1
tup2 += (4,)
# print(tup2)
# print(tup1)

# Q4
my_tup = (1,(2,3))
# my_tup[1][0] = 5
# print(my_tup) # doesnt suppprt item assignment

# Tuple manipulation
# Q1
# list1 = [(1, 2),(3, 4, 10)]
# list2 = [(5, 6, 9),(7, 8)]
# def concatenate():
#     list_minor_1 = []
#     list_minor_1 = list1[0] + list2[0]
#     list_minor_2 = []
#     list_minor_2 = list1[1] + list2[1]
#     list_major = [list_minor_1, list_minor_2]
#     return list_major
# print(concatenate())

# Q2
# input = [(1, 5), (3, 2), (8, 6), (10,5), (2,11), (4,5)]
# list1 = []
# list2 = []
# for tuples in input:
#     list1.append(tuples[0])
#     list2.append(tuples[1])
# def finding_max_min():
#     l1_max = max(list1)
#     l2_max = max(list2)
#     max_tup = tuple([l1_max, l2_max])
#     l1_min = min(list1)
#     l2_min = min(list2)
#     min_tup = tuple([l1_min, l2_min])
#     return max_tup, min_tup
# print(finding_max_min())

# Q3
# data = [(2, 6), (4, 8), (8, 6), (9, 8), (1,4), (6,4)]
# target = (10, 12)
# pair_tup = []
# def sum_pair():
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i][0] + data[j][0] == target[0] and data[i][1] + data[j][1] == target[1]:
#                 pair = [data[i], data[j]]
#                 pair_tup.append(tuple(pair))
#     return (pair_tup)
# print(sum_pair())

# Q4
# data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (9,4,2)]
# indices = [2, 0, 1]
# def reorder_tuples():
#     retup = []
#     for tup in data:
#         retup.append([tup[indices[0]], tup[indices[1]], tup[indices[2]]])
#     return retup
# print(reorder_tuples())

# scenario based questions
# q1

# dim_no = int(input())
# dims = []
# for i in range(dim_no):
#     dim = list(map(int, input("Enter length, width: ").split()))
#     dims.append(dim)  
# print(dims)
# def calculate_areas(dims):
#     rectangles = []
#     for dim in dims:
#         a = dim[0] * dim[1]
#         rectangles.append((dim, a))
#     return rectangles
# print(calculate_areas(dims))

# Q2

city_no = int(input("Enter the number of cities: "))
city_metrics = []
for i in range(city_no):
    city = input("Enter the city name: ")  
    lat, lon = map(int, input("Enter latitude and longitude separated by space: ").split())  
    compiled = (city, (lat, lon))  
    city_metrics.append(compiled)  
print(city_metrics)

def calc_distance(coord1, coord2):
    return ((coord2[0] - coord1[0]) ** 2 + (coord2[1] - coord1[1]) ** 2) ** 0.5

