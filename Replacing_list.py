# Python code to replacing given numbers in the list with specified integer

# Declaring a list and giving random numbers


numbers = [5, 2, 5, 2, 2]

# Use for loop to iterate words and our output will be empty strings first
for x_count in numbers:
    output = ''
# Then we replace every number with desired letter
    for count in range(x_count):
        output += 'x'
    print(output)
