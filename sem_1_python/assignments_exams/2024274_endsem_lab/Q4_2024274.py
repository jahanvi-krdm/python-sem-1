menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print(*menu)

# Taking input
order = []
order_item = tuple(map(str, input("Please place your order from above menu (item and quantity): ").split()))
order.append(order_item)
while True:
    order_item = tuple(map(str, input("Want more? Item and quantity please: ").split()))
    if order_item != ():
        order.append(order_item)
    elif order_item == ():
        break

# making bill
full_bill = []
def bill(order):
    for food in menu:
        for items in order:
            if str(items[0]).lower() == str(food[0]).lower():
                price_item = int(items[1]) * food[1]
                item_lst = (str(items[0]).capitalize(), int(items[1]), price_item)
                full_bill.append(item_lst)
    return full_bill

# printing bill
total_item = 0
total_price = 0
def printing_bill(order):
    global total_item, total_price
    print("Item \t Qty \t Amount")
    for item_list in order:
        print_items = str(item_list[0]) + "\t" + str(item_list[1]) + "\t" + "Rs " + str(item_list[2])
        total_item += int(item_list[1])
        total_price += int(item_list[2])
        print(print_items)
    print(f"Total ({total_item}): Rs {total_price}")
printing_bill(full_bill)



# re-done

menu = [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25)]
print(*menu)

# Taking input
order = []
order_item = tuple(map(str, input("Please place your order from above menu (item and quantity): ").split()))
order.append(order_item)
while True:
    order_item = tuple(map(str, input("Want more? Item and quantity please: ").split()))
    if order_item:
        order.append(order_item)
    else:
        break

# Making bill
full_bill = []
def bill(order):
    for food in menu:
        for items in order:
            if str(items[0]).lower() == str(food[0]).lower():
                price_item = int(items[1]) * food[1]
                item_lst = (str(items[0]).capitalize(), int(items[1]), price_item)
                full_bill.append(item_lst)
    return full_bill

bill(order)

# Printing bill
total_item = 0
total_price = 0
def printing_bill(order):
    global total_item, total_price
    print("Item\t\tQty\tAmount")
    for item_list in order:
        print_items = f"{item_list[0]:<10}\t{item_list[1]:<5}\tRs {item_list[2]}"
        total_item += int(item_list[1])
        total_price += int(item_list[2])
        print(print_items)
    print("\n-------------------------------------------")
    print(f"\nTotal ({total_item} items): Rs {total_price}")

printing_bill(full_bill)