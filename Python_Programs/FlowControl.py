
"""
users_name = input('What is your name? ')
password = input('What is your password? ')

if users_name == 'user':
    print('Hello, User')
    if password == 'squirmbag':
        print('Access granted')
    else:
        print('Access denied')

times_run = 0
while times_run < 10:
    print('Hello!')
    times_run = times_run + 1

while True:
    username = input('What is your username?')
    if username != 'admin':
        continue
    password = input('What is the password?')
    if password == 'topsecret':
        break
print('Access granted')

"""
teletubbies = ['Tinky Winky', 'Dipsy', 'Laa-Laa','Po']
for index in range(0, len(teletubbies)):
    print('The Teletubby at index ' + str(index) + ' is ' + teletubbies[index])

number = 12
try:
    msg = 'hello' + number
except TypeError:
    print('Something went wrong!')
finally:
    print('Exiting the try block')

number = 12
dict = {}
try:
    dict['Apple']
except KeyError:
    print('Something went wrong!')
finally:
    print('Exiting the try block')