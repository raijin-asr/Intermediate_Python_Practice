# create a try block
try:
    countries = {'Nepal' : 'Kathmandu', 'Sweden' : 'Stockholm', 'Italy' : 'Rome'}

    # take string input
    key = input()

    # print the value present at key
    print(countries[key])
# create the except block
except KeyError:
    print("Key is not available")