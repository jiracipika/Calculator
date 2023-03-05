from cmath import sqrt
import math

choice = input('''
    Choose your operation:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        % for percentage
        ^ for square root
''')

if choice != '^':
    number_1 = float(input('Enter first number: '))
    number_2 = float(input('Enter second number: '))

# add
if choice == "+":
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

# subtract
elif choice == "-":
    print('{} - {} ='.format(number_1, number_2))
    print(number_1 - number_2)

# multiplication
elif choice == "*":
    print('{} * {} ='.format(number_1, number_2))
    print(number_1 * number_2)

# division
elif choice == "/":
    print('{} / {} ='.format(number_1, number_2))
    print(number_1 / number_2)

# percent
elif choice == "%":
    print('{} % {} ='.format(number_1, number_2))
    print(number_1 % number_2)

# square root
elif choice == "^":
    num = float(input("Enter a number: "))
    if num < 0:
        print("Cannot take square root of a negative number!")
    else:
        result = sqrt(num)
        print("Square root of {} is {}".format(num, result))

else:
    print('Invalid entry, please try again')
