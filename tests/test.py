"""
values = input("Please, type 2 numbers separated by a space (' '): ").split(" ")
values = [int(v) for v in values]
"""

numbers = input("Type the numbers spaced between each other: ").split(" ")
# Use of the brackets '[...]' implies the creation of an array
# The operation using, firstly, specifies the variable type to convert to, shwon by the 'float(n)'...
# Then, it effectuates a loop using the 'for n in numbers' to apply the type conversion for each item/value/element 

numbers = [float(n) for n in numbers]