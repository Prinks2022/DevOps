"""
Write a Python program that prints the numbers from 1 to 100. If a number is a multiple of three,
print "Fizz" instead of the number. If the number is a multiple of five, print "Buzz" instead of the
number. For numbers which are multiples of both three and five, print "FizzBuzz" instead of the
number.

If a number is a multiple of 7, print "Bang" instead of the number. For numbers which are
multiples of seven and three / five, append Bang to what you'd have printed anyway. (E.g. 3 *
7 = 21: "FizzBang").
• If a number is a multiple of 11, print "Bong" instead of the number. Do not print anything else
in these cases. (E.g. 3 * 11 = 33: “Bong").

If a number is a multiple of 13, print "Fezz" instead of the number. For multiples of most other
numbers, the Fezz goes immediately in front of the first thing beginning with B, or at the end if
there are none. (E.g. 5 * 13 = 65: "FezzBuzz", 3 * 5 * 13 = 195: "FizzFezzBuzz"). Note that Fezz
should be printed even if Bong is also present (E.g. 11 * 13 = 143: “FezzBong").
• If a number is a multiple of 17, reverse the order in which any fizzes, buzzes, bangs etc. are
printed. (E.g. 3 * 5 * 17 = 255: “BuzzFizz")
"""

number = input("please enter a number: ")
for num in range(1, int(number) ) :
    if (num%11 == 0):
        print('Bong')
    elif (num%3 ==0):
        if(num%5 == 0):
            print('FizzBuzz')   
        elif (num%7 == 0):
            print('FizzBang')
        else:
            print('Fizz')
    elif (num%5 == 0):
        print('Buzz')
    elif (num%7 == 0):
        print('Bang')
    else:
        print(num)
num +1