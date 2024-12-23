def f(x,y):
    return x + y 

x_target = float(input("Enter value of target x: "))
h = 0.1 # step size
y_initial = 1 # initial value of y

def euler(x_target, y_initial, h):
    x_initial = 0
    y = y_initial
    while x_initial < x_target:
        y += f(x_initial,y) * h
        x_initial += h
    return y

def test_euler():
    assert euler(0, 1, 0.1) == 1, "Test failed for x=0"
    assert euler(2, 1, 0.1) == 10.454999898651202, "Test failed for x=2"
    assert euler(8, 1, 0.1) == 4497.380472088025, "Test failed for x=3"


test_euler()

print(euler(x_target, y_initial, h))