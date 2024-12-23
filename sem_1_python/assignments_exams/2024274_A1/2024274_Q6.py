x_guess = float(input("Enter the initial guess: "))

def f(x):
    return x**3 - 10.5 * x**2 + 34.5 * x - 35

def f_prime(x):
    return 3 * x**2 - 21 * x + 34.5

def find_roots(x_guess):
    x0 = x_guess
    for i in range(100):
        y = f(x0)
        if y <= 0.2 and y >= -0.2:
            return x0  # Found a root within the desired range
        slope = f_prime(x0)
        if slope == 0:
            print("Slope is zero.")
            return None  
        x0 = x0 - y / slope  # Update x0 using Newton-Raphson method
    print("Newton-Raphson did not converge.")
    return None  

print("Root found:",find_roots(x_guess))