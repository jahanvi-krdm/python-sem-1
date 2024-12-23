def upper_half(size, row = 1, col = 1):
    if row > size:
        return
    if col > (2 * size):
        print()
        upper_half(size, row + 1, 1)
        return
    if row > (size - col + 1):
        print(" ", end = "")
    else:
        print("*", end = "")
    if (row + size) > col:
        print(" ", end = "")
    else:
        print("*", end = "")
    upper_half(size, row, col + 1)

def lower_half(size, row = 1, col = 1):
    if row > size:
        return
    if col > (2 * size):
        print()
        lower_half(size, row + 1, 1)
        return
    if row < col:
        print(" ", end = "")
    else:
        print("*", end = "")
    if row <= (2 * size - col):
        print(" ", end = "")
    else:
        print("*", end = "")
    lower_half(size, row, col + 1)

def print_pattern(size):
    upper_half(size) 
    lower_half(size)  

n = int(input("Enter n: "))  
print_pattern(n)