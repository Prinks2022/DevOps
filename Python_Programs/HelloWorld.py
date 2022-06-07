from pickle import PicklingError

print('Hello World')

##Strings
a_string = 'Example'
print (a_string[-1])
print (a_string[-3])

original_string ='Supercalifragilistic'
print (original_string[0:5]) # 'Super'

print (original_string[5:9]) # 'cali'
print(original_string[:5]) # 'Super'
print(original_string[9:]) #'fragilistic'
print(original_string[-3:]) #'tic'

my_string = 'abc'
#my_string[0] = 'd' # error - strings are immutable

##Lists
list_of_numbers = [1, 2, 3, 4, 5]
list_of_strings = ['one', 'two', 'three','four', 'five']
list_of_booleans = [False, True, True, False,True]

list_of_animals = ['armadillo', 'bear','crocodile', 'deer', 'elephant']

print(list_of_animals[4]) # 'elephant'
print(list_of_animals[-1]) # 'elephant'

my_list = [1, 2,4]
my_list[0]=4 #modify list
print(my_list)

list_one = [1, 2, 3, 4, 5]
list_one.remove(1)
print(list_one)
del list_one[1]
print(list_one)
list_two = [1, 2, 3, 4, 5]
list_two.append(6)
list_two.insert(2, 7)
print(list_two)
print(list_two * 3)

##Dictionary

dictionary_of_favourite_colours = {'Alice': 'Purple', 'Bob':'Green', 'Charlie': 'Scarlet'}
print(dictionary_of_favourite_colours['Charlie']) #Scarlet
dictionary_of_favourite_colours['Priyanka'] ='Pink' #add
print(dictionary_of_favourite_colours)
del dictionary_of_favourite_colours['Bob'] #delete
print(dictionary_of_favourite_colours)
print(len(dictionary_of_favourite_colours))

basket = {'apple','orange', 'apple', 'pear','orange', 'banana'}
print(basket) # sets don't store duplicate

