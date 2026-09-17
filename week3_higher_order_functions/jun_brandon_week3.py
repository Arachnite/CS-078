
# Brandon Jun // COMSC 078 // Higher Order Functions

def summation(f, lower, upper):

    total = 0
    while lower <= upper : total, lower = total + f(lower), lower + 1
    return total

def square(x) : return x * x

def fourth_power(x) : return x**4

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