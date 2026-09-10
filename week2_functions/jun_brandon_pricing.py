
# Brandon Jun // COMSC 078 // Functions

def main():

    price = input("What is the price of each item? ")
    amount = input("How many are you ordering? ")
    subtotal = float(price) * int(amount)

    discount = 0.00
    if float(amount) >= 100:
        discount = subtotal * 0.30
    elif float(amount) >= 50:
        discount = subtotal * 0.25
    elif float(amount) >= 20:
        discount = subtotal * 0.20
    elif float(amount) >= 10:
        discount = subtotal * 0.10

    print("Subtotal: $", format(subtotal, '.2f'))
    print("Discount: $", format(discount, '.2f'))
    print("Total: $", format(float(price) * int(amount) - discount, '.2f'))

main()