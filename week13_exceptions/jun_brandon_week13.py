
# Brandon Jun // COMSC 078 // Handling Exceptions

from fractions import Fraction

def readVal(valType, promptMsg, errorMsg):

    while True:

        val = input(promptMsg + ": ")

        try:

            return valType(val)

        except ValueError:

            print(f"{val} {errorMsg}. Please try again")

def main():

    # Integer
    intVal = readVal(int, "Enter an integer", "is not an integer")
    print(f"The square of the integer you entered is: {intVal**2}")
    print()

    # Fraction
    fracVal = readVal(Fraction, "Enter a fraction (format: 3/4)", "is not a fraction")
    print(f"The square of the fraction you entered is: {Fraction(fracVal)**2}")
    print()

    # Float
    floatVal = readVal(float, "Enter a float", "is not a float")
    print(f"The square of the float you entered is: {floatVal**2}")
    print()

    # Complex
    complexVal = readVal(complex, "Enter a complex number (format: 3+4j)", "is not a complex number")
    print(f"The square of the complex number you entered is: {complexVal**2}")
    print()

main()