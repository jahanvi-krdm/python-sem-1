menu = [("samosa", 15), ("idli", 30), ("maggie", 35), ("dosa", 70), ("tea", 10), ("black tea", 7), ("coffee", 15), ("bread omelette", 40), ("veg sandwich", 30), ("cold drink", 20)]

print('''
Menu:
    1. Samosa (15 rs)
    2. Idli (30 rs)
    3. Maggie (35 rs)
    4. Dosa (70 rs)
    5. Tea (10 rs)
    6. Black tea (7 rs)
    7. Coffee (15 rs)
    8. Bread Omelette (40 rs)
    9. Veg sandwich (30 rs)
    10. Cold drink (20 rs)
      ''')

def calculate_price(ordered_quantity, price):
    item_total = price * ordered_quantity
    return item_total

def order_items(items):
    orders = []  
    for item in items:
        food_name, quantity = item
        food_name = food_name.lower()  # Convert food name to lowercase
        orders.append((food_name, quantity))
    return orders

def total_price_and_items(orders):
    total_price = 0
    total_items = 0
    for order in orders:
        ordered_item, ordered_quantity = order
        for item, price in menu:
            if item == ordered_item:
                item_total = calculate_price(ordered_quantity, price)
                total_price += item_total
                total_items += ordered_quantity
                break
        else:
            print(f"{ordered_item.capitalize()} is not on the menu!")
    return total_items, total_price

orders = []
n = int(input("Total number of food items: "))
for i in range(n):
    order_input = input(f"Enter food item {i + 1} in the format 'item, quantity': ")
    food_name, quantity = order_input.split(", ")
    food_name = food_name.lower()  # Convert food name to lowercase
    quantity = int(quantity)
    orders.append((food_name, quantity))

print("\nYour order:")

total_price = 0
total_items = 0
for order in orders:
    ordered_item, ordered_quantity = order
    for item, price in menu:
        if item == ordered_item:
            item_total = calculate_price(ordered_quantity, price)
            total_price += item_total
            total_items += ordered_quantity
            print(f"{ordered_quantity} x {item.capitalize()} = {item_total} rs")
            break
    else:
        print(f"{ordered_item.capitalize()} is not on the menu!")

def test():
    test_input_1 = [
        ("samosa", 2), 
        ("idli", 1), 
        ("maggie", 3)
    ]
    expected_total_items_1 = 6
    expected_total_price_1 = 165
    orders_1 = order_items(test_input_1)
    total_items_1, total_price_1 = total_price_and_items(orders_1)
    assert total_items_1 == expected_total_items_1
    assert total_price_1 == expected_total_price_1

    test_input_2 = [
        ("tea", 2), 
        ("bread omelette", 1)
    ]
    expected_total_items_2 = 3
    expected_total_price_2 = 60
    orders_2 = order_items(test_input_2)
    total_items_2, total_price_2 = total_price_and_items(orders_2)
    assert total_items_2 == expected_total_items_2
    assert total_price_2 == expected_total_price_2

    test_input_3 = [
        ("dosa", 1),
        ("cold drink", 2)
    ]
    expected_total_items_3 = 3
    expected_total_price_3 = 110
    orders_3 = order_items(test_input_3)
    total_items_3, total_price_3 = total_price_and_items(orders_3)
    assert total_items_3 == expected_total_items_3
    assert total_price_3 == expected_total_price_3

test()

print(f"\nTotal, {total_items} items, Rs {total_price}") 


