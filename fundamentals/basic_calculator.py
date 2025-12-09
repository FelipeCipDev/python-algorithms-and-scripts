"""
Description:
Create a Python program that functions as a simple interactive calculator.

The program must:
- Ask the user to input two numerical values
- Ask the user to choose one mathematical operation:
- Addition
- Subtraction
- Multiplication
- Division
- Perform the selected operation
- Display the result in a clear format

Requirements:
- Validate all user inputs
- Prevent division by zero (show a user-friendly message instead)
- The program must keep running until the user chooses to exit
- Use functions to organize the logic when possible

Bonus (Optional):
- Allow the user to chain operations without restarting the program
- Add support for more operations (square root, exponentiation, modulo)
- Add a simple menu interface
"""
print("\nAt any moment, type 'exit' to close this program -\n")

def CalculateOperation():
    values = input("Please, type 2 numbers separated by a space (' '): ").split(" ")

    if (len(values) < 2) or (len(values) > 2):
        print("Sorry, try again, this time type 2 values...")
        CalculateOperation()
    try:
        """ 
        Use of the brackets '[...]' implies the creation of an array; The operation used, firstly, specifies the 
        variable type to convert to, shown by the 'float(n)'; Then, it effectuates a loop using the 'for n in numbers' 
        to apply the type conversion for each item/value/element 
        """
        values = [int(v) for v in values]
    except ValueError:
        print("Sorry, try again, this time with a valid numerical value...")
        CalculateOperation()

    op = input("Select the desired mathematical equation, type... " \
    "\n + _ Addition; \n - _ Subtraction; \n * - Multiply; \n % - Division \n\nOpção selecionada: ")

    result = 0.0
    if op == "+":
        result = sum(values)
    elif op == "-":
        result = values[0] - values[1]
    elif op == "*":
        result = values[0] * values[1]
    else:
        result = values[0] / values[1]

    print(f"\nResultado da arredondado (2 casas decimais): {result:.2f}\n-----------------------------------------------------")
    CalculateOperation()

CalculateOperation()
