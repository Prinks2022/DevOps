'''file1 = open("step_3.txt", mode='r')
lines = file1.read().splitlines()
for l in lines:
    line = l.split()
    if line[1] == 'calc':
        user_operand = line[2]
        number1 = int(line[3])
        number2 = int(line[4])
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
    elif (line[0] == 'goto') and (line[1] != 'calc'):
        newline = l.line[1]
        print(newline)
file1.close()
'''
def calc_function(symbol, value_a, value_b):
    if (symbol == 'x'):
        return value_a * value_b
    elif (symbol == '+'):
        return value_a + value_b
    elif (symbol == '-'):
        return value_a - value_b
    elif (symbol == '/'):
        return value_a / value_b
    else:
        print("Unknown symbol!")

with open("step_3.txt", mode="r") as file:
    result = file.read().splitlines()
    are_we_finished = False
    line_we_are_on = 0
    lines_weve_seen = []
    while not are_we_finished:
        line_we_are_on = int(line_we_are_on)
        print(line_we_are_on)
        split_result = result[line_we_are_on].split()
        if len(split_result) == 2:
            a, b = split_result
        else:
            a, b, c, d, e = split_result
        if (b != "calc"):
            line_we_are_on = int(b) - 1
            if line_we_are_on in lines_weve_seen:
                are_we_finished = True
            lines_weve_seen.append(line_we_are_on)
            continue
        print("the second word was calc")    
        line_we_are_on = calc_function(c, int(d), int(e)) - 1
        if line_we_are_on in lines_weve_seen:
            are_we_finished = True
        lines_weve_seen.append(line_we_are_on)
