file1 = open("step_2.txt", mode='r')
lines = file1.read().splitlines()
for l in lines:
    line = l.split()
    user_operand = line[1]
    number1 = int(line[2])
    number2 = int(line[3])
    if user_operand == 'x':
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
        #print(line)
        #print(f)
file1.close()
