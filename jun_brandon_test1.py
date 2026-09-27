
# Brandon Jun // COMSC 078 // Test #1 - Program

import random

"""
Returns True if the number is even, False otherwise

Args:
    num: an integer
    
Returns:
    whether or not number is even
"""
def isEven(num) : return num % 2 == 0

def main():

    while True:

        evenCount = 0
        oddCount = 0

        for i in range(100):
            currentNumber = random.randint(1, 1000)

            if isEven(currentNumber) == True : evenCount += 1
            else : oddCount += 1

        print(f"Out of 100 random numbers, {oddCount} were odd, and {evenCount} were even.")
        if input("Would you like to run the program again (Y/N: ").lower() == "n" : break

main()