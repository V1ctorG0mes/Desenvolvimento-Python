print("This program swaps the contents of two variables")

# User inputs
A = input("Enter the content of variable 1: ")
B = input("Enter the content of variable 2: ")

# The swapping logic
swap = A
A = B
B = swap

# Displaying the result
print("Now that we swapped, variable A contains {} and variable B contains {}".format(A, B))