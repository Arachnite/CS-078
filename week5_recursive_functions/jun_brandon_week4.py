
# Brandon Jun // COMSC 078 // Recursive Functions

"""
This recursive function displays the consecutive integers form its lower to its upper bounds
"""
def display_em(lower, upper):

    if lower == upper : print(lower)
    else : print(lower) ; display_em(lower + 1, upper)

"""
This recursive function calculates the sum of the consecutive integers from its lower to its upper bounds
"""
def add_em(lower, upper):

    if lower == upper : return lower
    else : return lower + add_em(lower + 1, upper)

"""
This higher-order function applies the included function to it lower and upper bound arguments
"""
def applyToEach(f, lower_bound, upper_bound):

    return f(lower_bound, upper_bound)

def main():

    lower_input = int(input("Enter a lower bound: "))
    upper_input = int(input("Enter an upper bound: "))
    print()
    print("The consecutive integers:")
    applyToEach(display_em, lower_input, upper_input)
    print()
    print("Add up to " + str(applyToEach(add_em, lower_input, upper_input)))

main()