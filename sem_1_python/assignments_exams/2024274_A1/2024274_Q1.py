import math

a = float(input("Enter starting time: "))
b = float(input("Enter ending time: "))
assert b <= 66.5, "Ending time should be less than 66.5"

d = 0.25  # delta

# Calculate the velocity of the rocket at a given time
def velocity_rocket(r):
    return 2000 * math.log(140000 / (140000 - 2100 * r)) - 9.8 * r

# Calculate the distance traveled by the rocket between two time points
def distance_rocket(a, b, d):
    r = a
    distance = 0.0  
    while r < b:
        distance_a = velocity_rocket(r)
        distance_d = velocity_rocket(r + d)
        distance += (distance_a + distance_d) / 2 * d
        r += d
    return distance

def test_rocket(a, b, d):
    a = 0
    b = 0
    d = 0.25
    assert distance_rocket(a, b, d) == 0.0

test_rocket(a, b, d)
final_distance = distance_rocket(a, b, d)
print("The distance travelled by the rocket is:", round(final_distance))


