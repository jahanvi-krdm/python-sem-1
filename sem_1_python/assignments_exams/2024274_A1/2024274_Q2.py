angle = float(input("Enter the angle: "))
assert angle > 0 and angle < 90, "Angle must be between 0 and 90"

base = float(input("Enter the horizontal distance: "))
assert base > 0, "Base must be greater than 0"

pi = 3.14

def factorial(n):
    if n == 0 and n == 1:
        return 1
    ans = 1
    for i in range(2, n+1):
        ans *= i 
    return ans

def sin(x):
    ans = 0
    for i in range(15):
        value = ((-1) ** i) * (x ** (2 * i + 1)) / factorial(2 * i + 1)
        ans += value
    return ans

def cos(x):
    ans = 0
    for i in range(15):
        value = ((-1) ** i) * (x ** (2 * i)) / factorial(2 * i)
        ans += value
    return ans

def convert_to_rad(angle):
    return angle * (pi / 180)

def tan(x):
    return sin(x) / cos(x)

# Converting angle to radians 
angle_in_radians = convert_to_rad(angle)

# Calculating height of the pole (perpendicular)
def perpendicular(base, angle_in_radians):
  return tan(angle_in_radians) * base


# Calculating distance between the person and the top of the pole (hypotenuse)
def hypotenuse( base , angle_in_radians):
   return base / cos(angle_in_radians)
h = hypotenuse 

def trignometric_test():
    rad_45 = convert_to_rad(45)
    assert abs(perpendicular(10, rad_45) - 9.99) < 0.01, "Height test failed"
    assert abs(hypotenuse(10,rad_45) - 14.14) < 0.01, "Hypotenuse test failed"
trignometric_test()

print("Height of the pole:", round(perpendicular(base, angle_in_radians)))
print("Distance between the person and the top of the pole:", round(hypotenuse(base, angle_in_radians)))

# help taken from online resources
   
