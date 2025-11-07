###
# Simple calculator
# Asks the user to enter a symbol of mathematical operation (+, -, *, /)
# and two numbers. The program should perform the appropriate
# mathematical operation on the given numbers and return the result.   
# 
number1 = int(input("Enter first number: "))
operator = input("Enter operator: ")
number2 = int(input("Enter second number: "))

if operator == '+':
    result = number1 + number2
elif operator == '-':
    result = number1 - number2
elif operator  == '*':
    result = number1 * number2
elif operator == '/':
    if number2 == 0:
        print("Cant divide by 0")
        quit()
    result = number1 / number2
else:
    print("Invalid operator")
    quit

# print result
print(f'{number1} {operator} {number2} = {result}')