import math

user_tolerance = float(input("Enter the tolerance percentage (decimal): "))
max_n = int(input("Enter the maximum size: "))

final_density_value = 0.0
final_n = 0

def gcd(a, b):
    while True:  
        if b == 0:  
            return a
        a, b = b, a % b  

def find_visible_density(tolerance, max_n):
    global final_n, final_density_value
    
    theoretical_density = 6 / (math.pi ** 2)
    
    for n in range(1, max_n + 1):
        coprime_count = sum(1 for i in range(1, n + 1) for j in range(1, n + 1) if gcd(i, j) == 1)
        density_value = coprime_count / (n * n)
        
        if (1 - tolerance) * theoretical_density <= density_value <= (1 + tolerance) * theoretical_density:
            final_n = n
            final_density_value = density_value
            return

def _test():
    assert gcd(2,4) == 2, "Test case 1 failed"  
_test()
# rest test functions dont suit the problem 

find_visible_density(user_tolerance, max_n)
print(f"Size: {final_n}")
print(f"Density: {final_density_value:.2f}")