# heights = list(map(int, input().split()))
# def check_order(heights):
#     new_ht = sorted(heights)
#     count = 0
#     for i in range(len(heights)):
#         if new_ht[i] != heights[i]:
#             count += 1
#     return count 
# print(check_order(heights))

# inp_no = int(input())
# lst = list(map(int, input().split()))[:inp_no] # adds constraint
# def count_distinct(lst):
#     new_lst = []  
#     for value in lst:
#         if value not in new_lst:
#             new_lst.append(value)  
#     return len(new_lst)
# print(count_distinct(lst))

# arr = list(map(int, input().split()))
# def max_array():
#     if not arr:
#         return 0
#     max_product = arr[0]
#     min_product = arr[0]
#     result = arr[0]
#     for i in range(1, len(arr)):
#         curr = arr[i]
#         if curr < 0:
#             max_product, min_product = min_product, max_product
#         max_product = max(curr, max_product * curr)
#         min_product = min(curr, min_product * curr)
#         result = max(result, max_product)
#     return result 
# print(max_array())

inp = str(input())
def count_letter(inp):
    new_str = ""
    count = 1
    for i in range(1, len(inp)):
        if inp[i] == inp[i-1]:
            count += 1
        else:
            new_str += inp[i-1]
            if count > 1:
                new_str += str(count)
            count = 1
    new_str += inp[-1]
    if count > 1:
        new_str += str(count)
    return new_str
output = count_letter(inp)
print(output)