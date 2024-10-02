# create the function
def multiply_numbers(*args):
    result=1
    for num in args:
        result*=num
    return result

# get three integer inputs
n1 = int(input())
n2 = int(input())
n3 = int(input())

# call the function
result = multiply_numbers(n1,n2,n3)

# print the result
print(result)