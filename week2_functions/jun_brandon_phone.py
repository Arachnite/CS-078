
# Brandon Jun // COMSC 078 // Functions

def get_units():

    while True:
        units = input("Enter number of units used: ")
        if int(units) >= 0 : return int(units)
        print("You cannot have negative units.")

def calculate_cost(units, base_cost, base_limit, cost_per_unit):
    if units <= base_limit : return base_cost
    return base_cost + (units - base_limit) * cost_per_unit

def main():
    units = get_units()
    cost1 = calculate_cost(units, 9.38, 65, 0.045)
    cost2 = calculate_cost(units, 8.57, 50, 0.052)
    print("Cost for plan 1: $", format(cost1, '.2f'))
    print("Cost for plan 2: $", format(cost2, '.2f'))
    if cost1 < cost2 : print("Plan 1 is cheaper.")
    else : print("Plan 2 is cheaper.")

main()