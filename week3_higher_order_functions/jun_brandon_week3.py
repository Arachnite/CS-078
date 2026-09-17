
# Brandon Jun // COMSC 078 // Higher Order Functions

"""
Calculates the sum of f(n), from n = lower to n = upper

Args:
    f: a function in terms of n
    lower: the lower bound of the summation
    upper: the upper bound of the summation

Returns:
    the sum of f(n), from n = lower to n = upper
"""
def summation(f, lower, upper):

    total = 0
    while lower <= upper : total, lower = total + f(lower), lower + 1
    return total

"""
Calculates the square of n, such that n = x

Args:
    x: an integer
    
Returns:
    the square of n, such that n = x
"""
def square(x) : return x * x

"""
Calculates the fourth power of n, such that n = x // NO USE OF X*X*X*X or math.pow(x, 4)

Args:
    x: an integer
    
Returns:
    the fourth power of n, such that n = x
"""
def fourth_power(x) : return x**4

"""
Retrieves user input for lower and upper bounds
Prints the sum of squares, from n = lower to n = upper
Prints the sum of fourth powers, from n = lower to n = upper
Prints the sum of square roots, from n = lower to n = upper, using a lambda function
"""
def main():
    print("User Input:")
    lower = int(input("Enter a lower bound for the sum: "))
    upper = int(input("Enter an upper bound for the sum: "))

    print()
    print("Program Output:")
    print("The sum of squares of the numbers from ", lower, "to", upper, "is", summation(square, lower, upper))
    print("The sum of fourth powers of the numbers from ", lower, "to", upper, "is", summation(fourth_power, lower, upper))
    print("The sum of square roots of the numbers from ", lower, "to", upper, "is", summation(lambda x: x**0.5, lower, upper))

main()