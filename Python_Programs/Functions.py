def print_item(name, price_in_pennies):
    formatted_price = '£{:.2f}'.format(price_in_pennies / 100.0)
    print('Item: ' + name)
    print('Price: ' + formatted_price)

print_item('Milk', 85)
print_item('Coffee', 249)
print_item('Orange Juice', 110)

# Function declaration
def greet_user(first_name, last_name =''):
    full_name = first_name + ' ' + last_name
    print('Hey there, ' + full_name)

# Calling the function
greet_user('Priyanka', 'Agarwal')
greet_user(last_name = 'Doe', first_name = 'Jane')
greet_user('Jane', last_name = 'Doe')

def empty_return():
    return
variable = empty_return()
print(variable) #Returns None

def square(number):
    return number * number
result = square(5)
print(result)
print(square(3))