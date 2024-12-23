# frnd_req = [
#     [3, 1, 4],
#     [2, 0, 5],
#     [1, 3, 2],
#     [0, 2, 3],
# ]
# new_frnd_req = []
# def minimum_tickets(frnd_req):
#     for lst in frnd_req:
#         new_frnd_row = []
#         for element in lst:
#             if element < 2:
#                 element = 0
#             new_frnd_row.append(element)
#         new_frnd_req.append(new_frnd_row)
#     return new_frnd_req
# print(minimum_tickets(frnd_req))


# food = [
#     ["Pizza", ["cheese", "tomato", "pepperoni"]],
#     ["Vegan Salad", ["lettuce", "tomato", "cucumber"]],
#     ["Chicken wings", ["chicken", "sauce"]],
#     ["Fruit platter", ["melon", "berry", "grapes"]]
# ]
# dietary_restrictions = [
#     ["Jake", ["pepperoni", "chicken"]],
#     ["Amy", ["dairy"]],
#     ["Terry", []],
#     ["Rosa", ["sauce"]],
# ]
# restricted_ingredients = []
# for _, restrictions in dietary_restrictions:
#     restricted_ingredients.extend(restrictions)    
# snacks_can_be_served = [
#     snack[0] for snack in food
#     if all(ingredient not in restricted_ingredients for ingredient in snack[1])
# ]
# print("Snacks that can be served:", snacks_can_be_served)

# tasks = [
#     ["Setup Booth", "Spider-Man", "complete"],
#     ["Prepare Snacks", "Wanda", "incomplete"],
#     ["Create Banners", "Spider-Man", "incomplete"],
#     ["Manage Guest List", "Wanda", "complete"],
#     ["Clean Up", "Spider-Man", "incomplete"]
# ]
# incomplete_spidey = []
# for task in tasks:
#     if task[1] == "Spider-Man" and task[2] == "incomplete":
#         incomplete_spidey.append(task[0])
# task_count = 0
# task_complete = 0
# for task in tasks:
#     if task[1] == "Wanda":
#         task_count += 1
#         if task[2] == "complete":
#             task_complete += 1
# print("Incomplete tasks of spider-man:", incomplete_spidey)
# print("Total tasks of wanda:", task_count)
# print("Completed tasks of wanda:", task_complete)
    
def replace_substring(test_str, s1, s2):
    result = ""
    i = 0
    while i < len(test_str):
        if test_str[i:i+len(s1)] == s1:
            result += s2
            i += len(s1)
        else:
            result += test_str[i]
            i += 1  # Increment i in else case
    return result
test_str = "eatclasscodeeatcodesleep"
s1 = "code"
s2 = "learn"
print(replace_substring(test_str, s1, s2))

test_str = 'ankankaaabcgu'
print("The original string is : " + str(test_str))
cnt = 0
res = 0
for idx in range(len(test_str)):
    if test_str[idx] == 'a':
        cnt += 1
    else:
        cnt = 0
    res = max(res, cnt)
print("The Longest Substring Length : " + str(res))

def string_balance_test(s1, s2):
    flag = True
    for char in s1:
        if char in s2:
            continue
        else:
            flag = False
    return flag

s1 = "turn"
s2 = "Return"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

s1 = "Ynf"
s2 = "PYnative"
flag = string_balance_test(s1, s2)
print("s1 and s2 are balanced:", flag)

        





