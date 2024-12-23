# Q1
ans = "[8, 2]"
# Q2
ans = "[[4, 16, 21], [5, 17, 34], [22, 13, 35]]"
# Q3
nums = [1,2,3,4,5,6,7,8,9,10]
sq_evens = [x**2 for x in nums if x%2==0]
print(nums)
print(sq_evens)
# Q4
matrix = [[1,2,3],[4,5,6],[7,8,9]]
odd_nums = [element for row in matrix for element in row if element % 2 != 0]
print(odd_nums)
# Q5
matrix = [[1,2,3],[4,5],[6,7,8,9]]
flatten_matrix = []
for sublist in matrix:
    for i in range(len(sublist)):
        flatten_matrix.append(sublist[i])
print(flatten_matrix)

# WAP
# Q1
lst = [73, 68, 75, 62, 79]
result = ["hot" if x>75 else "cold" if x<65 else "warm" for x in lst]

# Q2
list1 = [1,2,3]
list2 = ['a', 'b']
pairs = [[x,y] for x in list1 for y in list2]
print(pairs)

# Q3
matrix = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]
transposed = [[[matrix[k][i][j] for k in range(len(matrix))] for j in range(len(matrix[0][0]))] for i in range(len(matrix[0]))]
print(transposed)