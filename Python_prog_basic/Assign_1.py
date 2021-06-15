
# ! Write a Python program to do arithmetical operations addition and division.?

import random


def add_div(arg_1, arg_2):
    add = arg_1 + arg_2
    div = arg_1 / arg_2
    return "ADD" + " = " + str(add) + "\n" + "DIV" + " = " + str(div)


print(add_div(8, 3))

# ! Write a Python program to find the area of a triangle?


def area(height, breadth):
    area = (height * breadth) / 2
    return "Area of triangle = " + str(area)


print(area(6, 2))
# ! Write a Python program to swap two variables?


def swap(v1, v2):
    print("Before swap :\t v1 = {v1} \t v2 = {v2}".format(v1=v1, v2=v2))
    tmp = v1
    v1 = v2
    v2 = tmp
    print("After swap :\t v1 = {v1} \t v2 = {v2}".format(v1=v1, v2=v2))
    return 1


print(swap(45, 54))
# ! Write a Python program to generate a random number?


n = random. random()
print(n)


# ! Write a Python program to print "Hello Python"?

print("Hello Python")
