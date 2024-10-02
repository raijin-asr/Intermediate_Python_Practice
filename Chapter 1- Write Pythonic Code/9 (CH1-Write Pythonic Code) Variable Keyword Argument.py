# create the function
def full_name(**kwargs):
    # print the argument
    print(kwargs)

first = input()
last = input()

full_name(first = first, last = last)