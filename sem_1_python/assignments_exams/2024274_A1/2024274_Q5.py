import math

# given constants
a = 10    
b = 1.05  
c = 1     
d = 1.06  
start_price = 1.0  
price_max = float(input("Enter the maximum price: "))

def demand(start_price):
    return math.exp(a - b * start_price)

def supply(start_price):
    return math.exp(c + d * start_price)

def equilibrium_price(start_price, price_max):
    demand_prev = demand(start_price)
    supply_prev = supply(start_price)
    
    while start_price <= price_max:
        demand_curr = demand(start_price)
        supply_curr = supply(start_price)

        # this condition is for calculating the equilibrium price 
        if supply_curr > demand_curr and supply_prev < demand_prev:
            print(f"Equilibrium price : {start_price:.2f}")
            print(f"At equilibrium {demand_curr:.2f} is demand ")
            print(f"At equilibrium: {supply_curr:.2f} is supply")
            return (start_price, demand_curr, supply_curr)  

        demand_prev = demand_curr
        supply_prev = supply_curr
        start_price += start_price * 0.05  

    # if above condition is not met, then this will be returned (no equilibrium found)
    else:
        print("No equilibrium found within the given price range.")
        return None 
actual_result=equilibrium_price(1,100)
expected_result =(4.32, 235.56, 265.41) 

def _test():
    result_1 = None  # Assuming no equilibrium found for range 1 to 1
    assert equilibrium_price(1,1) == result_1
    assert abs(actual_result[0]-expected_result[0])<0.01  # Assuming equilibrium found for range 1 to 100
_test()

equilibrium_price(start_price, price_max)