'''It should accept 3 pieces of input from the user: a string that's one of "x", "+", "-", or 
"/" (an operation), an integer (parameter A), and another integer (parameter B). 
It should then emit the result of performing the operation on A and B. 
For example, if your application asks the user for an operation and 2 numbers, and 
the user enters "+", "1", "2", then the application should output "3". 
If the user supplied "/", "5", "2", the application should output "2.5". 
If the user supplied "x", "5", "0", the application should output 0.
'''

#def calculator(operand, num1, num2):
#    return(num1 operand num2)
#print (calculator('+',1,2))

user_operand = input('Enter the Operand? ')
number1 = int(input('Enter number 1? '))
number2 = int(input('Enter number 2? '))

if user_operand == '*':
    result = number1 * number2
    print(result)
elif user_operand == '+':
    result = number1 + number2
    print(result)
elif user_operand == '-':
    result = number1 - number2
    print(result)
elif user_operand == '/':
    result = number1 / number2
    print(result)
else:
    print("Invalid operation")