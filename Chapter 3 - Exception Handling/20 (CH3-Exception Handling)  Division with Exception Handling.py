# create a try block
try:
    # take input for numerator
    numerator = int(input())
    # take input for denominator
    denominator = int(input())

    # Divide numerator by denominator and print the result
    print(numerator/denominator)

# create the except block
except ZeroDivisionError:
    print("Denominator cannot be 0. Try again.")