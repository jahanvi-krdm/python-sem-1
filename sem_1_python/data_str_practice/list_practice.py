# Q1
output = [8, 2]

# Q2

# Q3
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squared_evens = [x**2 for x in numbers if x % 2 == 0]  
# print(numbers)
# print(squared_evens)

# Q4
matrix_0 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
odd_numbers = [element for row in matrix_0 for element in row if element % 2 != 0]
# print(odd_numbers)

# Q5
matrix_1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flatten_matrix = []
for sublist in matrix_1:
    for i in range(len(sublist)): 
        flatten_matrix.append(sublist[i])   
# print(flatten_matrix)

# Q5
list_no = [73, 68, 75, 62, 79]
converted = ['hot' if element > 75 else 'cold' if element < 65 else 'warm' for element in list_no]
# print(converted)

# Q6
list1 = [1, 2, 4, 5, 7]
list2 = [3, 7, 8, 10]
new_list = []
for i in range(len(list1)):
    for j in range(len(list2)):
        pair = (list1[i], list2[j])
        new_list.append(pair)   
# print(new_list)

# Q7
matrix = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]
transpose  = [[matrix[k][i][j] for k in range(len(matrix))]for j in range(len(matrix[0][0])) for i in range(len(matrix[0])) ]
# print(transpose)

# scenario based
# Q1
friend_requests = [[3, 1, 4], # avni
                   [2, 0, 5], # jahanvi
                   [1, 3, 2], # nikhil
                   [0, 2, 3]] # rudra
new_requests = []
for sublist in friend_requests:
    chota_list = []
    for element in sublist:
        if element < 2:
            element = 0
            chota_list.append(element)
        else:
            chota_list.append(element)
    new_requests.append(chota_list)
# print(new_requests)

# Q2
food = [
    ["Pizza", ["cheese", "tomato", "pepperoni"]],
    ["Vegan Salad", ["lettuce", "tomato", "cucumber"]],
    ["Chicken Wings", ["chicken", "sauce"]],
    ["Fruit Platter", ["melon", "berry", "grapes"]],
]
dietary_restrictions = [
   ["Avni", ["pepperoni", "chicken"]],
   ["Rudra", ["cheese", "milk", "yogurt", "ice cream"]],
   ["Jahanvi", []],
   ["Nikhil", ["sauce"]],
]
ingredient_restrictions = []
for name, ingredient_list in dietary_restrictions:
    for ingredient in ingredient_list:
        ingredient_restrictions.append(ingredient)

snack_served = []
for snack, ingredient_used in food:
    found = True
    for ingredient in ingredient_used:
        if ingredient in ingredient_restrictions:
            found = False
            break
    if found:
        snack_served.append(snack)
print(list(set(snack_served)))

# Q3
tasks = [
    ["Setup Booth", "Spider-Man", "complete"],
    ["Prepare Snacks", "Wanda", "incomplete"],
    ["Create Banners", "Spider-Man", "incomplete"],
    ["Manage Guest List", "Wanda", "complete"],
    ["Clean Up", "Spider-Man", "incomplete"]
]
incomplete_tasks = []
for task in tasks:
    if task[1] == "Spider-Man":
        if task[2] == "incomplete":
            incomplete_tasks.append(task[0])
# print(incomplete_tasks)

complete_tasks_wanda = 0
count = 0
for task in tasks:
    if task[1] == "Wanda":
        count += 1
        if task[2] == "complete":
            complete_tasks_wanda += 1
# print(count)
# print(complete_tasks_wanda)


