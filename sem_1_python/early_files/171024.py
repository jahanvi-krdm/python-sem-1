# my_tuple = (1,2,[3,4])
# my_tuple[2][0] = 5 
# print(my_tuple) # (1, 2, [5, 4])

# my_tuple = (1, 2, 3)
# my_tuple += (4, 5, 6)
# print(my_tuple) # (1, 2, 3, 4, 5, 6)

# tuple1 = (1, 2, 3,)
# tuple2 = tuple1
# tuple2 += (4,)
# print(tuple1) # (1, 2, 3)
# print(tuple2) # (1, 2, 3, 4)

# l1 = [(1, 2),(3, 4, 10)]
# l2 = [(5, 6, 9),(7, 8)]
# l3 = [l1[i] + l2[i] for i in range(len(l1))]
# print(l3)

# input_list = [(1, 5), (3, 2), (8, 6), (10,5), (2,11), (4,5)]
# def find_min(input_list):
#     min_first = input_list[0][0]
#     min_second = input_list[0][1]
#     for tup in input_list:
#         min_first = min(min_first,tup[0])
#         min_second = min(min_second,tup[1])
#     return (min_first, min_second)
# def find_max(input_list):
#     max_first = input_list[0][0]
#     max_second = input_list[0][1]
#     for tup in input_list:
#         max_first = max(max_first, tup[0])
#         max_second = max(max_second, tup[1])
#     return (max_first, max_second)
# print(find_min(input_list),"," ,find_max(input_list))

def find_pairs_with_target_sum(input_data, target_sum):
    pairs = []
    for i in range(len(input_data)):
        for j in range(i + 1, len(input_data)):
            elementwise_sum = (input_data[i][0] + input_data[j][0], input_data[i][1] + input_data[j][1])
            if elementwise_sum == target_sum:
                pairs.append((input_data[i], input_data[j]))
    return pairs
input_data = [(2, 6), (4, 8), (8, 6), (9, 8), (1, 4), (6, 4)]
target_sum = (10, 12)
output = find_pairs_with_target_sum(input_data, target_sum)
print(output)
