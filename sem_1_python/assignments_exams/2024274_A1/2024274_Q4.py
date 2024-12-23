def calculate_population(initial, growth_rate, years):
    population = initial
    for _ in range(years):
        population *= (1 + growth_rate / 100)
        growth_rate -= 0.1
    return population

def _test():
    assert calculate_population(100, 2.5, 4) == 109.73630975999998, "Test failed for 4 year"
    assert calculate_population(100, 2.5, 7) == 116.45293787675409, "Test failed for 7 years"
_test()

pop1 = 50
pop2 = 1450
pop3 = 1400
pop4 = 1700
pop5 = 1500
pop6 = 600
pop7 = 1200

growth1 = 2.5
growth2 = 2.1
growth3 = 1.7
growth4 = 1.3
growth5 = 0.9
growth6 = 0.5
growth7 = 0.1

total_population = pop1 + pop2 + pop3 + pop4 + pop5 + pop6 + pop7
previous_population = total_population
max_population = total_population
year_of_max = 0
years_passed = 0

while True:
    years_passed += 1

    new_pop1 = calculate_population(pop1, growth1, years_passed)
    new_pop2 = calculate_population(pop2, growth2, years_passed)
    new_pop3 = calculate_population(pop3, growth3, years_passed)
    new_pop4 = calculate_population(pop4, growth4, years_passed)
    new_pop5 = calculate_population(pop5, growth5, years_passed)
    new_pop6 = calculate_population(pop6, growth6, years_passed)
    new_pop7 = calculate_population(pop7, growth7, years_passed)

    new_total_population = new_pop1 + new_pop2 + new_pop3 + new_pop4 + new_pop5 + new_pop6 + new_pop7

    if new_total_population > max_population:
        max_population = new_total_population
        year_of_max = years_passed

    if new_total_population < previous_population:
        print(f"Maximum population YEAR: {year_of_max}. Population: {max_population:.2f} million.")
        break

    previous_population = new_total_population
